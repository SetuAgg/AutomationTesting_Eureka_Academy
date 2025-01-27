from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from base_pages.Eureka_Main_Screen import Eureka_Main_Screen
from test_cases.configurations import setup
from assertpy import assert_that, soft_assertions
import time
import allure
from selenium.webdriver.common.by import By


class Test_06_Eureka_Session_Tab:
    page_url = "https://eurekaacademy-preprod.niit.com"
    username = "3014029@mailinator.com"
    password = "Eureka@123"

    def test_session_tab(self, setup):
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
        self.main_screen.click_session_tab()
        time.sleep(3)

        # Use soft assertions
        with soft_assertions():
            elements = [
                {
                    "locator": '//div[@class="col-md-12 calendar-banner text-center"]',
                    "name": "Session Tab Header",
                    "success_message": "Session Tab Header Text i.e 'Schedule' is visible and test-case passed successfully..",
                    "failure_message": "Session Tab Header Text i.e 'Schedule' is not visible and test-case failed..",
                },
                {
                    "locator": "//button[text()='Day']",
                    "name": "Day Button",
                    "success_message": "'Day' named button is visible and test-case passed successfully..",
                    "failure_message": "'Day' named button is not visible and test-case failed..",
                },
                {
                    "locator": "//button[text()='Month']",
                    "name": "Month Button",
                    "success_message": "'Month' named button is visible and test-case passed successfully..",
                    "failure_message": "'Month' named button is not visible and test-case failed..",
                },
                {
                    "locator": "//button[text()='Week']",
                    "name": "Week Button",
                    "success_message": "'Week' named button is visible and test-case passed successfully..",
                    "failure_message": "'Week' named button is not visible and test-case failed..",
                },
                {
                    "locator": '//label[@class="calendar-label-title"]',
                    "name": "Calender Label",
                    "success_message": "Calender Label is visible and test-case passed successfully..",
                    "failure_message": "Calender Label is not visible and test-case failed..",
                },
                {
                    "locator": '//div[@class="d-flex button-filteralignment"]',
                    "name": "Arrow Buttons",
                    "success_message": "Arrow Buttons is visible and test-case passed successfully..",
                    "failure_message": "Arrow Buttons is not visible and test-case failed..",
                },
                {
                    "locator": '//div[@class="side-calender session-calendar"]',
                    "name": "Short Calender",
                    "success_message": "Short Calender is visible and test-case passed successfully..",
                    "failure_message": "Short Calender is not visible and test-case failed..",
                },
                {
                    "locator": '//div[@class="rbc-time-view"]',
                    "name": "Main Calender",
                    "success_message": "Main Calender is visible and test-case passed successfully..",
                    "failure_message": "Main Calender is not visible and test-case failed..",
                },
                {
                    "locator": '//div[@class="calendar-bckbtn ms-0"]',
                    "name": "Back Button",
                    "success_message": "Back Button is visible and test-case passed successfully..",
                    "failure_message": "Back Button is not visible and test-case failed..",
                },
                {
                    "locator": '//footer[@class="footer-eureka mobfooter"]',
                    "name": "Page Footer",
                    "success_message": "Footer is visible and test-case passed successfully..",
                    "failure_message": "Footer is not visible and test-case failed..",
                },
            ]
            # Check visibility of elements
            for element in elements:
                elem = self.driver.find_element(By.XPATH, element["locator"])

                # Scroll into view and highlight
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", elem)
                self.driver.execute_script("arguments[0].style.border='5px solid pink'", elem)
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
                    allure.attach(element["failure_message"], name=f"{element['name']}_Visibility",
                                  attachment_type=allure.attachment_type.TEXT)

                # Close the driver
            self.driver.close()


    def test_session_tab_buttons(self, setup):
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
        self.main_screen.click_session_tab()
        time.sleep(3)
        self.main_screen.click_session_tab_day_btn()
        time.sleep(3)
        element1 = self.driver.find_element(By.XPATH, '//div[@class="calscroll"]')
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element1)
        time.sleep(3)
        if element1.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_session_tab_day_btn', attachment_type=allure.attachment_type.PNG)
            message01 = "calender view is visible and test-case passed successfully.."
            allure.attach(message01, name="Calender View Visibility", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_assessments_tab',
                          attachment_type=allure.attachment_type.PNG)
            message02 = "Assessments Tab is not visible and test-case failed.."
            allure.attach(message02, name="Assessments_Tab_Visibility", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        self.main_screen.click_session_tab_month_btn()
        time.sleep(3)
        element2 = self.driver.find_element(By.XPATH, '//div[@class="rbc-calendar"]')
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element2)
        time.sleep(3)
        if element2.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_session_tab_month_btn', attachment_type=allure.attachment_type.PNG)
            message03 = "calender view is visible and test-case passed successfully.."
            allure.attach(message03, name="Calender View Visibility", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_assessments_tab', attachment_type=allure.attachment_type.PNG)
            message04 = "Assessments Tab is not visible and test-case failed.."
            allure.attach(message04, name="Assessments_Tab_Visibility", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        self.main_screen.click_session_tab_week_btn()
        time.sleep(3)
        element3 = self.driver.find_element(By.XPATH, '//div[@class="rbc-time-view"]')
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element3)
        time.sleep(3)
        if element3.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_session_tab_week_btn', attachment_type=allure.attachment_type.PNG)
            message05 = "calender view is visible and test-case passed successfully.."
            allure.attach(message05, name="Calender View Visibility", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_assessments_tab', attachment_type=allure.attachment_type.PNG)
            message06 = "Assessments Tab is not visible and test-case failed.."
            allure.attach(message06, name="Assessments_Tab_Visibility", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        self.main_screen.click_back_btn_session_tab()
        time.sleep(3)
        element4 = self.driver.find_element(By.XPATH, '//div[@class="chart-sec"]')
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element4)
        time.sleep(3)
        if element4.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_back_btn_session_tab', attachment_type=allure.attachment_type.PNG)
            message07 = "calender view is visible and test-case passed successfully.."
            allure.attach(message07, name="Calender View Visibility", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_assessments_tab',
                          attachment_type=allure.attachment_type.PNG)
            message08 = "Assessments Tab is not visible and test-case failed.."
            allure.attach(message08, name="Assessments_Tab_Visibility", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
            assert False



'''''
        # Use soft assertions
        with soft_assertions():
            actions = [
                {
                    "click_action": self.main_screen.click_session_tab_day_btn,
                    "locator": '//div[@class="rbc-time-content"]',
                    "name": "rbc-time-content",
                    "success_message": "Element selected is visible and test-case passed successfully..",
                    "failure_message": "Element is not visible and test-case failed..",
                },
                {
                    "click_action": self.main_screen.click_session_tab_month_btn,
                    "locator": '//div[@class="rbc-month-view"]',
                    "name": "rbc-month-view",
                    "success_message": "Element selected is visible and test-case passed successfully..",
                    "failure_message": "Element is not visible and test-case failed..",
                },
                {
                    "click_action": self.main_screen.click_session_tab_week_btn,
                    "locator": '//div[@class="rbc-time-view"]',
                    "name": "rbc-time-view",
                    "success_message": "Element selected is visible and test-case passed successfully..",
                    "failure_message": "Element is not visible and test-case failed..",
                },
            ]

            for action in actions:
                action["click_action"]()  # Call the method here
                time.sleep(3)

                # Find and highlight element
                element = self.driver.find_element(By.XPATH, action["locator"])
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element)
                self.driver.execute_script("arguments[0].style.border='5px solid blue'", element)
                time.sleep(2)

                # Wait for element to be clickable and handle possible overlays
                try:
                    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))

                    # Check for any potential modal or overlay that might be blocking the click
                    overlays = self.driver.find_elements(By.CSS_SELECTOR,
                                                         '.overlay-class')  # Modify with actual overlay class or ID
                    if overlays:
                        # Handle overlay, for example, close it if possible
                        self.driver.execute_script("arguments[0].style.display='none';",
                                                   overlays[0])  # Close overlay if found

                    # Now click the element
                    element.click()
                    time.sleep(2)  # Allow click time to be processed
                except Exception as e:
                    print(f"Error during click action: {e}")
                    # If click fails, you can try using JavaScript to click the element
                    self.driver.execute_script("arguments[0].click();", element)
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
'''''



