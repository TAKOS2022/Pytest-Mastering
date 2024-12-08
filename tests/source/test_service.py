import pytest
import pytest_mastering.source.service as service
import unittest.mock as mock

'''
mock_get_user_fron_db arguments will be replace by the value of pytest_mastering.source.service.get_user_from_db
'''
@mock.patch("pytest_mastering.source.service.get_user_from_db")
def test_get_user_from_db(mock_get_user_fron_db):
    # We modify the return value
    mock_get_user_fron_db.return_value = "Mocked Alice"
    user_name = service.get_user_from_db(1)
    assert user_name == "Mocked Alice"