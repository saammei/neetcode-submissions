class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        # print(cars)

        steps = []
        for p, s in cars:
            x = (target - p) / s
            steps.append(x)

        # print(steps)
        ans = []
        for x in steps:
            if not ans or x > ans[-1]:
                ans.append(x)
        # print(ans)
        return len(ans)
