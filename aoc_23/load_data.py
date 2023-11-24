import requests
from dotenv import load_dotenv
import os

load_dotenv()
COOKIE = os.environ.get("SESSION")

def check_file_exists(day):
    filepath = os.path.join('real_data', '{day}.txt')
    return os.path.isfile(filepath)

def get_data(day):
    if check_file_exists(day):
        with open(f'real_data/{day}.txt') as f:
            raw_data = f.read()
    else: 
        response = requests.get(f'https://adventofcode.com/2023/day/{day}/input',
                            cookies={'session': COOKIE})
        raw_data = response.content.decode('UTF-8')
        with open(f'real_data/{day}.txt', 'w') as f:
            f.write(raw_data)
    return raw_data

def get_test_data(day):
    with open(f'test_data/{day}.txt') as f:
        data = f.read()
    return data

if __name__ == '__main__':
    print(get_test_data(1))