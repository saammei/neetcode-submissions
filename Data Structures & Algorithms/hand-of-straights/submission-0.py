class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        c = collections.Counter(hand)
        heapq.heapify(hand)

        while hand:
            min_val = heapq.heappop(hand)
            if c[min_val] > 0:
                c[min_val] -= 1
                for i in range(1, groupSize):
                    x = min_val + i
                    if x not in c or c[x] == 0:
                        return False
                    c[x] -= 1
        return True
