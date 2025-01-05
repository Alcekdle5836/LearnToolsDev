import json
# python 读取
with open("C:/Users/79160/Desktop/LearnToolsDev/NamePattern.json", 'r', encoding='utf-8') as temp_json:
    json_data = temp_json.read()

obj = json.loads(json_data)
print(obj[0]["structure"])