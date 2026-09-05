class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        covered = [ False ] * 3
        for x in triplets:
            if x[0] > target[0] or x[1] > target[1] or x[2] > target[2]:
                continue
            if x[0] == target[0]: covered[0] = True
            if x[1] == target[1]: covered[1] = True
            if x[2] == target[2]: covered[2] = True
        return covered[0] and covered[1] and covered[2]
