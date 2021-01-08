
# requests dep is from our lambda layer
import requests

def lambda_handler(event, context):
    r = requests.get('https://httpbin.org/get')
    return {'body': r.text, 'statusCode': 200}