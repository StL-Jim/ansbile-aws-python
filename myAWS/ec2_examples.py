'''
Some examples of interacting with the EC2 client

https://boto3.amazonaws.com/v1/documentation/api/latest/guide/ec2-example-managing-instances.html
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_instances
'''
from boto3 import client, resource
from pprint import pprint

# Connect and get my instances (in json)
ec2 = client('ec2', region_name='us-east-2')
response = ec2.describe_instances()
print(response)

# Monitoring costs, but here's a quck enable 
response = ec2.describe_instances()
# My primary instance = u'InstanceId': 'i-03831566db711066d',

# Ha haaaa, now you have a list which is a ugly list that has dics in the list.  
# Better to stick with json or collecti9on.
reservations = response.get("Reservations")

for reservation in response['Reservations']:
  for instance in reservation['Instances']:
      print instance['InstanceId'], instance['Hypervisor']
    for blockDev in i['BlockDeviceMappings']:
      print "Block Device Name: " + blockDev['DeviceName'], "EBS VolumeId " + blockDev['Ebs']['VolumeId'], "EBS Volume Status " + blockDev['Ebs']['Status']

# pretty print
pprint(response)

# now if I wanted to create a file of all instances and important stuff and things
name = ec2.describe_instances(Filters=[{'Name': 'tag:Name', 'Values': ['rhel7-ec2-east2-01']}])

instId = name['Reservations'][0]['Instances'][0]['InstanceId']
instIdState = name['Reservations'][0]['Instances'][0]['State']

for key, value in reservations.items():
    # print key, value
    print key
    # print value






