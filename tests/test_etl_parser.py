import pytest
from machine_measurements import *


def test_weighted_average(monkeypatch):
    values = [10, 20, 30]
    counts = [1, 2, 3]
    assert weighted_average(values, counts) == pytest.approx((10*1 + 20*2 + 30*3) / 6)
    

def test_parse_bucket_definitions():
    mapping = {}
    bucket_definitions = [
        {'sequenceNumber': 1, 'description': 'Working'},
        {'sequenceNumber': 2, 'description': 'Transport'},
        {'sequenceNumber': 0, 'description': 'Idle'},
    ]

    expected = {
        1: 'Working',
        2: 'Transport',
        0: 'Idle',
    }
    result = parse_bucket_definitions(mapping, bucket_definitions)
    assert result == expected
    
def test_parse_resolve_labels():
    name = "On Time"
    axesgroup = "On"
    def_index = 0
    sequence = 1
    has_description = True
    descriptions_mapping = {
        name: {
            axesgroup: {
                def_index: {
                    sequence: axesgroup
                }
            }
        }
    }

    l1, l2 = resolve_labels(name, axesgroup, descriptions_mapping, def_index, sequence, has_description)
    
    assert l1 == axesgroup
    assert l2 == descriptions_mapping[name][axesgroup][def_index][sequence]
    
def test_extract_values_and_counts():
    buckets = [
        {'sequenceNumber': 1, 'value': 10, 'count': 1},
        {'sequenceNumber': 2, 'value': 20, 'count': 2},
        {'sequenceNumber': 1, 'value': 30, 'count': 3},
        {'sequenceNumber': 0, 'value': 40, 'count': 3},
    ]
    dt_filter = None
    values, counts = extract_values_and_counts(buckets, dt_filter)
    
    assert values == {1: [10, 30], 2: [20], 0: [40]}
    assert counts == {1: [1, 3], 2: [2], 0: [3]}
    
def test_extract_buckets():
    definition = {
        'series': {
            'intervals': [
                {
                    'buckets': {
                        'buckets': [
                            {'sequenceNumber': 1, 'value': 10, 'count': 1},
                            {'sequenceNumber': 2, 'value': 20, 'count': 2},
                        ]
                    }
                },
                {
                    'buckets': {
                        'buckets': [
                            {'sequenceNumber': 3, 'value': 30, 'count': 3},
                            {'sequenceNumber': 4, 'value': 40, 'count': 4},
                        ]
                    }
                }
            ]
        }
    }
    
    expected = [
        {'sequenceNumber': 1, 'value': 10, 'count': 1},
        {'sequenceNumber': 2, 'value': 20, 'count': 2},
        {'sequenceNumber': 3, 'value': 30, 'count': 3},
        {'sequenceNumber': 4, 'value': 40, 'count': 4},
    ]
    
    result = extract_buckets(definition)
    assert result == expected