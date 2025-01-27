from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Eureka_Login_Page import Eureka_Login_Page
from test_cases.configurations import setup
import pytest
import time
import allure


class Test_01_Eureka_Login:
    page_url = "https://eurekaacademy-preprod.niit.com"
    username = "3014029@mailinator.com"
    password = "Eureka@123"
    invalid_username = "301402904@mailinator.com"
    invalid_password = "Eureka@12345"
    success_login_Xpath = '//div[@class="scoringpoints"]'
    unsuccess_login_Xpath = '//div[@class="mb-2 login-msg"]'


    def test_valid_login(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        self.admin_lp = Eureka_Login_Page(self.driver)
        self.admin_lp.enter_user_name(self.username)
        self.admin_lp.enter_pass_word(self.password)
        self.admin_lp.click_login_button()
        time.sleep(3)
        act_success_login = self.driver.find_element(By.XPATH,self.success_login_Xpath)
        self.driver.execute_script("arguments[0].style.border='5px solid red'", act_success_login)
        if act_success_login.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_valid_login', attachment_type=AttachmentType.PNG)
            message01 = "Login is successful with highlight and test-case passed successfully.."
            allure.attach(message01, name="Successful_Login", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_valid_login', attachment_type=AttachmentType.PNG)
            message02 = "Login Failed and test-case didn't passed successfully.."
            allure.attach(message02, name="Failed_Login", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
            assert False

    def test_invalid_login(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        self.admin_lp = Eureka_Login_Page(self.driver)
        self.admin_lp.enter_user_name(self.invalid_username)
        self.admin_lp.enter_pass_word(self.invalid_password)
        self.admin_lp.click_login_button()
        time.sleep(3)
        act_invalid_login = self.driver.find_element(By.XPATH,self.unsuccess_login_Xpath)
        self.driver.execute_script("arguments[0].style.border='5px solid red'", act_invalid_login)
        if act_invalid_login.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_invalid_login', attachment_type=AttachmentType.PNG)
            message03 = "Login Failed with highlight and test-case passed successfully.."
            allure.attach(message03, name="Failed_Login", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_invalid_login', attachment_type=AttachmentType.PNG)
            message04 = "Login is successful and test-case didn't passed successfully.."
            allure.attach(message04, name="Successful_Login", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
            assert False


    def test_login_btn_visible(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        self.admin_lp = Eureka_Login_Page(self.driver)
        act_login_btn = self.driver.find_element(By.XPATH,'//button[@class="eureka_submit_btn_block "]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", act_login_btn)
        if act_login_btn.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_login_btn_visible', attachment_type=AttachmentType.PNG)
            message05 = "Login Button is visible and test-case passed successfully.."
            allure.attach(message05, name="Login_Button", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_login_btn_visible', attachment_type=AttachmentType.PNG)
            message06 = "Login Button is not visible and test-case failed.."
            allure.attach(message06, name="Login_Button", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
            assert False

    def test_eye_patch_invisible(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        self.admin_lp = Eureka_Login_Page(self.driver)
        self.admin_lp.enter_user_name(self.username)
        self.admin_lp.enter_pass_word(self.password)
        time.sleep(3)
        assert True
        allure.attach(self.driver.get_screenshot_as_png(), name='test_eye_patch_invisible', attachment_type=AttachmentType.PNG)
        message07 = "Password is not visible before eye patch click and test-case passed successfully.."
        allure.attach(message07, name="Eye_Patch_Invisible", attachment_type=allure.attachment_type.TEXT)
        self.driver.close()

    def test_eye_patch_click(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        self.admin_lp = Eureka_Login_Page(self.driver)
        self.admin_lp.enter_user_name(self.username)
        self.admin_lp.enter_pass_word(self.password)
        time.sleep(3)
        self.admin_lp.click_eye_patch_button()
        time.sleep(3)
        assert True
        allure.attach(self.driver.get_screenshot_as_png(), name='test_eye_patch_click', attachment_type=AttachmentType.PNG)
        message08 = "Password is visible after eye patch click and test-case passed successfully.."
        allure.attach(message08, name="Eye_Patch_Click", attachment_type=allure.attachment_type.TEXT)
        self.driver.close()
























