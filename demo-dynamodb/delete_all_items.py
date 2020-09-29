import boto3

# getting the dynamodb resource
dynamodb = boto3.resource('dynamodb')

table_name = 'songs'
# resource representing a dynamodb table
table = dynamodb.Table(table_name)


def delete_all_items():
    deleted_items = 0

    # scan()
    # Returns one or more items and item attributes by accessing every item in a table or a secondary index.
    # To have dynamodb return fewer items, you can provide a FilterExpression operation.
    response = table.scan()
    with table.batch_writer() as batch:
        for song in response['Items']:
            batch.delete_item(
                Key={
                    'song_id': song['song_id'],
                }
            )
            deleted_items = deleted_items + 1

    if deleted_items > 0:
        print('{} item(s) are successfully deleted from the dB'.format(deleted_items))
    else:
        print('Either table is empty or some error occurred while deleting the items from the dB')


delete_all_items()