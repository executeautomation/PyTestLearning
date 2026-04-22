import pytest;

@pytest.fixture(scope="session")
def browser():
    print("Setting up browser")
    b = {"name": "chrome", "version": "100.0", "platform": "windows"}

    yield b

    print("Tearing down browser")

@pytest.fixture(scope="module")
def page(browser):
    print("Setting up page with browser:", browser["name"])
    p = {"url": "http://eaapp.somee.com", "title": "EA Employee App"}

    yield p

    print("Tearing down page")

