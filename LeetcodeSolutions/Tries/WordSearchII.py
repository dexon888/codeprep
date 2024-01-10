class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def addWord(self, word):
        curr = self
        for c in word:
            if c not in word.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True


class Solution(object):
    def findWords(self, board, words):
        root = TrieNode()
        for w in words:
            root.addWord(w)
        ROWS, COLS = len(board), len(board[0])
        result, visit = set(), set()

        def dfs(row, col, node, word):
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or (row, col) in visit or board[row][col] not in node.children:
                return False
            visit.add((row, col))
            node = node.children[board[row][col]]
            word += board[row][col]
            if node.endOfWord:
                result.add(word)

            dfs(row - 1, col, node, word)
            dfs(row + 1, col, node, word)
            dfs(row, col - 1, node, word)
            dfs(row, col + 1, node, word)

            visit.remove((row, col))
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        return list(result)
