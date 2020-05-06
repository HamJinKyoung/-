""" 이백만 이하 소수의 합

10 이하의 소수를 모두 더하면 2 + 3 + 5 + 7 = 17 이 됩니다.

이백만(2,000,000) 이하 소수의 합은 얼마입니까? """

def is_prime(n):
    if n == 2 or n == 3:    # 시간 단축을 위해 2와 3은 True
        return True
    if n % 2 == 0 or n < 2: # 짝수와 1 제외
        return False
    for i in range(3, int(n**0.5)+1, 2):  # 3부터 n의 중간값까지 2씩 증가(짝수는 앞에서 이미 제외했으므로 홀수만 확인하면 됨), n**0.5는 제곱근
        if n % i == 0:  # 어떤 수라도 나누어 떨어지면 소수가 아님
            return False
    return True

sum = 2
for i in range (3,2000001,2):
    if is_prime(i):
        sum += i

print(sum)