from selenium import webdriver
#pip install selenium

import time
from random import randint

class InstagramBot:
    def __init__(self , username , password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
        #install web driver chrome

    def Quit(self):
        self.driver.quit()

    #login function
    def Login(self):
        self.driver.get('https://www.instagram.com/')
        time.sleep(2)
        user_name = self.driver.find_element_by_xpath('//input[@name="username"]')
        user_name.clear()
        user_name.send_keys(self.username)
        pass_word = self.driver.find_element_by_xpath('//input[@name="password"]')
        pass_word.clear()
        pass_word.send_keys(self.password)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        time.sleep(3)

    #like function
    def Like(self,hs,num):
        driver = self.driver
        hashtag = hs.split(',')
        for i in range(len(hashtag)):
            driver.get(f'https://www.instagram.com/explore/tags/{hashtag[i]}/')
            link_2 = []

            for j in range(num):  
                link = driver.find_elements_by_tag_name('a')
                link_2 = [l.get_attribute('href') for l in link if 'com/p/' in l.get_attribute('href') ]
                time.sleep(4)
                driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
                time.sleep(4)
            for i in range(len(link_2)):
                driver.get(link_2[i])
                driver.find_element_by_class_name('wpO6b ').click()
                time.sleep(randint(1,5))

# Enter Username and Passsword
user = InstagramBot(input('Enter Username : '),input('Enter Passsword : '))

user.Login()
user.Like(input('Enter Tags : '),4)