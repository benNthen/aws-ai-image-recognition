# AWS Image Recognition App
A program that uses AWS API Rekognition Image's DetectLabels action to recognize the image of the vehicle. The result with the highest confidence value is extracted and
returned as an output on the IDE's console window.

You may wish to add your own files and store them inside the `images` folder, then provide their full file path when you run the program.

As of October 2021, this program only supports analysing files that are contained inside the images folder.

## Using this repository
You can run the app on your local computer using the latest version of JetBrain's PyCharm.

## Prerequisites
To use this repository, you need the following installed locally:

- Windows 10 / macOS 10 or higher 
- Python 3.7+ or PyCharm 2019+ IDE
- The AWS Command Line Interface (CLI) 

### How to Run:
-----------
Select and run the `main.py file` of this folder.

You will then be prompted to enter the file path.

Enter the file path for one of the pictures contained inside the `images` folder(`bike.jpg`, `car.jpg`, `truck.jpg`) and press enter.

These are the three possible outputs :

If a Bicycle image is selected
![bike](https://user-images.githubusercontent.com/53241776/137043482-31502742-6a9e-424d-8dd3-1225c44c2fa4.jpg)
```
Please enter image path: {filepath}/bike.jpg   // where {filepath} is the complete directory of the images folder
This vehicle is a Bicycle.
```

If a Car image is selected
![car](https://user-images.githubusercontent.com/53241776/137043515-8fbaa3ab-d9c1-4974-9e5d-5f44911eab52.jpg)

```
Please enter image path: {filepath}/car.jpg   
This vehicle is a Car.
```

If a Truck image is selected
![truck](https://user-images.githubusercontent.com/53241776/137043526-9ba3d6ad-bfe5-4187-9909-a01c456a4dd9.png)

```
Please enter image path: {filepath}/truck.jpg   
This vehicle is a Truck.
```
### How it works : Code of the program
-----------
The main file of interest is the `vehicle_detect.py`. It consists of two parts.

First half of the file contains a function that connects and sends the image file as data to the online AWS API 'Rekognition'.
Once a connection between the program and the online API has been established, the DetectLabels action is then selected and used to analyze the image.
The matching results are returned as a string array of data that is then stored in the 'json-data.txt'. 

```python
import boto3
import image_helpers

filename = 'json-data.txt'

# communicates with the AWS API 'Rekognition' to see which image matches
def detect_labels_local_file(photoname):

    client = boto3.client('rekognition') # Communes with the AWS API Reference Rekognition

    imgbytes = image_helpers.get_image_from_file(photoname) # Gets the image file from the images folder

    response = client.detect_labels(Image={'Bytes': imgbytes}) # AWS API Rekognition's 'DetectLabels' action is selected

    with open(filename, 'w') as f: # JSON data received is filtered, only Labels portion is saved onto 'json-data.txt'
        for label in response['Labels']:

            print(label['Name'], file=f)

    return response
```

The code below shows the second half of the file. This function will analyze the `json-data.txt` file and extract the top most accurate result.
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

### Understanding how the data is retrieved
-----------

When the program sends the picture file(for example `bike.jpg`) from the images folder as data to the AWS API, the resulting JSON data returned actually looks like this:

```python
{'Labels': [
{'Name': 'Bicycle', 'Confidence': 98.90534973144531, 'Instances': [{'BoundingBox': {'Width': 0.9214262962341309, 'Height': 0.6056628823280334, 'Left': 0.0382184237241745, 'Top': 0.21384571492671967}, 'Confidence': 98.90534973144531}], 'Parents': [{'Name': 'Vehicle'}, {'Name': 'Transportation'}]}, 
{'Name': 'Bike', 'Confidence': 98.90534973144531, 'Instances': [], 'Parents': [{'Name': 'Vehicle'}, {'Name': 'Transportation'}]}, 
{'Name': 'Vehicle', 'Confidence': 98.90534973144531, 'Instances': [], 'Parents': [{'Name': 'Transportation'}]}, 
{'Name': 'Transportation', 'Confidence': 98.90534973144531, 'Instances': [], 'Parents': []}, 
{'Name': 'Mountain Bike', 'Confidence': 97.97901153564453, 'Instances': [], 'Parents': [{'Name': 'Bicycle'}, {'Name': 'Vehicle'}, {'Name': 'Transportation'}]}], 'LabelModelVersion': '2.0', 'ResponseMetadata': {'RequestId': '6436ec18-e443-4075-8e40-f3bd85196be1', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '6436ec18-e443-4075-8e40-f3bd85196be1', 'content-type': 'application/x-amz-json-1.1', 'content-length': '769', 'date': 'Wed, 13 Oct 2021 00:05:57 GMT'}, 'RetryAttempts': 0}}

```

The program filters the data to only display the top five matching labels that were determined by the AWS Rekognition Image's DetectLabels action. 
These are stored as an array of strings in the `json-data.txt` as shown below.

![image](https://user-images.githubusercontent.com/53241776/137045990-bb23d947-45b2-41e0-ae04-caee9027c97a.png)

The first result in this string array represents the label with the highest confidence(in this case its Bicyle) and this is what gets displayed on the output of the program.



