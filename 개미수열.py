""" 
1		    1이 있고
1 1		    윗줄에 1이 1개
1 2		    윗줄에 1이 2개
1 1 2 1		윗줄에 1이 1개 2가 1개
1 2 2 1 1 1	윗줄에 1이 2개 2가 1개 1이 1개
1 1 2 2 1 3	윗줄에 1이 1개 2가 2개 1이 3개 """

# line1 = 1
# line2 = line1[0], line1.count(line1[0])
# line3 = line2[0], line2.count(line2[0])
# line4 = line3[0], line3.count(line3[0]), line3[1], line3.count(line3[1]))
# line5 = line4[0], line4.count(line3[0]), line4[1], line4.count(line3[1]))
# print(line1, line2)


# sol1) 이중 for문
line = "1"
for j in range(10):
    print(line)
    now = "1"
    newLine = ""
    count = 0
    for i in line:
        if now == i:
            count += 1
        else:
            newLine += now + str(count)
            now = i
            count = 1
    line = newLine + now + str(count)

# sol2) 재귀함수
