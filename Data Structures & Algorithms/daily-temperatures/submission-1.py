class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        output = [0] * len(temperatures) #[3,2,1,0]

        stack = [] #[]

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                output[prev] = i - prev

            stack.append(i)
        
        return output
        