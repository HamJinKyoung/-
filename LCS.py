"""
# LCS : 가장 긴 공통의 부분문자열
abcde랑 abefg에서 LCS = abe
이차배열을 이용
  a b c d e
a 1 1 1 1 1
b 1 2 2 2 2
e 1 2 2 2 3
f 1 2 2 2 3
g 1 2 2 2 3

변화가 있는 지역 a,b,e """

s1 = "abcde"
s2 = "abefg"

m = [[0 for col in range(5)] for row in range(5)]

for i in m:
    print(i)

