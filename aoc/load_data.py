import requests
from dotenv import load_dotenv
import os

load_dotenv()
COOKIE = os.environ.get("SESSION")

def get_data(day):
    response = requests.get(f'https://adventofcode.com/2021/day/{day}/input',
                            cookies={'session': COOKIE})
    raw_data = response.content.decode('UTF-8')
    return raw_data

def get_test_data(day):
    with open(f'test_data/{day}.txt') as f:
        data = f.read()
    return data

if __name__ == '__main__':
    print(get_test_data(1))