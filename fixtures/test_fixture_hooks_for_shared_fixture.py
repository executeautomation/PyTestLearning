class TestDatabaseOperationsForStaging:
    def test_db_connection(self, db_connection):
        assert db_connection == "connected"
        print("The test_db_connection has passed for staging")

    def test_db_connection_another(self, db_connection):
        assert db_connection == "connected"
        print("The test_db_connection_another has passed for staging")
