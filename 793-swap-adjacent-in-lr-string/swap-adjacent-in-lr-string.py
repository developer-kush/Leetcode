class Solution:
    def canTransform(self, start: str, end: str) -> bool:

        if start.replace('X', '') != end.replace('X', ''): return False
        l_pos_start = []
        r_pos_start = []
        l_pos_end = []
        r_pos_end = []

        for idx, ch in enumerate(start):
            if ch == 'L': l_pos_start.append(idx)
            if ch == 'R': r_pos_start.append(idx)
        
        for idx, ch in enumerate(end):
            if ch == 'L': l_pos_end.append(idx)
            if ch == 'R': r_pos_end.append(idx)

        for i in range(len(l_pos_start)):
            if l_pos_start[i] < l_pos_end[i]: return False
        for i in range(len(r_pos_start)):
            if r_pos_start[i] > r_pos_end[i]: return False
        
        return True