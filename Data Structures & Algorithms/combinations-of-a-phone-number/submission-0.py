class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        digits_map = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        out = []

        def dfs(i, cur):

            if i >= len(digits):
                out.append(''.join(cur))
                return 

            for d in digits_map[digits[i]]:
                cur.append(d)
                dfs(i+1, cur)
                cur.pop()

        dfs(0, [])

        return out
