from collections import defaultdict
from boto3 import resource, ec2
"""
Now that I've begun to wrap my head around
getting some basic information from running EC2 instances.
I just want important stuff to put in a static inventory file for ansible
"""

# Connect to EC2
ec2 = resource('ec2')

# Get information for all running instances
running_instances = ec2.instances.filter(Filters=[{
    'Name': 'instance-state-name',
    'Values': ['running']}])

# Create a defaultdict to work with
ec2info = defaultdict()
for instance in running_instances:
    for tag in instance.tags:
        if 'Name'in tag['Key']:
            name = tag['Value']
    # Add instance info to a dictionary         
    ec2info[instance.id] = {
        'Name': name,
        'Type': instance.instance_type,
        'State': instance.state['Name'],
        'Private IP': instance.private_ip_address,
        'Public IP': instance.public_ip_address,
        'Launch Time': instance.launch_time
        }

attributes = ['Name', 'Type', 'State', 'Private IP', 'Public IP', 'Launch Time']
for instance_id, instance in ec2info.items():
    for key in attributes:
        print("{0}: {1}".format(key, instance[key]))
    print("------")

'''
In [91]: name['Reservations'][0]['Instances'][0]
Out[91]: 
{u'AmiLaunchIndex': 0,
 u'Architecture': 'x86_64',
 u'BlockDeviceMappings': [{u'DeviceName': '/dev/sda1',
   u'Ebs': {u'AttachTime': datetime.datetime(2019, 3, 22, 13, 41, 4, tzinfo=tzlocal()),
    u'DeleteOnTermination': True,
    u'Status': 'attached',
    u'VolumeId': 'vol-0b2af60c768069772'}}],
 u'CapacityReservationSpecification': {u'CapacityReservationPreference': 'open'},
 u'ClientToken': '',
 u'CpuOptions': {u'CoreCount': 1, u'ThreadsPerCore': 1},
 u'EbsOptimized': False,
 u'EnaSupport': True,
 u'HibernationOptions': {u'Configured': False},
 u'Hypervisor': 'xen',
 u'ImageId': 'ami-0b500ef59d8335eee',
 u'InstanceId': 'i-03831566db711066d',
 u'InstanceType': 't2.micro',
 u'KeyName': 'jimm_aws_ec2',
 u'LaunchTime': datetime.datetime(2019, 3, 22, 13, 41, 4, tzinfo=tzlocal()),
 u'Monitoring': {u'State': 'disabled'},
 u'NetworkInterfaces': [{u'Association': {u'IpOwnerId': 'amazon',
    u'PublicDnsName': 'ec2-3-16-125-45.us-east-2.compute.amazonaws.com',
    u'PublicIp': '3.16.125.45'},
   u'Attachment': {u'AttachTime': datetime.datetime(2019, 3, 22, 13, 41, 4, tzinfo=tzlocal()),
    u'AttachmentId': 'eni-attach-0aa04c1483ab92fc8',
    u'DeleteOnTermination': True,
    u'DeviceIndex': 0,
    u'Status': 'attached'},
   u'Description': '',
   u'Groups': [{u'GroupId': 'sg-06173e97d7085001e',
     u'GroupName': 'securityGroup_ssh_in_only'}],
   u'Ipv6Addresses': [],
   u'MacAddress': '0a:41:24:bc:d3:8e',
   u'NetworkInterfaceId': 'eni-08e584149e03bc2f8',
   u'OwnerId': '936859625049',
   u'PrivateDnsName': 'ip-172-31-39-195.us-east-2.compute.internal',
   u'PrivateIpAddress': '172.31.39.195',
   u'PrivateIpAddresses': [{u'Association': {u'IpOwnerId': 'amazon',
      u'PublicDnsName': 'ec2-3-16-125-45.us-east-2.compute.amazonaws.com',
      u'PublicIp': '3.16.125.45'},
     u'Primary': True,
     u'PrivateDnsName': 'ip-172-31-39-195.us-east-2.compute.internal',
     u'PrivateIpAddress': '172.31.39.195'}],
   u'SourceDestCheck': True,
   u'Status': 'in-use',
   u'SubnetId': 'subnet-8e8e50c2',
   u'VpcId': 'vpc-6e6f7e06'}],
 u'Placement': {u'AvailabilityZone': 'us-east-2c',
  u'GroupName': '',
  u'Tenancy': 'default'},
 u'PrivateDnsName': 'ip-172-31-39-195.us-east-2.compute.internal',
 u'PrivateIpAddress': '172.31.39.195',
 u'ProductCodes': [],
 u'PublicDnsName': 'ec2-3-16-125-45.us-east-2.compute.amazonaws.com',
 u'PublicIpAddress': '3.16.125.45',
 u'RootDeviceName': '/dev/sda1',
 u'RootDeviceType': 'ebs',
 u'SecurityGroups': [{u'GroupId': 'sg-06173e97d7085001e',
   u'GroupName': 'securityGroup_ssh_in_only'}],
 u'SourceDestCheck': True,
 u'State': {u'Code': 16, u'Name': 'running'},
 u'StateTransitionReason': '',
 u'SubnetId': 'subnet-8e8e50c2',
 u'Tags': [{u'Key': 'dbServer', u'Value': 'No'},
  {u'Key': 'vpnServer', u'Value': 'Not Yet'},
  {u'Key': 'Name', u'Value': 'rhel7-ec2-east2-01'},
  {u'Key': 'os', u'Value': 'Linux'},
  {u'Key': 'vpn', u'Value': 'unknown'},
  {u'Key': 'osTemplate', u'Value': 'notUsed'},
  {u'Key': 'owner', u'Value': 'Jim'},
  {u'Key': 'securityGroup', u'Value': 'lowSec'},
  {u'Key': 'webServer', u'Value': 'maybe'},
  {u'Key': 'vpc', u'Value': 'unknown'}],
 u'VirtualizationType': 'hvm',
 u'VpcId': 'vpc-6e6f7e06'}
'''