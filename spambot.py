import time
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import random
import os, shutil

driver = webdriver.Chrome()

driver.get("https://discord.com/login")
time.sleep(6)

#--------------- Edit Here -------------------------------------------------------------

# Enter your account details here 
username = '' #Enter your username
password = '' #Enter your password

# Copy the URL of channel where you wanna send messages and paste below
channelURL = ""

#-------------- Edit End ----------------------------------------------------------------

# Initialize and input email
username_input = driver.find_element_by_name('email')
username_input.send_keys(username)

# Initialize and input password
password_input = driver.find_element_by_name('password')
password_input.send_keys(password)

# Initialize and login
login_button = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]')
login_button.click()
print(">>Login Complete!")
time.sleep(10)

driver.get(channelURL)
print(">Opening The Server Link...")
time.sleep(5)

# Msg Sending
text = ['asd', 'asdasd', 'afafsf', 'AAAAAA', 'aaaaaa', 'a', 'aa', 'asdaas', 'jsjsjs', 'qweqwe', 'qwerty'] #You can change this word list however you want
x = random.randint(3, 7) #X in this is case is used to determine the time interval of sending each message
i = 0
while True:
    time.sleep(x)
    msg_input = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[2]/div')

    msg_input.send_keys(random.choice(text))
    msg_input.send_keys(Keys.ENTER)
    i+=1
    print(">Number of Messages sent: "+str(i))
print("Its Done!")