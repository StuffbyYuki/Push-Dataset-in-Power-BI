import psutil
import requests
import datetime
import json
# from config import URL

def push_data():
    now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent

    data = [{ "CPU_USAGE": cpu_usage, "RAM_USAGE": ram_usage, "DATETIME": now }]

    headers = {
    "Content-Type": "application/json"
    } 

    response = requests.request(
        method="POST",
        url="YOUR PUSH URL",
        headers=headers,
        data=json.dumps(data)
    )   

    if response.status_code == 200:
        print('Pushded data successfully.\n')
    else:
        print('Something went wrong.\n')


def main():
    cnt = 1
    while True:
        print(cnt)
        push_data()
        cnt += 1


if __name__ == '__main__':
    main()
