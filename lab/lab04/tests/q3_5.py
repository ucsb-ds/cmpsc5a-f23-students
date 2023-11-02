OK_FORMAT = True

test = {   'name': 'q3_5',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> "(No previous year)" not in with_previous_compensation.column("% Change")\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> t = with_previous_compensation.sort("2014 Total Pay ($)", descending = True)\n'
                                               '>>> value = t.column("2014 Total Pay ($)").item(0)\n'
                                               '>>> np.isclose(value, 67700000.0, rtol = 0.01)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> with_previous_compensation.num_rows == 81\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
