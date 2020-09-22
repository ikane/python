import boto3

# getting the dynamodb resource
dynamodb = boto3.resource('dynamodb')

table_name = 'songs'

# resource representing a dynamodb table
table = dynamodb.Table(table_name)


def get_all_items():
    # scan
    response = table.scan()
    items = response['Items']

    print('Printing data from the table.')

    for item in items:
        print(item)
        print('\n')


get_all_items()
