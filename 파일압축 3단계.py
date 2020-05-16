""" """ """ 
압축할 파일 내용: ababcababcdef...
딕셔너리: {ab:A, abc:B}
압축결과 파일 내용: ABAB...

압축할 딕셔너리를 어떻게 구성해야 할까? """

# step1. 두개씩 잘라서 총 몇 개의 딕셔너리가 나오는지 구현해보기
dic = {}
d_value = ord('A')  # ord(): 특정한 한 문자를 아스키 코드 값으로 변환해 주는 함수
with open("C:/Users/HJK/Desktop/likelion_8th/대표부스트코스/abc.txt") as f:
    content = f.read()
    for i in range(0,len(content),2):
        key = content[i:i+2]
        value = chr(d_value)    # chr(): 아스키 코드 값을 문자로 변환해 주는 함수(10진수, 16진수 사용가능)
        if key not in dic:
            dic[key] = chr(d_value)
            d_value += 1
print(dic)

