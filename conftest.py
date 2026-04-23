

def pytest_configure(config):
    config.addinivalue_line("markers", "smoke: mark a test as smoke test")
    config.addinivalue_line("markers", "regression: mark a test as regression test")
    config.addinivalue_line("markers", "slow: mark a test as slow test")