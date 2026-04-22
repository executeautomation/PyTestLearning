import pytest;

@pytest.fixture
def user():
    return {"name": "Karthik", "age": 30, "city": "Auckland"}



def test_user_name(user):
    assert user["name"] == "Karthik"
    print(f"The test_user_name has passed for user {user['name']}")


def test_user_city(user):
    assert user["city"] == "Auckland"
    print(f"The test_user_city has passed for user {user['name']}")


def test_user_age(user):
    assert user["age"] == 30
    print(f"The test_user_age has passed for user {user['name']}")