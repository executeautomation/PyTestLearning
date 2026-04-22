import pytest;
import time;

@pytest.fixture(scope="session")
def db_connection():
    connection = "connected"
    print(f"Setting up database connection - {connection}")
    time.sleep(2)

    yield connection

    connection = "disconnected"
    print(f"Tearing down database connection - {connection}")