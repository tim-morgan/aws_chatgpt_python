import os
import pandas as pd
import pickle
from jinja2 import Environment, FileSystemLoader

def interactive_mode():
    # Load the metadata DataFrame from the metadata pickle file
    with open('data/app/metadata.pkl', 'rb') as f:
        metadata_df = pickle.load(f)

    # Load the costs DataFrame from the costs pickle file
    with open('data/app/costs.pkl', 'rb') as f:
        costs_df = pickle.load(f)

    # Create a Jinja2 environment and load the template
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('report_template.html')

    while True:
        # Ask the user for the account id or 'e' to exit
        account_id = input("Enter account id or 'e' to exit: ")
        if account_id.lower() == 'e':
            break
        else:
            # Filter the metadata DataFrame based on the account id
            account_metadata = metadata_df[metadata_df['AccountID'] == account_id]

            # Filter the costs DataFrame based on the account id
            account_costs = costs_df[costs_df['account_id'] == account_id]

            if account_metadata.empty:
                print("No metadata found for the given account id.")
            else:
                # Convert the metadata to a dictionary
                metadata = account_metadata.iloc[0].to_dict()
                
                # Convert the costs to a list of dictionaries and format the 'TimePeriod' and 'UnblendedCost' fields
                costs = []
                for _, row in account_costs.iterrows():
                    month = pd.to_datetime(row['TimePeriod']['Start']).strftime('%B')
                    amount = float(row['UnblendedCost'])
                    costs.append({'month': month, 'amount': amount})

                # Render the template with the metadata and costs
                report = template.render(account_id=account_id, metadata=metadata, costs=costs)

                # Write the report to an HTML file
                os.makedirs('data/output', exist_ok=True)
                with open(f'data/output/{account_id}.html', 'w') as f:
                    f.write(report)

                print(f"Report for account id {account_id} has been generated.")

def generate_all_reports():
    # Load the metadata DataFrame from the metadata pickle file
    with open('data/app/metadata.pkl', 'rb') as f:
        metadata_df = pickle.load(f)

    # Load the costs DataFrame from the costs pickle file
    with open('data/app/costs.pkl', 'rb') as f:
        costs_df = pickle.load(f)

    # Create a Jinja2 environment and load the template
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('report_template.html')

    # Iterate over all accounts in the metadata
    for account_id in metadata_df['AccountID'].unique():
        # Filter the metadata DataFrame based on the account id
        account_metadata = metadata_df[metadata_df['AccountID'] == account_id]

        # Filter the costs DataFrame based on the account id
        account_costs = costs_df[costs_df['account_id'] == account_id]

        if not account_metadata.empty:
            # Convert the metadata to a dictionary
            metadata = account_metadata.iloc[0].to_dict()
            
            # Convert the costs to a list of dictionaries and format the 'TimePeriod' and 'UnblendedCost' fields
            costs = []
            for _, row in account_costs.iterrows():
                month = pd.to_datetime(row['TimePeriod']['Start']).strftime('%B')
                amount = float(row['UnblendedCost'])
                costs.append({'month': month, 'amount': amount})

            # Render the template with the metadata and costs
            report = template.render(account_id=account_id, metadata=metadata, costs=costs)

            # Write the report to an HTML file
            os.makedirs('data/output', exist_ok=True)
            with open(f'data/output/{account_id}.html', 'w') as f:
                f.write(report)

            print(f"Report for account id {account_id} has been generated.")
