from Hello_module import Hello


def test_Fn_Hello():
    assert Hello('Python') == "Hello Pytho, howdy!"


if __name__ == "__main__":
    try:
        test_Fn_Hello()
    except AssertionError:
        print('Name does not match')