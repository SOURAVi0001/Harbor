import csv
import json

def load_csv_data(filepath):
    with open(filepath, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def filter_active_users(users):
    return [
        user for user in users
        if user.get('active', '').lower() == 'true'
    ]

def save_json_data(data, filepath):
    with open(filepath, mode='w', encoding='utf-8') as f:
        json.dump(data, f)

def main():
    input_path = '/app/input.csv'
    output_path = '/app/output.json'
    
    users = load_csv_data(input_path)
    active_users = filter_active_users(users)
    save_json_data(active_users, output_path)

if __name__ == "__main__":
    main()
