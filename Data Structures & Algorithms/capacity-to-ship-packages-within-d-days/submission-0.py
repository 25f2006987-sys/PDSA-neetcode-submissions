class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        cap = sum(weights)
        def count_days(L, cap):
            daysc = 1
            load = 0
            for w in L:
                if load + w > cap:
                    daysc += 1
                    load = 0
                load += w
            return daysc
        l, r = max(weights), cap
        while l <= r:
            mid = (l + r) // 2
            req_days = count_days(weights, mid)
            if req_days > days:
                l = mid + 1
            else:
                r = mid - 1
        return l
