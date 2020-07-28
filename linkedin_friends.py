import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from settings import CHROME_PATH, username, password, MOBILE_UA, amount_of_people_to_add


def main():
    options = Options()
    options.add_argument(f"user-agent={MOBILE_UA}")
    driver = webdriver.Chrome(CHROME_PATH, chrome_options=options)
    driver.get('https://www.linkedin.com/login/ru?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

    try:
        driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
        driver.find_element_by_xpath('//*[@id="app__container"]/main/div[2]/div[2]/form/div[3]/button').click()
    except:
        pass

    try:
        driver.get('https://www.linkedin.com/mynetwork/')
        time.sleep(3)
        try:
            driver.find_element_by_xpath('//*[@id="app-upsell-container"]/button').click()
        except:
            pass
        for i in range(amount_of_people_to_add):
            btn_location = pyautogui.locateOnScreen('btn_img.PNG')
            if btn_location:
                pyautogui.click(btn_location)
                print(f'Sent a connection request => #{i}')
            else:
                for scroll in range(20):
                    pyautogui.keyDown('down')
    except:
        pass
    driver.quit()


if __name__ == '__main__':
    main()
