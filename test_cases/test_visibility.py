import pytest
from selenium import webdriver
from base_pages.Eureka_Main_Screen import Eureka_Main_Screen
from test_cases.configurations import setup
from assertpy import assert_that, soft_assertions
import time
import allure
from selenium.webdriver.common.by import By


class Test_03_Visibility:
    page_url = "https://eurekaacademy-preprod.niit.com"
    username = "3014029@mailinator.com"
    password = "Eureka@123"

    def test_visibility(self, setup):
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
        logo = self.driver.find_element(By.XPATH, '//div[@class=" content-logo "]')
        self.driver.execute_script("arguments[0].style.border='5px solid yellow'", logo)
        time.sleep(2)
        if logo.is_displayed():
            assert True
            message01 = "Logo is visible and test-case passed successfully.."
            allure.attach(message01, name="Logo_Visibility", attachment_type=allure.attachment_type.TEXT)
        else:
            message02 = "Logo is not visible and test-case failed.."
            allure.attach(message02, name="Logo_Visibility", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(2)
        search_box = self.driver.find_element(By.XPATH, '//li[@class="nav-item"]')
        self.driver.execute_script("arguments[0].style.border='5px solid yellow'", search_box)
        time.sleep(2)
        if search_box.is_displayed():
            assert True
            message03 = "Search Box is visible and test-case passed successfully.."
            allure.attach(message03, name="Search_Box_Visibility", attachment_type=allure.attachment_type.TEXT)
        else:
            message04 = "Search Box is not visible and test-case failed.."
            allure.attach(message04, name="Search_Box_Visibility", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(2)
        programs = self.driver.find_element(By.XPATH, "//a[text()='Program']")
        self.driver.execute_script("arguments[0].style.border='5px solid yellow'", programs)
        time.sleep(2)
        if programs.is_displayed():
            assert True
            message05 = "Programs is visible and test-case passed successfully.."
            allure.attach(message05, name="Programs_Visibility", attachment_type=allure.attachment_type.TEXT)
        else:
            message06 = "Programs is not visible and test-case failed.."
            allure.attach(message06, name="Programs_Visibility", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(2)
        courses = self.driver.find_element(By.XPATH, "//a[text()='Courses']")
        self.driver.execute_script("arguments[0].style.border='5px solid yellow'", courses)
        time.sleep(2)
        if courses.is_displayed():
            assert True
            message07 = "Courses is visible and test-case passed successfully.."
            allure.attach(message07, name="Courses_Visibility", attachment_type=allure.attachment_type.TEXT)
        else:
            message08 = "Courses is not visible and test-case failed.."
            allure.attach(message08, name="Courses_Visibility", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(2)
        sessions = self.driver.find_element(By.XPATH, "//a[text()='Sessions']")
        self.driver.execute_script("arguments[0].style.border='5px solid yellow'", sessions)
        time.sleep(2)
        if sessions.is_displayed():
            assert True
            message09 = "Sessions is visible and test-case passed successfully.."
            allure.attach(message09, name="Sessions_Visibility", attachment_type=allure.attachment_type.TEXT)
        else:
            message10 = "Sessions is not visible and test-case failed.."
            allure.attach(message10, name="Sessions_Visibility", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(2)
        assesments = self.driver.find_element(By.XPATH, "//a[text()='Assessments']")
        self.driver.execute_script("arguments[0].style.border='5px solid yellow'", assesments)
        time.sleep(2)
        if assesments.is_displayed():
            assert True
            message11 = "Assesments is visible and test-case passed successfully.."
            allure.attach(message11, name="Assesments_Visibility", attachment_type=allure.attachment_type.TEXT)
        else:
            message12 = "Assesments is not visible and test-case failed.."
            allure.attach(message12, name="Assesments_Visibility", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(2)
        profile = self.driver.find_element(By.XPATH, '//ul[@class="navbar-nav profile_thumbImg realtor_manager_login"]')
        self.driver.execute_script("arguments[0].style.border='5px solid yellow'", profile)
        time.sleep(2)
        if profile.is_displayed():
            assert True
            message13 = "Profile is visible and test-case passed successfully.."
            allure.attach(message13, name="Profile_Visibility", attachment_type=allure.attachment_type.TEXT)
        else:
            message14 = "Profile is not visible and test-case failed.."
            allure.attach(message14, name="Profile_Visibility", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(2)
        chart_sec = self.driver.find_element(By.XPATH, '//div[@class="chart-sec"]')
        self.driver.execute_script("arguments[0].style.border='5px solid yellow'", chart_sec)
        time.sleep(2)
        if chart_sec.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_visibility', attachment_type=allure.attachment_type.PNG)
            message15 = "Chart Section is visible and test-case passed successfully.."
            allure.attach(message15, name="Chart_Section_Visibility", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_visibility', attachment_type=allure.attachment_type.PNG)
            message16 = "Chart Section is not visible and test-case failed.."
            allure.attach(message16, name="Chart_Section_Visibility", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(2)
        container_sec = self.driver.find_element(By.XPATH, '//div[@class="row view-sec-row"]')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", container_sec)
        time.sleep(2)
        self.driver.execute_script("arguments[0].style.border='5px solid yellow'", container_sec)
        time.sleep(2)
        if container_sec.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_visibility', attachment_type=allure.attachment_type.PNG)
            message17 = "Container Section is visible and test-case passed successfully.."
            allure.attach(message17, name="Container_Section_Visibility", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_visibility', attachment_type=allure.attachment_type.PNG)
            message18 = "Container Section is not visible and test-case failed.."
            allure.attach(message18, name="Container_Section_Visibility", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(2)
        performance_sec = self.driver.find_element(By.XPATH, '//div[@class="performance-slider"]')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", performance_sec)
        time.sleep(2)
        self.driver.execute_script("arguments[0].style.border='5px solid yellow'", performance_sec)
        time.sleep(2)
        if performance_sec.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_visibility', attachment_type=allure.attachment_type.PNG)
            message19 = "Performance Section is visible and test-case passed successfully.."
            allure.attach(message19, name="Performance_Section_Visibility", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_visibility', attachment_type=allure.attachment_type.PNG)
            message20 = "Performance Section is not visible and test-case failed.."
            allure.attach(message20, name="Performance_Section_Visibility", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(2)
        slider_sec = self.driver.find_element(By.XPATH, '//section[@class="container ps-0 pe-0 about-slider"]')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", slider_sec)
        time.sleep(2)
        self.driver.execute_script("arguments[0].style.border='5px solid yellow'", slider_sec)
        time.sleep(2)
        if slider_sec.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_visibility',
                          attachment_type=allure.attachment_type.PNG)
            message21 = "Slider Section is visible and test-case passed successfully.."
            allure.attach(message21, name="Slider_Section_Visibility", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_visibility',
                          attachment_type=allure.attachment_type.PNG)
            message22 = "Slider Section is not visible and test-case failed.."
            allure.attach(message22, name="Slider_Section_Visibility", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(2)
        slider_dots = self.driver.find_element(By.XPATH, '//ul[@class="slick-dots"]')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", slider_dots)
        time.sleep(2)
        self.driver.execute_script("arguments[0].style.border='5px solid yellow'", slider_dots)
        time.sleep(2)
        if slider_dots.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_visibility',
                          attachment_type=allure.attachment_type.PNG)
            message23 = "Slider Dots Section is visible and test-case passed successfully.."
            allure.attach(message23, name="Slider_Dots_Section_Visibility", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_visibility',
                          attachment_type=allure.attachment_type.PNG)
            message24 = "Slider Dots Section is not visible and test-case failed.."
            allure.attach(message24, name="Slider_Dots_Section_Visibility", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(2)
        feedback_btn = self.driver.find_element(By.XPATH, '//div[@class="feedback--button contentDesktopView"]')
        self.driver.execute_script("arguments[0].style.border='5px solid yellow'", feedback_btn)
        time.sleep(2)
        if feedback_btn.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_visibility',
                          attachment_type=allure.attachment_type.PNG)
            message25 = "Feedback Button Section is visible and test-case passed successfully.."
            allure.attach(message25, name="Feedback_Button_Section_Visibility",
                          attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_visibility',
                          attachment_type=allure.attachment_type.PNG)
            message26 = "Feedback Button Section is not visible and test-case failed.."
            allure.attach(message26, name="Feedback_Button_Section_Visibility",
                          attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(2)
        footer = self.driver.find_element(By.XPATH, '//footer[@class="footer-eureka mobfooter"]')
        self.driver.execute_script("arguments[0].style.border='5px solid yellow'", footer)
        time.sleep(2)
        if footer.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_visibility',
                          attachment_type=allure.attachment_type.PNG)
            message27 = "Footer Section is visible and test-case passed successfully.."
            allure.attach(message27, name="Footer_Section_Visibility", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_visibility',
                          attachment_type=allure.attachment_type.PNG)
            message28 = "Footer Section is not visible and test-case failed.."
            allure.attach(message28, name="Footer_Section_Visibility", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
            assert False

'''
    def test_element_visibility(self, setup):
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

        # Use soft assertions
        with soft_assertions():
            # Elements to check
            elements = [

                {"locator": '//div[@class=" content-logo "]', "name": "Logo",
                 "message": "Logo is visible and test-case passed successfully.."},
                {"locator": '//li[@class="nav-item"]', "name": "Search Box",
                 "message": "Search Box is visible and test-case passed successfully.."},
                {"locator": "//a[text()='Program']", "name": "Programs",
                 "message": "Programs is visible and test-case passed successfully.."},
                {"locator": "//a[text()='Courses']", "name": "Courses",
                 "message": "Courses is visible and test-case passed successfully.."},
                {"locator": "//a[text()='Sessions']", "name": "Sessions",
                 "message": "Sessions is visible and test-case passed successfully.."},
                {"locator": "//a[text()='Assessments']", "name": "Assessments",
                 "message": "Assessments is visible and test-case passed successfully.."},
                {"locator": '//ul[@class="navbar-nav profile_thumbImg realtor_manager_login"]', "name": "Profile",
                 "message": "Profile is visible and test-case passed successfully.."},
                {"locator": '//div[@class="rank-bg"]', "name": "Rank bar",
                 "message": "Rank bar is visible and test-case passed successfully.."},
                {"locator": '//div[@class="chart-sec"]', "name": "Chart Section",
                 "message": "Chart Section is visible and test-case passed successfully.."},
                {"locator": '//div[@class="row view-sec-row"]', "name": "Container Section",
                 "message": "Container Section is visible and test-case passed successfully.."},
                {"locator": '//div[@class="performance-slider"]', "name": "Performance Section",
                 "message": "Performance Section is visible and test-case passed successfully.."},
                {"locator": '//section[@class="container ps-0 pe-0 about-slider"]', "name": "Slider Section",
                 "message": "Slider Section is visible and test-case passed successfully.."},
                {"locator": '//ul[@class="slick-dots"]', "name": "Slider Dots Section",
                 "message": "Slider Dots Section is visible and test-case passed successfully.."},
                {"locator": '//div[@class="feedback--button contentDesktopView"]', "name": "Feedback Button Section",
                 "message": "Feedback Button Section is visible and test-case passed successfully.."},
                {"locator": '//footer[@class="footer-eureka mobfooter"]', "name": "Footer Section",
                 "message": "Footer Section is visible and test-case passed successfully.."},
                {"Locator": '//img[@id="niit_logo_mob"]', "name": "Logo_Bell",
                 "message": "Logo_Bell is visible and test-case passed successfully.."}
            ]

            # Check visibility for each element
            for element in elements:
                elem = self.driver.find_element(By.XPATH, element["locator"])
                self.driver.execute_script("arguments[0].style.border='5px solid yellow'", elem)
                time.sleep(2)

                # Scroll element into view
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", elem)
                time.sleep(2)

                try:
                    assert_that(elem.is_displayed()).is_true()
                    allure.attach(self.driver.get_screenshot_as_png(), name=f'{element["name"]}_visibility',
                                  attachment_type=allure.attachment_type.PNG)
                    allure.attach(element["message"], name=f"{element['name']}_Visibility",
                                  attachment_type=allure.attachment_type.TEXT)
                except AssertionError:
                    failure_message = f"{element['name']} is not visible and test-case failed.."
                    allure.attach(self.driver.get_screenshot_as_png(), name=f'{element["name"]}_visibility',
                                  attachment_type=allure.attachment_type.PNG)
                    allure.attach(failure_message, name=f"{element['name']}_Visibility",
                                  attachment_type=allure.attachment_type.TEXT)
        self.driver.close()
'''

































