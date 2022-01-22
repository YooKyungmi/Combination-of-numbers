numbers = [0, 0, 0]
# 979 97 978 818 81 817


def solution(numbers):
    numbers = list(map(str, numbers))
    numSort = sorted(numbers, key=lambda x: x*3, reverse=True)
    answer = "".join(numSort)
    if answer[0] == '0':
        answer = '0'
    return answer


print(solution(numbers))
