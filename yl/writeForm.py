from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from time import sleep
from pathlib import Path

import os

# 个人信息
name = "张三"
idNum = "你的学号"
phone = "你的手机号"
major = "你的专业"


# Path
tmpFilePath = str(Path("./tmp.txt"))
driverPath = str(Path("./chromedriver.exe"))


# 元素定位
nameXpath = (
    '//*[@id="root"]/div/form/div[3]/div[1]/div[2]/div/div/div[2]/div[1]/div/span/input'
)
idXpath = (
    '//*[@id="root"]/div/form/div[3]/div[1]/div[4]/div/div/div[2]/div[1]/div/span/input'
)
phoneXpath = '//*[@id="root"]/div/form/div[3]/div[1]/div[6]/div/div/div[2]/div[1]/div/span/div/span/input'
majorPath = '//*[@id="root"]/div/form/div[3]/div[1]/div[10]/div/div/div[2]/div[1]/div/span/input'
localXpath1 = '//*[@id="root"]/div/form/div[3]/div[1]/div[8]/div/div/div[2]/div/div/span/div/div/div/div/div[1]'
localXpath2 = '//*[@id="react-select-2-option-21"]'
branchXpath1 = '//*[@id="root"]/div/form/div[3]/div[1]/div[10]/div/div/div[2]/div/div/span/div/div/div/div/div[1]'
branchXpath2 = '//*[@id="react-select-3-option-29"]'
commitXpath = '//*[@id="root"]/div/form/div[5]/div[1]/button'



# 映射，减少代码量
sign1 = {nameXpath: name, idXpath: idNum, phoneXpath: phone, majorPath: major}
list1 = [localXpath1, localXpath2, branchXpath1, branchXpath2]

# 读取url并删除文件
with open(tmpFilePath, "r") as f:
    qrcodeUrl = f.read()


# chrome额外设置
chrome_opt = webdriver.ChromeOptions()
# chrome_opt.add_argument("--headless")  # 是不是有界面
chrome_opt.add_argument("--disable-gpu")


# 起服务
svc = Service(driverPath)
driver = webdriver.Chrome(service=svc, options=chrome_opt)
driver.get(qrcodeUrl)
driver.implicitly_wait(10)


# 填信息
for k, v in sign1.items():
    driver.find_element(By.XPATH, k).send_keys(v)

for i in list1:
    driver.find_element(By.XPATH, i).click()



driver.get_screenshot_as_file(str(Path("./提交前信息.png")))
#driver.find_element(By.XPATH, commitXpath).click()  # 提交按钮
sleep(2)
print("Form write succeed!")
driver.get_screenshot_as_file(str(Path("./提交后结果.png")))
driver.quit()
