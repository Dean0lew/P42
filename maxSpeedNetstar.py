import pip
#!pip install boto3 pandas
import boto3
import pandas as pd
from io import StringIO

aws_id = "AWS_ID"
aws_secret = "AWS_SECRET_KEY"

client = boto3.client('s3', aws_access_key_id=aws_id,
                      aws_secret_access_key=aws_secret)

bucket_name = 'netstar-south-africa'

# access vehicles.csv
object_key = 'vehicles.csv'

# information for bucket from s3
csv_obj = client.get_object(Bucket=bucket_name, Key=object_key)
body = csv_obj['Body']
csv_string = body.read().decode('utf-8')

df = pd.read_csv(StringIO(csv_string))

# create list of cars
cars = []

for car in df['VbuNo']:
    object_key = str(car) + '.csv'

    # extract information for bucket from s3
    csv_obj = client.get_object(Bucket=bucket_name, Key=object_key)
    body = csv_obj['Body']
    csv_string = body.read().decode('utf-8')

    #create dataframe
    df = pd.read_csv(StringIO(csv_string))

    #store results in a list
    x = max(pd.to_numeric(df["Speed"]))
    if x >= 150:
        cars.append(car)
        if len(cars) == 3:
                print(cars)
                break
