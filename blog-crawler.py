# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 20:04:00 2021

@author: kevin
"""



import requests
from bs4 import BeautifulSoup


#search_name = input("輸入餐廳名稱:")

def blog_crawler(search_name):
    name_list=[]
    url_list=[]
    #==============================================================
    
    web = 'https://tisshuang.tw/blog/post/banqiaofoods'
    
    
    content = requests.get(web)    
    objSoup = BeautifulSoup(content.text,"lxml")
    obja = objSoup.find_all('a')
    
    
    for data in obja:
        if search_name in data.text:
            name_list.append(data.text)
            url_list.append(data.get('href'))
            #print(data.text)
            #print(data.get('href'))
            
    #==============================================================
    
    web = 'https://anikolife.com/taipei-hotpot/'
    
    
    content = requests.get(web)            
    objSoup = BeautifulSoup(content.text,"lxml")
    
    obja = objSoup.find_all('a')
        
    for data in obja:
        if data.get('title') and search_name in data.get('title'):
            #print(data.get('title'))
            #print(data.get('href'))
            name_list.append(data.get('title'))
            url_list.append(data.get('href'))
            
            
        elif search_name in data.text:
            #print(data.text)
            #print(data.get('href'))
            name_list.append(data.text)
            url_list.append(data.get('href'))
            
    #==============================================================
    web = 'https://anikolife.com/ramen-lazybag/'
    
    content = requests.get(web)           
    objSoup = BeautifulSoup(content.text,"lxml")
    obja = objSoup.find_all('a')
    
    for data in obja:
        if search_name in data.text:
            #print(data.text)
            #print(data.get('href'))  
            name_list.append(data.text)
            url_list.append(data.get('href'))
            
    #==============================================================
    web = 'https://www.liviatravel.com/2011/10/blog-post_5530.html'
    
    
    content = requests.get(web)          
    objSoup = BeautifulSoup(content.text,"lxml")
    obja = objSoup.find_all('a')
    
    for data in obja:
        if search_name in data.text:
            #print(data.text)
            #print(data.get('href'))
            name_list.append(data.text)
            url_list.append(data.get('href'))
    
    #==============================================================
    web = 'https://tisshuang.tw/blog/post/taipaeistation'
    
    
    content = requests.get(web)      
    objSoup = BeautifulSoup(content.text,"lxml")
    
    obja = objSoup.find_all('a')
    
    for data in obja:
        if search_name in data.text:
            
            #print(data.text)
            #print(data.get('href'))
            name_list.append(data.text)
            url_list.append(data.get('href'))
            
    #==============================================================
    web = 'https://tisshuang.tw/blog/post/zhongshan'
    
    
    content = requests.get(web)       
    
    objSoup = BeautifulSoup(content.text,"lxml")
    
    obja = objSoup.find_all('a')
    
    for data in obja:
        if search_name in data.text:
            
            #print(data.text)
            #print(data.get('href'))
            name_list.append(data.text)
            url_list.append(data.get('href'))
        
    #==============================================================    
    web = 'https://tisshuang.tw/blog/post/taipei101'
    
    
    content = requests.get(web)         
    objSoup = BeautifulSoup(content.text,"lxml")
    obja = objSoup.find_all('a')
    
    for data in obja:
        if search_name in data.text:
            
            #print(data.text)
            #print(data.get('href'))
            name_list.append(data.text)
            url_list.append(data.get('href'))
            
    all_dict = dict(zip(name_list,url_list)) 
    
    return all_dict
    #print(all_dict)       
            
#web_crawler(search_name)
        
              
        
        
        
        
        
        
        
        
        
        
        