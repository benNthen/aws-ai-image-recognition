# AWS Image Recognition App
A program that uses AWS API to recognize the image of the vehicle.

## Using this repository
You can run the app on your local computer using the latest version of JetBrain's PyCharm.

## Prerequisites
To use this repository, you need the following installed locally:

- Windows 10 or higher
- Python 3.7+ or PyCharm 2019+
- The AWS Command Line Interface (CLI) 

### How to Run:
-----------
Select and run the `main.py file` of this folder.

You will then be prompted to enter the file path.

Enter the file path for one of the pictures contained inside the `images` folder(`bike.jpg`, `car.jpg`, `truck.jpg`) and press enter.

These are the three possible outputs :

If a Bicycle image is selected
```
Please enter image path: {filepath}/bike.jpg   // where {filepath} is the complete directory of the file
This vehicle is a Bicycle.
```

If a Car image is selected
```
Please enter image path: {filepath}/car.jpg   
This vehicle is a Car.
```

If a Truck image is selected
```
Please enter image path: {filepath}/truck.jpg   
This vehicle is a Truck.
```
### How it works
-----------
The main file of interest is the `vehicle_detect.py`. It consists of two functions.

First half of the file contains a function that connects and sends the image file as data to the AWS API 'Rekognition' 
The matching results are returned as a string array of data that is then stored in the 'json-data.txt'. 

```python
import boto3
import image_helpers

filename = 'json-data.txt'

# communicates with the AWS API 'Rekognition' to see which image matches
# extracts JSON data related to most matched label
def detect_labels_local_file(photoname):

    client = boto3.client('rekognition') # AWS API Reference

    imgbytes = image_helpers.get_image_from_file(photoname)

    response = client.detect_labels(Image={'Bytes': imgbytes})

    with open(filename, 'w') as f:
        for label in response['Labels']:

            print(label['Name'], file=f)

    return response
```

The code below shows the second half of the file. This function will analyze the 'json-data.txt' file and extract the top most accurate result.
The result is then sent to the `main.py` file to be displayed as part of the output.

```python
# generate output regarding the best matched vehicle result
def output_display(num):

    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    print('This vehicle is a ' + content[num] + '.')


def main():


    if __name__ == "__main__":
        main()

```

Other Notes: 
- You may wish to add your own files and store them inside the `images` folder, then provide their full file path when you run the program.
- As of October 2021, this program only supports analysing files that are contained inside the images folder.
- `boto3.py` is imported in this code. Its used to establish the online connection AWS API 'Rekognition'.
- `image_helpers.py` contains one function that extracts and reads the image file from the images folder.

