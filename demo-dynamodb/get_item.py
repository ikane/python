import boto3

# getting the dynamodb resource
dynamodb = boto3.resource('dynamodb')

table_name = 'songs'

# resource representing a dynamodb table
table = dynamodb.Table(table_name)

song_id = '5'


def get_item():
    print('Fetching item id = {} from the dB\n'.format(song_id))

    # get_item(...)
    # get a single item from the table.
    response = table.get_item(
        Key={
            'song_id': song_id
        }
    )

    if 'Item' in response:
        print(response['Item'])
    else:
        print('Item id = {} not found in the dB'.format(song_id))


get_item()