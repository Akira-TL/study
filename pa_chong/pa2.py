import json
import os
import re
import sqlite3
import requests
from selenium import webdriver
import time

file_path = 'study/pa_chong/database.db'
def writef(data:dict):
    check_file()
    a = sqlite3.connect(f'{file_path}')
    b = a.cursor()
    number = list(data.keys())[0]
    b.execute(f'''insert into imojimix (number,name,status,img_url,url) values('{number}','{data[number]["name"]}','{data[number]["status"]}','{data[number]["img_url"]}','{data[number]["url"]}')''')
    b.close()
    a.commit()
    a.close()

def check_file():
    try:
        with open(f'{file_path}','r') as f:
            pass
    except FileNotFoundError:
        try:
            os.mkdir('data')
        except:
            pass
        a = sqlite3.connect(f'{file_path}')
        b = a.cursor()
        b.execute('''create table imojimix(number text,name text,status integer,img_url text,url text)''')
        b.close()
        a.commit()
        a.close()





# driver.minimize_window()
# start = int(input('开始:'))
# end = int(input('结束:'))
while True:
    with open(f'study/pa_chong/count.json','r') as f:
        a:dict = json.load(f)
    left = a['cnt'][0] + 1
    right = a['cnt'][1] + 1
    print(left,right)
    cnt = False
    last_img = ''
    count = 0
    edge_options = webdriver.EdgeOptions()
    edge_options.add_argument('--ignore-certificate-errors')
    edge_options.add_experimental_option("excludeSwitches",["enable-logging"])
    driver = webdriver.Edge(options=edge_options)
    driver.get('https://tikolu.net/emojimix/🤣+🤣')
    # driver.find_element_by_id('emoji-id').send_keys('hhh')
    # print(driver.get_cookies())
    input()
    driver.find_element_by_id('cover-skip').click()
    # content = {}
    # driver.find_element_by_xpath(f'//div[@id="slider1"]/div[2]').click()
    # driver.find_element_by_xpath(f'//div[@id="slider2"]/div[157]').click()
    for i in range(left,224):
        driver.find_element_by_xpath(f'//div[@id="slider1"]/div[{i}]').click()
        time.sleep(1)
        if not cnt:
            k = right
            cnt = True
        else:
            k = i
        for j in range(k,224):
            print(f'//将读取第{i-1}-{j-1}个',end='')
            driver.find_element_by_xpath(f'//div[@id="slider2"]/div[{j}]').click()
            time.sleep(2)
            url = driver.current_url
            name = driver.current_url.split('/')[-1].replace('+','_') + '.png'
            img_url = driver.find_element_by_id("output").get_attribute("src")
            status = 1
            if 'blob' in img_url:
                status = 0
                img_url = 'error'

            # data = {f'{i-1}-{j-1}':{'name':name,'status':status,'img_url':img_url,'url':url}}
            # with open(f'study/pa_chong/database.json','r') as f:
            #     content:dict = json.load(f)
            # with open(f'study/pa_chong/database.json','w') as f:
            #     content.update(data)
            #     json.dump(content,f)
            
            data = {f'{i-1}-{j-1}':{'name':name,'status':status,'img_url':img_url,'url':url}}
            writef(data)

            downlouded = 222*221/2 - (222-i)*(222-i-1)/2 + j
            allimg = 222*221/2
            rate = round(downlouded / allimg * 100,2)
            if status:
                while True:
                    try:
                        img = requests.get(img_url)
                        break
                    except:
                        pass
                with open(f'study/pa_chong/img/{name}','wb') as f:
                    f.write(img.content)
                print(f' | \033[35msuccess\033[0m | \033[35m进度:{rate}%\033[0m | \033[94m链接:{img_url}')
            else:
                with open(f'study/pa_chong/img/{name}','w') as f:
                    f.write(img_url)
                print(f' | \033[91m error \033[0m | \033[35m进度:{rate}%\033[0m | \033[94m链接:{img_url}')
            with open(f'study/pa_chong/count.json','w') as f:
                json.dump({'cnt':[i-1,j-1]},f)
    # with open(f'img{start}-{end}.json','w',encoding='utf-8') as f:
    #     json.dump(content,f,ensure_ascii=False)



