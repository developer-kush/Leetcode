class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:

        n = len(times)

        timepoints = set()
        arriv = {}
        leave = defaultdict(list)
        for idx, (u, v) in enumerate(times):
            arriv[u] = idx
            leave[v].append(idx)
            timepoints |= {u, v}

        reserved = {}
        arr = list(range(n))
        heapify(arr)
        for timepoint in sorted(timepoints):
            for user in leave[timepoint]:
                heappush(arr, reserved[user])
                del reserved[user]
            if timepoint in arriv:
                if arriv[timepoint] == targetFriend: return arr[0]
                reserved[arriv[timepoint]] = arr[0]
                heappop(arr)
            
        