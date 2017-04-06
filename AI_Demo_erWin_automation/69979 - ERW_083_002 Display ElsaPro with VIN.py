import unittest
import time
import HTMLTestRunner

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

url = "http://audi-pilot.erwin-portal.com"
key = "erWin"
usr = "user1"
pwd = "Password00"
AUDI_VIN = "WAUZZZ8T88A001190"


class ErwinLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Ie() #instance of IE webdriver
        print "\n\n\n Successfully opened the IE Browser!"
        
        
    def login_erwin(self):
        driver = self.driver
        driver.get(url) #enter url
        print "\nerWin Welcome Page is displayed"
        self.assertIn(key, driver.title) #assertion to confirm that title has <<key>> word in it 
        username = driver.find_element_by_name('loginName')
        username.send_keys(usr)#enter username
        print "\nuser name entered"
        password = driver.find_element_by_name('password')
        password.send_keys(pwd)#enter password
        print "\npassword entered"
        time.sleep(2)
        #password.send_keys(Keys.CONTROL + Keys.RETURN + "2")
        search_box = driver.find_element_by_xpath("html/body/div[1]/div[2]/div[3]/aside/div[1]/form/div[3]/span/input")
        search_box.click()
        print "\nPressed Login Button"
        time.sleep(1)
        search_box = driver.find_element_by_xpath(".//*[@id='agreeToDisclaimerForm']/div/div/span/input")
        search_box.click()
        print "\nDisclaimer accepted"
        print "\nLogin Successful"        

    def logout_erwin(self):
         driver = self.driver
         search_box = driver.find_element_by_xpath(".//*[@id='root']/li[5]/span/span")
         search_box.click()
         time.sleep(2)
         search_box = driver.find_element_by_xpath(".//*[@id='root']/li[5]/ul/li[6]/a")
         search_box.click()
         time.sleep(5)
         print "\n Successfully Logged Out!"

    def test_69979(self):
         try:
             print 'Start!!!'
             driver = self.driver
             self.login_erwin()
             
             search_box = driver.find_element_by_xpath(".//*[@id='root']/li[3]/span/span")
             search_box.click()
             time.sleep(2)
             search_box = driver.find_element_by_xpath(".//*[@id='root']/li[3]/ul/li/a")
             search_box.click()
             time.sleep(2)
             print "\nStep 2 successful"
             search_box = driver.find_element_by_id('form_vin')
             time.sleep(1)
             search_box.clear()
             search_box.send_keys(AUDI_VIN)
             time.sleep(2)
             print "\nStep 3 successful"
             search_box = driver.find_element_by_xpath(".//*[@id='searchExpert']/div[2]/span/input")
             search_box.click()
             time.sleep(5)
             print "\nStep 4 successful"
             driver.switch_to_alert();
             time.sleep(2)
             search_box = driver.find_element_by_xpath(".//*[@id='serviceHints']/button")
             search_box.click()
             print "\nAlert accepted"
             time.sleep(5)
             driver.switch_to_default_content()
             time.sleep(2)
             search_box = driver.find_element_by_xpath("html/body/div[1]/div[2]/div[1]/nav/ul/li[4]/a")
             search_box.click()
             print "\nStep 5 successful"
             time.sleep(5)          
             
             self.logout_erwin()
         except:
            print 'Exception occurred!!!'
                              
        
    def tearDown(self):
        time.sleep(2)
        self.driver.close()
        print "\n\n\n Successfully Closed the IE Browser!"


if __name__ == '__main__':
    test_classes_to_run = [ErwinLogin]

    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    filename = "erWinTestReport.html"
    output = open (filename,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=output,title="erWin Test report")
    results = runner.run(big_suite)


