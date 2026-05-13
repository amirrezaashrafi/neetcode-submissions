class Solution:
    def carFleet(self, target, position, speed):
        time = []
        pos_spe = []
        for pos, spe in zip(position, speed):
            pos_spe.append((pos, spe))

        pos_spe.sort(reverse=True)

        for fleet in pos_spe:
            current_time = (target - fleet[0]) / fleet[1]
            if not time:
                time.append(current_time)
            elif current_time > time[-1]:
                time.append(current_time)

        return len(time)  