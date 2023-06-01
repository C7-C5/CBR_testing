from src.baseclasses.currency_class import Valute
from src.baseclasses.compare_class import CompareCurrency
from src.schemas.currency_schema import Currencies
from src.schemas.compare_schema import CurrenciesLib
from src.utils.time import form_date
from configuration import TEST_DATE_FORMAT

def test_status_code(get_response):
    """
    In that test we try to check status code of response from daily quotes endpoint
    :param get_response:
    :return:
    """
    Valute(get_response).assert_status_code(200).validate(Currencies)


def test_reference_status_code(get_reference_response):
    """
   In that test we try to check status code of response from currency codes reference endpoint
   :param get_response:
   :return:
   """
    CompareCurrency(get_reference_response).assert_status_code(200).validate(CurrenciesLib)


def test_response_date(get_response):
    """
    In that test we try to check an accordance of date of response with the current date
    :param get_response:
    :return:
    """
    test_object = Valute(get_response).validate(Currencies)
    date = form_date(TEST_DATE_FORMAT)
    test_object.assert_response_date(date)

def test_compare_attributes(get_response, get_reference_response):
    """
    In that test we try to compare data from daily quotes endpoint with data from currency codes reference endpoint
    :param get_response:
    :param get_reference_response:
    :return:
    """
    test_object = Valute(get_response).validate(Currencies)
    compare_object = CompareCurrency(get_reference_response).validate(CurrenciesLib)
    for value in test_object.valute_object.values:
        compare_object.assert_currency(value)
