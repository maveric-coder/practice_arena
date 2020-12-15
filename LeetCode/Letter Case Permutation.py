class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        s = list(S)
        res = []
        
        def util(i, cur):
            if i == len(s):
                res.append(''.join(cur[:]))
                return
            if s[i].isdigit():
                cur.append(s[i])
                util(i+1, cur)
            else:
                cur.append(s[i].lower())
                util(i+1, cur)
                cur.pop()
                cur.append(s[i].upper())
                util(i+1, cur)
            cur.pop()
        
        util(0, [])
        return res
        
