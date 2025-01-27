import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Eureka_Main_Screen import Eureka_Main_Screen
from test_cases.configurations import setup
from assertpy import assert_that, soft_assertions
import time
import allure


class Test_04_Eureka_Courses_Tab:
    page_url = "https://eurekaacademy-preprod.niit.com"
    username = "3014029@mailinator.com"
    password = "Eureka@123"



    def test_courses_tab(self, setup):
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
        self.main_screen.click_courses_tab()
        time.sleep(3)

        # Use soft assertions
        with soft_assertions():
            actions = [
                {
                    "locator": '//h3[@class="program-head"]',
                    "name": "Courses Tab",
                    "success_message": "Courses Tab is visible and test-case passed successfully..",
                    "failure_message": "Courses Tab is not visible and test-case failed..",
                },
                {
                    "locator": '//div[@class="bckbtn-main ms-0 mt-1"]',
                    "name": "Back Button",
                    "success_message": "Back Button is visible and test-case passed successfully..",
                    "failure_message": "Back Button is not visible and test-case failed..",
                },
                {
                    "locator": '//ul[@class="mb-3 nav nav-fill nav-justified nav-tabs program-tab nav nav-tabs"]',
                    "name": "Tabs",
                    "success_message": "Tabs are visible and test-case passed successfully..",
                    "failure_message": "Tabs are not visible and test-case failed..",
                },
                {
                    "locator": '//div[@class="tab-content"]',
                    "name": "Tabs Content",
                    "success_message": "Tabs Content are visible and test-case passed successfully..",
                    "failure_message": "Tabs Content are not visible and test-case failed..",
                },
                {
                    "locator": '//footer[@class="footer-eureka mobfooter"]',
                    "name": "Footer",
                    "success_message": "Footer is visible and test-case passed successfully..",
                    "failure_message": "Footer is not visible and test-case failed..",
                },
            ]

            for action in actions:
                element = self.driver.find_element(By.XPATH, action["locator"])

                # Scroll into view and highlight element
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                self.driver.execute_script("arguments[0].style.border='5px solid green'", element)
                time.sleep(2)

                # Perform visibility check
                try:
                    assert_that(element.is_displayed()).is_true()
                    allure.attach(self.driver.get_screenshot_as_png(), name=f'{action["name"]}_Visibility',
                                  attachment_type=allure.attachment_type.PNG)
                    allure.attach(action["success_message"], name=f"{action['name']}_Visibility",
                                  attachment_type=allure.attachment_type.TEXT)
                except AssertionError:
                    allure.attach(self.driver.get_screenshot_as_png(), name=f'{action["name"]}_Visibility',
                                  attachment_type=allure.attachment_type.PNG)
                    allure.attach(action["failure_message"], name=f"{action['name']}_Visibility",
                                  attachment_type=allure.attachment_type.TEXT)

        # Close the driver
        self.driver.close()


    def test_courses_tab_buttons(self, setup):
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
        self.main_screen.click_courses_tab()
        time.sleep(3)

        # Use soft assertions
        with soft_assertions():
            actions = [
                {
                    "method": self.main_screen.click_not_started_tab,
                    "locator": '//div[@class="tab-content"]',
                    "name": "Not Selected Tab",
                    "success_message": "Not Selected Tab is visible and test-case passed successfully.",
                    "failure_message": "Not Selected Tab is not visible and test-case failed."
                },
                {
                    "method": self.main_screen.click_started_tab,
                    "locator": '//div[@class="not-found mt-3"]',
                    "name": "Started Tab",
                    "success_message": "Started Tab is visible and test-case passed successfully.",
                    "failure_message": "Started Tab is not visible and test-case failed."
                },
                {
                    "method": self.main_screen.click_completed_tab,
                    "locator": '//div[@class="not-found mt-3"]',
                    "name": "Completed Tab",
                    "success_message": "Completed Tab is visible and test-case passed successfully.",
                    "failure_message": "Completed Tab is not visible and test-case failed."
                },
                {
                    "method": self.main_screen.click_back_button,
                    "locator": '//div[@class="chart-sec"]',
                    "name": "Back Button",
                    "success_message": "Back Button is visible and test-case passed successfully.",
                    "failure_message": "Back Button is not visible and test-case failed."
                },
            ]

            for action in actions:
                action["method"]()
                time.sleep(3)
                element = self.driver.find_element(By.XPATH, action["locator"])

                # Highlight the element for better screenshot visibility
                self.driver.execute_script("arguments[0].style.border='5px solid green'", element)
                time.sleep(2)

                # Perform visibility check
                try:
                    assert_that(element.is_displayed()).is_true()
                    allure.attach(self.driver.get_screenshot_as_png(), name=f'{action["name"]}_Visibility',
                                  attachment_type=allure.attachment_type.PNG)
                    allure.attach(action["success_message"], name=f"{action['name']}_Visibility",
                                  attachment_type=allure.attachment_type.TEXT)
                except AssertionError:
                    allure.attach(self.driver.get_screenshot_as_png(), name=f'{action["name"]}_Visibility',
                                  attachment_type=allure.attachment_type.PNG)
                    allure.attach(action["failure_message"], name=f"{action['name']}_Visibility",
                                  attachment_type=allure.attachment_type.TEXT)

        # Close the driver
        self.driver.close()


'''
    def test_courses_tab(self,setup):
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
        self.main_screen.click_courses_tab()
        time.sleep(3)
        element = self.driver.find_element(By.XPATH,'//h3[@class="program-head"]')
        self.driver.execute_script("arguments[0].style.border='5px solid green'", element)
        if element.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_courses_tab', attachment_type=allure.attachment_type.PNG)
            message01 = "Courses Tab is visible and test-case passed successfully.."
            allure.attach(message01, name="Courses_Tab_Visibility", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_courses_tab', attachment_type=allure.attachment_type.PNG)
            message02 = "Courses Tab is not visible and test-case failed.."
            allure.attach(message02, name="Courses_Tab_Visibility", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        element2 = self.driver.find_element(By.XPATH,'//div[@class="bckbtn-main ms-0 mt-1"]')
        self.driver.execute_script("arguments[0].style.border='5px solid green'", element2)
        if element2.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_courses_tab', attachment_type=allure.attachment_type.PNG)
            message09 = "Back Button is visible and test-case passed successfully.."
            allure.attach(message09, name="Back_Button_Visibility", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_courses_tab', attachment_type=allure.attachment_type.PNG)
            message10 = "Back Button is not visible and test-case failed.."
            allure.attach(message10, name="Back_Button_Visibility", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        element3 = self.driver.find_element(By.XPATH,'//ul[@class="mb-3 nav nav-fill nav-justified nav-tabs program-tab nav nav-tabs"]')
        self.driver.execute_script("arguments[0].style.border='5px solid green'", element3)
        if element3.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_courses_tab', attachment_type=allure.attachment_type.PNG)
            message11 = "Tabs are visible and test-case passed successfully.."
            allure.attach(message11, name="Tabs_Visibility", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_courses_tab', attachment_type=allure.attachment_type.PNG)
            message12 = "Tabs are not visible and test-case failed.."
            allure.attach(message12, name="Tabs_Visibility", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        element4 = self.driver.find_element(By.XPATH,'//div[@class="tab-content"]')
        self.driver.execute_script("arguments[0].style.border='5px solid green'", element4)
        if element4.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_courses_tab', attachment_type=allure.attachment_type.PNG)
            message13 = "Tabs Content are visible and test-case passed successfully.."
            allure.attach(message13, name="Tabs_Content_Visibility", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_courses_tab', attachment_type=allure.attachment_type.PNG)
            message14 = "Tabs Content are not visible and test-case failed.."
            allure.attach(message14, name="Tabs_Content_Visibility", attachment_type=allure.attachment_type.TEXT)
            assert False
        element5 = self.driver.find_element(By.XPATH,'//footer[@class="footer-eureka mobfooter"]')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element5)
        time.sleep(3)
        self.driver.execute_script("arguments[0].style.border='5px solid green'", element5)
        time.sleep(3)
        if element5.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_courses_tab', attachment_type=allure.attachment_type.PNG)
            message15 = "Footer is visible and test-case passed successfully.."
            allure.attach(message15, name="Footer_Visibility", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_courses_tab', attachment_type=allure.attachment_type.PNG)
            message16 = "Footer is not visible and test-case failed.."
            allure.attach(message16, name="Footer_Visibility", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
            assert False
'''

'''
    def test_courses_tab_buttons(self,setup):
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
        self.main_screen.click_courses_tab()
        time.sleep(3)
        self.main_screen.click_not_started_tab()
        time.sleep(3)
        element1 = self.driver.find_element(By.XPATH,'//div[@class="tab-content"]')
        self.driver.execute_script("arguments[0].style.border='5px solid green'", element1)
        time.sleep(3)
        if element1.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_courses_tab', attachment_type=allure.attachment_type.PNG)
            message04 = "Not Selected Tab is visible and test-case passed successfully.."
            allure.attach(message04, name="Not_Selected_Tab_Visibility", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_courses_tab', attachment_type=allure.attachment_type.PNG)
            message05 = "Not Selected Tab is not visible and test-case failed.."
            allure.attach(message05, name="Not_Selected_Tab_Visibility", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        self.main_screen.click_started_tab()
        time.sleep(3)
        element2 = self.driver.find_element(By.XPATH,'//div[@class="not-found mt-3"]')
        self.driver.execute_script("arguments[0].style.border='5px solid green'", element2)
        time.sleep(2)
        if element2.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_courses_tab', attachment_type=allure.attachment_type.PNG)
            message07 = "Started Tab is visible and test-case passed successfully.."
            allure.attach(message07, name="Started_Tab_Visibility", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_courses_tab', attachment_type=allure.attachment_type.PNG)
            message08 = "Started Tab is not visible and test-case failed.."
            allure.attach(message08, name="Started_Tab_Visibility", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        self.main_screen.click_completed_tab()
        time.sleep(3)
        element3 = self.driver.find_element(By.XPATH,'//div[@class="not-found mt-3"]')
        self.driver.execute_script("arguments[0].style.border='5px solid green'", element3)
        time.sleep(3)
        self.main_screen.click_back_button()
        time.sleep(2)
        element4 = self.driver.find_element(By.XPATH,'//div[@class="chart-sec"]')
        self.driver.execute_script("arguments[0].style.border='5px solid green'", element4)
        time.sleep(3)
        if element4.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_courses_tab', attachment_type=allure.attachment_type.PNG)
            message17 = "Completed Tab is visible and test-case passed successfully.."
            allure.attach(message17, name="Completed_Tab_Visibility", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_courses_tab', attachment_type=allure.attachment_type.PNG)
            message18 = "Completed Tab is not visible and test-case failed.."
            allure.attach(message18, name="Completed_Tab_Visibility", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
            assert False
'''



















