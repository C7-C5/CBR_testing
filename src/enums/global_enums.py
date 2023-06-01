from enum import Enum


class ErrorMessages(Enum):
    WRONG_STATUS_CODE = "Wrong status code!"
    WRONG_DATE = "Response have a wrong date!"
    WRONG_ID = "Currency have invalid ID!"
    WRONG_NAME = "Currency have invalid name!"
    WRONG_NOMINAL = "Currency have invalid nominal!"
    WRONG_NUM_CODE = "Currency have invalid num code!"
    WRONG_CHAR_CODE = "Currency have invalid char code!"