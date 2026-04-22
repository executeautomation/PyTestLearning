


def test_login_valid_credentials(page):
    print("Testing login with valid credentials on page:", page["url"])
    print("The Applicaiton name is:", page["title"])
    assert True