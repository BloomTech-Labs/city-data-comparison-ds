import boto3
ddb = boto3.resource('dynamodb', region_name='us-east-2')
tbl = ddb.Table('sc_data')
response = tbl.get_item(
        Key={
            '_id': 7,
            'city_st':'New Hope, AL'
            })

item = response['Item']
print(item.keys())
print(item['_id'], item['city_st'])
