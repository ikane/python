import json

import boto3

# getting the dynamodb resource
dynamodb = boto3.resource('dynamodb')

table_name = 'songs'

# resource representing a dynamodb table
table = dynamodb.Table(table_name)


def create_data():
    total_items = 0
    with open('songs.json') as datafile:
        songs = json.load(datafile)

    for index, song in enumerate(songs):
        # print(song)
        item = {
            "song_id": str(index + 1),
            "name": song['name'],
            "artist": song['artist'],
            "publisher": song['publisher'],
            "priceInUsd": song['priceInUsd']
        }
        # print(item)
        print('Saving item id = {} to the DB'.format(item['song_id']))
        # put_item
        # Creates a new item or replaces an old item with a new item. If an item that has the same primary key as the
        # new item already exists in the specified table, the new item completely replaces the existing item.
        response = table.put_item(
            Item=item
        )

        if response['ResponseMetadata']['HTTPStatusCode']== 200:
            print('Item saved with status code = {} OK\n'.format(response['ResponseMetadata']['HTTPStatusCode']))
            total_items += 1
        else:
            print('Item id = {} could be saved in the dB\n'.format(item['song_id']))

    print('Total {} item(s) saved to the DB:'.format(total_items))


create_data()