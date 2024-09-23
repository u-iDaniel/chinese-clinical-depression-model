import json
import csv
import os

if __name__ == '__main__':
    # Define the path to the JSON files
    json_path = 'test_json'

    # Define the path to the CSV files
    csv_path = 'test_csv'

    for file in os.listdir(json_path):
        with open(f'{json_path}/{file}', encoding='utf-8') as file:
            json_data = json.load(file)
            data = json.loads(json_data['data'])

        # Define CSV headers
        headers = ['bg', 'ed', 'onebest', 'si', 'speaker', 'wordsName', 'wc', 'wordBg', 'wordEd', 'wp']

        # Prepare data for CSV
        csv_data = []
        for item in data:
            for word in item['wordsResultList']:
                row = {
                    'bg': item['bg'],
                    'ed': item['ed'],
                    'onebest': item['onebest'],
                    'si': item['si'],
                    'speaker': item['speaker'],
                    'wordsName': word['wordsName'],
                    'wc': word['wc'],
                    'wordBg': word['wordBg'],
                    'wordEd': word['wordEd'],
                    'wp': word['wp']
                }
                csv_data.append(row)

        # Write data to CSV
        file_name = str(file.name).split('/')[1].split('.')[0]
        if not os.path.exists(csv_path):
            os.makedirs(csv_path)
        os.chdir(csv_path)
        with open(f'{file_name}.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            for row in csv_data:
                writer.writerow(row)

        # Change directory back to the original
        os.chdir('..')