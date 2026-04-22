import pytest;

def test_first():
    assert 1 == 1
    names = ["Karthik", "Suresh", "Ramesh"]
    assert "Karthik" in names
    users1 = {"Karthik": 30, "Suresh": 25, "Ramesh": 35}
    users2 = {"Karthik": 23, "Suresh": 25, "Ramesh": 35}
    assert users1 == users2
    print("The test_first has passed")
    

def test_string_assertions():
    name = "Karthik"
    assert name == "Karthik"
    assert name.lower() == "karthik"
    assert name.startswith("Kar")
    assert name.endswith("thik")

def test_floating_point_comparison():
    result =0.2 + 0.1
    assert pytest.approx(result) == 0.3

def test_first_string_comparison():
    assert "Karthik" == "Karthik"
    assert "Kar" in "Karthik"
    print("The test_first_string_comparison has passed")


def test_second_string_comparison():
    assert "Karthik" == "Karthik"
    assert "Car" in "Karthik"
    print("The test_second_string_comparison has passed")
