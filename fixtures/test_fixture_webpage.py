import pytest;

@pytest.fixture
def page_detail():
    return {"url": "http://eaapp.somee.com", "name": "ExecuteAutomation Employee App"}

@pytest.fixture
def environment_details():
    return {"env":"production", "version":"2.0"}

def test_ea_app_for_production(page_detail, environment_details):
    print(f"Testing {page_detail['name']} at {page_detail['url']} in {environment_details['env']} environment with version {environment_details['version']}")
