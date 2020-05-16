""" 파일 압축 1단계 
파일 열어서 연속된 문자가 몇개씩 있는지 출력해보기
예) 1111223 => 1:4, 2:2, 3:1 """

f = open("C:/Users/HJK/Desktop/likelion_8th/대표부스트코스/Project_Euler/01.py", mode='rt', encoding='utf-8')
content = f.read()
# print(content)

now = content[0]
count = 0
for i in content:
    if now == i:
        count += 1
    else:
        print(now, ":", count)
        now = i
        count = 1

f.close()