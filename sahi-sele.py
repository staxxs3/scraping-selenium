from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from fake_useragent import UserAgent
import os
import time
import json
import random

_start_links = [
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-dacia-duster-1.5-dci-comfort?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-dacia-duster-1.5-dci-laureate?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-dacia-duster-1.5-dci-prestige?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-dacia-duster-1.6?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-dacia-duster-1.6-sce?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-daewoo?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-daihatsu?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-ds-automobiles?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-fiat?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-ford-ecosport?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-ford-edge?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-ford-expedition?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-ford-explorer?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-ford-ranger?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-hummer?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-hyundai-ix35?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-hyundai-ix55?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-hyundai-kona?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-infiniti?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-isuzu?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-jeep-patriot?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-jeep-renegade?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-jeep-wrangler?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-kia-sportage-1.6?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-land-rover-defender?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-land-rover-discovery?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-land-rover-range-rover?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-land-rover-range-rover-evoque?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-land-rover-range-rover-sport-2.0?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-land-rover-range-rover-sport-2.0-phev?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-land-rover-range-rover-sport-2.0-sd4?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-mitsubishi-outlander?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-mitsubishi-pajero?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-nissan-country?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-nissan-navara?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-nissan-pathfinder?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-nissan-qashqai-2.0?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-nissan-qashqai-2.0-dci?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-nissan-qashqai-plus2?pagingOffset="
    },
{
        "url": "https://www.sahibinden.com/arazi-suv-pickup-nissan-terrano?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-nissan-x-trail?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-oldsmobile?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-opel?pagingOffset="
    },
    {
        "url": "https://www.sahibinden.com/arazi-suv-pickup-peugeot-2008?pagingOffset="
    }
]

_results = []

options = Options()
options.add_experimental_option("prefs", {
    "download.default_directory": r"C:\Users\admin\PycharmProjects\Selenium\db",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})
options.add_experimental_option("excludeSwitches", ['enable-automation'])
driver = webdriver.Chrome('C:/Users/admin/Desktop/sahi/chromedriver.exe', chrome_options=options)
wait = WebDriverWait(driver, 10)
action = ActionChains(driver)

get_links_code = '''
var arr = []
var temp = document.querySelectorAll('.classifiedTitle')
for(var i in temp){
arr.push(temp[i].href)
}
return arr
'''
last_page_code = "return parseInt(document.querySelectorAll('.mbdef')[0].innerText.split('sayfa')[0].replace('Toplam','').trim())"

scrap_code = '''
var car = {};
car['Url'] = window.location.href;
prix = document.querySelectorAll('.classifiedInfo > h3')[0].innerText.split(' ');
car['prix'] = prix[0].replace('.','');
car['currency'] = prix[1];
try {
car['image'] = document.querySelectorAll('.stdImg')[0].src;
}
catch(error) {car['image'] = ''}
arr = document.querySelectorAll('.classifiedInfoList>li')
for (var i=0;i<arr.length;i++){
car[arr[i].querySelector('strong').innerText.trim()] = arr[i].querySelector('span').innerText.trim()
}
temp = document.querySelectorAll('#classifiedProperties > h3')
temp2 = document.querySelectorAll('#classifiedProperties > ul')
for(var i=0;i<temp2.length;i++){
car[temp[i].innerText] = []
temp_arr = temp2[i].querySelectorAll('.selected')
for(var j=0;j<temp_arr.length;j++){
    car[temp[i].innerText].push(temp_arr[j].innerText)
}
}
try {
temp = document.querySelectorAll('.classifiedTechDetails > h3')
temp2 = document.querySelectorAll('.classifiedTechDetails > table')
for(var i=0;i<temp.length;i++){
    car[temp[i].innerText.trim()] = {}
    temp_arr = temp2[i].querySelectorAll('tr')
    console.log(temp_arr)
    for(var j=0;j<temp_arr.length;j++){
        var key = temp_arr[j].querySelector('.title').innerText.trim().replace(/\\n/g,' ').replace(/\ {2,}/g,' ')
        var value = temp_arr[j].querySelector('.value').innerText.trim().replace(/\\n/g,' ').replace(/\ {2,}/g,' ')
        car[temp[i].innerText.trim()][key] = value
    }
}
}
catch(error) {}
txt = document.querySelectorAll('.classifiedInfo > h2')[0].innerText.split('/')
try {car['city'] = txt[0].trim()}catch(error) {}
try {car['province'] = txt[1].trim()}catch(error) {}
try {car['location'] = txt[2].trim()}catch(error) {}
car['description'] = document.querySelector('#classifiedDescription').innerText.replace(/\\n/g,' ').replace(/\ {2,}/g,' ').trim()

var StandartDonanım = {}
var OpsiyonelDonanım = {}
car['StandartDonanım'] = {}
car['OpsiyonelDonanım'] = {}
arr = document.querySelectorAll('.equipments > ul > li > table > tbody > tr')
try{
for (var i=0;i<arr.length;i++){
    console.log(arr[i])
    if(arr[i].querySelectorAll('td').length==1){
        category = arr[i].querySelectorAll('td')[0].innerText.trim()
        StandartDonanım[category] = []
        OpsiyonelDonanım[category] = []
    }
    if(arr[i].querySelectorAll('td').length==3){
        if(arr[i].querySelectorAll('td')[2].getAttribute('class')){
            OpsiyonelDonanım[category].push(arr[i].querySelectorAll('td')[0].innerText)
        }
        if(arr[i].querySelectorAll('td')[1].getAttribute('class')){
            StandartDonanım[category].push(arr[i].querySelectorAll('td')[0].innerText)
        }
    }
}
car['StandartDonanım'] = StandartDonanım
car['OpsiyonelDonanım'] = OpsiyonelDonanım
}catch(error) {}

return car
'''
licznik = 0
licznik_2 = 0
licznik_3 = 0
executer = """
              Object.defineProperty(navigator, 'webdriver', {
                  get: () => undefined
              })
          """

# for uri in _start_links:
# url = uri['url']
options.add_argument("start-maximized")
# driver.execute_cdp_cmd(driver.get(executer)
options.add_experimental_option("excludeSwitches", ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
driver.execute_cdp_cmd("Network.enable", {})
# ua = UserAgent()
# user_agent = ua.random
# options.add_argument(f'user-agent={user_agent}')
# driver = webdriver.Chrome('C:/Users/admin/Desktop/sahi/chromedriver.exe',
#                           chrome_options=options)

moze = """
page.evaluateOnNewDocument(() = > {
    Object.defineProperty(navigator, 'webdriver', {
        get: () = > false,
    })
})

await page.evaluateOnNewDocument(() = > {
    window.navigator = {}
})

await page.evaluateOnNewDocument(() = > {
    window.navigator.chrome = {
    runtime: {},
    }
})

await page.evaluateOnNewDocument(() = > {
    const originalQuery = window.navigator.permissions.query
    return (window.navigator.permissions.query = parameters = >
    parameters.name == = 'notifications'
    ? Promise.resolve({state: Notification.permission})
    : originalQuery(parameters))
})

await page.evaluateOnNewDocument(() = > {
Object.defineProperty(navigator, 'languages', {
    get: () = > ['en-US', 'en'],
        })
    })
"""
driver.execute_script(moze)
driver.get('https://bot.sannysoft.com/')
# driver.get(url.replace('?pagingOffset=', ''))
try:
    last_page = driver.execute_script(last_page_code)
except:
    last_page = 1
    # last_page = 1

    # =========================== Przechodzenie po linkach bezposrednio
    # for x in range(last_page):
    #     driver.get(url + str(x * 20))
    #     print(url + str(x * 20))
    #     ad_links = driver.execute_script(get_links_code)
    #     for ad in ad_links:
    #         time.sleep(10)
    #         if ad:
    #             driver.get(ad)
    #             _results.append(driver.execute_script(scrap_code))
    #             print(len(_results))
    #             if len(_results) >999:
    #                 licznik = licznik+1
    #                 with open('sahi_part'+str(licznik)+'.json', 'w', encoding='utf8', errors='surrogatepass') as outfile:
    #                     json.dump(_results, outfile, indent=4, skipkeys=True, ensure_ascii=False)

    # =========================== Klikanie w linki i wracanie do poprzedniej strony
    for x in range(last_page):
        if licznik_2 >= 20:
            licznik_2 = 0
            licznik_3 = licznik_3 + 1
            path_to_json = 'C:/Users/admin/PycharmProjects/untitled1/test'
            json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

            full_data = []
            number_of_json = len(json_files)
            print('POSZEDL DUZY SAVE')

            for z in range(number_of_json):
                with open(path_to_json + '/' + json_files[z], 'r', encoding='utf8') as file:
                    data = json.load(file)
                full_data.extend(data)

            with open(path_to_json + '/SCALE/' + 'big_part_' + str(licznik_3) + '.json', 'w',
                      encoding='utf8') as outfile:
                json.dump(full_data, outfile, indent=4, ensure_ascii=False)
        try:
            _str = url + str(x * 20)
            driver.get(_str)
            print(_str)
            temp = driver.find_elements_by_class_name('classifiedTitle')
            add_number = len(temp)
            for page_number in range(add_number - 1):
                licznik_2 = licznik_2 + 1
                try:
                    driver.execute_script("window.scrollTo(0, " + str(page_number * 85) + ")")
                    time.sleep(random.randrange(10, 150) / 10)
                    driver.find_elements_by_class_name('classifiedTitle')[page_number].click()
                    time.sleep(random.randrange(10, 160) / 10)
                    _results.append(driver.execute_script(scrap_code))
                    print(len(_results))
                    if len(_results) > 4:
                        licznik = licznik + 1
                        with open('test/sahi_part' + str(licznik) + '.json', 'w', encoding='utf8',
                                  errors='surrogatepass') as outfile:
                            json.dump(_results, outfile, indent=4, skipkeys=True, ensure_ascii=False)
                        _results = []
                    driver.back()
                    time.sleep(random.randrange(10, 170) / 10)
                except:
                    try:
                        driver.delete_all_cookies()
                        driver.close()
                        ua = UserAgent()
                        user_agent = ua.random
                        options.add_argument(f'user-agent={user_agent}')
                        driver = webdriver.Chrome('C:/Users/admin/Desktop/sahi/chromedriver.exe',
                                                  chrome_options=options)
                        driver.get(_str)
                        driver.execute_script("window.scrollTo(0, " + str(page_number * 85) + ")")
                        time.sleep(random.randrange(10, 150) / 10)
                        driver.find_elements_by_class_name('classifiedTitle')[page_number].click()
                        time.sleep(random.randrange(10, 160) / 10)
                        _results.append(driver.execute_script(scrap_code))
                        print(len(_results))
                        if len(_results) > 4:
                            licznik = licznik + 1
                            with open('test/sahi_part-' + str(licznik) + '.json', 'w', encoding='utf8',
                                      errors='surrogatepass') as outfile:
                                json.dump(_results, outfile, indent=4, skipkeys=True, ensure_ascii=False)
                            _results = []
                        driver.back()
                        time.sleep(random.randrange(10, 170) / 10)
                    except:
                        None
        except:
            None
