import json

with open('E:\myproj\langmerge\en_us.json', 'r', encoding='utf-8') as en_f:
    en_data = json.load(en_f)
with open('E:\myproj\langmerge\zh_cn.json', 'r', encoding='utf-8') as zh_f:
    zh_data = json.load(zh_f)

merged_data = en_data.copy()
temp_data = en_data.copy()

temp_data.update(zh_data)

for key in merged_data:
    merged_data[key]=temp_data[key]

with open('E:\myproj\langmerge\merged.json', 'w', encoding='utf-8') as output:
    json.dump(merged_data, output, indent=4, ensure_ascii=False)

print('成功合并！')