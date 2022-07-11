# ======================================================================================================================

# office_crop

# ======================================================================================================================

import json
import os

json_path = '/home/user/Desktop/car_train/사람/office_crop.json'
with open(json_path, 'r') as f:
    new_json = json.load(f)

    # with unicode
    uni_json = json.dumps(new_json, indent='\t')

    # convert json file to text file
    path = '/home/user/Desktop/convert/car_train/사람/office_crop.txt'
    text_file1 = open(path,'w')
    text_file1.write(uni_json)
    text_file1.close()

    # total row
    text_file2 = open(path,'r')
    total = len(text_file2.readlines())
    ran = total + 1
    text_file2.close()

# ======================================================================================================================

# convert txt to json
file = open('/home/user/Desktop/convert/car_train/사람/office_crop.json','w')
text_file2 = open(path,'r')
for i in range(1,ran):
    line = text_file2.readline()
    if "filename" in line:
        uni_line = line.encode('utf-8')
        cha_line = uni_line.decode('unicode_escape')
        line = cha_line
        file.writelines(line)
    else:
        file.writelines(line)

file.close()

# 파일 삭제
os.remove(path)

# ======================================================================================================================

# night.json

# ======================================================================================================================

import json
import os

json_path = '/home/user/Desktop/car_train/야간/night.json'
with open(json_path, 'r') as f:
    new_json = json.load(f)

    # with unicode
    uni_json = json.dumps(new_json, indent='\t')

    # convert json file to text file
    path = '/home/user/Desktop/convert/car_train/야간/night.txt'
    text_file1 = open(path,'w')
    text_file1.write(uni_json)
    text_file1.close()

    # total row
    text_file2 = open(path,'r')
    total = len(text_file2.readlines())
    ran = total + 1
    text_file2.close()

# ======================================================================================================================

# convert txt to json
file = open('/home/user/Desktop/convert/car_train/야간/night.json','w')
text_file2 = open(path,'r')
for i in range(1,ran):
    line = text_file2.readline()
    if "filename" in line:
        uni_line = line.encode('utf-8')
        cha_line = uni_line.decode('unicode_escape')
        line = cha_line
        file.writelines(line)
    else:
        file.writelines(line)

file.close()

# 파일 삭제
os.remove(path)


# ======================================================================================================================

# car.json

# ======================================================================================================================

import json
import os

json_path = '/home/user/Desktop/car_train/차량/car.json'
with open(json_path, 'r') as f:
    new_json = json.load(f)

    # with unicode
    uni_json = json.dumps(new_json, indent='\t')

    # convert json file to text file
    path = '/home/user/Desktop/convert/car_train/차량/car.txt'
    text_file1 = open(path,'w')
    text_file1.write(uni_json)
    text_file1.close()

    # total row
    text_file2 = open(path,'r')
    total = len(text_file2.readlines())
    ran = total + 1
    text_file2.close()

# ======================================================================================================================

# convert txt to json
file = open('/home/user/Desktop/convert/car_train/차량/car.json','w')
text_file2 = open(path,'r')
for i in range(1,ran):
    line = text_file2.readline()
    if "filename" in line:
        uni_line = line.encode('utf-8')
        cha_line = uni_line.decode('unicode_escape')
        line = cha_line
        file.writelines(line)
    else:
        file.writelines(line)

file.close()

# 파일 삭제
os.remove(path)

# ======================================================================================================================

# 특수.json

# ======================================================================================================================

import json
import os

json_path = '/home/user/Desktop/car_train/차량/특수.json'
with open(json_path, 'r') as f:
    new_json = json.load(f)

    # with unicode
    uni_json = json.dumps(new_json, indent='\t')

    # convert json file to text file
    path = '/home/user/Desktop/convert/car_train/차량/특수.txt'
    text_file1 = open(path,'w')
    text_file1.write(uni_json)
    text_file1.close()

    # total row
    text_file2 = open(path,'r')
    total = len(text_file2.readlines())
    ran = total + 1
    text_file2.close()

# ======================================================================================================================

# convert txt to json
file = open('/home/user/Desktop/convert/car_train/차량/특수.json','w')
text_file2 = open(path,'r')
for i in range(1,ran):
    line = text_file2.readline()
    if "filename" in line:
        uni_line = line.encode('utf-8')
        cha_line = uni_line.decode('unicode_escape')
        line = cha_line
        file.writelines(line)
    else:
        file.writelines(line)

file.close()

# 파일 삭제
os.remove(path)

# ======================================================================================================================

# car_classify_sample.json

# ======================================================================================================================

import json
import os

json_path = '/home/user/Desktop/car_train/car_classify_sample.json'
with open(json_path, 'r') as f:
    new_json = json.load(f)

    # with unicode
    uni_json = json.dumps(new_json, indent='\t')

    # convert json file to text file
    path = '/home/user/Desktop/convert/car_train/car_classify_sample.txt'
    text_file1 = open(path,'w')
    text_file1.write(uni_json)
    text_file1.close()

    # total row
    text_file2 = open(path,'r')
    total = len(text_file2.readlines())
    ran = total + 1
    text_file2.close()

# ======================================================================================================================

# convert txt to json
file = open('/home/user/Desktop/convert/car_train/car_classify_sample.json','w')
text_file2 = open(path,'r')
for i in range(1,ran):
    line = text_file2.readline()
    if "filename" in line:
        uni_line = line.encode('utf-8')
        cha_line = uni_line.decode('unicode_escape')
        line = cha_line
        file.writelines(line)
    else:
        file.writelines(line)

file.close()

# 파일 삭제
os.remove(path)