from Hello_module import Hello


def test_Fn_Hello():
    assert Hello('Ranjith') == "Hello Ranjith, howdy!"
    return 'Test Passed!'


if __name__ == "__main__":
    try:
        print(test_Fn_Hello())
    except AssertionError:
        print('Test Failed!, Name does not match')