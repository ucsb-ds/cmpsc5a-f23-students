OK_FORMAT = True

test = {   'name': 'q1_1_5',
    'points': [0, 0, 1],
    'suites': [   {   'cases': [   {'code': '>>> print(len(cities.labels) == 8)\nTrue\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> print(cities.labels[-1] == "Region")\nTrue\n', 'hidden': False, 'locked': False},
                                   {'code': ">>> print(cities.row(0).item('Region') == 'Northwest')\nTrue\n", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
