import pytest;
import time


# Scope for Function - The fixture will be invoked for each test function
# Scope for Class - The fixture will be invoked once per test class, and all test methods in that class will share the same fixture instance
# Scope for Module - The fixture will be invoked once per module, and all test functions in that module will share the same fixture instance
# Scope for Session - The fixture will be invoked once per test session, and all test functions across all modules will share the same fixture instance

class TestDatabaseOperationsForProduction:
    def test_db_connection(self, db_connection):
        assert db_connection == "connected"
        print("The test_db_connection has passed for production")

    def test_db_connection_another(self, db_connection):
        assert db_connection == "connected"
        print("The test_db_connection_another has passed for production")


class TestDatabaseOperations:
    def test_db_connection(self, db_connection):
        assert db_connection == "connected"
        print("The test_db_connection has passed")

    def test_db_connection_another(self, db_connection):
        assert db_connection == "connected"
        print("The test_db_connection_another has passed")