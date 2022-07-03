#import all needed libraries
import pandas as pd
import statistics
import re
#%matplotlib inline
from matplotlib import pyplot as plt
from matplotlib import interactive
import plotly.express as px
import scraper
import apifunction
import fromstringtoint

#scrape data from Zillow
frames = []
for i in range(1,21):
    url=f'https://www.zillow.com/los-angeles-ca/{i}_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A{i}%7D%2C%22usersSearchTerm%22%3A%22Los%20Angeles%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-118.95143586914062%2C%22east%22%3A-117.87202913085937%2C%22south%22%3A33.6682876634696%2C%22north%22%3A34.372392743232595%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12447%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D'
    df = scraper.scraper(url)
    frames.append(df)
result = pd.concat(frames)
result.index = range(200)
result = result.dropna() #no rows with null values
print('This is a real-time dataset scraped from Zillow:\n', result)

#using Open Cage Geocoding API
addresses = list(result['name'])
lat_list =[]
lng_list = []
for address in addresses:
    lat_list.append(apifunction.geocode(address)[0])
    lng_list.append(apifunction.geocode(address)[1])
result['lat']=lat_list
result['lng']=lng_list
#result.to_csv('datafromZillow.csv')
print('This is the real-time scraped data from Zillow combined with coordinates API data:\n', result)


#In data analysis part, I utilized the saved dataset when I did web scrape and API 
df = pd.read_csv('datafromZillow.csv') 
print('I saved the dataset as datafromZillow.csv when I did web scraping and API, so the following dataset might be slightly differernt from the real-time one')

#drop the outlier values
for i in [8,61,62,166]:
    df = df.drop(i)
print('This is the dataset from Zillow and API (on May 10）: \n',df)
price_list = []

#change from string to integer in LA dataset for further arithmetic calculation
for i in df['price']:
    price = fromstringtoint.str_int(i)
    price_list.append(price)
size_list = []
for i in df['floorSize']:
    size = fromstringtoint.str_int(i)
    size_list.append(size)
y = price_list
x = size_list
df['price'] = y
df['floorSize'] = x
df['price_sf'] = df['price']/df['floorSize']
print('This is the dataset in LA with price per square foot column:\n', df)

#process the CA dataset from Kaggle
df1 = pd.read_csv('datasetfromKaggle.csv')
df2=df1.query("State == 'CA'")
df_related_column = df2[['Title','Sqr Ft','Price','Latitude','Longitude']]
df_related_column.columns =['name','floorSize','price','lat','lng']
df_no_null = df_related_column.dropna()
df_no_null.index = range(2555)
df_no_null = df_no_null[df_no_null['price'] != 'Contact For Estimate']
df_no_null = df_no_null[df_no_null['floorSize'] != '1 sqft']
print('This is the dataset from Kaggle:\n',df_no_null)
#df_no_null.to_csv('datafromKaggleCA.csv')

#change from string to integer in CA dataset for further arithmetic calculation
size_list1 = []
for i in df_no_null['floorSize']:
    size = fromstringtoint.str_int(i)
    size_list1.append(size)
df_no_null['floorSize'] = size_list1
price_list1 = []
for i in df_no_null['price']:
    price = fromstringtoint.str_int(i)
    price_list1.append(price)
df_no_null['price'] = price_list1
df_no_null['price_sf'] = df_no_null['price']/df_no_null['floorSize']

print('This is the dataset in CA with price per square foot column:\n', df_no_null)
df_no_null = df_no_null[df_no_null['price_sf'] <= 10000] #remove two extreme values of which over 10000

#print three boxplots
print('Boxplot of price per square foot column in LA dataset:')
plt.boxplot(df['price_sf'], showmeans = True)
print('First show\n')
plt.show()

print('Boxplot of price per square foot column in CA dataset:')
plt.boxplot(df_no_null['price_sf'], showmeans = True)
print('Second show\n')
plt.show()

Q = (df['price_sf'],df_no_null['price_sf'])
print('Show two boxplots in one canvas, the left one shows the price per square foot in LA, and the right one shows the price per square foot in CA.')
plt.boxplot(Q, showmeans = True)
print('Third show\n')
plt.show()

#print descriptive data
print('The maximum value of price per square foot in LA is',max(df['price_sf']), 
      '\nThe maximum value of price per square foot in LA is ', min(df['price_sf']),
     '\nThe mean value of price per square foot in LA is ',statistics.mean(df['price_sf']),
     '\nThe median value of price per square foot in LA is ',statistics.median(df['price_sf']),
     '\nThe standard deviation of price per square foot in LA is ', statistics.stdev(df['price_sf']))

print('The maximum value of price per square foot in CA is',max(df_no_null['price_sf']), 
      '\nThe maximum value of price per square foot in CA is ', min(df_no_null['price_sf']),
     '\nThe mean value of price per square foot in CA is ',statistics.mean(df_no_null['price_sf']),
     '\nThe median value of price per square foot in CA is ',statistics.median(df_no_null['price_sf']),
     '\nThe standard deviation of price per square foot in CA is ', statistics.stdev(df_no_null['price_sf']))

#plot map
px.scatter(df,x = 'lng', y = 'lat',size = 'price_sf').show()
print('\nLast is the scatter plot, which shows the house pricing per square foot in LA')





