import pytest
import pytest_mastering.source.service as service
import unittest.mock as mock
import requests

'''
mock_get_user_fron_db arguments will be replace by the value of pytest_mastering.source.service.get_user_from_db
'''
@mock.patch("pytest_mastering.source.service.get_user_from_db")
def test_get_user_from_db(mock_get_user_fron_db):
    # We modify the return value
    mock_get_user_fron_db.return_value = "Mocked Alice"
    user_name = service.get_user_from_db(1)

    assert user_name == "Mocked Alice"

# We don't want to test the functions but the response
@mock.patch("requests.get")
def test_get_users(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "id": 1, "name": "John Doe"
    }
    mock_get.return_value = mock_response
    data = service.get_users()
    assert data ==  {"id": 1, "name": "John Doe"}


# This function test the status code of the request. The status should be different to 200. 
# If status = 200 it will fail. 
@mock.patch("requests.get")
def test_get_users_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_get.return_value = mock_response
    with pytest.raises(requests.HTTPError):
        service.get_users()