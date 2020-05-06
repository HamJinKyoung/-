""" 10001번째의 소수

소수를 크기 순으로 나열하면 2, 3, 5, 7, 11, 13, ... 과 같이 됩니다.

이 때 10,001번째의 소수를 구하세요. """

# 소수: 1과 자기자신만을 약수로 갖는 수
# 소수 판별 함수
def is_prime(n):
    if n == 2 or n == 3:    # 시간 단축을 위해 2와 3은 True
        return True
    if n % 2 == 0 or n < 2: # 짝수와 1 제외
        return False
    for i in range(3, int(n**0.5)+1, 2):  # 3부터 n의 중간값까지 2씩 증가(짝수는 앞에서 이미 제외했으므로 홀수만 확인하면 됨), n**0.5는 제곱근
        if n % i == 0:  # 어떤 수라도 나누어 떨어지면 소수가 아님
            return False
    return True

# 10001번째 소수 찾기
count = 1
i = 3   # 3부터 시작
while count < 10001:
    if is_prime(i):
        count += 1
        prime = i
    i += 2  # 짝수는 건너뜀

print(prime)


# primesieve를 사용하면 한줄로 해결..!
# from primesieve import nth_prime
# print(nth_prime(10001))