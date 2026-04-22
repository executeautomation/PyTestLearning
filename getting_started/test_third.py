import pytest;

def test_third():
    assert 1 == 1
    print("The test_third has passed")


class TestThird:

    def test_third_string_comparison(self):
        assert "Karthik" == "Karthik"
        assert "Kar" in "Karthik"
        print("The test_third_string_comparison has passed")


    def test_third_string_comparison_another(self):
        assert "Karthik" == "Karthik"
        assert "Kar" in "Karthik"
        print("The test_third_string_comparison_another has passed")