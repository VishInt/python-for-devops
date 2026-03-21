info = {
    "name": "Vishal Lilhare", #str
    "city": "Nagpur", #str
    "qualification": "BE", #str
    "age" : 26, #int
    "salary": 22.5,  # float
    "Married": False,# Boolean
    "favourites": ["Money", "Movies", "Cricket", 18]
}

print("I live in", info["city"])
print("I love", info["favourites"])
print("I love", info.get("favourite", "Not Found"))  # even if you missmatch any key but still you will not get any error because of .get

info.update({"channel": "TrainWithVishal"})
print(info)
print(dir(info))  # dir is used to know about what we can perform with the info dictioary
print(info.get.__doc__) # to know about the particular functions detail

# iterate a dictionary
for key,value in info.items():
    print(key,value)

