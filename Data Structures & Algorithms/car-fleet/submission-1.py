class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        eta = [(target-pos)  / s for pos, s in cars]
        
        stack = []
        for time in eta:
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)