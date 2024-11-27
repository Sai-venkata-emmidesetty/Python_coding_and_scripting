"""
Here's a Python script that automates the management of AWS EC2 instances, fulfilling the tasks mentioned:

Task breakdown:
Lists all running EC2 instances in a specific region.
Filters instances with the tag Environment: Development.
Stops these filtered instances
"""

import boto3

ec2=boto3.client("ec2",region_name="us-east-1")
response=ec2.describe_instances(
    Filters=[
        {
            "Name": "instance-state-name",
             "Values": ["running"]
        }
             ]
             )
final_list=[]
for value1 in response["Reservations"]:
    for value2 in value1["Instances"]:
        for value3 in value2.get("Tags", []):
            if value3["Key"]=="Environment" and value3["Value"]=="Development":
                final_list.append(value2["InstanceId"])


if final_list:
    print(f"Stopping instances: {final_list}")
    ec2.stop_instances(InstanceIds=final_list)
else:
    print("No instances found with the 'Environment: Development' tag.")
