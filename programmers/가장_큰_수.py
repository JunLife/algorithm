def solution(numbers):
    answer = ''
    numbers.sort(
        # 길이가 다른 경우 최대로 생각해서 비교 (1000 이하 값)
        # 10, 1 인 경우 -> '101010' 과 '111'을 비교
        # '111' > '101010' -> 1, 10 순으로 정렬됨.
        # 110이 101 보다 큼.
        key = lambda x : (str(x) + str(x) + str(x)),
        reverse = True
    )
    for number in numbers:
        answer += str(number)

    answer = str(int(answer))
    return answer