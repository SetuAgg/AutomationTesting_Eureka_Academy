from selenium.webdriver.common.by import By




class Eureka_Login_Page:
    textbox_username_name = "email"
    textbox_password_id = "passInput"
    login_btn_Xpath = '//button[@class="eureka_submit_btn_block "]'
    forgot_pass_close_btn = '//button[@class="btn-close"]'

    def __init__(self,driver):
        self.driver = driver


    def enter_user_name(self, username):
        self.driver.find_element(By.NAME, self.textbox_username_name).clear()
        self.driver.find_element(By.NAME, self.textbox_username_name).send_keys(username)

    def enter_pass_word(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)


    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login_btn_Xpath).click()

    def click_forgot_password_tab(self):
        self.driver.find_element(By.XPATH,'//a[@class="forgot-pwd-text"]').click()

    def click_eye_patch_button(self):
        self.driver.find_element(By.XPATH,'//div[@class="show-password"]').click()

    def click_forgot_password_close_button(self):
        self.driver.find_element(By.XPATH,self.forgot_pass_close_btn).click()

















