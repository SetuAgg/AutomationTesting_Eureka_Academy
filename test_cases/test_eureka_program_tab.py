import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from test_cases.configurations import setup
from assertpy import assert_that, soft_assertions
import time
import allure
from base_pages.Eureka_Main_Screen import Eureka_Main_Screen

class Test_07_Eureka_Program_Tab:
    page_url = "https://eurekaacademy-preprod.niit.com"
    username = "3014029@mailinator.com"
    password = "Eureka@123"

    def test_program_tab(self, setup):
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
        self.main_screen.click_program_tab()
        time.sleep(3)
        element1 = self.driver.find_element(By.XPATH,'//h3[@class="program-head"]')
        self.driver.execute_script("arguments[0].style.border='5px solid purple'", element1)
        time.sleep(3)
        if element1.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab', attachment_type=allure.attachment_type.PNG)
            message01 = "Program Tab Header Text i.e 'Programs' is visible and test-case passed successfully.."
            allure.attach(message01, name='test_program_tab', attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab', attachment_type=allure.attachment_type.PNG)
            message02 = "Program Tab Header Text i.e 'Programs' is not visible and test-case failed.."
            allure.attach(message02, name='test_program_tab', attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        element2 = self.driver.find_element(By.XPATH,'//div[@class="bckbtn-main ms-0 mt-1"]')
        self.driver.execute_script("arguments[0].style.border='5px solid purple'", element2)
        time.sleep(3)
        if element2.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab', attachment_type=allure.attachment_type.PNG)
            message03 = "Back Button is visible and test-case passed successfully.."
            allure.attach(message03, name='test_program_tab', attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab', attachment_type=allure.attachment_type.PNG)
            message04 = "Back Button is not visible and test-case failed.."
            allure.attach(message04, name='test_program_tab', attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        element3 = self.driver.find_element(By.XPATH,'//ul[@class="nav nav-fill nav-justified nav-tabs program-tab"]')
        self.driver.execute_script("arguments[0].style.border='5px solid purple'", element3)
        time.sleep(3)
        if element3.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab', attachment_type=allure.attachment_type.PNG)
            message05 = "Tabs are visible and test-case passed successfully.."
            allure.attach(message05, name='test_program_tab', attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab', attachment_type=allure.attachment_type.PNG)
            message06 = "Tabs are not visible and test-case failed.."
            allure.attach(message06, name='test_program_tab', attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        element4 = self.driver.find_element(By.XPATH,"//p[text()='New Program For Enrollment']")
        self.driver.execute_script("arguments[0].style.border='5px solid purple'", element4)
        time.sleep(3)
        if element4.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab', attachment_type=allure.attachment_type.PNG)
            message07 = "New Program For Enrollment Tab is visible and test-case passed successfully.."
            allure.attach(message07, name='test_program_tab', attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab', attachment_type=allure.attachment_type.PNG)
            message08 = "New Program For Enrollment Tab is not visible and test-case failed.."
            allure.attach(message08, name='test_program_tab', attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        element5 = self.driver.find_element(By.XPATH,'//div[@class="slick-slider slick-initialized"]')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element5)
        time.sleep(3)
        self.driver.execute_script("arguments[0].style.border='5px solid purple'", element5)
        time.sleep(3)
        if element5.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab', attachment_type=allure.attachment_type.PNG)
            message09 = "Slick Slider is visible and test-case passed successfully.."
            allure.attach(message09, name='test_program_tab', attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab', attachment_type=allure.attachment_type.PNG)
            message10 = "Slick Slider is not visible and test-case failed.."
            allure.attach(message10, name='test_program_tab', attachment_type=allure.attachment_type.TEXT)
            assert False
        element6 = self.driver.find_element(By.XPATH,"//p[text()='Designo NXT W2 May24']")
        self.driver.execute_script("arguments[0].style.border='5px solid purple'", element6)
        time.sleep(3)
        if element6.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab', attachment_type=allure.attachment_type.PNG)
            message11 = "Designo NXT W2 May24 Tab is visible and test-case passed successfully.."
            allure.attach(message11, name='test_program_tab', attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab', attachment_type=allure.attachment_type.PNG)
            message12 = "Designo NXT W2 May24 Tab is not visible and test-case failed.."
            allure.attach(message12, name='test_program_tab', attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        element7 = self.driver.find_element(By.XPATH,"//p[text()='Behavior and Grooming Weekly Assessment May 24']")
        self.driver.execute_script("arguments[0].style.border='5px solid purple'", element7)
        time.sleep(3)
        if element7.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab', attachment_type=allure.attachment_type.PNG)
            message13 = "Behavior and Grooming Weekly Assessment Tab is visible and test-case passed successfully.."
            allure.attach(message13, name='test_program_tab', attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab', attachment_type=allure.attachment_type.PNG)
            message14 = "Behavior and Grooming Weekly Assessment Tab is not visible and test-case failed.."
            allure.attach(message14, name='test_program_tab', attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        element8 = self.driver.find_element(By.XPATH,"//p[text()='LVAC App Guide Weekly Assessment Apr24']")
        self.driver.execute_script("arguments[0].style.border='5px solid purple'", element8)
        time.sleep(3)
        if element8.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab', attachment_type=allure.attachment_type.PNG)
            message15 = "LVAC App Guide Weekly Assessment Tab is visible and test-case passed successfully.."
            allure.attach(message15, name='test_program_tab', attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab', attachment_type=allure.attachment_type.PNG)
            message16 = "LVAC App Guide Weekly Assessment Tab is not visible and test-case failed.."
            allure.attach(message16, name='test_program_tab', attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        element9 = self.driver.find_element(By.XPATH,"//p[text()='NPS Weekly Assessment  Apr 24']")
        self.driver.execute_script("arguments[0].style.border='5px solid purple'", element9)
        time.sleep(3)
        if element9.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab', attachment_type=allure.attachment_type.PNG)
            message17 = "NPS Weekly Assessment Tab is visible and test-case passed successfully.."
            allure.attach(message17, name='test_program_tab', attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab', attachment_type=allure.attachment_type.PNG)
            message18 = "NPS Weekly Assessment Tab is not visible and test-case failed.."
            allure.attach(message18, name='test_program_tab', attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        element10 = self.driver.find_element(By.XPATH,"//p[text()='Nova Weekly Assessment Apr 24']")
        self.driver.execute_script("arguments[0].style.border='5px solid purple'", element10)
        time.sleep(3)
        if element10.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab', attachment_type=allure.attachment_type.PNG)
            message19 = "Nova Weekly Assessment Tab is visible and test-case passed successfully.."
            allure.attach(message19, name='test_program_tab', attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab', attachment_type=allure.attachment_type.PNG)
            message20 = "Nova Weekly Assessment Tab is not visible and test-case failed.."
            allure.attach(message20, name='test_program_tab', attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        element11 = self.driver.find_element(By.XPATH,"//p[text()='NPS- Direct Sales - Apr 24']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element11)
        time.sleep(3)
        self.driver.execute_script("arguments[0].style.border='5px solid purple'", element11)
        time.sleep(3)
        if element11.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab', attachment_type=allure.attachment_type.PNG)
            message21 = "NPS- Direct Sales - Apr 24 Tab is visible and test-case passed successfully.."
            allure.attach(message21, name='test_program_tab', attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab', attachment_type=allure.attachment_type.PNG)
            message22 = "NPS- Direct Sales - Apr 24 Tab is not visible and test-case failed.."
            allure.attach(message22, name='test_program_tab', attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        element12 = self.driver.find_element(By.XPATH,"//p[text()='LVAC App Guide Apr 24']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element12)
        time.sleep(3)
        self.driver.execute_script("arguments[0].style.border='5px solid purple'", element12)
        time.sleep(3)
        if element12.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab', attachment_type=allure.attachment_type.PNG)
            message23 = "LVAC App Guide Tab is visible and test-case passed successfully.."
            allure.attach(message23, name='test_program_tab', attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab', attachment_type=allure.attachment_type.PNG)
            message24 = "LVAC App Guide Tab is not visible and test-case failed.."
            allure.attach(message24, name='test_program_tab', attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        element13 = self.driver.find_element(By.XPATH,"//p[text()='Selling Skills Direct Sales Apr 24']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element13)
        time.sleep(3)
        self.driver.execute_script("arguments[0].style.border='5px solid purple'", element13)
        time.sleep(3)
        if element13.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab', attachment_type=allure.attachment_type.PNG)
            message25 = "Selling Skills Direct Sales Tab is visible and test-case passed successfully.."
            allure.attach(message25, name='test_program_tab', attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab', attachment_type=allure.attachment_type.PNG)
            message26 = "Selling Skills Direct Sales Tab is not visible and test-case failed.."
            allure.attach(message26, name='test_program_tab', attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        element14 = self.driver.find_element(By.XPATH,"//p[text()='SS Tank and Vector Weekly Assessment Mar 24']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element14)
        time.sleep(3)
        self.driver.execute_script("arguments[0].style.border='5px solid purple'", element14)
        time.sleep(3)
        if element14.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab', attachment_type=allure.attachment_type.PNG)
            message27 = "SS Tank and Vector Weekly Assessment Tab is visible and test-case passed successfully.."
            allure.attach(message27, name='test_program_tab', attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab', attachment_type=allure.attachment_type.PNG)
            message28 = "SS Tank and Vector Weekly Assessment Tab is not visible and test-case failed.."
            allure.attach(message28, name='test_program_tab', attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        element15 = self.driver.find_element(By.XPATH,"//p[text()='Vector - W4 Mar 24']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element15)
        time.sleep(3)
        self.driver.execute_script("arguments[0].style.border='5px solid purple'", element15)
        time.sleep(3)
        if element15.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab', attachment_type=allure.attachment_type.PNG)
            message29 = "Vector - W4 Tab is visible and test-case passed successfully.."
            allure.attach(message29, name='test_program_tab', attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab', attachment_type=allure.attachment_type.PNG)
            message30 = "Vector - W4 Tab is not visible and test-case failed.."
            allure.attach(message30, name='test_program_tab', attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        element16 = self.driver.find_element(By.XPATH,'//footer[@class="footer-eureka mobfooter"]')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element16)
        time.sleep(3)
        self.driver.execute_script("arguments[0].style.border='5px solid purple'", element16)
        time.sleep(3)
        if element16.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab', attachment_type=allure.attachment_type.PNG)
            message31 = "Footer Tab is visible and test-case passed successfully.."
            allure.attach(message31, name='test_program_tab', attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab', attachment_type=allure.attachment_type.PNG)
            message32 = "Footer Tab is not visible and test-case failed.."
            allure.attach(message32, name='test_program_tab', attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
            assert False

    def test_program_tab_btns(self,setup):
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
        self.main_screen.click_program_tab()
        time.sleep(2)
        self.main_screen.click_program_tab_nsb()
        time.sleep(2)
        element = self.driver.find_element(By.XPATH,'//div[@class="program-accordion"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element)
        time.sleep(3)
        if element.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab_btns', attachment_type=allure.attachment_type.PNG)
            message01 = "New Program For Enrollment Tab is visible and test-case passed successfully.."
            allure.attach(message01, name='test_program_tab_btns', attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab_btns', attachment_type=allure.attachment_type.PNG)
            message02 = "New Program For Enrollment Tab is not visible and test-case failed.."
            allure.attach(message02, name='test_program_tab_btns', attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        self.main_screen.click_program_tab_sb()
        time.sleep(2)
        element1 = self.driver.find_element(By.XPATH,'//div[@class="program-accordion"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element1)
        time.sleep(3)
        if element1.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab_btns', attachment_type=allure.attachment_type.PNG)
            message03 = "New Program For Sellers Tab is visible and test-case passed successfully.."
            allure.attach(message03, name='test_program_tab_btns', attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab_btns', attachment_type=allure.attachment_type.PNG)
            message04 = "New Program For Sellers Tab is not visible and test-case failed.."
            allure.attach(message04, name='test_program_tab_btns', attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        self.main_screen.click_program_tab_cb()
        time.sleep(2)
        element2 = self.driver.find_element(By.XPATH,'//div[@class="interboxes"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element2)
        time.sleep(3)
        if element2.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab_btns', attachment_type=allure.attachment_type.PNG)
            message05 = "New Program For Customer Benefit Tab is visible and test-case passed successfully.."
            allure.attach(message05, name='test_program_tab_btns', attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab_btns', attachment_type=allure.attachment_type.PNG)
            message06 = "New Program For Customer Benefit Tab is not visible and test-case failed.."
            allure.attach(message06, name='test_program_tab_btns', attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        self.main_screen.click_back_btn_program_tab()
        time.sleep(2)
        element3 = self.driver.find_element(By.XPATH,'//div[@class="chart-sec"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element3)
        time.sleep(3)
        if element3.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab_btns', attachment_type=allure.attachment_type.PNG)
            message07 = "Back Button is working fine.."
            allure.attach(message07, name='test_program_tab_btns', attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_program_tab_btns', attachment_type=allure.attachment_type.PNG)
            message08 = "Back Button is not working.."
            allure.attach(message08, name='test_program_tab_btns', attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
            assert False




























