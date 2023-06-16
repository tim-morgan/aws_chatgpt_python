import argparse
from interactive_handler import interactive_mode, generate_all_reports
from dynamodb_handler import fetch_dynamodb_data
from cost_explorer_handler import fetch_cost_explorer_data

# Map command line arguments to function names
command_map = {
    'metadata': fetch_dynamodb_data,
    'costs': fetch_cost_explorer_data,
    'interactive': interactive_mode,
    'all': generate_all_reports
}

def main():
    parser = argparse.ArgumentParser(description='AWS account data handler.')
    parser.add_argument('--metadata', action='store_true')
    parser.add_argument('--costs', action='store_true')
    parser.add_argument('--interactive', action='store_true')
    parser.add_argument('--all', action='store_true')
    args = parser.parse_args()

    for command, function in command_map.items():
        if vars(args)[command]:
            function()

if __name__ == "__main__":
    main()
