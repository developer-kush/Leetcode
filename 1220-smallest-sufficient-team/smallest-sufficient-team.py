class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:

        req = (1<<len(req_skills))-1
        mask = {word:(1<<idx) for idx, word in enumerate(req_skills)}
        people = [reduce((lambda x, y: x|y), (mask[i] for i in arr)) if arr else 0 for arr in people]
        
        @cache
        def rec(pos, mask):
            if mask == req: return []
            if pos >= len(people): return None 

            take = rec(pos+1, mask|people[pos])
            notake = rec(pos+1, mask)

            if take is not None: take = take + [pos]

            if take is None or notake is None: return take or notake
            if len(take) <= len(notake): return take
            return notake

            return ans

        return sorted(rec(0, 0))