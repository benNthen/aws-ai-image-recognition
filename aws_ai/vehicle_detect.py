import boto3
import image_helpers


filename = 'json-data.txt'

# photo = 'images/truck.png'  # images/truck.png, images/car.jpg, images/bike.jpg


# extracts JSON data related to most matched label
def detect_labels_local_file(photoname):

    client = boto3.client('rekognition') # AWS API Reference

    imgbytes = image_helpers.get_image_from_file(photoname)

    response = client.detect_labels(Image={'Bytes': imgbytes})

    with open(filename, 'w') as f:
        for label in response['Labels']:

            print(label['Name'], file=f)

    return response

# generate output regarding the best matched vehicle result
def output_display(num):

    # x = detect_labels_local_file(photoname)

    # print(x)

    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    print('This vehicle is a ' + content[num] + '.')


def main():


    if __name__ == "__main__":
        main()
