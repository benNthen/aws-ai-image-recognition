import requests


def get_image_from_url(imgurl): #Gets raw image from url
    resp = requests.get(imgurl)
    imgbytes = resp.content #grabs content from response
    return imgbytes #return content


def get_image_from_file(filename): #Gets image from a file
    '''Based on
       https://docs.aws.amazon.com/rekognition/latest/dg/example4.html,
       last access 10/3/2017'''
    with open(filename, 'rb') as imgfile:
        return imgfile.read()