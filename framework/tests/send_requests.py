import pytest as pytest


from app.api.api_client import ApiClient


@pytest.fixture
def get_token():
    return ApiClient().login()


def test_root_folder_succesfull(get_token):
    assert ApiClient().get_root_folder(get_token) is 200


def test_count_succesfull(get_token):
    assert ApiClient().get_count(get_token) is not None


def test_runs_succesfull(get_token):
    assert ApiClient().get_runs(get_token) is 200


def test_analyses_succesfull(get_token):
    assert ApiClient().get_analyses(get_token) is 200


def test_artifacts_succesfull(get_token):
    assert ApiClient().get_artifacts(get_token) is 200