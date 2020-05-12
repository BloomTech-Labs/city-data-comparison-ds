import pymongo
import dns
from pymongo import MongoClient
from decouple import config
import json
import pandas as pd
MONGO_URI = config('MONGO_URI')

client = MongoClient(MONGO_URI)
#client = MongoClient('mongodb+srv://citrus_user:sM9MrUjDKMzbzYVs@cluster0-ak1hs.mongodb.net/test?retryWrites=true&w=majority')
# test = client.test.table_name.find_one({'_id':1})
# print(type(test))
# print(test)
with open('./apps/data/city_ids.json', 'r') as f:
    jdata = json.load(f)
jdf = pd.DataFrame(data = jdata)
jdf = jdf.T


y_df = pd.read_csv('./apps/data/yelp_data_14.csv')
#print(y_df['_id'][0], y_df.city[0], y_df.category[0], y_df.type[0], y_df['1'][0])

def get_yelp_data(city, y_df):
  """
  Input: string with city name and state abbreviation (i.e 'Barstow, CA'), and
    the batch as a dataframe
  Output: Multi-layered dictionary (city -> category -> type)
    categories: 'restuarants', 'nightlife', 'arts', 'parks', 'sports_clubs',
       'fashion', 'hotels'
    types: 'name', 'image_url', 'url'
  """
  cats = ['restuarants', 'nightlife', 'arts', 'parks', 'sports_clubs',
       'fashion', 'hotels']

  #cat_data = {'name':'', 'image_url':'', 'url':''}
  cat_data = {}
  #dc = dc * 21
  #print(dc)
  for cat in cats:
    name_l = []
    for i in range(0, 9):
        t_n = str(y_df[(y_df['city']==city) & (y_df['category']==cat) & (y_df['type'] == 'name')][str(i+1)].values)
        t_n = t_n.replace('[', '')
        t_n = t_n.replace(']', '')
        t_n = t_n.replace('\'', '')
        t_n = t_n.replace('\"', '')
        name_l.append(t_n)
    #dc = dc + 1
    #print(dc)

    image_l = []
    for i in range(0, 9):
        t_i = str(y_df[(y_df['city']==city) & (y_df['category']==cat) & (y_df['type'] == 'image_url')][str(i+1)].values)
        t_i = t_i.replace('[', '')
        t_i = t_i.replace(']', '')
        t_i = t_i.replace('\'', '')
        t_i = t_i.replace('\"', '')
        image_l.append(t_i)
    #dc = dc + 1
    #print(dc)

    url_l = []
    for i in range(0, 9):
        t_u = str(y_df[(y_df['city']==city) & (y_df['category']==cat) & (y_df['type'] == 'url')][str(i+1)].values)
        t_u = t_u.replace('[', '')
        t_u = t_u.replace(']', '')
        t_u = t_u.replace('\'', '')
        t_u = t_u.replace('\"', '')
        url_l.append(t_u)
    #dc = dc + 1
    #print(dc)

    cat_data[cat] ={'name':name_l,
                    'image_url':image_l,
                    'url':url_l
                    }

    y_data = {city : cat_data}
  return cat_data

cities = y_df.city.unique()

#print(get_yelp_data(cities[2], y_df, 2))
#print(y_df[y_df.city == cities[0]]['_id'][0])

#print(cities[1])
# tv = y_df[(y_df['city']==cities[1]) & (y_df['category']=='restuarants') & (y_df['type'] == 'name')]['1'].values
# print(tv)
# print(y_df[(y_df['city']==cities[1]) & (y_df['category']=='nightlife') & (y_df['type'] == 'name')]['1'])
# print(y_df[(y_df['city']==cities[1]) & (y_df['category']=='parks') & (y_df['type'] == 'name')]['1'])
# print(y_df[(y_df['city']==cities[9]) & (y_df['category']=='restuarants') & (y_df['type'] == 'name')]['1'])

# for i in range(0, len(cities)):
#     ttt = str(y_df[y_df.city == cities[i]]['_id'].unique())
#     print(ttt, type(ttt))
# ttt = str(y_df[y_df.city == cities[0]]['_id'].unique())
# ttt = ttt.replace('[', '')
# ttt = ttt.replace(']', '')
# print(ttt, type(ttt))

for i in range(0, len(cities)):
    yd = get_yelp_data(cities[i], y_df)
    #print(yd.keys())
    ttt = str(y_df[y_df.city == cities[i]]['_id'].unique())
    ttt = ttt.replace('[', '')
    ttt = ttt.replace(']', '')
    insertt = client.test.yelp_data.insert_one({'_id':ttt,
                                           'city_st':cities[i],
                                           'yelp_data':yd})
    print(i, cities[i], 'inserted successfully!')
# result = client.test.test.insert_many([{'_id':y_df['_id'][i],
#                                          'city_st':y_df.city[i],
#                                          'yelp_data':get_yelp_data(y_df.city[i], y_df)
#                                         } for i in range(0, len(y_df['_id']))])
# print(result.inserted_ids)
# print(client.test.test.count_documents({}))
