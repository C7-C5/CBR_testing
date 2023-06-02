from xsdata.formats.dataclass.parsers import XmlParser
from src.enums.global_enums import ErrorMessages

class CompareCurrency:
    """
    class for validation data from Currency schema
    """
    def __init__(self, response):
        self.response = response
        self.response_status_code = self.response.status_code
        self.response_xml = response.text.replace('<?xml version="1.0" encoding="windows-1251"?>', '')
        self.compare_object = None

    def validate(self, schema):
        self.compare_object = XmlParser().from_string(self.response_xml, schema)

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

    def assert_currency(self, obj):
        """
        method designed to compare data from daily quotes endpoint with data from currency codes reference endpoint
        :param obj: Currency object with all attributes
        :return:
        """
        compare_obj = next((currency for currency in self.compare_object.values if currency.id == obj.id), None)
        if not compare_obj:
            raise ValueError(f'{ErrorMessages.WRONG_ID.value}, ID: {obj.id}, name: {obj.name}')

        assert compare_obj.num_code == str(obj.num_code), f'{ErrorMessages.WRONG_NUM_CODE.value},' \
                                                     f' num code: {obj.num_code}, valid num code: {compare_obj.num_code}'
        assert compare_obj.char_code == obj.char_code, f'{ErrorMessages.WRONG_CHAR_CODE.value}, ' \
                                                       f'char code: {obj.char_code}, valid char code: {compare_obj.char_code}'



