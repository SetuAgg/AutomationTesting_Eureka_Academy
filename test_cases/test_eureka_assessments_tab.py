import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from base_pages.Eureka_Main_Screen import Eureka_Main_Screen
from test_cases.configurations import setup
from assertpy import assert_that, soft_assertions
import time
import allure


class Test_05_Eureka_Assessments_Tab:
    page_url = "https://eurekaacademy-preprod.niit.com"
    username = "3014029@mailinator.com"
    password = "Eureka@123"



    def test_assessments_tab(self, setup):
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
        self.main_screen.click_assessment_tab()
        time.sleep(3)

        # Use soft assertions
        with soft_assertions():
            elements = [
                {
                    "locator": '//h3[@class="program-head"]',
                    "name": "Assessments Tab",
                    "success_message": "Assessments Tab is visible and test-case passed successfully..",
                    "failure_message": "Assessments Tab is not visible and test-case failed..",
                },
                {
                    "locator": '//ul[@class="nav nav-fill nav-justified nav-tabs program-tab"]',
                    "name": "Tabs",
                    "success_message": "Tabs are visible and test-case passed successfully..",
                    "failure_message": "Tabs are not visible and test-case failed..",
                },
                {
                    "locator": '//div[@class="bckbtn-main ms-0 mt-1"]',
                    "name": "Back Button",
                    "success_message": "Back Button is visible and test-case passed successfully..",
                    "failure_message": "Back Button is not visible and test-case failed..",
                },
                {
                    "locator": '//div[@class="not-found mt-3"]',
                    "name": "No Assessment Section",
                    "success_message": "No Assessment is visible and test-case passed successfully..",
                    "failure_message": "No Assessment is not visible and test-case failed..",
                },
                {
                    "locator": '//footer[@class="footer-eureka mobfooter"]',
                    "name": "Footer",
                    "success_message": "Footer is visible and test-case passed successfully..",
                    "failure_message": "Footer is not visible and test-case failed..",
                },
            ]

            # Check visibility of elements
            for element in elements:
                elem = self.driver.find_element(By.XPATH, element["locator"])

                # Scroll into view and highlight
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", elem)
                self.driver.execute_script("arguments[0].style.border='5px solid blue'", elem)
                time.sleep(2)

                # Perform visibility check
                try:
                    assert_that(elem.is_displayed()).is_true()
                    allure.attach(self.driver.get_screenshot_as_png(), name=f'{element["name"]}_visibility',
                                  attachment_type=allure.attachment_type.PNG)
                    allure.attach(element["success_message"], name=f"{element['name']}_Visibility",
                                  attachment_type=allure.attachment_type.TEXT)
                except AssertionError:
                    allure.attach(self.driver.get_screenshot_as_png(), name=f'{element["name"]}_visibility',
                                  attachment_type=allure.attachment_type.PNG)
                    allure.attach(element["failure_message"], name=f"{element['name']}_Visibility", attachment_type=allure.attachment_type.TEXT)
                time.sleep(3)
        # Use soft assertions
        with soft_assertions():
            actions = [
                {
                    "click_action": self.main_screen.click_not_started_btn_assessment_tab,
                    "locator": '//div[@class="not-found mt-3"]',
                    "name": "Not Started Tab",
                    "success_message": "Not Selected Tab is visible and test-case passed successfully..",
                    "failure_message": "Not Selected Tab is not visible and test-case failed..",
                },
                {
                    "click_action": self.main_screen.click_started_btn_assessment_tab,
                    "locator": '//div[@class="not-found mt-3"]',
                    "name": "Started Tab",
                    "success_message": "Selected Tab is visible and test-case passed successfully..",
                    "failure_message": "Selected Tab is not visible and test-case failed..",
                },
                {
                    "click_action": self.main_screen.click_completed_btn_assessment_tab,
                    "locator": '//div[@class="not-found mt-3"]',
                    "name": "Completed Tab",
                    "success_message": "Completed Tab is visible and test-case passed successfully..",
                    "failure_message": "Completed Tab is not visible and test-case failed..",
                },
                {
                    "click_action": self.main_screen.click_back_btn_assessment_tab,
                    "locator": '//div[@class="chart-sec"]',
                    "name": "Back Button",
                    "success_message": "Back Button is visible and test-case passed successfully..",
                    "failure_message": "Back Button is not visible and test-case failed..",
                },
            ]

            for action in actions:
                action["click_action"]()
                time.sleep(3)

                # Find and highlight element
                element = self.driver.find_element(By.XPATH, action["locator"])
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element)
                self.driver.execute_script("arguments[0].style.border='5px solid pink'", element)
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
    def test_assessments_tab(self,setup):
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
        self.main_screen.click_assessment_tab()
        time.sleep(3)
        element1 = self.driver.find_element(By.XPATH,'//h3[@class="program-head"]')
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element1)
        time.sleep(3)
        if element1.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_assessments_tab', attachment_type=allure.attachment_type.PNG)
            message01 = "Assessments Tab is visible and test-case passed successfully.."
            allure.attach(message01, name="Assessments_Tab_Visibility", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_assessments_tab', attachment_type=allure.attachment_type.PNG)
            message02 = "Assessments Tab is not visible and test-case failed.."
            allure.attach(message02, name="Assessments_Tab_Visibility", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        element2 = self.driver.find_element(By.XPATH,'//ul[@class="nav nav-fill nav-justified nav-tabs program-tab"]')
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element2)
        time.sleep(3)
        if element2.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_assessments_tab', attachment_type=allure.attachment_type.PNG)
            message03 = "Tabs are visible and test-case passed successfully.."
            allure.attach(message03, name="Tabs_Visibility", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_assessments_tab', attachment_type=allure.attachment_type.PNG)
            message04 = "Tabs are not visible and test-case failed.."
            allure.attach(message04, name="Tabs_Visibility", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        element3 = self.driver.find_element(By.XPATH,'//div[@class="bckbtn-main ms-0 mt-1"]')
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element3)
        time.sleep(3)
        if element3.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_assessments_tab', attachment_type=allure.attachment_type.PNG)
            message05 = "Back Button is visible and test-case passed successfully.."
            allure.attach(message05, name="Back_Button_Visibility", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_assessments_tab', attachment_type=allure.attachment_type.PNG)
            message06 = "Back Button is not visible and test-case failed.."
            allure.attach(message06, name="Back_Button_Visibility", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        element4 = self.driver.find_element(By.XPATH,'//div[@class="not-found mt-3"]')
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element4)
        time.sleep(3)
        if element4.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_assessments_tab', attachment_type=allure.attachment_type.PNG)
            message07 = "No Assessment is visible and test-case passed successfully.."
            allure.attach(message07, name="No_Assessment_Visibility", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_assessments_tab', attachment_type=allure.attachment_type.PNG)
            message08 = "No Assessment is not visible and test-case failed.."
            allure.attach(message08, name="No_Assessment_Visibility", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        element5 = self.driver.find_element(By.XPATH,'//footer[@class="footer-eureka mobfooter"]')
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element5)
        time.sleep(3)
        if element5.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_assessments_tab', attachment_type=allure.attachment_type.PNG)
            message07 = "Footer is visible and test-case passed successfully.."
            allure.attach(message07, name="Footer_Visibility", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_assessments_tab', attachment_type=allure.attachment_type.PNG)
            message08 = "Footer is not visible and test-case failed.."
            allure.attach(message08, name="Footer_Visibility", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
            assert False
'''

'''
    def test_assessments_tab_buttons(self,setup):
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
        self.main_screen.click_assessment_tab()
        time.sleep(3)
        self.main_screen.click_not_started_btn_assessment_tab()
        time.sleep(3)
        element1 = self.driver.find_element(By.XPATH,'//div[@class="not-found mt-3"]')
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element1)
        time.sleep(3)
        if element1.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_assessments_tab', attachment_type=allure.attachment_type.PNG)
            message04 = "Not Selected Tab is visible and test-case passed successfully.."
            allure.attach(message04, name="Not_Selected_Tab_Visibility", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_assessments_tab', attachment_type=allure.attachment_type.PNG)
            message05 = "Not Selected Tab is not visible and test-case failed.."
            allure.attach(message05, name="Not_Selected_Tab_Visibility", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        self.main_screen.click_started_btn_assessment_tab()
        time.sleep(3)
        element2 = self.driver.find_element(By.XPATH,'//div[@class="not-found mt-3"]')
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element2)
        time.sleep(3)
        if element2.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_assessments_tab', attachment_type=allure.attachment_type.PNG)
            message06 = "Selected Tab is visible and test-case passed successfully.."
            allure.attach(message06, name="Selected_Tab_Visibility", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_assessments_tab', attachment_type=allure.attachment_type.PNG)
            message07 = "Selected Tab is not visible and test-case failed.."
            allure.attach(message07, name="Selected_Tab_Visibility", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        self.main_screen.click_completed_btn_assessment_tab()
        time.sleep(3)
        element3 = self.driver.find_element(By.XPATH,'//div[@class="not-found mt-3"]')
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element3)
        time.sleep(3)
        if element3.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_assessments_tab', attachment_type=allure.attachment_type.PNG)
            message08 = "Selected Tab is visible and test-case passed successfully.."
            allure.attach(message08, name="Selected_Tab_Visibility", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_assessments_tab', attachment_type=allure.attachment_type.PNG)
            message09 = "Selected Tab is not visible and test-case failed.."
            allure.attach(message09, name="Selected_Tab_Visibility", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        self.main_screen.click_back_btn_assessment_tab()
        time.sleep(3)
        element4 = self.driver.find_element(By.XPATH,'//div[@class="chart-sec"]')
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element4)
        time.sleep(3)
        if element4.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_assessments_tab', attachment_type=allure.attachment_type.PNG)
            message10 = "Back Button is visible and test-case passed successfully.."
            allure.attach(message10, name="Back_Button_Visibility", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_assessments_tab', attachment_type=allure.attachment_type.PNG)
            message11 = "Back Button is not visible and test-case failed.."
            allure.attach(message11, name="Back_Button_Visibility", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
            assert False
'''











