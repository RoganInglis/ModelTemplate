
def test_out(pass_condition, name):
    if pass_condition:
        print('Passed: ' + name)
        return True
    else:
        print('Failed: ' + name)
        return False