# -------------String----------------
## 转义字符
# txt = "We are the so-called "Vikings" from the north."
# pass
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

## Mehthod
a = "Hello, World!"
print(a.startswith("Hello"))    # True
print(a.endswith("World"))      # False
print(a.endswith("!"))          # True

txt = "Company12"
# # 仅包含
print(txt.isalnum())              # True     ## letter (a-z) and numbers (0-9)
print(txt.isalpha())              # False     ## letter (a-z)
print(txt.isdigit())              # False     ## numbers (0-9)

# -------------List:Sort----------------
my_list = ["apple", "cherry", "banana"]
my_list.sort()                  # ['apple', 'banana', 'cherry']
my_list.sort(reverse = True)    # ['cherry', 'banana', 'apple']
def myfunc(s):
    return len(s)
my_list.sort(key = myfunc)
print(my_list)                  # ['apple', 'cherry', 'banana']

# -------------List:Case-Sensitive----------------
my_list = ["banana", "Orange", "Kiwi", "cherry"]
my_list.sort()                  # ['Kiwi', 'Orange', 'banana', 'cherry']
my_list = ["banana", "Orange", "Kiwi", "cherry"]
my_list.sort(key = str.lower)   # ['banana', 'cherry', 'Kiwi', 'Oran
my_list = ["banana", "Orange", "Kiwi", "cherry"]
my_list.reverse()               # ['cherry', 'Kiwi', 'Orange', 'banana']

# 排序
def takeSecond(elem):
    return elem[1]
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
# 指定第二个元素排序
random.sort(key=takeSecond)
print(random)

# -------------List:Other----------------
my_list = ["apple", "cherry", "banana"]
new_list = my_list.copy()
new_list2 = list(new_list)            # Blender常用
print(new_list)
print(new_list2)

list1 = ["a", "b","c"]
list2 = [1, 2, 3]
list3 = list1 + list2           # ['a', 'b', 'c', 1, 2, 3]
list2.extend(list1)             # 类比之前的append方法。Extend list by appending elements from the iterable
print(list1)
print(list2)
print(list3)

# -------------Tupe----------------
# 元组中可以是任意的数据类型
tup1 = ('apple', 'cherry', 199, 200)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print ("tup1[0]:", tup1[0])             # tup1[0]:apple
print ("tup2[1:5]:", tup2[1:5])         # tup2[1:5]:(2，3，4，5)

color_list = [
    ("_red", "red_红", ""),
    ("_yellow", "yellow_黄", "")
]

value = color_list[0][0]
print(value)                        # _red

# 元组的值无法修改
# color_list[0][0] = "test"
print(color_list)