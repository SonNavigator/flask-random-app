import csv
import random

def csv_reader():
    with open('data2.csv', 'r') as file:
        reader = csv.reader(file)
        # Skip CSV's header using next() function
        next(reader)
        data = []
        for row in reader:
            data.append(row)
    
        random_data = random.sample(data, 3)
        final_data = " และคุณ ".join(map(str, random_data))
        unwanted_chars = [']', '[', '\'', ',']

        for i in unwanted_chars:
            final_data = final_data.replace(i, '')

        return final_data
