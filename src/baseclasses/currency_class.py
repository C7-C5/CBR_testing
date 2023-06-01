from src.schemas.compare_schema import CurrenciesLib
from xsdata.formats.dataclass.parsers import XmlParser
from src.enums.global_enums import ErrorMessages
from datetime import datetime
from src.utils.time import find_past_date


class Valute:
    """
    class for validation data from Currency schema
    """

    def __init__(self, response):
        self.response = response
        self.response_status_code = self.response.status_code
        self.response_xml = response.text.replace('<?xml version="1.0" encoding="windows-1251"?>', '')
        self.valute_object = None

    def validate(self, data_class):
        self.valute_object = XmlParser().from_string(self.response_xml, data_class)

        return self


    def assert_status_code(self, status_code):
        """
        method for check status code of our response from API
        :param status_code: 200 by default
        :return:
        """
        if isinstance(status_code, list):
            assert self.response_status_code in status_code, ErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status_code == status_code, ErrorMessages.WRONG_STATUS_CODE.value

        return self

    def assert_response_date(self, request_date):
        """
        method for check date from response attribute Date.
        Documentation from CBR says, that xml-form doesn't forms every date, so i made a check for a days, on which form
         definietley doesn't -  for weekend
        :param request_date: by default today
        :return:
        """

        if datetime.weekday(request_date) in [5, 6]:
            assert self.valute_object.date in (find_past_date(1), find_past_date(2)), ErrorMessages.WRONG_DATE.value
        else:
            assert self.valute_object.date == request_date, ErrorMessages.WRONG_DATE.value

