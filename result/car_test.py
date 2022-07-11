# convert unicode to hangul

# ======================================================================================================================

# car_test_new

# ======================================================================================================================

import json
import os

json_path = '/home/user/Desktop/car_test/car_test_json/test_sets_new.json'
with open(json_path, 'r') as f:
    new_json = json.load(f)

    # with unicode
    uni_json = json.dumps(new_json, indent='\t')

    # convert json file to text file
    text_file1 = open(r'/home/user/Desktop/convert/car_test/car_test_new.txt','w')
    text_file1.write(uni_json)
    text_file1.close()

    # total row
    text_file2 = open(r'/home/user/Desktop/convert/car_test/car_test_new.txt','r')
    total = len(text_file2.readlines())
    ran = total + 1

    text_file2.close()

# ======================================================================================================================

# convert txt to json
file = open('/home/user/Desktop/convert/car_test/car_test_new.json','w')
text_file2 = open(r'/home/user/Desktop/convert/car_test/car_test_new.txt','r')
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

rm_txt = '/home/user/Desktop/convert/car_test/car_test_new.txt'
os.remove(rm_txt)

# ======================================================================================================================

# car_test_old

# ======================================================================================================================

json_path = '/home/user/Desktop/car_test/car_test_json/test_sets_old.json'
with open(json_path, 'r') as f:
    new_json = json.load(f)

    # with unicode
    uni_json = json.dumps(new_json, indent='\t')

    # convert json file to text file
    path = '/home/user/Desktop/convert/car_test/car_test_old.txt'
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
file = open(json_path,'w')
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