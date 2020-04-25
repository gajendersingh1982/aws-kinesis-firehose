import json
import boto3
import random
import datetime

session = boto3.session.Session(profile_name='vdinfradev')

kinesis = session.client('firehose')
#list = kinesis.list_delivery_streams( Limit=123, DeliveryStreamType='DirectPut' )
#print(list)

def getReferrer():
    data = {}
    #now = datetime.datetime.now()
    #str_now = now.isoformat()
    #data['EVENT_TIME'] = str_now
    data['fname'] = random.choice(['Gajender', 'Ronav', 'Ekansh', 'Anusha', 'Lalit'])
    data['lname'] = random.choice(['Singh', 'Loonaich', 'Chaudhary'])
    data['email'] = random.choice(['chsadhgsadha', 'ghhgj', 'mnmnn', 'yyyyyuyuyu'])
    age = random.random() * 100
    data['age'] = int(age) #round(age, 0)
    return data

while True:
        data = json.dumps(getReferrer())
        print(data)
        kinesis.put_record(
                DeliveryStreamName="ExampleInputStream",
                Record={      'Data': data + '\n'   }
                )