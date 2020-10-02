from bs4 import BeautifulSoup #helps with page scraping
import requests #allows html downloads
import pprint #pretty print
def find_stats():
   res = requests.get('https://www.worldometers.info/coronavirus/')#scrape target
   stats = BeautifulSoup(res.text, 'html.parser')#parses into html
   trs = stats.table.find_all('tr')
   i=8
   covidinfo = ''
   while i< 14:
      details = trs[i].contents   
      if i == 8:rank = ''
      else:rank = f'{details[1].text}) '
      country,total,ntotal = details[3].text,f'  total cases:{details[5].text}',f'  new cases:{details[7].text}'
      death,ndeath = f'  total deaths:{details[9].text}',f'  new deaths:{details[11].text}'
      recover,cases = f'  total recoveries:{details[13].text}',f'  active cases:{details[15].text}'
      population = f'  population:{details[29].text}'
      covidinfo += f'{rank}{country}\n{population}\n{total}\n{ntotal}\n{death}\n{ndeath}\n{recover}\n{cases}\n\n'
      i+=1
   return covidinfo
#print(find_stats())