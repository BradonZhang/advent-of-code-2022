import datetime as dt
import os
import subprocess
import argparse

import requests
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    AOC_SESSION = os.environ['AOC_SESSION']

    parser = argparse.ArgumentParser()
    parser.add_argument('day', nargs='?', type=int)
    args = parser.parse_args()

    day = args.day
    if day is None:
        now = dt.datetime.utcnow() - dt.timedelta(hours=5)
        if now.month == 12 and 1 <= now.day <= 25:
            day = now.day
        else:
            day = int(input('Enter a day (1-25):'))
    assert 1 <= day <= 25

    if not os.path.exists(f'./in/{day}.txt'):
        with open(f'./in/{day}.txt', 'w') as f:
            res = requests.get(
                f'https://adventofcode.com/2022/day/{day}/input',
                headers={
                    'cookie': f'session={AOC_SESSION};'
                }
            )
            f.write(res.text)
    subprocess.call(['python3', f'./src/{day}.py'])
