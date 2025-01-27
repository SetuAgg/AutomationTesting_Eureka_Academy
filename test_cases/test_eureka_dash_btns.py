import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver

from base_pages.Eureka_Dash_Btns import Eureka_Dash_Btns
from base_pages.Eureka_Main_Screen import Eureka_Main_Screen
from test_cases.configurations import setup
import time
import allure

class Test_08_Eureka_Dash_Btns:
    page_url = "https://eurekaacademy-preprod.niit.com"
    username = "3014029@mailinator.com"
    password = "Eureka@123"

    def test_dash_btns(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        self.main_screen = Eureka_Main_Screen(self.driver)
        self.main_screen.enter_username(self.username)
        self.main_screen.enter_password(self.password)
        self.main_screen.click_login_button()
        time.sleep(3)
        self.admin_lp = Eureka_Dash_Btns(self.driver)
        self.admin_lp.click_program_tab()
        time.sleep(3)
        element1 = self.driver.find_element(By.XPATH,'//h3[@class="program-head"]')
        time.sleep(2)
        self.driver.execute_script("arguments[0].style.border='5px solid magenta'", element1)
        time.sleep(2)
        if element1.is_displayed():
            assert True
            time.sleep(2)
            allure.attach(self.driver.get_screenshot_as_png(), name='test_dash_btns', attachment_type=allure.attachment_type.PNG)
            message01 = "Dash Button is visible and test-case passed successfully.."
            allure.attach(message01, name="Dash_Button", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_dash_btns', attachment_type=allure.attachment_type.PNG)
            message02 = "Dash Button is not visible and test-case failed.."
            allure.attach(message02, name="Dash_Button", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        self.admin_lp.click_courses_tab()
        time.sleep(3)
        element2 = self.driver.find_element(By.XPATH,'//h3[@class="program-head"]')
        time.sleep(2)
        self.driver.execute_script("arguments[0].style.border='5px solid magenta'", element2)
        if element2.is_displayed():
            assert True
            time.sleep(2)
            allure.attach(self.driver.get_screenshot_as_png(), name='test_dash_btns', attachment_type=allure.attachment_type.PNG)
            message03 = "Dash Button is visible and test-case passed successfully.."
            allure.attach(message03, name="Dash_Button", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_dash_btns', attachment_type=allure.attachment_type.PNG)
            message04 = "Dash Button is not visible and test-case failed.."
            allure.attach(message04, name="Dash_Button", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        self.admin_lp.click_session_tab()
        time.sleep(3)
        element3 = self.driver.find_element(By.XPATH,'//p[@class="lable-heading_search"]')
        time.sleep(2)
        self.driver.execute_script("arguments[0].style.border='5px solid magenta'", element3)
        if element3.is_displayed():
            assert True
            time.sleep(2)
            allure.attach(self.driver.get_screenshot_as_png(), name='test_dash_btns', attachment_type=allure.attachment_type.PNG)
            message05 = "Dash Button is visible and test-case passed successfully.."
            allure.attach(message05, name="Dash_Button", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_dash_btns', attachment_type=allure.attachment_type.PNG)
            message06 = "Dash Button is not visible and test-case failed.."
            allure.attach(message06, name="Dash_Button", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        self.admin_lp.click_assessments_tab()
        time.sleep(3)
        element4 = self.driver.find_element(By.XPATH,'//h3[@class="program-head"]')
        time.sleep(2)
        self.driver.execute_script("arguments[0].style.border='5px solid magenta'", element4)
        if element4.is_displayed():
            assert True
            time.sleep(2)
            allure.attach(self.driver.get_screenshot_as_png(), name='test_dash_btns', attachment_type=allure.attachment_type.PNG)
            message07 = "Dash Button is visible and test-case passed successfully.."
            allure.attach(message07, name="Dash_Button", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_dash_btns', attachment_type=allure.attachment_type.PNG)
            message08 = "Dash Button is not visible and test-case failed.."
            allure.attach(message08, name="Dash_Button", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        self.admin_lp.click_back_btn()
        time.sleep(2)
        self.admin_lp.click_feedback_tab()
        time.sleep(3)
        element8 = self.driver.find_element(By.XPATH,'//div[@class="modal-content"]')
        time.sleep(2)
        self.driver.execute_script("arguments[0].style.border='5px solid magenta'", element8)
        if element8.is_displayed():
            assert True
            time.sleep(2)
            allure.attach(self.driver.get_screenshot_as_png(), name='test_dash_btns', attachment_type=allure.attachment_type.PNG)
            message15 = "Dash Button is visible and test-case passed successfully.."
            allure.attach(message15, name="Dash_Button", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_dash_btns', attachment_type=allure.attachment_type.PNG)
            message16 = "Dash Button is not visible and test-case failed.."
            allure.attach(message16, name="Dash_Button", attachment_type=allure.attachment_type.TEXT)
            assert False
        self.admin_lp.click_skip_btn()
        time.sleep(3)
        self.admin_lp.click_view_join_tab()
        time.sleep(3)
        element9 = self.driver.find_element(By.XPATH,'//p[@class="lable-heading_search"]')
        self.driver.execute_script("arguments[0].style.border='5px solid magenta'", element9)
        if element9.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_dash_btns', attachment_type=allure.attachment_type.PNG)
            message17 = "Dash Button is visible and test-case passed successfully.."
            allure.attach(message17, name="Dash_Button", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_dash_btns', attachment_type=allure.attachment_type.PNG)
            message18 = "Dash Button is not visible and test-case failed.."
            allure.attach(message18, name="Dash_Button", attachment_type=allure.attachment_type.TEXT)
            assert False
        self.admin_lp.click_back_btn2()
        time.sleep(3)
        self.admin_lp.click_view_assigned_tab()
        time.sleep(3)
        element10 = self.driver.find_element(By.XPATH,'//h3[@class="program-head"]')
        self.driver.execute_script("arguments[0].style.border='5px solid magenta'", element10)
        if element10.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_dash_btns', attachment_type=allure.attachment_type.PNG)
            message19 = "Dash Button is visible and test-case passed successfully.."
            allure.attach(message19, name="Dash_Button", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_dash_btns', attachment_type=allure.attachment_type.PNG)
            message20 = "Dash Button is not visible and test-case failed.."
            allure.attach(message20, name="Dash_Button", attachment_type=allure.attachment_type.TEXT)
            assert False
        self.admin_lp.click_back_btn3()
        time.sleep(3)
        self.admin_lp.click_view_assigned_programs_tab()
        time.sleep(3)
        element11 = self.driver.find_element(By.XPATH,'//h3[@class="program-head"]')
        self.driver.execute_script("arguments[0].style.border='5px solid magenta'", element11)
        if element11.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_dash_btns', attachment_type=allure.attachment_type.PNG)
            message21 = "Dash Button is visible and test-case passed successfully.."
            allure.attach(message21, name="Dash_Button", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_dash_btns', attachment_type=allure.attachment_type.PNG)
            message22 = "Dash Button is not visible and test-case failed.."
            allure.attach(message22, name="Dash_Button", attachment_type=allure.attachment_type.TEXT)
            assert False
        self.admin_lp.click_back_btn4()
        time.sleep(3)
        self.admin_lp.click_event_assessment_tab()
        time.sleep(3)
        element12 = self.driver.find_element(By.XPATH,'//h3[@class="program-head"]')
        self.driver.execute_script("arguments[0].style.border='5px solid magenta'", element12)
        if element12.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_dash_btns', attachment_type=allure.attachment_type.PNG)
            message23 = "Dash Button is visible and test-case passed successfully.."
            allure.attach(message23, name="Dash_Button", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_dash_btns', attachment_type=allure.attachment_type.PNG)
            message24 = "Dash Button is not visible and test-case failed.."
            allure.attach(message24, name="Dash_Button", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
            assert False





