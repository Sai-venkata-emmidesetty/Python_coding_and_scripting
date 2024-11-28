#delete EBS volumes that are not attached to any EC2 instances

import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    # Get all volumes
    volumes = ec2.describe_volumes()['Volumes']
    
    # Collect IDs of attached volumes
    attached_ids = set()
    for volume in volumes:
        for attachment in volume.get('Attachments', []):
            attached_ids.add(attachment['VolumeId'])
    
    # Delete unattached volumes
    for volume in volumes:
        if volume['VolumeId'] not in attached_ids:
            try:
                ec2.delete_volume(VolumeId=volume['VolumeId'])
                print(f"Deleted volume: {volume['VolumeId']}")
            except Exception as e:
                print(f"Error deleting volume {volume['VolumeId']}: {e}")
    
    return {
        'statusCode': 200,
        'body': 'Unattached EBS volumes processed.'
    }



#example output of describe volumes
"""
{
    'NextToken': '',
    'Volumes': [
        {
            'Attachments': [
                {
                    'AttachTime': datetime(2013, 12, 18, 22, 35, 0, 2, 352, 0),
                    'DeleteOnTermination': True,
                    'Device': '/dev/sda1',
                    'InstanceId': 'i-1234567890abcdef0',
                    'State': 'attached',
                    'VolumeId': 'vol-049df61146c4d7901',
                },
            ],
            'AvailabilityZone': 'us-east-1a',
            'CreateTime': datetime(2013, 12, 18, 22, 35, 0, 2, 352, 0),
            'Size': 8,
            'SnapshotId': 'snap-1234567890abcdef0',
            'State': 'in-use',
            'VolumeId': 'vol-049df61146c4d7901',
            'VolumeType': 'standard',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}
"""