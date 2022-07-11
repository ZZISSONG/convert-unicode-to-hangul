# ======================================================================================================================

# plate_train2

# ======================================================================================================================

import json
import os

json_path = '/home/user/Desktop/plate_train/real_plate2.json'
with open(json_path, 'r') as f:
    new_json = json.load(f)

    # with unicode
    uni_json = json.dumps(new_json, indent='\t')

    # convert json file to text file
    path = '/home/user/Desktop/convert/plate_train/real_plate2.txt'
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
file = open('/home/user/Desktop/convert/plate_train/real_plate2.json','w')
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

# plate_bbox_info

# ======================================================================================================================

import json
import os

json_path = '/home/user/Desktop/plate_train/plate_bbox_info.json'
with open(json_path, 'r') as f:
    new_json = json.load(f)

    # with unicode
    uni_json = json.dumps(new_json, indent='\t')

    # convert json file to text file
    path = '/home/user/Desktop/convert/plate_train/plate_bbox_info.json.txt'
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
file = open('/home/user/Desktop/convert/plate_train/plate_bbox_info.json','w')
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