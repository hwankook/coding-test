# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    first = A[0]
    second = sum(A[1:])
    answer = abs(first - second)
    for i in range(1, len(A) - 1):
        first += A[i]
        second -= A[i]
        answer = min(answer, abs(first - second))
    return answer
