import pytest;

def test_second():
    assert 1 == 1
    print("The test_second has passed")


def test_second_string_comparison():
    assert "Karthik" == "Karthik"
    assert "Kar" in "Karthik"
    print("The test_second_string_comparison has passed")

