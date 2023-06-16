# AWS Account Data Handler

This project is a command line application that fetches and manages data related to AWS accounts from a DynamoDB table and AWS Cost Explorer. It has functionalities to fetch metadata and cost data and store it locally as pickle files. It also allows interactive querying of the data and generates HTML reports of the account details.

## Features
- Fetch metadata from DynamoDB table and store it locally
- Fetch cost data from AWS Cost Explorer and store it locally
- Interactive mode for querying specific account data
- Generate HTML reports for individual accounts

## Dependencies
- Python 3.8
- Boto3
- Pandas
- Jinja2

## Setup and Installation
1. Clone this repository
    ```
    git clone https://github.com/tim-morgan/aws_chatgpt_python
    ```
2. Navigate to the project directory
    ```
    cd aws_chatgpt_python
    ```
3. Install the necessary Python packages
    ```
    pip install -r requirements.txt
    ```

## Usage
The command line application can be run using Python:
- To fetch metadata from DynamoDB table:
    ```
    python run.py --metadata
    ```
- To fetch cost data from AWS Cost Explorer:
    ```
    python run.py --costs
    ```
- To enter interactive mode for querying specific account data:
    ```
    python run.py --interactive
    ```
- To generate HTML reports for all accounts:
    ```
    python run.py --all
    ```

## Output
HTML reports for individual accounts are generated in the `data/output` directory with the account ID as the filename.
