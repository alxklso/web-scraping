from selenium import webdriver
from selenium.webdriver.support import ui, expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

class Bot():
    def __init__(self):
        self.login('username', 'password')

    def login(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.get('https://instagram.com')
        sleep(1)
        
        # enter username
        username_login = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_login.send_keys(username)
        sleep(1)

        #enter password
        password_login = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_login.send_keys(password)
        sleep(1)

        # click login button
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
        sleep(2)


def main():
    instabot = Bot()
    instabot()

if __name__ == '__main__':
    main()