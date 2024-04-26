class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        dig = []
        let = []
        for log in logs:
            if log[-1].isdigit(): dig.append(log)
            else: let.append(log)

        return sorted(let, key = lambda log: log.split(' ', 1)[::-1]) + dig