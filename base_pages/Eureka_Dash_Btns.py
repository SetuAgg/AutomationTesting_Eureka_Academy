from selenium.webdriver.common.by import By

class Eureka_Dash_Btns:
    program_tab_Xpath = "//a[text()='Program']"
    courses_tab_Xpath = "//a[text()='Courses']"
    session_tab_Xpath = "//a[text()='Sessions']"
    assessments_tab_Xpath = "//a[text()='Assessments']"
    search_tab_Xpath = '//div[@class="headersearch-btn"]'
    feedback_tab_Xpath = '//div[@class="feedback--button contentDesktopView"]'
    view_join_tab_Xpath = "//p[text()='View/Join your scheduled sessions']"
    view_assigned_tab_Xpath = "//p[text()='View assigned courses']"
    view_assigned_programs_tab_Xpath = "//p[text()='View assigned programs']"
    event_assessment_tab_Xpath = "//p[text()='Event assessments']"
    back_btn = '//button[@class="bckbtn"]'
    skip_btn = '//button[@class="skipBtn btn btn-primary"]'
    back_btn2 = '//button[@class="btn btn-primary bckbtn"]'
    back_btn3 = '//button[@class="bckbtn"]'
    back_btn4 = '//button[@class="bckbtn"]'




    def __init__(self,driver):
        self.driver = driver

    def click_program_tab(self):
        self.driver.find_element(By.XPATH,self.program_tab_Xpath).click()

    def click_courses_tab(self):
        self.driver.find_element(By.XPATH,self.courses_tab_Xpath).click()

    def click_session_tab(self):
        self.driver.find_element(By.XPATH,self.session_tab_Xpath).click()

    def click_assessments_tab(self):
        self.driver.find_element(By.XPATH,self.assessments_tab_Xpath).click()
    def click_search_tab(self):
        self.driver.find_element(By.XPATH,self.search_tab_Xpath).click()

    def click_feedback_tab(self):
        self.driver.find_element(By.XPATH,self.feedback_tab_Xpath).click()

    def click_view_join_tab(self):
        self.driver.find_element(By.XPATH,self.view_join_tab_Xpath).click()

    def click_view_assigned_tab(self):
        self.driver.find_element(By.XPATH,self.view_assigned_tab_Xpath).click()

    def click_view_assigned_programs_tab(self):
        self.driver.find_element(By.XPATH,self.view_assigned_programs_tab_Xpath).click()

    def click_event_assessment_tab(self):
        self.driver.find_element(By.XPATH,self.event_assessment_tab_Xpath).click()

    def click_back_btn(self):
        self.driver.find_element(By.XPATH,self.back_btn).click()

    def click_skip_btn(self):
        self.driver.find_element(By.XPATH,self.skip_btn).click()

    def click_back_btn2(self):
        self.driver.find_element(By.XPATH,self.back_btn2).click()

    def click_back_btn3(self):
        self.driver.find_element(By.XPATH,self.back_btn3).click()

    def click_back_btn4(self):
        self.driver.find_element(By.XPATH,self.back_btn4).click()






