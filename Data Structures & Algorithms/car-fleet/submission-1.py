class Solution:
    def carFleet(self, target, position, speed):
        pos_spe = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, spe in pos_spe:
            time = (target - pos) / spe
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)  