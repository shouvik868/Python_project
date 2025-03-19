import sys
import pytest
import pytest_html
from datetime import datetime
from pytest_metadata.plugin import metadata_key
from selenium import webdriver


# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests")

@pytest.fixture()
def chromedriverSetup():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=options)
    return driver
@pytest.fixture()
def firefoxdriverSetup():
    driver = webdriver.Firefox()
    return driver
@pytest.fixture()
def edgedriverSetup():
    driver = webdriver.Edge()
    return driver

@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        print("Launching chrome browser")
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(options=options)
        return driver

    elif browser=="firefox":
        print("Launching Firefox browser")
        driver = webdriver.Firefox()
        return driver

    elif browser=="edge":
        print("Launching Edge browser")
        driver = webdriver.Edge()
        return driver
        print("Launching Edge browser")
    else:
        print("Wrong browser name..")

def pytest_addoption(parser):
    #parser.addoption("--browser")
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests")
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
#html report
def pytest_html_report_title(report):
        report.title = "Test_Report_"+str(datetime.now())
def pytest_configure(config):
    config.stash[metadata_key]["Project Name"] = "Open Cart"
    config.stash[metadata_key]["Module Name"] = "Open Cart-Suite"
    config.stash[metadata_key]["Tester"] = "Shouvik Biswas"

#@pytest.mark.optionalhook
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
