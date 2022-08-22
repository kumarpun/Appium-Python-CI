import logging

import pytest
from base.DriverClass import Driver
import time

@pytest.fixture(scope='class')
def beforeClass(request):
    print("Before Class")
    driver1 = Driver()
    # driver = driver1.getDriverMethod()
    driver = driver1.cloudDriver()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()
    print("After Class")

@pytest.fixture()
def beforeMethod():
    print("Before Method")
    yield
    print("After Method")

@pytest.fixture(autouse=True)
def no_logs_gte_error(caplog):
    yield
    errors = [record for record in caplog.get_records('call') if record.levelno >= logging.ERROR]
    assert not errors