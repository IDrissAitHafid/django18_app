
from django import test
from selenium.webdriver.firefox import webdriver
from selenium.webdriver.common.keys import Keys
import time


class BasicTestWithSelenium(test.LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.selenium = webdriver.WebDriver()
        super(BasicTestWithSelenium, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(BasicTestWithSelenium, cls).tearDownClass()
        cls.selenium.quit()

    def test_register(self):

        selenium = self.selenium

        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/login/')

        #find sign up id
        time.sleep(2)
        sign_up_nav = selenium.find_element_by_id('sign_up_nav')
        sign_up_nav.click()
        time.sleep(2)

        #find the form element
        first_name = selenium.find_element_by_id('id_first_name')
        last_name = selenium.find_element_by_id('id_last_name')
        username = selenium.find_element_by_id('id_username')
        email = selenium.find_element_by_id('id_email')
        password1 = selenium.find_element_by_id('id_password1')
        password2 = selenium.find_element_by_id('id_password2')
        submit = selenium.find_element_by_id('register')

        #Fill the form with data
        username.send_keys('idriss ait hafid')
        time.sleep(2)
        first_name.send_keys('idriss')
        time.sleep(2)
        last_name.send_keys('ait hafid')
        time.sleep(2)
        email.send_keys('idrissaithafid@gmail.com')
        time.sleep(2)
        password1.send_keys('ayomiTest')
        time.sleep(2)
        password2.send_keys('ayomiTest')

        #submitting the form
        time.sleep(3)
        submit.click()
        time.sleep(2)
        log_out_nav = selenium.find_element_by_id('log_out_nav')
        log_out_nav.click()
        time.sleep(3)

        ##############################
       
        username = selenium.find_element_by_id('id_username')
        password = selenium.find_element_by_id('id_password')
        submit = selenium.find_element_by_id('login')

        #Fill the form with data
        username.send_keys('idriss ait hafid')
        password.send_keys('ayomiTest')


        #submitting the form
        submit.send_keys(Keys.RETURN)
        time.sleep(3)

        #click on modifier les informations
        submit1 = selenium.find_element_by_id('modifier_email')
        submit1.send_keys(Keys.RETURN)

        #insert the new email
        time.sleep(3)
        email = selenium.find_element_by_id('id_email')
        email.click()
        time.sleep(3)
        email.clear()
        time.sleep(3)
        email.send_keys('idriss@ayomi.com')
        
        #click on modifier
        submit2 = selenium.find_element_by_id('update_email')
        submit2.send_keys(Keys.RETURN)
        time.sleep(2)






