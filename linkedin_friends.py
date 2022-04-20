import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from settings import CHROME_PATH, CHROME_BINARY_PATH, username, password, MOBILE_UA, amount_of_people_to_add


def execute_login(driver):
    driver.get(
        'https://www.linkedin.com/login/ru?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
    driver.find_element_by_xpath(
        '//*[@id="organic-div"]/form/div[3]/button').click()


def find_connection_button() -> tuple:
    pyautogui.press('down', presses=25)
    time.sleep(1)
    btn_location = pyautogui.locateAllOnScreen('default.PNG')
    if not btn_location:
        btn_location = pyautogui.locateAllOnScreen('dark.PNG')
    if not btn_location:
        btn_location = pyautogui.locateAllOnScreen('light.PNG')
    return btn_location


def start_adding(amount_of_people: int):
    for i in range(amount_of_people):
        for button in find_connection_button():
            pyautogui.click(button)


def main():
    options = Options()
    options.add_argument(f"user-agent={MOBILE_UA}")
    options.binary_location = CHROME_BINARY_PATH
    driver = webdriver.Chrome(CHROME_PATH, chrome_options=options)
    execute_login(driver)
    driver.get('https://www.linkedin.com/mynetwork/')
    time.sleep(3)
    start_adding(amount_of_people_to_add)
    driver.quit()


if __name__ == '__main__':
    main()
