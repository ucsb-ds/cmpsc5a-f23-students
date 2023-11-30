OK_FORMAT = True

test = {   'name': 'q2_3',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> print(len(simulate_several_key_strikes(15)) == 15)\nTrue\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> print(isinstance(simulate_several_key_strikes(15), str))\nTrue\n', 'hidden': False, 'locked': False},
                                   {   'code': ">>> # It looks like your simulation doesn't use all the letters, or it uses more than the 26 lower-case letters.\n"
                                               '>>> import numpy as np\n'
                                               '>>> np.random.seed(22)\n'
                                               '>>> print(62 >= len(np.unique(list(simulate_several_key_strikes(500)))) >= 45)\n'
                                               'True\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
