OK_FORMAT = True

test = {   'name': 'q3_1',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> print(full_data.num_rows -- 562)\n1124\n', 'hidden': False, 'locked': False},
                                   {   'code': ">>> # Double check the way you're combining the two tables. Are you combining in the correct order (in terms of the arguments)?\n"
                                               '>>> # The problem statement saying "except \'Name\' column" is a hint at the order in which you should combine the tables.\n'
                                               ">>> print(list(full_data.labels)[0] == 'Player')\n"
                                               'True\n',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> print(full_data.select(sorted(full_data.labels)).sort(4).take(range(3)).column(0).item(0) == 0.6)\nTrue\n', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
