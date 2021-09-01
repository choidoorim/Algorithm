"""
- Programmers - 위클리 4주차
- CDR
- dictionary 에서 value 값이 가장 큰 key를 찾는 방법
    - max(dic, key=dic.get) : 값이 같을 경우 1개만 출력
    - [k for k,v in dic.items() if max(dic.values()) == v] : 값이 같을 경우 배열에 저장 됌
"""


def solution(table, languages, preference):
    new_table = []      # 직업별 언어만 담을 배열
    job = []            # 직업만 담을 배열 
    dic = dict()        # 결과 값들을 담을 배열
    for tb in table:    # 테이블에서 언어들과 직업 나누기 위한 로직
        new_array = list(tb.split(' '))
        job.append(new_array[0])
        new_table.append(new_array[1:])
    for i in range(len(job)):   # 직업 별 총합 계산
        result = 0  # 직업 별 총합
        for j in range(len(languages)):
            for k in range(1, 6):   # 직업 별 언어는 무조건 5개 이므로
                if new_table[i][k - 1] == languages[j]:     # 직군에서 선호하는 언어와 나의 언어가 같을 경우
                    result += (6 - k) * preference[j]       # 직업군 언어 점수 * 언어 선호도
        dic[job[i]] = result
    answer = [k for k,v in dic.items() if max(dic.values()) == v]   # dictionary 에서 직업군 별로 총합이 최대인 것을 저장
    answer.sort()   # 이름이 사전순으로 정렬
    return answer[0]    # 총합이 여러개 일 경우 사전순에서 가장 빠른 직업군


print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["JAVA", "JAVASCRIPT"], [7, 5]))
