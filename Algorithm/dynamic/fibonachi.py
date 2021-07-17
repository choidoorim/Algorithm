"""
피보나치 수열은 이전 두항의 합으로 값이 결정되는 특징이 있다.
재귀를 통해 구현하게 된다면 반복해서 호출하는 경우가 많아진다.
따라서 메모제이션 기법을 활용한 다이나믹 프로그래밍을 활용한다면 훨씬 효율적이다.
* 메모제이션 기법은 값을 저장하는 방식이므로 캐싱이라고 한다
탑다운 방식 : 재귀 함수를 이용하여 큰 문제를 해결하기 위해 작은 문제를 호출하는 방식
보텀업 방식 : 단순히 반복문을 이용하여  소스코드를 작성하는 경우, 작은 문제부터 차근차근 답을 도출
"""

def fibo(x):

    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)


array = [0] * 100   # 계산 된 결과를 저장
def fibo_memozation(x):
    if x == 1 or x == 2:
        return 1

    if array[x] != 0:
        return array[x]

    array[x] = fibo_memozation(x - 1) + fibo_memozation(x - 2)
    return array[x]


print(fibo_memozation(10))
