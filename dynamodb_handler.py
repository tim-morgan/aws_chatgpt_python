import boto3
import os
import pandas as pd
import pickle

def fetch_dynamodb_data():
    # Get the DynamoDB table name from the DATATABLE environment variable
    table_name = os.getenv('DATATABLE')

    if not table_name:
        print("Error: The DATATABLE environment variable is not set.")
        return

    # Create a DynamoDB client
    dynamodb = boto3.resource('dynamodb')

    # Connect to the DynamoDB table
    table = dynamodb.Table(table_name)

    # Scan all items in the table
    response = table.scan()

    # Create a pandas DataFrame from the scanned items
    df = pd.DataFrame(response['Items'])

    # Create a directory to store the pickle file if it does not exist
    os.makedirs('data/app', exist_ok=True)

    # Save the DataFrame to a pickle file
    with open('data/app/metadata.pkl', 'wb') as f:
        pickle.dump(df, f)

    print('Metadata has been successfully saved.')
