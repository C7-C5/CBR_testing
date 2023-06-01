import pytest
import requests
from configuration import CRB_URL, REFERENCE_URL, URL_DATE_FORMAT
from src.utils.time import form_date


@pytest.fixture
def get_response():
    response = requests.get(CRB_URL + form_date(URL_DATE_FORMAT))
    return response

@pytest.fixture
def get_reference_response():
    response = requests.get(REFERENCE_URL)
    return response
