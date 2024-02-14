import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/photos")
data = response.json()


# def wirteadatar(data1):
#     with open("js.json", 'w') as file:
#         json.dump(data1, file, indent=2)
#
#
# wirteadatar(data)

def read():
    with open("js.json", 'r') as file:
        data = json.load(file)
        count = 0
        for x in data:
            if x['albumId'] == 5:
                count += 1
                print(x)
        print(count)


read()
