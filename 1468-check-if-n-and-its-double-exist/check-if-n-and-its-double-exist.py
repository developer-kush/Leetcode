class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        st = set()
        for val in arr:
            if val*2 in st or val/2 in st: return True
            st.add(val)
        return False