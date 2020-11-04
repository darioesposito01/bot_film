#!/usr/bin/env/python3.6.5
import telegram
from telegram.ext import Updater, CommandHandler,MessageHandler, Filters
from selenium import webdriver

import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from selenium import *

token = "1204302236:AAEbjN95KA2OYM1G1BedjcYO_9JuQCOnxiI"

caratteri_da_eliminare = [":", ";",",",".","–"," "]
link_try = "prova"
bot = telegram.Bot(token = token)

GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'

def ottieni_link(nome_film):
    link_da_mand = ""
    nomi_film = []
    nomi_film_non_modificati = []
    #driver = webdriver.Chrome(executable_path= r"/Users/darioesposito/Downloads/chromedriver")
    
    opt = Options()
    opt.add_argument("--headless")
    opt.add_argument("--window-size=5000,2800")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    opt.binary_location = GOOGLE_CHROME_PATH
    driver = webdriver.Chrome(execution_path = CHROMEDRIVER_PATH, options=opt)
  
    #driver.maximize_window()

    driver.get("https://altadefinizione.dance/")
    
    time.sleep(5)

    cont1 = driver.find_element_by_xpath("/html/body/section[3]/div/div[2]/div[2]/div[1]/div/form/div[1]/input")
    
    cont1.send_keys(nome_film)

    cont = driver.find_element_by_xpath("/html/body/section[3]/div/div[2]/div[2]/div[1]/div/form/div[2]/input")
    cont.click()
    time.sleep(5)
    name = driver.find_elements_by_class_name("titleFilm")
   

    for t in caratteri_da_eliminare:
        nome_film = nome_film.replace(t, "")
        print(nome_film+"nome film tele")
    print(nome_film+"nome finale")    
    for h in name:
        nomi_film.append(h.text)
        nomi_film_non_modificati.append(h.text)
        print(h.text+"h text")
        print(nomi_film)


    for k in caratteri_da_eliminare:   
        for j in nomi_film:
            print(j+"sono j")
            num = nomi_film.index(j)
            nomi_film[num] = nomi_film[num].replace(k, "")
            
            #print(nomi_film[num]+"array")
           # print("nome1"+nomi_film[num].lower()+"nome 2"+nome_film.lower())
            if nomi_film[num].lower() == nome_film.lower():
                #print(nomi_film[num].lower()+"lowewr")
                print("trovato")
                for d in name:
                    print("d text"+ d.text+ "j"+j)
                    print(nomi_film_non_modificati[num]+"non mod num")
                    if d.text == nomi_film_non_modificati[num]:
                        print("uguali")
                        try:
                            print(d.text+"d.text")
                            d.click()
                            nomi_film.clear()
                            break
                            
                        except:
                            d.click()
                            print("errore")
                            
                        #print(nome_film)
                        time.sleep(2)
                        break
                      

    

    '''
    searc_piccolo = driver.find_element_by_class_name("searchIcon")
    searc_piccolo.click()
    time.sleep(2)
    search = driver.find_element_by_xpath("/html/body/section[1]/div/div[1]/div[2]/div/form/div[1]/input")
    search.send_keys(nome_film)
    time.sleep(1)
    button = driver.find_element_by_xpath("/html/body/section[1]/div/div[1]/div[2]/div/form/div[2]/input")
    button.click()
    name_mobile = driver.find_elements_by_class_name("titleFilmMobile")
    nomi_film = name_mobile
    for i in nomi_film:
        #print(i.text.lower())
        
       if i.text.lower().find(nome_film) != -1:
            link_click = driver.find_element_by_link_text("regexpi:blackhat")
            print(i.text)
            #k = i
            #k.click()
            link_click.click()

   '''


   

    #close = driver.find_element_by_xpath('//*[@id="download-table"]/tbody/tr[1]')


    #close.click()
   
    #nomi_film.clear()
    nomi_film_non_modificati.clear()
    time.sleep(6)
    print(nomi_film)
    video_link = driver.find_element_by_xpath("/html/body/section[3]/div/div/div[1]/div[5]/div/iframe")

    link = video_link.get_attribute('src')
    print(video_link.get_attribute('src'))
    driver.get(link)
    time.sleep(3)
    link2 = driver.find_element_by_xpath("/html/body/table/tbody/tr[1]")

    link3 = link2.get_attribute('onclick')
    print(link3[14:-3])
    link_to_go = link3[14:-3]
    driver.get(link_to_go)
    a = False
    while a == False:
        try:
            link_to_down = driver.find_element_by_xpath("/html/body/div[4]")
            #time.sleep(4)
            print(link_to_down)
            link_finale = link_to_down.get_attribute('innerHTML')
            print(link_to_down.get_attribute('innerHTML'))
             
            a = True
            
        except:
            link_to_down = driver.find_element_by_id("videolink")
            print(link_to_down.text)

    link_f = link_finale[2:].replace("amp;", "")

    print("http://" +link_f)
    #driver.get(link_f[:-1])

    driver.get("http://www."+link_f)

    link_da_mand= "%s" %link_f

    print(link_da_mand+"da mand")
    
    driver.close()
    driver.quit()
    return link_da_mand 

def send(update, context):
    try:
        l = ottieni_link((update.message.text).lower())
    
        context.bot.send_message(chat_id= update.effective_chat.id, text="http://"+l)
       
    except:
         context.bot.send_message(chat_id= update.effective_chat.id, text="deve essersi verificato un problema, riprova togliendo eventiali segni di punteggiatura come (- , : . ;)")
         
    #bot.sendMessage(chat_id="613345494", text=link_da_mand)



updater = Updater(token=token, use_context=True)
disp= updater.dispatcher
hand= MessageHandler(Filters.text, send)
disp.add_handler(hand)
updater.start_polling()
updater.idle()



