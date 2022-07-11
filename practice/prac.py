"""
# 작업 디렉토리 설정

# get current path
import os
curPath = os.getcwd() #/home/user/PycharmProjects/prac1
print(curPath)

# change path
os.chdir('/home/user/Desktop/car_train')
print(os.getcwd()) #/home/user/Desktop/car_train
"""

# ======================================================================================================================

# json 읽어오기

# open 함수를 이용하여 경로와 이름을 적고 파일을 불러온다.
# json.load() 함수로 json 일을 파이썬의 딕셔너리나 리스트 자료형으로 반환한다.
# json 파일을 읽어들이면, 딕셔너리 형태로 변수에 저장된다. --> 해당 변수에 접근하여 특정 요소의 값을 출력할 수 있다.
import json

json_path = '/home/user/Desktop/car_test/car_test_json/test_sets_new.json'
with open(json_path, 'r') as f:
    new_json = json.load(f)

# json 파일 내 filename 추출
print(new_json[800]['filename'])

# ======================================================================================================================

# img

import os

img_path = '/home/user/Desktop/car_test/car_test/test_sets_new'
img_path = os.listdir(img_path)
img_path
len(img_path)  # 1,430

# 절대경로 추출
import glob

path = '/home/user/Desktop/car_test/car_test/test_sets_new/*'
output = glob.glob(path)
print(output[800])

# 비교 문자 추출
k = output[800]
print(k.rindex('/'))  # /home/user/Desktop/car_test/car_test/test_sets_new/ㅅ94.jpg 중 ㅅ94.jpg만
# 50

total = len(output[800])  # 58
pre = k.rindex('/')

print(k[-(total - pre) + 1:])

# ======================================================================================================================

'''
import json
json_path = '/home/user/Desktop/car_test/car_test_json/test_sets_new.json'
with open(json_path,'r') as f:
    new_json = json.load(f)
print(json.dumps(new_json,ensure_ascii=False))

output = json.dumps(new_json, ensure_ascii=False)

# 변환 X
# 저장..?
file_path='/home/user/Desktop/unicode/change.json'
with open(file_path,'w',encoding='utf-8') as f:
    json.dump(new_json,f, indent ='\t')
'''

# ======================================================================================================================

# developer-joe.tistory.com/210
# 유니코드 형태의 한글을 정상적으로 표시하도록 하는 방법

# json 파일 읽어오기
# 유니코드 --> 해석 : json.load

import json
json_path = '/home/user/Desktop/car_test/car_test_json/test_sets_new.json'
with open(json_path,'r') as f:
    new_json = json.load(f)

# 유니코드 해석 없이 읽어오기 : json.dumps
# guru99.com/python-json.html
prac = json.dumps(new_json, indent='\t')

# 한줄씩 읽으려고 했을 때 에러 : AttributeError: 'str' object has no attribute 'ReadAllLines'
# str --> text file로 변경
# datatofish.com/string-to-text-file-python/

text_file = open(r'/home/user/Desktop/unicode/prac1.txt','w')
text_file.write(prac)
text_file.close()

'''
# 리스트 형식으로 파일 읽기
# jimmy-ai.tistory.com/232
with open('/home/user/Desktop/unicode/prac1.txt','r') as f:
    example = f.readlines()
    print(example[3])
'''

# 한줄 한줄씩 읽기
with open('/home/user/Desktop/unicode/prac1.txt','r') as f:
    line = f.readline()
    print(line)         # [
    line = f.readline()
    print(line)         # {
    line = f.readline()
    print(line)         # "filename"
    line = f.readline()
    print(line)         # width

# ======================================================================================================================

# 파일의 총 줄 수 구하기
# dororongju.tistory.com/44
with open('/home/user/Desktop/unicode/prac1.txt','r') as f:
    print(len(f.readlines()))   # 47,531

# ======================================================================================================================

'''
f = open('/home/user/Desktop/unicode/prac1.txt','r')
line = f.readline()
print(line)
print('filename' in line)
line = f.readline()
print(line)
print('filename' in line)
line = f.readline()
print(line)
print('filename' in line)
line = line.encode('utf-8')
line = line.decode('unicode_escape')
print(line)
f.close

# 들여쓰기 o
with open('/home/user/Desktop/unicode/prac1.txt', 'r') as f:
    while True:
        line = f.readline()
        if "filename" in line:
            uni_line = line.encode('utf-8')
            cha_line = uni_line.decode('unicode_escape')
            line = cha_line
            print(line)
        else :
            print(line)

# 들여쓰기 x
with open('/home/user/Desktop/unicode/prac1.txt', 'r') as f:
    for i in range (0,10):
        line = f.readline()
        if "filename" in line:
            uni_line = line.encode('utf-8')
            cha_line = uni_line.decode('unicode_escape')
            line = cha_line
            print(line.strip())
        else :
            print(line.strip())


# 일부 실행한 뒤 결과 확인 (연습)
# codechacha.com/ko/python-read-write-file/
f = open('/home/user/Desktop/unicode/prac1.txt','r')
with open('/home/user/Desktop/unicode/prac2.txt','w') as file:
    for i in range(0, 10):
        line = f.readline()
        if "filename" in line:
            uni_line = line.encode('utf-8')
            cha_line = uni_line.decode('unicode_escape')
            line = cha_line
            file.writelines(line.strip())
        else:
            file.writelines(line.strip())
f.close()
'''

# convert txt to json
f = open('/home/user/Desktop/unicode/prac1.txt','r')
with open('/home/user/Desktop/unicode/prac3.json','w') as file:
    for i in range(0,47531):        # 총 줄 수 47530 --> 총 줄 수 + 1
        line = f.readline()
        if "filename" in line:
            uni_line = line.encode('utf-8')
            cha_line = uni_line.decode('unicode_escape')
            line = cha_line
            file.writelines(line)
        else:
            file.writelines(line)
f.close()