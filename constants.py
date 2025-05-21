

MACHINE_MEASUREMENTS__DEFINITION__MAPPING = {

    # 'Machine Utilization': 'Machine Utilization',

    'Fuel Consumed': 'Fuel Consumed',

#     'Avg Fuel Rate': 'Avg Fuel Rate',

#     'Avg Ground Speed': 'Avg Ground Speed',
#     'Avg Machine Speed': 'Avg Ground Speed',


#     # Avg Engine Load Factor
#     'Avg Engine Load Factor': 'Avg Engine Load Factor',

#     # Avg Engine Speed
#     'Avg Engine Speed': 'Avg Engine Speed',
#     'Average Engine Speed': 'Avg Engine Speed',
#     'Ave Engine Speed': 'Avg Engine Speed', # Cotton

#     # Coolant Temp
#     'Avg Coolant Temp': 'Avg Coolant Temp',
#     'Max Coolant Temp': 'Max Coolant Temp',

#     # Avg Hydraulic Oil Temp
#     'Avg Hydraulic Oil Temp': 'Avg Hydraulic Oil Temp',
#     'Avg Hydraulic Oil Temperature': 'Avg Hydraulic Oil Temp',
#     'Average Hydraulic Oil Temp': 'Avg Hydraulic Oil Temp',
#     'Average Hydraulic Oil Temperature': 'Avg Hydraulic Oil Temp',
#     # Max Hydraulic Oil Temp
#     'Max Hydraulic Oil Temp': 'Max Hydraulic Oil Temp',
#     'Max Hydraulic Oil Temperature': 'Max Hydraulic Oil Temp',
#     'Maximum Hydraulic Oil Temp': 'Max Hydraulic Oil Temp',
#     'Maximum Hydraulic Oil Temperature': 'Max Hydraulic Oil Temp',

#     # Trans Oil Temp
#     'Avg Trans Oil Temp': 'Avg Trans Oil Temp',
#     'Max Trans Oil Temp': 'Max Trans Oil Temp',


#     # ALL
#     'AutoTrac™': 'AutoTrac',
#     'Time at Engine Load': 'Time at Engine Load',
#     # 'Road Transport Switch': 'Road Transport Switch', # Not used yet

#     # Combine
#     'RowSense™': 'RowSense',
#     'Auto Header Height (Flex Header)': 'Auto Header Height Flex Header',
#     'Auto Header Float': 'Auto Header Float',
#     'Auto Header Height': 'Auto Header Height',
#     'Auto Reel Speed': 'Auto Reel Speed',
#     'Auto Reel Position': 'Auto Reel Position',
#     'Harvest Smart Active': 'Harvest Smart Active',
#     'Active Terrain Adjustment™': 'Active Terrain Adjustment',
#     'Active Yield': 'Active Yield',
#     'SmartClean System Hours': 'SmartClean',

#     # Sugar
#     'Field Cruise': 'Field Cruise',
#     'Auto Field Cruise': 'Auto Field Cruise',
#     'Floating Crop Divider': 'Floating Crop Divider',
#     'Contour Base-cutter Height Control': 'Contour Base-cutter Height Control',
#     'Topper Utilization': 'Topper Utilization',

#     # Cotton
#     'Header Control Response': 'Header Control Response',
#     'Right Hand Header Height': 'Right Hand Header Height',
#     'Left Hand Header Height': 'Left Hand Header Height',

#     # Tractor
#     'FieldCruise™': 'FieldCruise',
#     'MFWD': 'MFWD',
#     'Rear PTO': 'Rear PTO',
#     'Diff Lock': 'Diff Lock',
#     'Wheel Slip Time at Level': 'Wheel Slip Time at Level',
#     'Efficiency Manager™ On Time': 'Efficiency Manager',
#     'IPM™': 'IPM',

#     # Sprayer
#     'Product Application Time': 'Product Application Time',
#     'Section Control': 'Section Control',
#     'Pulsing': 'Pulsing', # TODO: review - machine: 632199	4030 Alvorada	1NW4030MVK0190339
#     'Avg Machine Speed (Pulsing)': 'Avg Machine Speed Pulsing',
#     'Avg Machine Speed (Not Pulsing)': 'Avg Machine Speed Not Pulsing',
# }


# MACHINE_MEASUREMENTS__BUCKET_DEF__MAPPING = {


#     'Machine Utilization': {

#         'Working': {'l1': 'machine_utilization', 'l2': 'working'},
#         'Transport': {'l1': 'machine_utilization', 'l2': 'transport'},
#         'Idle': {'l1': 'machine_utilization', 'l2': 'idle'},
#         'Wrapping': {'l1': 'machine_utilization', 'l2': 'wrapping'},
#         'Ejecting': {'l1': 'machine_utilization', 'l2': 'ejecting'},
#         'Forming': {'l1': 'machine_utilization', 'l2': 'forming'},
#         'Service Wrap': {'l1': 'machine_utilization', 'l2': 'service_wrap'},
#         'Service Lube': {'l1': 'machine_utilization', 'l2': 'service_lube'},
#         'Service General': {'l1': 'machine_utilization', 'l2': 'service_general'},
#         'Harvest': {'l1': 'machine_utilization', 'l2': 'harvest'},
#         'Maneuvering':{'l1': 'machine_utilization', 'l2': 'maneuvering'},
#         'Harvesting': {'l1': 'machine_utilization', 'l2': 'harvesting'},
#         'Harvesting and Unloading': {'l1': 'machine_utilization', 'l2': 'harvesting_unloading'},
#         'Headland Turn Separator Engaged': {'l1': 'machine_utilization', 'l2': 'headland_turn_separator_engaged'},
#         'Idle with Grain Tank Full': {'l1': 'machine_utilization', 'l2': 'idle_grain_tank_full'},
#         'Idle with Grain Tank not Full': {'l1': 'machine_utilization', 'l2': 'idle_grain_tank_not_full'},
#         'Unloading not Harvesting': {'l1': 'machine_utilization', 'l2': 'unloading_not_harvesting'},

#         'Transport - Road Disconnect On': {'l1': 'machine_utilization', 'l2': 'transport_road_disconnect_on'},
#         'Transport - Road Disconnect Off': {'l1': 'machine_utilization', 'l2': 'transport_road_disconnect_off'},

#         'Transport above 16 kph (10 mph) or Road Switch On': {'l1': 'machine_utilization', 'l2': 'transport_above_sixteen_road_switch_on'},
#         'Transport below 16 kph (10 mph) Separator Off': {'l1': 'machine_utilization', 'l2': 'transport_below_sixteen_separator_off'},

#         'Work Time':{'l1': 'machine_utilization','l2':'work_time'},
#         'Idle Time':{'l1': 'machine_utilization','l2':'idle_time'},
#         '8031':{'l1': 'machine_utilization','l2':'8031'},

#         'Idle with Cutterhead Off': {'l1': 'machine_utilization', 'l2': 'idle_with_cutterhead_off'},
#         'Harvesting High Load': {'l1': 'machine_utilization', 'l2': 'harvesting_high_load'},
#         'Harvesting Medium Load': {'l1': 'machine_utilization', 'l2': 'harvesting_medium_load'},
#         'Headland Turn Cutterhead On':{'l1': 'machine_utilization', 'l2':'headland_turn_cutterhead_on'},
#         'Idle with Cutterhead On': {'l1': 'machine_utilization', 'l2': 'idle_with_cutterhead_on'},
#         'Transport below 16 kph Cutterhead Off': {'l1': 'machine_utilization', 'l2': 'transport_below_sixteen_cutterhead_off'},
#         'Harvesting Low Load': {'l1': 'machine_utilization', 'l2': 'harvesting_low_load'},
#         'Feedroll Reverse': {'l1': 'machine_utilization', 'l2': 'feedroll_reverse'},
#     },


#     'Avg Coolant Temp': {
#         'Avg Coolant Temp': {'l1': 'engine_temperature', 'l2': 'avg_coolant_temp'},
#     },

#     'Average Hydraulic Oil Temp': {
#         'Average Hydraulic Oil Temp': {'l1': 'engine_temperature', 'l2': 'avg_hydraulic_oil_temp'},
#     },


#     'Maximum Hydraulic Oil Temperature': {
#         'Maximum Hydraulic Oil Temperature': {'l1': 'engine_temperature', 'l2': 'max_hydraulic_oil_temp'},
#     },

#     'Average Hydraulic Oil Temperature': {
#         'Average Hydraulic Oil Temperature': {'l1': 'engine_temperature', 'l2': 'avg_hydraulic_oil_temp'},
#     },


#     'Maximum Hydraulic Oil Temp': {
#         'Maximum Hydraulic Oil Temp': {'l1': 'engine_temperature', 'l2': 'max_hydraulic_oil_temp'},
#     },

#     'Max Coolant Temp': {
#         'Max Coolant Temp': {'l1': 'engine_temperature', 'l2': 'max_coolant_temp'},
#     },


#     'Fuel Consumed': {

#         'Working': {'l1': 'consumed_fuel_liters', 'l2': 'working'},
#         'Transport': {'l1': 'consumed_fuel_liters', 'l2': 'transport'},
#         'Idle': {'l1': 'consumed_fuel_liters', 'l2': 'idle'},

#         'Wrapping': {'l1': 'consumed_fuel_liters', 'l2': 'wrapping'},
#         'Ejecting': {'l1': 'consumed_fuel_liters', 'l2': 'ejecting'},
#         'Forming': {'l1': 'consumed_fuel_liters', 'l2': 'forming'},
#         'Service Wrap': {'l1': 'consumed_fuel_liters', 'l2': 'service_wrap'},
#         'Service Lube': {'l1': 'consumed_fuel_liters', 'l2': 'service_lube'},
#         'Service General': {'l1': 'consumed_fuel_liters', 'l2': 'service_general'},
#         'Harvest': {'l1': 'consumed_fuel_liters', 'l2': 'harvest'},
#         'Maneuvering':{'l1': 'consumed_fuel_liters', 'l2': 'maneuvering'},
#         'Harvesting': {'l1': 'consumed_fuel_liters', 'l2': 'harvesting'},
#         'Harvesting and Unloading': {'l1': 'consumed_fuel_liters', 'l2': 'harvesting_unloading'},
#         'Headland Turn Separator Engaged': {'l1': 'consumed_fuel_liters', 'l2': 'headland_turn_separator_engaged'},
#         'Idle with Grain Tank Full': {'l1': 'consumed_fuel_liters', 'l2': 'idle_grain_tank_full'},
#         'Idle with Grain Tank not Full': {'l1': 'consumed_fuel_liters', 'l2': 'idle_grain_tank_not_full'},
#         'Transport - Road Disconnect On': {'l1': 'consumed_fuel_liters', 'l2': 'transport_road_disconnect_on'}, # TODO: review
#         'Transport - Road Disconnect Off': {'l1': 'consumed_fuel_liters', 'l2': 'transport_road_disconnect_off'}, # TODO: review
#         'Unloading not Harvesting': {'l1': 'consumed_fuel_liters', 'l2': 'unloading_not_harvesting'},

#         'Transport above 16 kph (10 mph) or Road Switch On': {'l1': 'consumed_fuel_liters', 'l2': 'transport_above_sixteen_road_switch_on'},
#         'Transport below 16 kph (10 mph) Separator Off': {'l1': 'consumed_fuel_liters', 'l2': 'transport_below_sixteen_separator_off'},

#         'Idle with Cutterhead Off': {'l1': 'consumed_fuel_liters', 'l2': 'idle_with_cutterhead_off'},
#         'Harvesting High Load': {'l1': 'consumed_fuel_liters', 'l2': 'harvesting_high_load'},
#         'Harvesting Medium Load': {'l1': 'consumed_fuel_liters', 'l2': 'harvesting_medium_load'},
#         'Headland Turn Cutterhead On':{'l1': 'consumed_fuel_liters', 'l2':'headland_turn_cutterhead_on'},
#         'Idle with Cutterhead On': {'l1': 'consumed_fuel_liters', 'l2': 'idle_with_cutterhead_on'},
#         'Transport below 16 kph Cutterhead Off': {'l1': 'consumed_fuel_liters', 'l2': 'transport_below_sixteen_cutterhead_off'},
#         'Harvesting Low Load': {'l1': 'consumed_fuel_liters', 'l2': 'harvesting_low_load'},
#         'Feedroll Reverse': {'l1': 'consumed_fuel_liters', 'l2': 'feedroll_reverse'},

#         '2': {'l1': 'consumed_fuel_liters', 'l2': '2'},
#         '1': {'l1': 'consumed_fuel_liters', 'l2': '1'},
#         '0': {'l1': 'consumed_fuel_liters', 'l2': '0'},
#     },


#     'Avg Fuel Rate': {

#         'Working': {'l1': 'average_fuel_consumption', 'l2': 'working'},
#         'Transport': {'l1': 'average_fuel_consumption', 'l2': 'transport'},
#         'Idle': {'l1': 'average_fuel_consumption', 'l2': 'idle'},
#         'Wrapping': {'l1': 'average_fuel_consumption', 'l2': 'wrapping'},
#         'Ejecting': {'l1': 'average_fuel_consumption', 'l2': 'ejecting'},
#         'Forming': {'l1': 'average_fuel_consumption', 'l2': 'forming'},
#         'Service Wrap': {'l1': 'average_fuel_consumption', 'l2': 'service_wrap'},
#         'Service Lube': {'l1': 'average_fuel_consumption', 'l2': 'service_lube'},
#         'Service General': {'l1': 'average_fuel_consumption', 'l2': 'service_general'},
#         'Harvest': {'l1': 'average_fuel_consumption', 'l2': 'harvest'},
#         'Maneuvering':{'l1': 'average_fuel_consumption', 'l2': 'maneuvering'},
#         'Harvesting': {'l1': 'average_fuel_consumption', 'l2': 'harvesting'},
#         'Harvesting and Unloading': {'l1': 'average_fuel_consumption', 'l2': 'harvesting_unloading'},
#         'Headland Turn Separator Engaged': {'l1': 'average_fuel_consumption', 'l2': 'headland_turn_separator_engaged'},
#         'Idle with Grain Tank Full': {'l1': 'average_fuel_consumption', 'l2': 'idle_grain_tank_full'},
#         'Idle with Grain Tank not Full': {'l1': 'average_fuel_consumption', 'l2': 'idle_grain_tank_not_full'},
#         'Transport - Road Disconnect On': {'l1': 'average_fuel_consumption', 'l2': 'transport_road_disconnect_on'}, # TODO: review
#         'Transport - Road Disconnect Off': {'l1': 'average_fuel_consumption', 'l2': 'transport_road_disconnect_off'}, # TODO: review
#         'Unloading not Harvesting': {'l1': 'average_fuel_consumption', 'l2': 'unloading_not_harvesting'},

#         'Transport above 16 kph (10 mph) or Road Switch On': {'l1': 'average_fuel_consumption', 'l2': 'transport_above_sixteen_road_switch_on'},
#         'Transport below 16 kph (10 mph) Separator Off': {'l1': 'average_fuel_consumption', 'l2': 'transport_below_sixteen_separator_off'},
#         'Idle with Cutterhead Off': {'l1': 'average_fuel_consumption', 'l2': 'idle_with_cutterhead_off'},
#         'Harvesting High Load': {'l1': 'average_fuel_consumption', 'l2': 'harvesting_high_load'},
#         'Harvesting Medium Load': {'l1': 'average_fuel_consumption', 'l2': 'harvesting_medium_load'},
#         'Headland Turn Cutterhead On':{'l1': 'average_fuel_consumption', 'l2':'headland_turn_cutterhead_on'},
#         'Idle with Cutterhead On': {'l1': 'average_fuel_consumption', 'l2': 'idle_with_cutterhead_on'},
#         'Transport below 16 kph Cutterhead Off': {'l1': 'average_fuel_consumption', 'l2': 'transport_below_sixteen_cutterhead_off'},
#         'Harvesting Low Load': {'l1': 'average_fuel_consumption', 'l2': 'harvesting_low_load'},
#         'Feedroll Reverse': {'l1': 'average_fuel_consumption', 'l2': 'feedroll_reverse'},
#     },


#     'Average Engine Speed': {

#         'Working': {'l1': 'average_engine_speed', 'l2': 'working'},
#         'Transport': {'l1': 'average_engine_speed', 'l2': 'transport'},
#         'Idle': {'l1': 'average_engine_speed', 'l2': 'idle'},

#         'Wrapping': {'l1': 'average_engine_speed', 'l2': 'wrapping'},
#         'Ejecting': {'l1': 'average_engine_speed', 'l2': 'ejecting'},
#         'Forming': {'l1': 'average_engine_speed', 'l2': 'forming'},
#         'Service Wrap': {'l1': 'average_engine_speed', 'l2': 'service_wrap'},
#         'Service Lube': {'l1': 'average_engine_speed', 'l2': 'service_lube'},
#         'Service General': {'l1': 'average_engine_speed', 'l2': 'service_general'},
#         'Harvest': {'l1': 'average_engine_speed', 'l2': 'harvest'},

#         'Maneuvering':{'l1': 'average_engine_speed', 'l2': 'maneuvering'},
#         'Harvesting': {'l1': 'average_engine_speed', 'l2': 'harvesting'},
#         'Harvesting and Unloading': {'l1': 'average_engine_speed', 'l2': 'harvesting_unloading'},
#         'Headland Turn Separator Engaged': {'l1': 'average_engine_speed', 'l2': 'headland_turn_separator_engaged'},
#         'Idle with Grain Tank Full': {'l1': 'average_engine_speed', 'l2': 'idle_grain_tank_full'},
#         'Idle with Grain Tank not Full': {'l1': 'average_engine_speed', 'l2': 'idle_grain_tank_not_full'},
#         'Transport - Road Disconnect On': {'l1': 'average_engine_speed', 'l2': 'transport_road_disconnect_on'}, # TODO: review
#         'Transport - Road Disconnect Off': {'l1': 'average_engine_speed', 'l2': 'transport_road_disconnect_off'}, # TODO: review
#         'Unloading not Harvesting': {'l1': 'average_engine_speed', 'l2': 'unloading_not_harvesting'},

#         'Transport above 16 kph (10 mph) or Road Switch On': {'l1': 'average_engine_speed', 'l2': 'transport_above_sixteen_road_switch_on'},
#         'Transport below 16 kph (10 mph) Separator Off': {'l1': 'average_engine_speed', 'l2': 'transport_below_sixteen_separator_off'},
#         'Average Engine Speed': {'l1': 'average_engine_speed', 'l2': 'average_engine_speed'},

#         'Idle with Cutterhead Off': {'l1': 'average_engine_speed', 'l2': 'idle_with_cutterhead_off'},
#         'Harvesting High Load': {'l1': 'average_engine_speed', 'l2': 'harvesting_high_load'},
#         'Harvesting Medium Load': {'l1': 'average_engine_speed', 'l2': 'harvesting_medium_load'},
#         'Headland Turn Cutterhead On':{'l1': 'average_engine_speed', 'l2':'headland_turn_cutterhead_on'},
#         'Idle with Cutterhead On': {'l1': 'average_engine_speed', 'l2': 'idle_with_cutterhead_on'},
#         'Transport below 16 kph Cutterhead Off': {'l1': 'average_engine_speed', 'l2': 'transport_below_sixteen_cutterhead_off'},
#         'Harvesting Low Load': {'l1': 'average_engine_speed', 'l2': 'harvesting_low_load'},
#         'Feedroll Reverse': {'l1': 'average_engine_speed', 'l2': 'feedroll_reverse'},
#     },


#     'Avg Engine Speed': {

#         'Working': {'l1': 'average_engine_speed', 'l2': 'working'},
#         'Transport': {'l1': 'average_engine_speed', 'l2': 'transport'},
#         'Idle': {'l1': 'average_engine_speed', 'l2': 'idle'},

#         'Maneuvering':{'l1': 'average_engine_speed', 'l2': 'maneuvering'},
#         'Harvesting': {'l1': 'average_engine_speed', 'l2': 'harvesting'},
#         'Wrapping': {'l1': 'average_engine_speed', 'l2': 'wrapping'},
#         'Ejecting': {'l1': 'average_engine_speed', 'l2': 'ejecting'},
#         'Forming': {'l1': 'average_engine_speed', 'l2': 'forming'},
#         'Service Wrap': {'l1': 'average_engine_speed', 'l2': 'service_wrap'},
#         'Service Lube': {'l1': 'average_engine_speed', 'l2': 'service_lube'},
#         'Service General': {'l1': 'average_engine_speed', 'l2': 'service_general'},
#         'Harvest': {'l1': 'average_engine_speed', 'l2': 'harvest'},

#         'Harvesting': {'l1': 'average_engine_speed', 'l2': 'harvesting'},
#         'Harvesting and Unloading': {'l1': 'average_engine_speed', 'l2': 'harvesting_unloading'},
#         'Headland Turn Separator Engaged': {'l1': 'average_engine_speed', 'l2': 'headland_turn_separator_engaged'},
#         'Idle with Grain Tank Full': {'l1': 'average_engine_speed', 'l2': 'idle_grain_tank_full'},
#         'Idle with Grain Tank not Full': {'l1': 'average_engine_speed', 'l2': 'idle_grain_tank_not_full'},
#         'Transport - Road Disconnect On': {'l1': 'average_engine_speed', 'l2': 'transport_road_disconnect_on'}, # TODO: review
#         'Transport - Road Disconnect Off': {'l1': 'average_engine_speed', 'l2': 'transport_road_disconnect_off'}, # TODO: review
#         'Unloading not Harvesting': {'l1': 'average_engine_speed', 'l2': 'unloading_not_harvesting'},

#         'Transport above 16 kph (10 mph) or Road Switch On': {'l1': 'average_engine_speed', 'l2': 'transport_above_sixteen_road_switch_on'},
#         'Transport below 16 kph (10 mph) Separator Off': {'l1': 'average_engine_speed', 'l2': 'transport_below_sixteen_separator_off'},

#     },


#     'Avg Ground Speed': {

#         'Working': {'l1': 'average_ground_speed', 'l2': 'working'},
#         'Transport': {'l1': 'average_ground_speed', 'l2': 'transport'},
#         'Idle': {'l1': 'average_ground_speed', 'l2': 'idle'},

#         'Wrapping': {'l1': 'average_ground_speed', 'l2': 'wrapping'},
#         'Ejecting': {'l1': 'average_ground_speed', 'l2': 'ejecting'},
#         'Forming': {'l1': 'average_ground_speed', 'l2': 'forming'},
#         'Service Wrap': {'l1': 'average_ground_speed', 'l2': 'service_wrap'},
#         'Service Lube': {'l1': 'average_ground_speed', 'l2': 'service_lube'},
#         'Service General': {'l1': 'average_ground_speed', 'l2': 'service_general'},
#         'Harvest': {'l1': 'average_ground_speed', 'l2': 'harvest'},
#         'Maneuvering':{'l1': 'average_ground_speed', 'l2': 'maneuvering'},
#         'Harvesting': {'l1': 'average_ground_speed', 'l2': 'harvesting'},
#         'Harvesting and Unloading': {'l1': 'average_ground_speed', 'l2': 'harvesting_unloading'},
#         'Headland Turn Separator Engaged': {'l1': 'average_ground_speed', 'l2': 'headland_turn_separator_engaged'},
#         'Idle with Grain Tank Full': {'l1': 'average_ground_speed', 'l2': 'idle_grain_tank_full'},
#         'Idle with Grain Tank not Full': {'l1': 'average_ground_speed', 'l2': 'idle_grain_tank_not_full'},
#         'Transport - Road Disconnect On': {'l1': 'average_ground_speed', 'l2': 'transport_road_disconnect_on'}, # TODO: review
#         'Transport - Road Disconnect Off': {'l1': 'average_ground_speed', 'l2': 'transport_road_disconnect_off'}, # TODO: review
#         'Unloading not Harvesting': {'l1': 'average_ground_speed', 'l2': 'unloading_not_harvesting'},

#         'Transport above 16 kph (10 mph) or Road Switch On': {'l1': 'average_ground_speed', 'l2': 'transport_above_sixteen_road_switch_on'},
#         'Transport below 16 kph (10 mph) Separator Off': {'l1': 'average_ground_speed', 'l2': 'transport_below_sixteen_separator_off'},
#         'Idle with Cutterhead Off': {'l1': 'average_ground_speed', 'l2': 'idle_with_cutterhead_off'},
#         'Harvesting High Load': {'l1': 'average_ground_speed', 'l2': 'harvesting_high_load'},
#         'Harvesting Medium Load': {'l1': 'average_ground_speed', 'l2': 'harvesting_medium_load'},
#         'Headland Turn Cutterhead On':{'l1': 'average_ground_speed', 'l2':'headland_turn_cutterhead_on'},
#         'Idle with Cutterhead On': {'l1': 'average_ground_speed', 'l2': 'idle_with_cutterhead_on'},
#         'Transport below 16 kph Cutterhead Off': {'l1': 'average_ground_speed', 'l2': 'transport_below_sixteen_cutterhead_off'},
#         'Harvesting Low Load': {'l1': 'average_ground_speed', 'l2': 'harvesting_low_load'},
#         'Feedroll Reverse': {'l1': 'average_ground_speed', 'l2': 'feedroll_reverse'},
#     },


#     'Avg Engine Load Factor': {

#         'Working': {'l1': 'average_engine_load_factor', 'l2': 'working'},
#         'Transport': {'l1': 'average_engine_load_factor', 'l2': 'transport'},
#         'Idle': {'l1': 'average_engine_load_factor', 'l2': 'idle'},

#         'Maneuvering':{'l1': 'average_engine_load_factor', 'l2': 'maneuvering'},
#         'Wrapping': {'l1': 'average_engine_load_factor', 'l2': 'wrapping'},
#         'Ejecting': {'l1': 'average_engine_load_factor', 'l2': 'ejecting'},
#         'Forming': {'l1': 'average_engine_load_factor', 'l2': 'forming'},
#         'Service Wrap': {'l1': 'average_engine_load_factor', 'l2': 'service_wrap'},
#         'Service Lube': {'l1': 'average_engine_load_factor', 'l2': 'service_lube'},
#         'Service General': {'l1': 'average_engine_load_factor', 'l2': 'service_general'},
#         'Harvest': {'l1': 'average_engine_load_factor', 'l2': 'harvest'},
#         'Harvesting': {'l1': 'average_engine_load_factor', 'l2': 'harvesting'},
#         'Harvesting and Unloading': {'l1': 'average_engine_load_factor', 'l2': 'harvesting_unloading'},
#         'Headland Turn Separator Engaged': {'l1': 'average_engine_load_factor', 'l2': 'headland_turn_separator_engaged'},
#         'Idle with Grain Tank Full': {'l1': 'average_engine_load_factor', 'l2': 'idle_grain_tank_full'},
#         'Idle with Grain Tank not Full': {'l1': 'average_engine_load_factor', 'l2': 'idle_grain_tank_not_full'},
#         'Transport - Road Disconnect On': {'l1': 'average_engine_load_factor', 'l2': 'transport_road_disconnect_on'}, # TODO: review
#         'Transport - Road Disconnect Off': {'l1': 'average_engine_load_factor', 'l2': 'transport_road_disconnect_off'}, # TODO: review
#         'Unloading not Harvesting': {'l1': 'average_engine_load_factor', 'l2': 'unloading_not_harvesting'},

#         'Transport above 16 kph (10 mph) or Road Switch On': {'l1': 'average_engine_load_factor', 'l2': 'transport_above_sixteen_road_switch_on'},
#         'Transport below 16 kph (10 mph) Separator Off': {'l1': 'average_engine_load_factor', 'l2': 'transport_below_sixteen_separator_off'},
#         'Avg Engine Load Factor':{'l1': 'average_engine_load_factor', 'l2': 'avg_engine_load_factor'},

#         'Idle with Cutterhead Off': {'l1': 'average_engine_load_factor', 'l2': 'idle_with_cutterhead_off'},
#         'Harvesting High Load': {'l1': 'average_engine_load_factor', 'l2': 'harvesting_high_load'},
#         'Harvesting Medium Load': {'l1': 'average_engine_load_factor', 'l2': 'harvesting_medium_load'},
#         'Headland Turn Cutterhead On':{'l1': 'average_engine_load_factor', 'l2':'headland_turn_cutterhead_on'},
#         'Idle with Cutterhead On': {'l1': 'average_engine_load_factor', 'l2': 'idle_with_cutterhead_on'},
#         'Transport below 16 kph Cutterhead Off': {'l1': 'average_engine_load_factor', 'l2': 'transport_below_sixteen_cutterhead_off'},
#         'Harvesting Low Load': {'l1': 'average_engine_load_factor', 'l2': 'harvesting_low_load'},
#         'Feedroll Reverse': {'l1': 'average_engine_load_factor', 'l2': 'feedroll_reverse'},
#     },


#     'Time at Engine Load': {
#         '0% - 40%': {'l1': 'time_at_engine_load', 'l2': '000_040'},
#         '40% - 60%': {'l1': 'time_at_engine_load', 'l2': '040_060'},
#         '60% - 80%': {'l1': 'time_at_engine_load', 'l2': '060_080'},
#         '80% - 100%': {'l1': 'time_at_engine_load', 'l2': '080_100'},
#         'Greater than 100%': {'l1': 'time_at_engine_load', 'l2': '100_999'},


#         '0-9 %': {'l1': 'time_at_engine_load', 'l2': '000_040'},
#         '10-19 %': {'l1': 'time_at_engine_load', 'l2': '000_040'},
#         '20-29 %': {'l1': 'time_at_engine_load', 'l2': '000_040'},
#         '30-39 %': {'l1': 'time_at_engine_load', 'l2': '000_040'},
#         '40-49 %': {'l1': 'time_at_engine_load', 'l2': '040_060'},
#         '50-59 %': {'l1': 'time_at_engine_load', 'l2': '040_060'},
#         '60-69 %': {'l1': 'time_at_engine_load', 'l2': '040_060'},
#         '70-79 %': {'l1': 'time_at_engine_load', 'l2': '060_080'}, # maybe 060_080
#         '80-89 %': {'l1': 'time_at_engine_load', 'l2': '080_100'},
#         '90-100 %': {'l1': 'time_at_engine_load', 'l2': '080_100'},

#     },

#     'Road Transport Switch': {
#         'On': {'l1': 'road_transport_switch', 'l2': 'on'},
#         'Off': {'l1': 'road_transport_switch', 'l2': 'off'},
#     },

#     'Auto Header Height (Flex Header)': {
#         'On': {'l1': 'auto_header_height_flex_header', 'l2': 'on'},
#         'Off': {'l1': 'auto_header_height_flex_header', 'l2': 'off'},
#     },

#     'Auto Header Float': {
#         'On': {'l1': 'auto_header_float', 'l2': 'on'},
#         'Off': {'l1': 'auto_header_float', 'l2': 'off'},
#     },

#     'Auto Header Height': {
#         'On': {'l1': 'auto_header_height', 'l2': 'on'},
#         'Off': {'l1': 'auto_header_height', 'l2': 'off'},
#     },

#     'Auto Reel Speed': {
#         'On': {'l1': 'auto_reel_speed', 'l2': 'on'},
#         'Off': {'l1': 'auto_reel_speed', 'l2': 'off'},
#     },

#     'Auto Reel Position': {
#         'On': {'l1': 'auto_reel_position', 'l2': 'on'},
#         'Off': {'l1': 'auto_reel_position', 'l2': 'off'},
#     },

#     'Harvest Smart Active': {
#         'On': {'l1': 'harvest_smart_active', 'l2': 'on'},
#         'Off': {'l1': 'harvest_smart_active', 'l2': 'off'},
#     },

#     'AutoTrac™': {
#         'On': {'l1': 'autotrac', 'l2': 'on'},
#         'Off': {'l1': 'autotrac', 'l2': 'off'},
#         'Active': {'l1': 'autotrac', 'l2': 'on'},
#         'Inactive': {'l1': 'autotrac', 'l2': 'off'},
#         '1': {'l1': 'autotrac', 'l2': 'on'},
#         '0': {'l1': 'autotrac', 'l2': 'off'},
#     },


#     'RowSense™': {
#         'On': {'l1': 'rowsense', 'l2': 'on'},
#         'Off': {'l1': 'rowsense', 'l2': 'off'},
#     },

#     'MFWD': {
#         'On': {'l1': 'mfwd', 'l2': 'on'},
#         'Off': {'l1': 'mfwd', 'l2': 'off'},
#     },

#     'Diff Lock': {
#         'On': {'l1': 'difflock', 'l2': 'on'},
#         'Off': {'l1': 'difflock', 'l2': 'off'},
#     },

#     'Avg Trans Oil Temp': {
#         'Avg Trans Oil Temp': {'l1': 'engine_temperature', 'l2': 'avg_trans_oil_temp'},
#     },

#     'Max Trans Oil Temp': {
#         'Max Trans Oil Temp': {'l1': 'engine_temperature', 'l2': 'max_trans_oil_temp'},
#     },


#     'Wheel Slip Time at Level': {
#         '0.00-2.00%': {'l1': 'wheel_slip_time_at_level', 'l2': 'v0_2'},
#         '2.01-4.00%': {'l1': 'wheel_slip_time_at_level', 'l2': 'v2_4'},
#         '4.01-6.00%': {'l1': 'wheel_slip_time_at_level', 'l2': 'v4_6'},
#         '6.01-8.00%': {'l1': 'wheel_slip_time_at_level', 'l2': 'v6_8'},
#         '8.01-10.00%': {'l1': 'wheel_slip_time_at_level', 'l2': 'v8_10'},
#         '10.01-12.00%': {'l1': 'wheel_slip_time_at_level', 'l2': 'v10_12'},
#         '12.01-14.00%': {'l1': 'wheel_slip_time_at_level', 'l2': 'v12_14'},
#         '14.01-16.00%': {'l1': 'wheel_slip_time_at_level', 'l2': 'v14_16'},
#         '16.01-18.00%': {'l1': 'wheel_slip_time_at_level', 'l2': 'v16_18'},
#         '18.01-100.00%': {'l1': 'wheel_slip_time_at_level', 'l2': 'v18_100'},


#         '2': {'l1': 'wheel_slip_time_at_level', 'l2': 'v0_2'},
#         '4': {'l1': 'wheel_slip_time_at_level', 'l2': 'v2_4'},
#         '6': {'l1': 'wheel_slip_time_at_level', 'l2': 'v4_6'},
#         '8': {'l1': 'wheel_slip_time_at_level', 'l2': 'v6_8'},
#         '10': {'l1': 'wheel_slip_time_at_level', 'l2': 'v8_10'},
#         '12': {'l1': 'wheel_slip_time_at_level', 'l2': 'v10_12'},
#         '14': {'l1': 'wheel_slip_time_at_level', 'l2': 'v12_14'},
#         '16': {'l1': 'wheel_slip_time_at_level', 'l2': 'v14_16'},
#         '18': {'l1': 'wheel_slip_time_at_level', 'l2': 'v16_18'},
#         '100': {'l1': 'wheel_slip_time_at_level', 'l2': 'v18_100'},






#     },

#     'Section Control':{
#         '1': {'l1': 'section_control', 'l2': 'active'},
#         '0': {'l1': 'section_control', 'l2': 'inActive'},
#     },

#     'Ave Engine Speed':{
#         'Transport': {'l1': 'average_engine_speed', 'l2': 'transport'},
#         'Idle': {'l1': 'average_engine_speed', 'l2': 'idle'},
#         'Wrapping': {'l1': 'average_engine_speed', 'l2': 'wrapping'},
#         'Ejecting': {'l1': 'average_engine_speed', 'l2': 'ejecting'},
#         'Forming': {'l1': 'average_engine_speed', 'l2': 'forming'},
#         'Service Wrap': {'l1': 'average_engine_speed', 'l2': 'service_wrap'},
#         'Service Lube': {'l1': 'average_engine_speed', 'l2': 'service_lube'},
#         'Service General': {'l1': 'average_engine_speed', 'l2': 'service_general'},
#         'Harvest': {'l1': 'average_engine_speed', 'l2': 'harvest'},
#     },

#     'Detailed Machine Utilization':{
#         'Transport': {'l1': 'detailed_machine_utilization', 'l2': 'transport'},
#         'Idle': {'l1': 'detailed_machine_utilization', 'l2': 'idle'},
#         'Wrapping': {'l1': 'detailed_machine_utilization', 'l2': 'wrapping'},
#         'Ejecting': {'l1': 'detailed_machine_utilization', 'l2': 'ejecting'},
#         'Forming': {'l1': 'detailed_machine_utilization', 'l2': 'forming'},
#         'Service Wrap': {'l1': 'detailed_machine_utilization', 'l2': 'service_wrap'},
#         'Service Lube': {'l1': 'detailed_machine_utilization', 'l2': 'service_lube'},
#         'Service General': {'l1': 'detailed_machine_utilization', 'l2': 'service_general'},
#         'Harvest': {'l1': 'detailed_machine_utilization', 'l2': 'harvest'},
#     },



#     'Pulsing':{
#         'Active': {'l1': 'pulsing', 'l2': 'active'},
#         'Inactive': {'l1': 'pulsing', 'l2': 'inActive'},
#     },

#     'Avg Machine Speed (Pulsing)':{
#         'Avg Machine Speed (Pulsing)': {'l1': 'average_engine_speed', 'l2': 'avg_machine_speed_pulsing'},
#     },
#     'Avg Machine Speed (Not Pulsing)':{
#         'Avg Machine Speed (Not Pulsing)': {'l1': 'average_engine_speed', 'l2': 'avg_machine_speed_not_pulsing'},
#     },
#     'Application Time':{
#         'On': {'l1': 'application_time', 'l2': 'time'},
#         '1': {'l1': 'application_time', 'l2': 'time'},
#         '0': {'l1': 'application_time', 'l2': 'off'},
#         'On': {'l1': 'application_time', 'l2': 'time'},
#         'Off': {'l1': 'application_time', 'l2': 'off'},
#     },

#     'Active Terrain Adjustment™':{
#         'On': {'l1': 'active_terrain_adjustment', 'l2': 'on'},
#         'Off': {'l1': 'active_terrain_adjustment', 'l2': 'off'},
#     },

#     'Active Yield':{
#         'On': {'l1': 'active_yield', 'l2': 'on'},
#         'Off': {'l1': 'active_yield', 'l2': 'off'},
#     },

#     'FieldCruise™': {
#         'On': {'l1': 'field_cruise', 'l2': 'on'},
#         'Off': {'l1': 'field_cruise', 'l2': 'off'},
#     },

#     'Field Cruise': {
#         'On': {'l1': 'field_cruise', 'l2': 'on'},
#         'Off': {'l1': 'field_cruise', 'l2': 'off'},
#     },
#     #AutoTrac Status

#     'Header Control Response':{
#         'Header Control Response': {'l1': 'cotton_system', 'l2': 'header_control_response'},
#     },

#     'Right Hand Header Height':{
#         'Right Hand Header Height':{'l1': 'cotton_system', 'l2': 'right_hand_header_height'}
#     },

#     'Left Hand Header Height':{
#         'Left Hand Header Height':{'l1': 'cotton_system', 'l2': 'left_hand_header_height'}
#     },

#     'Auto Field Cruise': {
#         'On': {'l1': 'auto_field_cruise', 'l2': 'on'},
#         'Off': {'l1': 'auto_field_cruise', 'l2': 'off'},
#     },

#     'Floating Crop Divider': {
#         'On': {'l1': 'floating_crop_divider', 'l2': 'on'},
#         'Off': {'l1': 'floating_crop_divider', 'l2': 'off'},
#     },

#     'Contour Base-cutter Height Control':{
#         'On': {'l1': 'contour_base_cutter_height_control', 'l2': 'on'},
#         'Off': {'l1': 'contour_base_cutter_height_control', 'l2': 'off'},
#     },

#     'Topper Utilization':{
#         'Left': {'l1': 'topper_utilization', 'l2': 'left'},
#         'Right': {'l1': 'topper_utilization', 'l2': 'right'},
#         'Off': {'l1': 'topper_utilization', 'l2': 'off'},
#     },

#     'Time in Soybeans': {
#         'Time': {'l1': '', 'l2': 'time'},
#     },

#     'IPM™':{
#         'On': {'l1': 'ipm', 'l2': 'on'},
#         'Off': {'l1': 'ipm', 'l2': 'off'},
#     },

#     'Efficiency Manager™ On Time':{
#         'Manual': {'l1': 'efficiency_manager_on_time', 'l2': 'manual'},
#         'Auto': {'l1': 'efficiency_manager_on_time', 'l2': 'auto'},
#     },

}
