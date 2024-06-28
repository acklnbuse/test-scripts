def test_function(x):
    return x + 1

def test_test_function():
    assert test_function(3) == 4
    assert test_function(-1) == 0
    print("All tests passed!")

if __name__ == "__main__":
    test_test_function()
