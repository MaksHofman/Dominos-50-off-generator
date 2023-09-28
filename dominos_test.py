import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
"""
mail = "https://www.youtube.com/"
"""
mail = "https://temp-mail.org/"

dominos = "https://dominospizza.pl/"

def open_10minutmail():
    driver = webdriver.Chrome()
    
    #loading 10 minut mail in
    driver.get(mail)
    time.sleep(20)
    #WebDriverWait(driver, 20).until(EC.not_(EC.text_to_be_present_in_element_value((By.ID, 'mail'), 'Loading')))
    dynamic_value = driver.find_element(By.ID, 'mail').get_attribute('value')
    ten_minut_mail_gen = dynamic_value
    print(ten_minut_mail_gen)

    #opening dominos an sending the mail
    driver.execute_script("window.open('', '_blank');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(dominos)
    svg_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="aside"]/aside[3]/div/button')))
    svg_button.click()
    email_input = driver.find_element(By.ID, "Email")
    email_input.send_keys(ten_minut_mail_gen)
    checkbox = driver.find_element(By.XPATH, '//*[@id="main"]/div[4]/div[2]/div/form/div[2]/label/span')
    checkbox.click()
    button = driver.find_element(By.XPATH, '//*[@id="main"]/div[4]/div[2]/div/form/button')
    button.click()
    driver.switch_to.window(driver.window_handles[0])

    #opening the first mail and acceping sub
    #no problem till here
    element = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[4]/ul/li[2]/div[1]/a')))
    driver.execute_script('arguments[0].click();', element)
    link_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//a[@style="color: rgb(255, 255, 255); font-size: 16px; font-weight: 600; line-height: 22px; text-transform: uppercase; text-decoration: none;" and contains(@href, "Aktywuj subskrypcję")]')))
    link_element.click()
    driver.switch_to.window(driver.window_handles[0])
    return_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//a[@class="back-btn-link"]')))
    return_button.click()
    
    #opening the second mail and getting the code
    time.sleep(90)
    element_2mail = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//span[@class="inboxSubject small subject-title d-none visable-xs-sm" and contains(text(), "Witaj w newsletterze Domino\'s!")]//ancestor::a')))
    element_2mail.click()
    element_code = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//p[@style="font-size: 16px; font-weight: bold; text-align: center; margin: 0px; color: rgb(23, 44, 58); line-height: 22px;"]')))
    text_to_save = element_code.text
    with open("dominos_cody.txt", "a") as file:
            file.write(text_to_save + "\n")

    time.sleep(400)
    driver.close()
open_10minutmail()