import boto3
from pprint import pprint
import image_helpers # used to access functions from this py file

client = boto3.client('rekognition')

imgurl = 'https://kaingaora.govt.nz/assets/Developments-and-Programmes/Auckland-developments/Mount-Wellington-images/malone-mt-wellington1.jpg'
imgbytes = image_helpers.get_image_from_url(imgurl)

req_resp= client.detect_labels(Image={'Bytes': imgbytes},
                               MinConfidence=1)

# pprint(req_resp)
print("Here's what I see in the image:")

for label in req_resp['Labels']:
    print(label['Name'])

