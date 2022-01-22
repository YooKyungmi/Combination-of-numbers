numbers = [979, 97, 978, 81, 818, 817]


def solution(numbers):
    numbers = list(map(str, numbers))
    numSort = sorted(numbers, key=lambda x: x[3]if len(
        x) >= 4 else (x[2] if len(x) >= 3 else '0'), reverse=True)
    numSort = sorted(numSort, key=lambda x: x[2]if len(
        x) >= 3 else (x[1] if len(x) >= 2 else '0'), reverse=True)
    numSort = sorted(numSort, key=lambda x: x[1]if len(
        x) >= 2 else x[0], reverse=True)
    numSort = sorted(numSort, key=lambda x: x[0], reverse=True)

    answer = "".join(numSort)
    return answer


print(solution(numbers))
