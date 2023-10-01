class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        num_days = [0] * len(temperatures)
        temperature_stack = []

        for i, temperature in enumerate(temperatures):
            while temperature_stack and temperature > temperature_stack[-1][1]:
                current_temp = temperature_stack.pop()
                num_days[current_temp[0]] = i - current_temp[0]
            temperature_stack.append((i, temperature))
        return num_days