class Solution:
    def isNumber(self, s: str) -> bool:
        ec = s.count('e') + s.count('E')
        if ec > 1: return False
        parts = s.replace("E", 'e').split('e')

        for idx, part in enumerate(parts):
            if not part: return False
            if part[0] in '+-': part = part[1:]

            if part.count('.') + idx > 1: return False
            part = "".join(part.split("."))
            if not part: return False

            for ch in part: 
                if not ch.isdigit(): return False

        return True