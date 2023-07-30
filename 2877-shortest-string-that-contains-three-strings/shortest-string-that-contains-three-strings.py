class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        
        def getPref(s):
            pref = set()
            curr = ""
            for i in s:
                curr+=i
                pref.add(curr)
            return pref
        
        prefa = getPref(a)
        prefb = getPref(b)
        prefc = getPref(c)
        
        
        def find(a, b, c):
            
            if b in c: b = c
            elif c in b: pass
            else:
                prefc = getPref(c)
                cres = len(b)
                curr = ""
                for i in range(len(b)-1,-1,-1):
                    curr = b[i]+curr
                    # print(curr)
                    if curr in prefc: cres = i
                
                b= b[:cres]+c
            
            prefb = getPref(b)
            # print(b, getPref(b))
            
            if a in b: a = b
            elif b in a: pass
            else:
                bres = len(a)
                curr = ""
                for i in range(len(a)-1,-1,-1):
                    curr = a[i]+curr
                    if curr in prefb: bres = i
                
                # print("bres:",bres)
                a= a[:bres] + b
            
            # print(len(a), a)
            # print()
            return [len(a), a]
            
        
        
        return min([find(a, b, c),
                    find(a, c, b),
                    find(b, a, c),
                    find(b, c, a),
                    find(c, a, b),
                    find(c, b, a)])[1]