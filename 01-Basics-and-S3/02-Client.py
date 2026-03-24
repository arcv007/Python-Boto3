import boto3

client = boto3.client('s3')

client.create_bucket(Bucket='rohiverm-boto3-test')

with open('myfile.txt', 'w') as file:
    file.write('This is a text file for upload')

client.upload_file(Filename='myfile.txt',
                Bucket = 'rohiverm-boto3-test',
                Key='test-upload-file')

client.delete_object(Bucket='rohiverm-boto3-test',
                    Key='test-upload-file')