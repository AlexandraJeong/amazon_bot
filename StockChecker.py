import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class AutoBuy:
    def __init__(self,x,y):#x is url of the item to watch, y is maximum buying price
        print(x)
        self.limitPrice=y
        self.username="username"#enter your username
        self.password="password"#enter your password
        self.url=x
        self.driver = webdriver.Chrome('C:\\Users\\lexij\\OneDrive\\Documents\\Personal\\chromedriver_win32\\chromedriver.exe')
    def logIn(self):
        self.driver.get(self.url)
        time.sleep(2)
        try:
            self.driver.find_element_by_class_name("a-icon a-icon-close a-icon-medium aod-close-button").click()
        except:
            pass
        try:
            self.driver.find_element_by_id("nav-link-accountList-nav-line-1").click()
        except:
            pass
        try:
            self.driver.find_element_by_id("nav-line-2 nav-short-width").click()
        except:
            pass
        self.driver.find_element_by_id("ap_email").send_keys(self.username+Keys.ENTER)
        self.driver.find_element_by_id("ap_password").send_keys(self.password+Keys.ENTER)
        self.driver.get(self.url)
    def infiniteCheck(self):
        inStock=False
        while inStock==False:
            siteText = self.driver.find_element_by_tag_name('body')
            str1=siteText.text.lower()
            str1= str1[0:str1.find("about this item")]
            if (str1.find("currently unavailable")!=-1):
                print("currently unavailable")
            elif(str1.find("in stock")!=-1):
                inStock=True
                print("in stock\n"+self.url)
            else:
                self.driver.find_element_by_id("buybox-see-all-buying-choices").click()
                time.sleep(2)
                try:
                    price = int(self.driver.find_element_by_class_name("a-price-whole").text.replace(',',''))
                    print(price)
                    if(price<self.limitPrice):
                        print("less than "+str(self.limitPrice))
                        inStock=True
                except:
                    print("not in stock")
            if inStock==False:
                self.driver.refresh()
                time.sleep(1)
    def buyItem(self):
        print("buying")
        try:
            self.driver.find_element_by_id("addToCart_feature_div").click()
        except:
            pass
        try:
            self.driver.find_element_by_id("a-autoid-2").click()
        except:
            pass
        try:
            self.driver.find_element_by_id("hlb-ptc-btn-native").click()
        except:
            pass
        try:
            self.driver.find_element_by_class_name("proceedToRetailCheckout").click()
        except:
            pass
        try:
            self.driver.find_element_by_id("ap_password").send_keys(self.password+Keys.ENTER)
        except:
            pass
        try:
            self.driver.find_element_by_id("placeYourOrder").click()
        except:
            pass
        try:
            self.driver.find_element_by_id("submitOrderButtonId").click()
        except:
            pass
        time.sleep(60)
        self.driver.refresh()
