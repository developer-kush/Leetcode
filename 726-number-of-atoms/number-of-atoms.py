class Solution:
    def countOfAtoms(self, formula: str) -> str:

        ptr = 0

        def rec(lvl = 0):
            nonlocal ptr
            res = Counter()
            curr = num = tempres = None

            while ptr < len(formula):
                
                if formula[ptr] == ")":  break
                elif formula[ptr].isalpha() and formula[ptr].islower():
                    curr += formula[ptr]
                elif formula[ptr] == "(" or formula[ptr].isalpha():
                    if curr and num: res[curr] += int(num)
                    elif curr: res[curr] += 1
                    elif tempres :
                        num = int(num) if num else 1
                        for key in tempres: res[key] += tempres[key]*num

                    if formula[ptr] == "(":
                        ptr += 1
                        curr = num = ""
                        tempres = rec(lvl+1)
                    else: curr = formula[ptr]
                    num = ""

                else: num += formula[ptr]

                ptr += 1
            
            if curr and num: res[curr] += int(num)
            elif curr: res[curr] += 1
            elif tempres:
                num = int(num) if num else 1
                for key in tempres: res[key] += tempres[key]*num

            return res

        res = rec()
        resstr = ""
        for key in sorted(res):
            resstr += key
            if res[key]>1: resstr += str(res[key])
        return resstr
