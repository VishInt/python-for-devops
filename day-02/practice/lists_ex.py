# a  = 100

# print(a, type(a))

# a = [100,200,300, True, 4.6]      # List
# print(type(a))
# a.append(200)
# print(a)

#------------------------------------------------------------------------#

clouds = list()
print(type(clouds))
clouds.append("aws")
clouds.append("aure")
clouds.append("azure")
clouds.append("ibm")
clouds.append("alibaba")
clouds.append("utho")
print(clouds)

print("The length of cloud is: ", len(clouds))

print("World Leader for Cloud Service Provider is:", clouds[0])

# print("Indian cloud provider is: ", clouds[5])  -----Method 1
print("Indian cloudprovider is:", clouds[-1])

print(dir(clouds))     # dir used to show what we can do with list means multiple operation we  can perform 
print(clouds.count.__doc__)  # count return the number of occurance of value  
print(clouds.reverse.__doc__)  # Reverse *IN PLACE*.
print(clouds.append.__doc__)   # Append object to the end of the list.
print(clouds.extend.__doc__)

# ['asw', 'Azure', 'gcp', 'ibm', 'alibaba', 'utho']
# range(5) -> 0,1,2,3,4

# for i in clouds:
#     print(i)

# for cloud in clouds:
#     print(cloud)

# iterate the list
for cloud in clouds:
    if cloud == "aws":
        print(f"{cloud} is the worlds leading cloud provider")
    elif cloud == "utho":
        print(f"{cloud} Indian Cloud")
    elif cloud == "azure" or cloud == "gcp":
        print(f"{cloud} Remaining days me wo bhi cover ho jayega")
    else:
        print(f"{cloud} baki cloud nahi ho payega")
