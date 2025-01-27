import os
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Eureka_Login_Page import Eureka_Login_Page
from test_cases.configurations import setup
import pytest
import time
import allure

class Test_02_Eureka_Login_Tabs:
    page_url = "https://eurekaacademy-preprod.niit.com"
    username = "3014029@mailinator.com"
    password = "Eureka@123"
    forgot_password_tab_Xpath = '//div[@class="forgot_password_text"]'

    @allure.title("Testing Title visibility of Login Page")
    def test_page_title(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        act_page_title = self.driver.title
        exp_page_title = "Eureka Forbes Academy"
        if act_page_title == exp_page_title:
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_page_title', attachment_type=AttachmentType.PNG)
            message01 = "Page Title i.e 'Eureka Forbes Academy' is matching with expected value and test-case passed successfully.."
            allure.attach(message01, name="Page_Title", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_page_title', attachment_type=AttachmentType.PNG)
            message02 = "Page Title is not matching with expected value and test-case failed.."
            allure.attach(message02, name="Page_Title", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
            assert False


    @allure.title("Testing Page Header Text visibility of Login Page")
    def test_page_header_text(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        act_welcome_message = self.driver.find_element(By.XPATH,'//p[@class="welcome_text"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", act_welcome_message)
        time.sleep(3)
        if act_welcome_message.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_page_header_text', attachment_type=AttachmentType.PNG)
            message01 = "Page Header Text is displayed and verified with highlight and test-case passed successfully.."
            allure.attach(message01, name="Header_Text", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_page_header_text', attachment_type=AttachmentType.PNG)
            message02 = "Page Header Text is not displayed and test-case failed.."
            allure.attach(message02, name="Header_Text", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
            assert False

    @allure.title("Testing Login Text visibility of Login Page")
    def test_page_login_text(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        act_login_text = self.driver.find_element(By.XPATH,'//div[@class="login_text"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", act_login_text)
        time.sleep(3)
        if act_login_text.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_page_login_text', attachment_type=AttachmentType.PNG)
            message01 = "Login Text is displayed and verified with highlight and test-case passed successfully.."
            allure.attach(message01, name="Login_Text", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_page_login_text', attachment_type=AttachmentType.PNG)
            message02 = "Login Text is not displayed and test-case failed.."
            allure.attach(message02, name="Login_Text", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
            assert False

    @allure.title("Testing Username_Label visibility of Login Page")
    def test_page_label01(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        act_label01 = self.driver.find_element(By.XPATH,"//label[text()='Email Address']")
        self.driver.execute_script("arguments[0].style.border='5px solid red'", act_label01)
        time.sleep(3)
        if act_label01.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_page_label01', attachment_type=AttachmentType.PNG)
            message01 = "Username Label text is displayed and verified with highlight and test-case passed successfully.."
            allure.attach(message01, name="Label_Username", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_page_label01', attachment_type=AttachmentType.PNG)
            message02 = "Username Label is not displayed and test-case failed.."
            allure.attach(message02, name="Label_Username", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
            assert False



    @allure.title("Testing Password_Label visibility of Login Page")
    def test_page_label02(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        act_label02 = self.driver.find_element(By.XPATH,"//label[text()='Password']")
        self.driver.execute_script("arguments[0].style.border='5px solid red'", act_label02)
        time.sleep(3)
        if act_label02.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_page_label02', attachment_type=AttachmentType.PNG)
            message01 = "Label02 is displayed and verified with highlight and test-case passed successfully.."
            allure.attach(message01, name="Label_Password", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_page_label02', attachment_type=AttachmentType.PNG)
            message02 = "Label02 is not displayed and test-case failed.."
            allure.attach(message02, name="Label_Password", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
            assert False


    def test_forgot_password_text(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        act_forgot_password_text = self.driver.find_element(By.XPATH,'//div[@class="forgot_password_text"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", act_forgot_password_text)
        time.sleep(3)
        if act_forgot_password_text.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_forgot_password_text', attachment_type=AttachmentType.PNG)
            message01 = "Forgot Password Text is displayed and verified with highlight and test-case passed successfully.."
            allure.attach(message01, name="Forgot_Password_Text", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_forgot_password_text', attachment_type=AttachmentType.PNG)
            message02 = "Forgot Password Text is not displayed and test-case failed.."
            allure.attach(message02, name="Forgot_Password_Text", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
            assert False

    def test_forgot_password_click(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        self.admin_lp = Eureka_Login_Page(self.driver)
        self.admin_lp.click_forgot_password_tab()
        time.sleep(3)
        forgot_dialog = self.driver.find_element(By.XPATH,'//p[@class="reset_paswd_text"]').text
        if forgot_dialog == "Set your default password? Please enter your Employee code.":
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_forgot_password_click', attachment_type=AttachmentType.PNG)
            message01 = "Forgot Password Dialog is displayed and test-case passed successfully.."
            allure.attach(message01, name="Forgot_Password_Text", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_forgot_password_click', attachment_type=AttachmentType.PNG)
            message02 = "Forgot Password Dialog is not displayed and test-case failed.."
            allure.attach(message02, name="Forgot_Password_Text", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
            assert False

    def test_eye_patch(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        act_eye_patch = self.driver.find_element(By.XPATH,'//div[@class="show-password"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", act_eye_patch)
        time.sleep(3)
        if act_eye_patch.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_eye_patch', attachment_type=AttachmentType.PNG)
            message01 = "Eye Patch is displayed and verified with highlight and test-case passed successfully.."
            allure.attach(message01, name="Eye_Patch", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_eye_patch', attachment_type=AttachmentType.PNG)
            message02 = "Eye Patch is not displayed and test-case failed.."
            allure.attach(message02, name="Eye_Patch", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
            assert False

    def test_sliding_dots(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        act_sliding_dots = self.driver.find_element(By.XPATH,'//ul[@class="slick-dots"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", act_sliding_dots)
        time.sleep(3)
        if act_sliding_dots.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_sliding_dots', attachment_type=AttachmentType.PNG)
            message01 = "Sliding Dots is displayed and verified with highlight and test-case passed successfully.."
            allure.attach(message01, name="Sliding_Dots", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_sliding_dots', attachment_type=AttachmentType.PNG)
            message02 = "Sliding Dots is not displayed and test-case failed.."
            allure.attach(message02, name="Sliding_Dots", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
            assert False

    def test_page_footer(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        act_footer = self.driver.find_element(By.XPATH,'//div[@class="desktop-footer"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", act_footer)
        time.sleep(3)
        if act_footer.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_page_footer', attachment_type=AttachmentType.PNG)
            message01 = "Footer is displayed and verified with highlight and test-case passed successfully.."
            allure.attach(message01, name="Footer", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_page_footer', attachment_type=AttachmentType.PNG)
            message02 = "Footer is not displayed and test-case failed.."
            allure.attach(message02, name="Footer", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
            assert False

    def test_page_logo(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        act_logo = self.driver.find_element(By.XPATH,'//div[@class="logo-left"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", act_logo)
        time.sleep(3)
        if act_logo.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_page_logo', attachment_type=AttachmentType.PNG)
            message01 = "Logo is displayed and verified with highlight and test-case passed successfully.."
            allure.attach(message01, name="Logo", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_page_logo', attachment_type=AttachmentType.PNG)
            message02 = "Logo is not displayed and test-case failed.."
            allure.attach(message02, name="Logo", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
            assert False

    def test_sliding_images(self, setup):
        self.driver = setup
        self.driver.get(self.page_url)
        self.driver.maximize_window()
        time.sleep(5)
        # Locator for the image inside the slider (update this according to the webpage structure)
        slider_image_locator = '//div[@class="slick-track"]'
        # Set for storing unique image URLs (prevents duplicates)
        unique_images = set()
        # Capture sliding images
        for i in range(4):
            try:
                # Find the current image in the slider
                current_image = self.driver.find_element(By.XPATH, slider_image_locator)
                # Get the image URL (src attribute)
                image_src = current_image.get_attribute("src")
                # If the image is unique, add it to the set and take a screenshot
                if image_src not in unique_images:
                    unique_images.add(image_src)
                    # Save screenshot to a file
                    screenshot_path = f"slider_image_{len(unique_images)}.png"
                    self.driver.save_screenshot(screenshot_path)
                    # Attach the screenshot to Allure
                    with open(screenshot_path, "rb") as image_file:
                        allure.attach(image_file.read(), name=f"Slider Image {len(unique_images)}", attachment_type=allure.attachment_type.PNG)
                        time.sleep(5)  # Adjust this based on the slider's interval
            except Exception as e:
                        print(f"Error capturing image: {e}")
                        break

            # Log the total number of unique images
            print(f"Total unique images in the slider: {len(unique_images)}")

            # Clean up
            self.driver.close()


    def test_page_image(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        act_image = self.driver.find_element(By.XPATH,'//div[@class="slick-slider slickDesktop slick-initialized"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", act_image)
        time.sleep(3)
        if act_image.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_page_image', attachment_type=AttachmentType.PNG)
            message01 = "Image is displayed and verified with highlight and test-case passed successfully.."
            allure.attach(message01, name="Image", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_page_image', attachment_type=AttachmentType.PNG)
            message02 = "Image is not displayed and test-case failed.."
            allure.attach(message02, name="Image", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
            assert False











































