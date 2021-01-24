#! /usr/bin/python3

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from decouple import config

print(
    """----------------WELCOME TO GITHUB AUTOMATION------------------\n
Which one is installed in your system?\n1. VS code or,\n2. Atom\nIf not please install anyone of them and run the program again.\n3. Exit: \nChoose to Proceed... """
)
nnn = int(input("CHOOSE: "))
print("""HAVE YOU ENABLED THE 2FA authentication on your Github Account: """)
twofactor_auth = int(
    input(
        "IF YES PRESS 1(Please Keep your phone close you would have to enter OTP in time limit of 20 seconds), else 2: "
    )
)
if nnn != 3:
    your_project_path = input(
        "ENTER YOUR PROJECTS DIRECTORY PATH (For eg. E:\My_Projects ) or leave it, the program will create the repo in the present directory :"
    )
    path_ = os.path.join(your_project_path)
    project_name = input("ENTER YOUR PROJECT_NAME : ")
    github_username = config("GITHUB_USERNAME")
    github_pass = config("GITHUB_PASSWORD")
    if len(github_username) == 0 and len(github_pass) == 0:  # if env variables not set in .env files
        print("Looks Like You have not created .env file don't worry enter your login credentials here,")
        github_username = input("ENTER YOUR GITHUB_USERNAME: ")
        github_pass = input("ENTER YOUR GITHUB_PASSWORD: ")
    new_repo_name = input("Enter your new github repo name: ")

    github_username = config("GITHUB_USERNAME")
    github_pass = config("GITHUB_PASSWORD")

    driver = webdriver.Chrome()
    driver.get("https://www.github.com/")
    driver.maximize_window()
    click_signin = driver.find_element_by_xpath(
        "/html/body/div[1]/header/div/div[2]/div[2]/a[1]"
    )
    click_signin.click()
    time.sleep(1.5)
    username_ = driver.find_element_by_xpath("""//*[@id="login_field"]""")
    username_.click()

    username_.send_keys(github_username)
    time.sleep(1.5)
    password = driver.find_element_by_name("password")
    password.click()
    password.send_keys(github_pass)
    time.sleep(1.5)
    click_login = driver.find_element_by_name("commit")
    click_login.click()
    time.sleep(1.5)

    # 2FA Authentication
    if twofactor_auth == 1:
        try:
            send_otp = driver.find_element_by_xpath("""//*[@id="otp"]""")
            send_otp.click()
            otp_ = int(input("ENTER OTP ( IN 20 seconds): "))
            send_otp.send_keys(otp_)
            time.sleep(20)
            otp_verify = driver.find_element_by_xpath(
                """//*[@id="login"]/div[5]/form/button"""
            )
            otp_verify.click()
        except:
            print("OTP Not entered/OTP did not match\nRun Again.")
            otp_verify.quit()

    new_repo = driver.find_element_by_xpath("""//*[@id="repos-container"]/h2/a""")
    new_repo.click()

    time.sleep(1.5)

    new_repo = driver.find_element_by_name("repository[name]")
    new_repo.click()

    time.sleep(1.5)

    new_repo.send_keys(new_repo_name)

    readme = driver.find_element_by_css_selector("#repository_auto_init")
    readme.click()

    try:
        create_repo = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "#new_repository > div.js-with-permission-fields > button",
                )
            )
        )
        create_repo.click()
    except:
        print("SOME ERROR CLICKING CREATE_REPO")
        create_repo.quit()

    time.sleep(2)

    repo_name_paste = f"https://github.com/{github_username}/{new_repo_name}.git"

    # path_ = os.path.join("/home/<username>/Projects")  # Eg. set your projects folder path here

    if len(path_) == 0:
        path_ = os.getcwd()

    os.chdir(path_)
    os.system(f"git clone {repo_name_paste}")
    path_2 = os.path.join(path_, new_repo_name)  # set your projects folder path here

    os.chdir(path_2)
    os.getcwd()
    os.system("git init")
    os.system(f"cd . > .gitignore")
    os.system("git add .")
    if nnn == 1:
        os.system("code .")
    if nnn == 2:
        os.system("atom .")
    print(
        "\n\n----------SUCCESSFULLY CREATED A REPOSITORY and set git tracked!\n Now you can see on github repository tab, your new repo already present.------------\n"
    )
    print(
        "------------------Created by TUSHAR RAO,  THANK YOU FOR USING-----------------!"
    )
    nnnn = input("--------------Press enter to close the window------------------")
    driver.close()
    driver.quit()
