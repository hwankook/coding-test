# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    L = len(A) + 1
    return int((L * (1 + L)) / 2) - sum(A)
