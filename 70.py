"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1

        steps = [1] * n
        count = 1
        takenSoloStairs = 0 
        amountOfTwosInSteps = 0
        
        while takenSoloStairs < (n / 2):
            takenSoloStairs += 2
            amountOfTwosInSteps += 1

            steps.pop(-1)
            
            if amountOfTwosInSteps == 1:
                count += len(steps)
            else:
                count += len(steps)
                count += (len(steps) - 1) * amountOfTwosInSteps

        print(count)
        print(steps)


solu = Solution()

solu.climbStairs(2)
solu.climbStairs(3)
solu.climbStairs(4)
solu.climbStairs(5)
solu.climbStairs(6)