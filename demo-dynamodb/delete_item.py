import boto3

# getting the dynamodb resource
dynamodb = boto3.resource('dynamodb')

table_name = 'songs'
# resource representing a dynamodb table
table = dynamodb.Table(table_name)

songId = '5'


def delete_item():
    print('Deleting item id = {} from the dB\n'.format(songId))

    # get_item(...)
    # get the item from the table.
    response = table.get_item(
        Key={
            'song_id': songId
        }
    )

    if 'Item' in response:
        # delete_item(...)
        # delete an item from the table based on the key.
        response = table.delete_item(
            Key={
                'song_id': songId
            }
        )

        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            print('Item deleted with status code = {} OK'.format(response['ResponseMetadata']['HTTPStatusCode']))
        else:
            print('Some error occurred while deleting the item from the dB')
    else:
        print('Item id = {} not found in the dB'.format(songId))


delete_item()