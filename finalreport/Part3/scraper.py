import sys
import requests
from bs4 import BeautifulSoup
import csv
import json
import pandas as pd
import numpy as np
def scraper(url):
    headers = {
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'cookie':'zguid=23|%245458752f-31b8-4dea-a1cb-d7d6779f47b4; _ga=GA1.2.1145500856.1649827235; zjs_user_id=null; zg_anonymous_id=%22a84bfaec-c46c-47ed-a842-c2aedac8fe62%22; zjs_anonymous_id=%225458752f-31b8-4dea-a1cb-d7d6779f47b4%22; _pxvid=723dc544-bae9-11ec-aa14-6e414e457a7a; _gcl_au=1.1.928991192.1649827238; __gads=ID=991b933f7d879702:T=1649827237:S=ALNI_MYgc33k6jmNDVAxLF5qjnK2D44vKg; _fbp=fb.1.1649827238119.674023835; __pdst=2fcd5017b7ec46628c1f34f465fd4f39; _pin_unauth=dWlkPU16SmhOVEF3WVRFdE1qQmtNaTAwT0RJMkxUZzRaVGd0T0RNNE9HSXpNek0xWkRFeg; _cs_c=0; g_state={"i_p":1650541591025,"i_l":1}; KruxPixel=true; KruxAddition=true; zgsession=1|2ed0d417-e742-41e2-8302-70609b575075; _gid=GA1.2.1592877173.1650960938; pxcts=0ddecdab-c539-11ec-b360-76757567554a; DoubleClickSession=true; utag_main=v_id:0180215dd24100124a69cdfa35e50508501b507d00978$_sn:5$_se:1$_ss:1$_st:1650962738206$dc_visit:5$ses_id:1650960938206%3Bexp-session$_pn:1%3Bexp-session$dcsyncran:1%3Bexp-session$tdsyncran:1%3Bexp-session$dc_event:1%3Bexp-session$dc_region:us-west-2%3Bexp-session; _clck=rd2ngp|1|f0y|0; __gpi=UID=000004a6b537d3ba:T=1650534403:RT=1650960943:S=ALNI_MYsBeO05_ID_y1Ykl2uiXUf1pR7oA; optimizelyEndUserId=oeu1650962554452r0.07081709645444811; FSsampler=1559682105; zjs_utmsource=%22msn%22; zjs_utmcampaign=%22zxw_br_natip_usa_x_nat_x_e_b_1%22; zjs_utmcontent=%22319854745|1300722401909701|kwd-81295207640272:loc-190|81295221403669|%22; zjs_utmmedium=%22cpc%22; _hp2_ses_props.1215457233=%7B%22r%22%3A%22https%3A%2F%2Fwww.bing.com%2F%22%2C%22us%22%3A%22msn%22%2C%22um%22%3A%22cpc%22%2C%22uc%22%3A%22319854745%7C1300722401909701%7Ckwd-81295207640272%3Aloc-190%7C81295221403669%7C%22%2C%22ua%22%3A%22zxw_br_natip_usa_x_nat_x_e_b_1%22%2C%22ts%22%3A1650972270430%2C%22d%22%3A%22www.zillow.com%22%2C%22h%22%3A%22%2F%22%7D; JSESSIONID=5EA2B5014B42249805382246943C21D6; _hp2_id.1215457233=%7B%22userId%22%3A%22477916834740457%22%2C%22pageviewId%22%3A%224623240782564150%22%2C%22sessionId%22%3A%222403927250512347%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _cs_id=cc38a9b2-c0fd-aa5f-c1af-d00a3b2852d7.1650534374.6.1650972909.1650972270.1.1684698374561; _cs_s=2.5.0.1650974709305; _px3=ad7228e406a0c7adcd527811e0792b69755fb97ebacc8de4f6c0158f66b31b66:5S0nMDIFTpgbtzRopXXruD61JAb6uXQutb2x3MyW2h8eYdXUw9wQvapFRe6t8XO9G7ZjRTIuJ3dcXTu8DNo80g==:1000:Fa8/b6LlRNXIPnjzPRgy0xIZqQUKHUiLIoH1/zr9fwZpxXj7d6QCOYeOsvG7zFg5PF+JP6opztcqL2j77GrfJVS61l0gBvWcDzdQyy/hWlDcb4Ead17TvJBZ7jMCrUI8vpAV+Xg/6OJjsMaJo+vB/PII6iRqY2ybcax4xfbw7Xg1iuk/yHvY7jh5ymnhYOLxBDTT9zTfCCrf2LCHgOy+Iw==; _uetsid=0e0bdd90c53911ec9d4b07a0700725e6; _uetvid=74274970bae911ec8f9851f73cfc69ce; _uetmsclkid=_uetc9124a200f0717f37e982847d7e2448c; _gat=1; AWSALB=9OHWGS6PW8wmsPsQ5QwQBtNOd25zlRegfRKqsjnP+5DOucVeiefMaN9OtAb4bWGpQe7CBa2s/3ljYm1wGK0XfIoZlmFEXER/SMGUB+zEV7KSWEvCfXgPpRIqobzt; AWSALBCORS=9OHWGS6PW8wmsPsQ5QwQBtNOd25zlRegfRKqsjnP+5DOucVeiefMaN9OtAb4bWGpQe7CBa2s/3ljYm1wGK0XfIoZlmFEXER/SMGUB+zEV7KSWEvCfXgPpRIqobzt; search=6|1653564995859%7Crect%3D34.070534043939105%252C-118.21558057885744%252C33.98252628604485%252C-118.3505064211426%26rid%3D95988%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26z%3D1%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%09%0995988%09%09%09%09%09%09; _clsk=13zizej|1650972996749|28|0|d.clarity.ms/collect',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50'
}
    content = requests.get(url, headers = headers)
    soup = BeautifulSoup(content.content, 'html.parser')
    cards = soup.findAll('article',{'class': 'list-card'})
    result = []
    for card in cards:
        try:
            name = card.find('address',{'class':'list-card-addr'}).text
        except:
            name = np.nan
        try:
            floorSize = card.find('ul',{'class':'list-card-details'}).findAll('li')[2].text
        except:
            floorSize = np.nan
        try:
            price = card.find('div',{'class':'list-card-price'}).text
        except:
            price = np.nan
        item = {
            'name':name,
            'floorSize':floorSize,
            'price':price
        }
        entity_list = []
        for i in item.values():
            entity_list.append(i)
        result.append(entity_list)
    df = pd.DataFrame(result,columns=['name','floorSize','price'])
    return df

if __name__ =="__main__":
    if len(sys.argv) == 1:
        url = 'https://www.zillow.com/los-angeles-ca-90007/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%2290007%22%2C%22mapBounds%22%3A%7B%22west%22%3A-118.3505064211426%2C%22east%22%3A-118.21558057885744%2C%22south%22%3A33.98252628604485%2C%22north%22%3A34.070534043939105%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A95988%2C%22regionType%22%3A7%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%7D'
        print(scraper(url))
    elif sys.argv[1] == '--scraper':
        url = 'https://www.zillow.com/los-angeles-ca-90007/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%2290007%22%2C%22mapBounds%22%3A%7B%22west%22%3A-118.3505064211426%2C%22east%22%3A-118.21558057885744%2C%22south%22%3A33.98252628604485%2C%22north%22%3A34.070534043939105%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A95988%2C%22regionType%22%3A7%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%7D'
        print(scraper(url).head(int(sys.argv[2])))
    elif sys.argv[1] == '--static':
        url ='https://www.zillow.com/los-angeles-ca-90007/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%2290007%22%2C%22mapBounds%22%3A%7B%22west%22%3A-118.3505064211426%2C%22east%22%3A-118.21558057885744%2C%22south%22%3A33.98252628604485%2C%22north%22%3A34.070534043939105%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A95988%2C%22regionType%22%3A7%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%7D'
        scraper(url).to_csv(sys.argv[2])
        

else:
    print(f'...Importing module {__name__}...')

