""" 파일 압축 2단계
파일(a.txt) 열어서 개미수열원리를 이용해 압축파일(b.txt) 만들기 """

with open("C:/Users/HJK/Desktop/likelion_8th/대표부스트코스/a.txt", mode='rt', encoding='utf-8') as a:
    with open("C:/Users/HJK/Desktop/likelion_8th/대표부스트코스/b.txt", mode='w') as b:
        content = a.read()
        print("a.txt 파일 내용: ", content)

        now = content[0]
        new = ""
        count = 0
        for i in content:
            if now == i:
                count += 1
            else:
                new += now + str(count)
                now = i
                count = 1
        new += now + str(count)
        print("압축결과: ", new)
        b.write(new)