from collections import deque
from copy import deepcopy
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        stack = deque()

        for w in word:
            if not sum([w in ch for ch in board]):
                return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
                    stack.appendleft([c, r, board[r][c], visited])

                    while stack:
                        x, y, w, v = stack.popleft()
                        v[y][x] = True

                        if w == word:
                            return True

                        if x + 1 < len(board[0]) and not v[y][x + 1] and word[len(w)] == board[y][x + 1]:
                            stack.appendleft([x + 1, y, w + board[y][x + 1], deepcopy(v)])
                        if x - 1 >= 0 and not v[y][x - 1] and word[len(w)] == board[y][x - 1]:
                            stack.appendleft([x - 1, y, w + board[y][x - 1], deepcopy(v)])
                        if y + 1 < len(board) and not v[y + 1][x] and word[len(w)] == board[y + 1][x]:
                            stack.appendleft([x, y + 1, w + board[y + 1][x], deepcopy(v)])
                        if y - 1 >= 0 and not v[y - 1][x] and word[len(w)] == board[y - 1][x]:
                            stack.appendleft([x, y - 1, w + board[y - 1][x], deepcopy(v)])
        return False
