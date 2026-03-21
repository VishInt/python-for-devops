import requests

api_url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url=api_url)

print(dir(response))

print(type(response.json()))

for key,value in response.json().items():
    # if key == "completed":
    #     if value == False:
    #         print("the data is not completed in the server")

    if key == "userId":
        if value in [100,200,300]:
            print("User found")
