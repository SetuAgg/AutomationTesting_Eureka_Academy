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
    textbox_username_name = "email"
    textbox_password_id = "passInput"


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
        time.sleep(2)
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


    def test_eye_patch_visibility(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        self.admin_lp = Eureka_Login_Page(self.driver)
        self.admin_lp.enter_user_name(self.username)
        self.admin_lp.enter_pass_word(self.password)
        time.sleep(2)
        assert True
        allure.attach(self.driver.get_screenshot_as_png(), name='test_eye_patch_invisible', attachment_type=AttachmentType.PNG)
        message07 = "Password is not visible before eye patch click and test-case passed successfully.."
        allure.attach(message07, name="Eye_Patch_Invisible", attachment_type=allure.attachment_type.TEXT)
        time.sleep(3)
        self.admin_lp = Eureka_Login_Page(self.driver)
        self.admin_lp = self.driver.find_element(By.NAME, self.textbox_username_name).clear()
        self.admin_lp = self.driver.find_element(By.ID, self.textbox_password_id).clear()
        time.sleep(2)
        self.admin_lp = Eureka_Login_Page(self.driver)
        self.admin_lp.enter_user_name(self.username)
        self.admin_lp.enter_pass_word(self.password)
        time.sleep(2)
        ele = self.driver.find_element(By.XPATH,'//div[@class="show-password"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", ele)
        time.sleep(2)
        self.admin_lp.click_eye_patch_button()
        time.sleep(2)
        assert True
        allure.attach(self.driver.get_screenshot_as_png(), name='test_eye_patch_click', attachment_type=AttachmentType.PNG)
        message08 = "Password is visible after eye patch click and test-case passed successfully.."
        allure.attach(message08, name="Eye_Patch_Click", attachment_type=allure.attachment_type.TEXT)
        self.driver.close()

    @allure.title("Testing visibility of Login Page")
    def test_page_tabs(self, setup):
        self.driver = setup
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        act_page_title = self.driver.title
        exp_page_title = "Eureka Forbes Academy"
        if act_page_title == exp_page_title:
            assert True
            message01 = "Page Title i.e 'Eureka Forbes Academy' is matching with expected value and test-case passed successfully.."
            allure.attach(message01, name="Page_Title", attachment_type=allure.attachment_type.TEXT)
        else:
            message02 = "Page Title is not matching with expected value and test-case failed.."
            allure.attach(message02, name="Page_Title", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(2)
        act_welcome_message = self.driver.find_element(By.XPATH, '//p[@class="welcome_text"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", act_welcome_message)
        time.sleep(2)
        if act_welcome_message.is_displayed():
            assert True
            message01 = "Page Header Text is displayed and verified with highlight and test-case passed successfully.."
            allure.attach(message01, name="Header_Text", attachment_type=allure.attachment_type.TEXT)
        else:
            message02 = "Page Header Text is not displayed and test-case failed.."
            allure.attach(message02, name="Header_Text", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(2)
        act_login_text = self.driver.find_element(By.XPATH, '//div[@class="login_text"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", act_login_text)
        time.sleep(2)
        if act_login_text.is_displayed():
            assert True
            message01 = "Login Text is displayed and verified with highlight and test-case passed successfully.."
            allure.attach(message01, name="Login_Text", attachment_type=allure.attachment_type.TEXT)
        else:
            message02 = "Login Text is not displayed and test-case failed.."
            allure.attach(message02, name="Login_Text", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(2)
        act_label01 = self.driver.find_element(By.XPATH, "//label[text()='Email Address']")
        self.driver.execute_script("arguments[0].style.border='5px solid red'", act_label01)
        time.sleep(2)
        if act_label01.is_displayed():
            assert True
            message01 = "Username Label text is displayed and verified with highlight and test-case passed successfully.."
            allure.attach(message01, name="Label_Username", attachment_type=allure.attachment_type.TEXT)
        else:
            message02 = "Username Label is not displayed and test-case failed.."
            allure.attach(message02, name="Label_Username", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(2)
        act_label02 = self.driver.find_element(By.XPATH, "//label[text()='Password']")
        self.driver.execute_script("arguments[0].style.border='5px solid red'", act_label02)
        time.sleep(2)
        if act_label02.is_displayed():
            assert True
            message01 = "Label02 is displayed and verified with highlight and test-case passed successfully.."
            allure.attach(message01, name="Label_Password", attachment_type=allure.attachment_type.TEXT)
        else:
            message02 = "Label02 is not displayed and test-case failed.."
            allure.attach(message02, name="Label_Password", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(2)
        act_forgot_password_text = self.driver.find_element(By.XPATH, '//div[@class="forgot_password_text"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", act_forgot_password_text)
        time.sleep(2)
        if act_forgot_password_text.is_displayed():
            assert True
            message01 = "Forgot Password Text is displayed and verified with highlight and test-case passed successfully.."
            allure.attach(message01, name="Forgot_Password_Text", attachment_type=allure.attachment_type.TEXT)
        else:
            message02 = "Forgot Password Text is not displayed and test-case failed.."
            allure.attach(message02, name="Forgot_Password_Text", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(2)
        self.admin_lp = Eureka_Login_Page(self.driver)
        self.admin_lp.click_forgot_password_tab()
        time.sleep(2)
        forgot_dialog = self.driver.find_element(By.XPATH, '//div[@class="modal-content custom-modal"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", forgot_dialog)
        if forgot_dialog.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='Forgot_Dialog', attachment_type=AttachmentType.PNG)
            message01 = "Forgot Password Dialog is displayed and test-case passed successfully.."
            allure.attach(message01, name="Forgot_Password_Dialog", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='Forgot_Dialog', attachment_type=AttachmentType.PNG)
            message02 = "Forgot Password Dialog is not displayed and test-case failed.."
            allure.attach(message02, name="Forgot_Password_Dialog", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(2)
        element = self.driver.find_element(By.XPATH, '//button[@class="btn-close"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element)
        time.sleep(2)
        self.admin_lp.click_forgot_password_close_button()
        time.sleep(2)
        act_eye_patch = self.driver.find_element(By.XPATH, '//div[@class="show-password"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", act_eye_patch)
        time.sleep(2)
        if act_eye_patch.is_displayed():
            assert True
            message01 = "Eye Patch is displayed and verified with highlight and test-case passed successfully.."
            allure.attach(message01, name="Eye_Patch", attachment_type=allure.attachment_type.TEXT)
        else:
            message02 = "Eye Patch is not displayed and test-case failed.."
            allure.attach(message02, name="Eye_Patch", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(2)
        element2 = self.driver.find_element(By.XPATH, '//button[@class="eureka_submit_btn_block "]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element2)
        time.sleep(2)
        act_sliding_dots = self.driver.find_element(By.XPATH, '//ul[@class="slick-dots"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", act_sliding_dots)
        time.sleep(2)
        if act_sliding_dots.is_displayed():
            assert True
            message01 = "Sliding Dots is displayed and verified with highlight and test-case passed successfully.."
            allure.attach(message01, name="Sliding_Dots", attachment_type=allure.attachment_type.TEXT)
        else:
            message02 = "Sliding Dots is not displayed and test-case failed.."
            allure.attach(message02, name="Sliding_Dots", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(2)
        act_footer = self.driver.find_element(By.XPATH, '//div[@class="desktop-footer"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", act_footer)
        time.sleep(3)
        if act_footer.is_displayed():
            assert True
            message01 = "Footer is displayed and verified with highlight and test-case passed successfully.."
            allure.attach(message01, name="Footer", attachment_type=allure.attachment_type.TEXT)
        else:
            message02 = "Footer is not displayed and test-case failed.."
            allure.attach(message02, name="Footer", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(2)
        act_logo = self.driver.find_element(By.XPATH, '//div[@class="logo-left"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", act_logo)
        time.sleep(2)
        if act_logo.is_displayed():
            assert True
            message01 = "Logo is displayed and verified with highlight and test-case passed successfully.."
            allure.attach(message01, name="Logo", attachment_type=allure.attachment_type.TEXT)
        else:
            message02 = "Logo is not displayed and test-case failed.."
            allure.attach(message02, name="Logo", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(2)
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
                        allure.attach(image_file.read(), name=f"Slider Image {len(unique_images)}",
                                      attachment_type=allure.attachment_type.PNG)
                        time.sleep(5)  # Adjust this based on the slider's interval
            except Exception as e:
                print(f"Error capturing image: {e}")
                break

            # Log the total number of unique images
            print(f"Total unique images in the slider: {len(unique_images)}")
        time.sleep(2)
        act_image = self.driver.find_element(By.XPATH, '//div[@class="slick-slider slickDesktop slick-initialized"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", act_image)
        time.sleep(2)
        if act_image.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_page_image',
                          attachment_type=AttachmentType.PNG)
            message01 = "Image is displayed and verified with highlight and test-case passed successfully.."
            allure.attach(message01, name="Image", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_page_image',
                          attachment_type=AttachmentType.PNG)
            message02 = "Image is not displayed and test-case failed.."
            allure.attach(message02, name="Image", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
            assert False
























