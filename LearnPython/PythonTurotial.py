############################### 变量Variables #####################################
## 数据类型转换
x = str(3)          # x will be '3'
y = int(3)          # y will be 3
z = float(3)        # z will be 3.0

## 变量命名规范
#2my_var = "John"    #不能以数字开头，需要以字母或下划线开头
my_var = "test"     # 在python里面约定俗成小写+下划线

## 变量区分大小写
a = 4
A = "test"          #A will not overwrite a

## 变量赋值
### 多对多：需要一一对应
x, y, z = "Orange", "Banana", "Cherry"
x, y, z = "Orange", 1 , 1.0         # 支持多种类型
### 一对多
x = y = z = "Orange"
### 取值
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits                    # 同样需要一一对应

## Global Variables
###不加global的情况
x = "global"
def myfunc():
    x = "local"
    print(x)            # local

myfunc()
print(x)                # global

### 如果加上global
x = "global"
def myfunc():
    global x
    x = "local"
    print(x)            # local

myfunc()
print(x)                # local

############################### 运算符Operator #####################################
## Logic
and / or / not

## Identify
x = ['apple','banana']
y = ['apple','banana']
z = x

print(x is z)           # true
print(x is not y)       # false
print(x == y)           # true

## MemberShip
x = ['apple','banana']
print('banana' in x)    # true
print('mouse' not in x) # true

## for:后面for循环也会说，这里简单提一下
fruit_list = ['apple','banana']
for item in fruit_list:
    print(item)         # item可以随便命名，只需保证前后一致即可

for index in range(len(fruit_list)):
    print(fruit_list[index])

## If else
a = 1
b = 2
if a > b:
    print("a is bigger than b")
elif a == b:
    print("a and b are equal")
else:
    print("b is bigger than a")

############################### 字符串String #####################################

b = "Hello,world"

## 字符串切片
print(b[2:5])   # llo
print(b[:5])    # Hello
print(b[2:])    # llo,world

## 字符串修改
a = 'Hello,world!'
print(a.replace("H","J"))   # Jello,world!
print(a.split(","))         # ['Hello','world!']
print(a.split('e'))         # ['H','llo,world!']
print(a.split(',')[0])      # 'Hello'

## 字符串格式化输出
number = 3
item = '鼠标'
price = 49.9
my_order = "I want {} pieces of item {} for {} yuan"        # 占位符
print(my_order.format(number , item , price))               # I want 3 pieces of item 鼠标 for 49.9 yuan

############################### 列表 List #####################################
## Access
fruit = ["apple", "banana" , "cherry"]
print(fruit[1])             # banana
print(fruit[-1])            # cherry
print(fruit[:3])            # 输出 0 1 2 三个元素 apple,banana,cherry

## Modify
fruit[0] = "mouse"

fruit.append("orange")
print(fruit)                # ['mouse', 'banana', 'cherry', 'orange']

fruit.insert(1,"insert_fruit")
print(fruit)                # ['mouse', 'insert_fruit', 'banana', 'cherry', 'orange']

fruit.remove("orange")
print(fruit)                # ['mouse', 'insert_fruit', 'banana', 'cherry']

fruit.clear()
print(fruit)                # []

## Loop
fruit_list = ["apple", "banana" , "cherry"]
for item in fruit_list:
    print(item)

for index in range(len(fruit_list)):         # length:3
    print(fruit_list[index])