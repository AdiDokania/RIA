import time
from behave import *
from selenium import webdriver
from Configuration.config import TestData
from Pages.ProductPage import ProductPage
from Utilities.CustomLogger import LogGen

global ppage
mylogger = LogGen.logger()

@given('Amazon is launched in Chrome')
def launch_browser(context):
    context.driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    mylogger.info("**** Driver Initialized ****")
    time.sleep(5)
    context.driver.maximize_window()
    context.driver.get(TestData.BASEURL)
    time.sleep(5)
    mylogger.info("** URL Launched **")

@when('We Select product Category')
def set_Email_Address(context):
    mylogger.info("** Search Products **")
    ppage = ProductPage(context.driver)
    ppage.search_product()

@then('We fetch product Details')
def set_Email_Address(context):
    mylogger.info("** Fetch Product Details **")
    ppage = ProductPage(context.driver)
    DisCount1 = ppage.get_productDetails1()
    if int(DisCount1) >= 25:
        assert True
        mylogger.info("**Discount Verified **")
    else:
        mylogger.info("**Discount Not Verified **")
        assert False
    ppage.get_productDetails2()
    ppage.get_productDetails3()

@then('We Validate details of Product1')
def set_Email_Address(context):
    mylogger.info("** Validate Product Details **")
    ppage = ProductPage(context.driver)
    ppage.validate_detailsof_product1()
    BrandName1 = ppage.validate_product1_brand()
    if BrandName1 == "Titan":
        assert True
        mylogger.info("**Brand Verified **")
    else:
        mylogger.info("**Brand Not Verified **")
        assert False
    Material1 = ppage.validate_product1_Material()
    if Material1 == "Leather":
        assert True
        mylogger.info("**Material Verified **")
    else:
        mylogger.info("**Material Not Verified **")
        assert False
    DeliveryType1 = ppage.validate_product1_DeliveryType()
    if DeliveryType1 == "FREE delivery":
        assert True
        mylogger.info("**Delivery Verified **")
    else:
        mylogger.info("**Delivery Not Verified **")
        assert False
    FulfilledBy1 = ppage.validate_product1_FulfillmentType()
    if FulfilledBy1 == "Fulfilled by Amazon":
        assert True
        mylogger.info("**Fulfilled Verified **")
    else:
        mylogger.info("**Fulfiled Not Verified **")
        assert False


