# -------------作业----------------
# 反向输出
fruit_list = ["apple", "banana", "cherry"]

# for x in fruit_list:
#     print(x)

# for item in reversed((fruit_list)):
#     print(item)

# new_list = [x.upper() for x in fruit_list if "apple" in x]
# for item in new_list:
#     print(item)

# 反向输出fruit_list

for index in range(len(fruit_list) - 1, -1, -1):
    print(fruit_list[index])

# -------------Directory----------------
my_dict = {
    "name": "this is name",
    "year": 2000
}

# Access
X = my_dict["name"]
# X = my_dict.get("name")
print(X)

if "name" in my_dict:
    print("Check key")

X = my_dict.keys()          # dict_keys(['name', 'year'])
X = my_dict.values()        # dict_values(['xxx', 2000])
X = my_dict.items()         # dict_items([('name', 'xxx'), ('year', 2000)])

# Update Element
my_dict["year"] = 2022
my_dict.update({"year": 2020})
print(my_dict)

# Add Element
my_dict["color"] = "red"
my_dict.update({"color": "red"})

my_dict.pop("name")         #删除特定
my_dict.popitem()           #删除最后
my_dict.clear()
print(my_dict)