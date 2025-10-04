# leetcode question 1796



class Solution:
    def secondHighest(self, s: str) -> int:
        largest = float("-inf")
        S_largest = float("-inf")
        n = len(s)
        for i in range(0,n):
            if s[i].isdigit():
                num = int(s[i])
                largest = max(largest,num)

        for i in range(0,n):
            if s[i].isdigit():
                num = int(s[i])
                if num > S_largest and num != largest:
                    S_largest = num
        return -1 if S_largest == float("-inf") else S_largest

obj = Solution()
print(obj.secondHighest("dfa12321afd"))
print(obj.secondHighest("abc1111"))
    

        