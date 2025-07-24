from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class CoworkingPage:
    def __init__(self, driver):
        self.driver = driver
        self.sign_up_btn = (By.CSS_SELECTOR, "#app > div > div.coworking > div > button")
        self.aybek_2_btn = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-container > div.material-dialog__window-body > div > div.container.coworking__page-dialog-follow-container > div.coworking__page-dialog-follow-branch > div:nth-child(2) > div.list-tile.coworking__page-dialog-follow-branch-item-list > div.list-tile__trailing")
        self.select_btn_1 = (By.CSS_SELECTOR, "#dialog > div.material-dialog.coworking__branch-dialog > div > div.material-dialog__window-actions > button:nth-child(2)")
        self.date_btn = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-container > div.material-dialog__window-body > div > div.container.coworking__page-dialog-follow-container > div.coworking__page-dialog-follow-date > div > div:nth-child(5) > button")
        self.group_btn = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-container > div.material-dialog__window-body > div > div.container.coworking__page-dialog-follow-container > div.list-tile.coworking__page-dialog-follow-list")
        self.round_btn = (By.CSS_SELECTOR, "#dialog > div:nth-child(2) > div > div.material-dialog__window-container > div.material-dialog__window-body > div > div > div > div.list-tile__trailing > button")
        self.select_btn_2 = (By.CSS_SELECTOR, "#dialog > div:nth-child(2) > div > div.material-dialog__window-actions > button:nth-child(2)")
        self.time = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-container > div.material-dialog__window-body > div > div.container.coworking__page-dialog-follow-container > div.coworking__page-dialog-follow-timeseat > div:nth-child(1) > label > input")
        self.hours = (By.CSS_SELECTOR, "#dialog > div.material-dialog.timepicker > div > div.material-dialog__window-container > div.material-dialog__window-body > div > label:nth-child(1) > input")
        self.minutes = (By.CSS_SELECTOR, "#dialog > div.material-dialog.timepicker > div > div.material-dialog__window-container > div.material-dialog__window-body > div > label:nth-child(2) > input")
        self.select_btn_3 = (By.CSS_SELECTOR, "#dialog > div.material-dialog.timepicker > div > div.material-dialog__window-actions > button:nth-child(2)")
        self.place = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-container > div.material-dialog__window-body > div > div.container.coworking__page-dialog-follow-container > div.coworking__page-dialog-follow-timeseat > div:nth-child(2) > div")
        self.computer = (By.CSS_SELECTOR, "#dialog > div:nth-child(2) > div > div.material-dialog__window-container > div.material-dialog__window-body > div.coworking__page-dialog-time-seats > div:nth-child(10)")
        self.select_btn_4 = (By.CSS_SELECTOR, "#dialog > div:nth-child(2) > div > div.material-dialog__window-actions > button:nth-child(2)")
        self.send_btn = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-actions > button:nth-child(2)")

    def click_sign_up_btn(self):
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable((self.sign_up_btn))).click()

    def click_aybek_2_btn(self):
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable((self.aybek_2_btn))).click()

    def click_select_btn_1(self):
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable((self.select_btn_1))).click()

    def click_date_btn(self):
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable((self.date_btn))).click()

    def click_group_btn(self):
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable((self.group_btn))).click()

    def click_round_btn(self):
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable((self.round_btn))).click()

    def click_select_btn_2(self):
                wait = WebDriverWait(self.driver, 10)
                wait.until(EC.element_to_be_clickable((self.select_btn_2))).click()

    def enter_time(self):
                wait = WebDriverWait(self.driver, 10)
                wait.until(EC.element_to_be_clickable((self.time))).click()

    def enter_hours(self, hours):
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located((self.hours))).send_keys(hours)

    def enter_minutes(self, minutes, ):
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located((self.minutes))).send_keys(minutes)

    def click_select_btn_3(self):
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable((self.select_btn_3))).click()

    def click_place(self,):
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located((self.place))).click()


    def click_computer(self):
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable((self.computer))).click()

    def click_select_btn_4(self):
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable((self.select_btn_4))).click()

    def click_send_btn(self):
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable((self.send_btn))).click()