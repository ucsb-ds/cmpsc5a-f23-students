OK_FORMAT = True

test = {   'name': 'q4_3',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> # It looks like your maximums array is empty!\n>>> print(len(maximums) != 0)\nTrue\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> print(len(maximums) == 5000)\nTrue\n', 'hidden': False, 'locked': False},
                                   {   'code': ">>> # The biggest simulated maximum can't be bigger than the actual maximum!\n>>> print(max(maximums) <= max(earthquakes.column('mag')))\nTrue\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
