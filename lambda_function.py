import boto3

client = boto3.client("ses")


def lambda_handler(event, context):
    for i in event["Records"]:
        action = i["eventName"]
        ip = i["requestParameters"]["sourceIPAddress"]
        bucket_name = i["s3"]["bucket"]["name"]
        subject = str(action) + 'Event from' + bucket_name
        body = """
         <br>
        This email is to notify you regarding {} event.
         Source IP: {}
        """.format(action, ip)

        message = {"Subject": {"Data": subject}, "Body": {"Html": {"Data": body}}}

        response = client.send_email(Source="a@gmail.com",
                                     Destination={"ToAddresses": ["a@gmail.com"]}, Message=message)
        print(response)
