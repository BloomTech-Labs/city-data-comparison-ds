import boto3
import json
import pandas as pd

ddb = boto3.resource('dynamodb', region_name='us-east-2')
table = ddb.Table('singlecity')

with open('./data/city_ids.json', 'r') as f:
    jdata = json.load(f)
jdf = pd.DataFrame(data = jdata)
jdf = jdf.T

y_df = pd.read_csv('./data/yelp_data_1.csv')


# table = ddb.create_table(
# TableName='scdata',
# KeySchema=[
#     {
#         'AttributeName': '_id',
#         'KeyType': 'HASH'
#     }],
# AttributeDefinitions=[
#     {
#         'AttributeName': '_id',
#         'AttributeType': 'N'
#     },
#     {
#         'AttributeName': 'city_st',
#         'AttributeType': 'S'
#     },
#     {
#         'AttributeName': 'yelp_data',
#         'AttributeType': 'M'
#     },
#     ])

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
  dc = 0

  for cat in cats:
    name_l = []
    for i in range(0, 9):
      name_l.append(y_df[(y_df['city']==city) & (y_df['category']==cat) & (y_df['type'] == 'name')][str(i+1)][dc])
    dc = dc + 1

    image_l = []
    for i in range(0, 9):
      image_l.append(y_df[(y_df['city']==city) & (y_df['category']==cat) & (y_df['type'] == 'image_url')][str(i+1)][dc])
    dc = dc + 1

    url_l = []
    for i in range(0, 9):
      url_l.append(y_df[(y_df['city']==city) & (y_df['category']==cat) & (y_df['type'] == 'url')][str(i+1)][dc])
    dc = dc + 1
    cat_data[cat] ={'name':name_l,
                    'image_url':image_l,
                    'url':url_l
                    }

    y_data = {city : cat_data}
  return(cat_data)


with table.batch_writer() as batch:
    for i in range(0, len(y_df.city)):
        batch.put_item(
            Item={
                '_id': y_df['_id'][i],
                'city_st': str(y_df.city[i]),
                'yelp_data':get_yelp_data(y_df.city[i], y_df)
            }
        )
