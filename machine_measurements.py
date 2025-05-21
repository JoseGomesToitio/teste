from collections import defaultdict
from email.mime import application
import json
from dateutil.parser import parse as datetime_parser
import pytz

# from ..constants import MACHINE_MEASUREMENTS__BUCKET_DEF__MAPPING as bucket_def_mapping
from constants import MACHINE_MEASUREMENTS__DEFINITION__MAPPING



tz = pytz.timezone('America/Sao_Paulo')


class ETL_Error(Exception): pass


from collections import defaultdict
from copy import deepcopy
from datetime import datetime

def parse_payload(raw_python_payload, dt_filter=None):
    data = defaultdict(lambda: defaultdict(dict))

    for r in raw_python_payload:
        descriptions_mapping = defaultdict(lambda: defaultdict(dict))

        for def_index, definition in enumerate(r['values']):
            def_meta = definition.get('machineMeasurementDefinition', {})
            raw_name = def_meta.get('name')
            if raw_name not in MACHINE_MEASUREMENTS__DEFINITION__MAPPING:
                continue

            name = MACHINE_MEASUREMENTS__DEFINITION__MAPPING[raw_name]
            axes_group = def_meta.get('axesGroup', {}).get('value', '')
            aggregation_type = def_meta.get('aggregationType', {}).get('value', '')
            measurement_type = def_meta.get('measurementType', {}).get('value', '')

            if name in ['Avg Fuel Rate', 'Fuel Consumed'] and measurement_type == 'SingleValue':
                continue

            descriptions_mapping[name][axes_group][def_index] = {}
            buckets = extract_buckets(definition)
            has_description = def_meta.get('bucketDefinitions', {}).get('total') != '0'

            if has_description:
                bucket_defs = def_meta.get('bucketDefinitions', {}).get('bucketDefinitions', [])
                descriptions_mapping[name][axes_group][def_index] = parse_bucket_definitions(
                    descriptions_mapping[name][axes_group][def_index],
                    bucket_defs
                )

            values, counts = extract_values_and_counts(buckets, dt_filter)

            for sequence in values:
                if not values[sequence]:
                    continue

                l1, l2 = resolve_labels(name, axes_group, descriptions_mapping, def_index, sequence, has_description)

                try:
                    if aggregation_type == 'SUM':
                        data[name][l1][l2] = sum(values[sequence])
                    elif aggregation_type == 'WEIGHTED_AVERAGE':
                        data[name][l1][l2] = weighted_average(values[sequence], counts[sequence])
                    elif aggregation_type == 'MAX':
                        data[name][l1][l2] = max(values[sequence])
                except Exception as e:
                    raise ETL_Error(f"Falha ao agregar '{name}' com sequência '{sequence}': {e}")

    return data



def extract_buckets(definition):
    buckets = []
    for interval in definition.get('series', {}).get('intervals', []):
        for bucket in interval.get('buckets', {}).get('buckets', []):
            buckets.append(bucket)
    return buckets


def extract_values_and_counts(buckets, dt_filter=None):
    values = defaultdict(list)
    counts = defaultdict(list)
    for bucket in buckets:
        sequence = bucket.get('sequenceNumber')
        value = bucket.get('value')
        count = int(bucket.get('count', 0))

        if dt_filter:
            ts_start = datetime_parser(bucket['actualStartDate'])
            dt = ts_start.astimezone(tz).date()
            if dt != dt_filter:
                continue

        if count:
            values[sequence].append(value)
            counts[sequence].append(count)

    return values, counts


def resolve_labels(name, axesgroup, descriptions_mapping, def_index, sequence, has_description):
    if has_description:
        try:
            l1 = axesgroup
            l2 = descriptions_mapping[name][axesgroup][def_index][sequence]
        except KeyError:
            raise ETL_Error(f"Chave ausente ao resolver labels: name={name}, seq={sequence}")
    else:
        l1 = name
        l2 = name
    print(l1)
    print(l2)
    print(name)
    return l1, l2

def parse_bucket_definitions(mapping, bucket_definitions):
    for bucket_definition in bucket_definitions:

        key = bucket_definition['sequenceNumber']
        value = bucket_definition['description']

        mapping[key] = value

    return mapping



def weighted_average(distribution, weights):
    print(weights)
    return sum([distribution[i]*weights[i] for i in range(len(distribution))])/sum(weights)

