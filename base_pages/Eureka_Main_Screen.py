from selenium.webdriver.common.by import By

class Eureka_Main_Screen:
    textbox_username_name = "email"
    textbox_password_id = "passInput"
    login_btn_Xpath = '//button[@class="eureka_submit_btn_block "]'
    courses_tab = "//a[text()='Courses']"
    not_selected_tab = "//button[text()='Not Started']"
    started_tab = "//button[text()='Started']"
    completed_tab = "//button[text()='Completed']"
    back_btn = '//button[@class="bckbtn"]'
    assessment_tab = "//a[text()='Assessments']"
    not_started_btn_assessment_tab = "//button[text()='Not Started']"
    started_btn_assessment_tab = "//button[text()='Started']"
    completed_btn_assessment_tab = "//button[text()='Completed']"
    back_btn_assessment_tab = '//button[@class="bckbtn"]'
    session_tab = "//a[text()='Sessions']"
    session_tab_day_btn = '//button[@class="btn btn-primary btn-block setup-button upgrate_colpeteBtn mr-2 active"]'
    session_tab_month_btn = '//button[@class="btn btn-primary btn-block setup-button upgrate_colpeteBtn mr-2 active"]'
    session_tab_week_btn = '//button[@class="btn btn-primary btn-block setup-button upgrate_colpeteBtn mr-2 active"]'
    session_tab_back_btn = '//button[@class="btn btn-primary bckbtn"]'
    program_tab = "//a[text()='Program']"
    program_tab_nsb = '//button[@class=" active nav-link"]'
    program_tab_sb = "//button[text()='Started']"
    program_tab_cb = "//button[text()='Completed']"
    program_tab_back_btn = '//button[@class="bckbtn"]'




    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.NAME, self.textbox_username_name).clear()
        self.driver.find_element(By.NAME, self.textbox_username_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login_btn_Xpath).click()



    def click_courses_tab(self):
        self.driver.find_element(By.XPATH,self.courses_tab).click()

    def click_not_started_tab(self):
        self.driver.find_element(By.XPATH,self.not_selected_tab).click()

    def click_started_tab(self):
        self.driver.find_element(By.XPATH,self.started_tab).click()

    def click_completed_tab(self):
        self.driver.find_element(By.XPATH,self.completed_tab).click()

    def click_back_button(self):
        self.driver.find_element(By.XPATH,self.back_btn).click()



    def click_assessment_tab(self):
        self.driver.find_element(By.XPATH,self.assessment_tab).click()

    def click_not_started_btn_assessment_tab(self):
        self.driver.find_element(By.XPATH,self.not_started_btn_assessment_tab).click()

    def click_started_btn_assessment_tab(self):
        self.driver.find_element(By.XPATH,self.started_btn_assessment_tab).click()

    def click_completed_btn_assessment_tab(self):
        self.driver.find_element(By.XPATH,self.completed_btn_assessment_tab).click()

    def click_back_btn_assessment_tab(self):
        self.driver.find_element(By.XPATH,self.back_btn_assessment_tab).click()




    def click_session_tab(self):
        self.driver.find_element(By.XPATH,self.session_tab).click()

    def click_session_tab_day_btn(self):
        self.driver.find_element(By.XPATH,self.session_tab_day_btn).click()

    def click_session_tab_month_btn(self):
        self.driver.find_element(By.XPATH,self.session_tab_month_btn).click()

    def click_session_tab_week_btn(self):
        self.driver.find_element(By.XPATH,self.session_tab_week_btn).click()

    def click_back_btn_session_tab(self):
        self.driver.find_element(By.XPATH,self.session_tab_back_btn).click()





    def click_program_tab(self):
        self.driver.find_element(By.XPATH,self.program_tab).click()

    def click_program_tab_nsb(self):
        self.driver.find_element(By.XPATH,self.program_tab_nsb).click()

    def click_program_tab_sb(self):
        self.driver.find_element(By.XPATH,self.program_tab_sb).click()

    def click_program_tab_cb(self):
        self.driver.find_element(By.XPATH,self.program_tab_cb).click()

    def click_back_btn_program_tab(self):
        self.driver.find_element(By.XPATH,self.program_tab_back_btn).click()

















