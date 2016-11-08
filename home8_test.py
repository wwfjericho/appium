import os
import unittest
from appium import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class Home8Tests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0'
        desired_caps['deviceName'] = '4d00302557b9606f'
        desired_caps['app'] = PATH(
            'D:/automation/home8.apk'
            #'../../../sample-code/apps/ContactManager/home8.apk'
        )
        desired_caps['appPackage'] = 'com.oplk.dragon'
        desired_caps['appActivity'] = 'com.oplk.dragon.OGFamilyAppActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_add_contacts(self):

       self.driver.find_element_by_id('com.oplk.dragon:id/configuration_menu_item').click() #Click configuration button
       self.driver.find_element_by_name('C4mi Server').click()
       self.driver.swipe(87,1611,87,297)
       self.driver.find_element_by_name('sqa.tp.oplab72').click()
       self.driver.press_keycode(4)
       self.driver.find_element_by_name('Agree & Continue').click()
       self.driver.find_element_by_name('OK').click()
       textfields = self.driver.find_elements_by_class_name("android.widget.EditText")
       textfields[1].send_keys("12345678")
       self.driver.find_element_by_name('Sign In').click()
       self.driver.find_element_by_name('Yes').click()
       sleep(10)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Home8Tests)
    unittest.TextTestRunner(verbosity=2).run(suite)
