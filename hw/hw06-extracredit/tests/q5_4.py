OK_FORMAT = True

test = {   'name': 'q5_4',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> # There should be exactly as many elements in deck_statistics as the number 'repetitions'\n>>> print(len(deck_statistics) == repetitions)\nTrue\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Each element of deck_statistics should be between 0 and 13 inclusive\n>>> print(all([0 <= k <= 13 for k in deck_statistics]))\nTrue\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
