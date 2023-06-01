from datetime import datetime, timedelta
from configuration import TEST_DATE_FORMAT

def find_past_date(day):
    """
    function for calculating weekend
    :param day:
    :return:
    """
    now = datetime.now()
    date = (now - timedelta(days=day)).strftime(TEST_DATE_FORMAT)
    return date

print(find_past_date(1))

def form_date(pattern):
    date = datetime.now().strftime(pattern)
    return date