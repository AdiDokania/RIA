import time
from selenium.webdriver.common.by import By
from Configuration.config import TestData
from Pages.BasePage import BasePage


class ProductPage(BasePage):

    SearchBox = (By.ID, "twotabsearchtextbox")
    SearchSymbol = (By.ID, "nav-search-submit-button")
    SeeMore = (By.XPATH, "//div[@id = 'brandsRefinements']/ul/li[8]/span/div/a/span[text() ='See more']")
    TitanCheckbox = (By.XPATH, "//li[@id ='p_89/Titan']/span/a/div/label/i")
    AnalogueCheckbox = (By.XPATH, "//li[@aria-label='Analogue']/span/a/div/label/i")
    LeatherCheckbox = (By.XPATH, "//li[@aria-label='Leather']/span/a/div/label/i")
    Discount = (By.XPATH, "//span[text()='25% Off or more']")
    FifthElement = (By.XPATH, "//span[@data-component-type='s-search-results']/div[2]/div[@data-index='6']")
    TenthElement = (By.XPATH, "//span[@data-component-type='s-search-results']/div[2]/div[@data-index='11']")
    FiftheenElement = (By.XPATH, "//span[@data-component-type='s-search-results']/div[2]/div[@data-index='17']")
    Price1 = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[7]/div/div/div/div/div[2]/div[3]/div/a/span[1]/span[2]/span[2]")
    Name1 = (By.XPATH, "//div[@data-index='6']/div/div/div/div/div[2]/div/h2/a/span")
    Price2 = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[12]/div/div/div/div/div[2]/div[3]/div/a/span[1]/span[2]/span[2]")
    Name2 = (By.XPATH, "//div[@data-index='11']/div/div/div/div/div[2]/div/h2/a/span")
    Name3 =(By.XPATH, "//div[@data-index='17']/div/div/div/div/div[2]/div/h2/a/span")
    Price3 =(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[18]/div/div/div/div/div[2]/div[3]/div/a/span[1]/span[2]/span[2]")
    Discount1 =(By.XPATH, "//div[@data-index='6']/div/div/div/div/div[2]/div[3]/div/span[2]")
    Discount2 = (By.XPATH, "//div[@data-index='11']/div/div/div/div/div[2]/div[3]/div/span[2]")
    Discount3 = (By.XPATH, "//div[@data-index='17']/div/div/div/div/div[2]/div[3]/div/span[2]")
    BrandName1 = (By.XPATH, "//table[@id='technicalSpecifications_section_1']/tbody/tr[4]/td")
    MaterialName1 = (By.XPATH, "//table[@id='technicalSpecifications_section_1']/tbody/tr[2]/td")
    DeliveryType =(By.XPATH, "//div[@id='deliveryBlockContainer']/div/div/div/div/span/a[text()='FREE delivery']")
    FulfilledBy = (By.XPATH, "//div[@id='shipsFromSoldByInsideBuyBox_feature_div']/div/div/a[2]/span[text()='Fulfilled by Amazon']")

    def __init__(self, driver):
        super().__init__(driver)

    def search_product(self):
        self.do_send_keys(self.SearchBox, "Wrist Watches")
        self.do_click(self.SearchSymbol)
        time.sleep(1)
        self.do_click(self.SeeMore)
        self.do_click(self.TitanCheckbox)
        time.sleep(1)
        self.do_click(self.AnalogueCheckbox)
        self.do_click(self.LeatherCheckbox)
        self.do_click(self.Discount)
        time.sleep(2)

    def get_productDetails1(self):
        Price1 = self.get_element_text(self.Price1)
        time.sleep(1)
        Name1 = self.get_element_text(self.Name1)
        Discount1 = self.get_element_text(self.Discount1)
        NumDis =""
        for c in Discount1:
            if c.isdigit():
                NumDis =NumDis + c
        print(NumDis)
        return int(NumDis)

    def get_productDetails2(self):
        Price2 = self.get_element_text(self.Price2)
        time.sleep(1)
        Name2 = self.get_element_text(self.Name2)
        Discount2 = self.get_element_text(self.Discount2)

    def get_productDetails3(self):
        Price3 = self.get_element_text(self.Price3)
        time.sleep(1)
        Name3 = self.get_element_text(self.Name3)
        Discount3 = self.get_element_text(self.Discount3)

    def validate_detailsof_product1(self):
        self.do_click(self.Name1)
        time.sleep(5)
        self.window_handle()

    def validate_product1_brand(self):
        BrandName = self.get_element_text(self.BrandName1)
        return BrandName
        time.sleep(5)

    def validate_product1_Material(self):
        Material = self.get_element_text(self.MaterialName1)
        return Material

    def validate_product1_DeliveryType(self):
        DeliveryType = self.get_element_text(self.DeliveryType)
        return DeliveryType

    def validate_product1_FulfillmentType(self):
        FulfilledBy = self.get_element_text(self.FulfilledBy)
        return FulfilledBy






