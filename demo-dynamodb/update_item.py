import boto3

# getting the dynamodb resource
dynamodb = boto3.resource('dynamodb')

table_name = 'songs'
# resource representing a dynamodb table
table = dynamodb.Table(table_name)

song_id = '5'


def update_item():
    print('Updating item id = {} from the dB\n'.format(song_id))

    # get_item(...)
    # get the item from the table.
    response = table.get_item(
        Key={
            'song_id': song_id
        }
    )

    if 'Item' in response:
        # update_item(...)
        # update an item from the table based on the key.
        response = table.update_item(
            Key={
                'song_id': song_id
            },
            UpdateExpression="set artist = :g",
            ExpressionAttributeValues={
                ':g': "Butterfly"
            }
        )

        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            print('Item updated with status code = {} OK'.format(response['ResponseMetadata']['HTTPStatusCode']))
        else:
            print('Some error occurred while updating the item from the dB')
    else:
        print('Item id = {} not found in the dB'.format(song_id))


update_item()