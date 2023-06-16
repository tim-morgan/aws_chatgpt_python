import boto3
import os
import pandas as pd
import pickle
from datetime import datetime

def fetch_cost_explorer_data():
    # Create a Cost Explorer client
    client = boto3.client('ce')

    # Define the start and end dates for the previous six full months
    today = datetime.now()
    end = datetime(today.year, today.month, 1)
    start = datetime(end.year if end.month > 6 else end.year - 1, (end.month - 6) % 12 or 12, 1)
    end_str = end.strftime('%Y-%m-%d')
    start_str = start.strftime('%Y-%m-%d')

    # Get the cost and usage data for the last six months
    response = client.get_cost_and_usage(
        TimePeriod={
            'Start': start_str,
            'End': end_str
        },
        Granularity='MONTHLY',
        Metrics=[
            'UnblendedCost',
        ],
        GroupBy=[
            {
                'Type': 'DIMENSION',
                'Key': 'LINKED_ACCOUNT'
            }
        ]
    )

    # Convert the response to a pandas DataFrame
    data = []
    for result_by_time in response['ResultsByTime']:
        for group in result_by_time['Groups']:
            account_id = group['Keys'][0]
            amount = group['Metrics']['UnblendedCost']['Amount']
            data.append({
                'TimePeriod': result_by_time['TimePeriod'],
                'account_id': account_id,
                'UnblendedCost': amount
            })

    df = pd.DataFrame(data)

    # Create a directory to store the pickle file if it does not exist
    os.makedirs('data/app', exist_ok=True)

    # Save the DataFrame to a pickle file
    with open('data/app/costs.pkl', 'wb') as f:
        pickle.dump(df, f)

    print('Cost data has been successfully saved.')
