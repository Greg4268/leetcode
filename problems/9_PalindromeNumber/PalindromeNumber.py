
# Solution 1 
class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or x % 10 == 0 and x != 0:
            return False
        
        x = str(x)

        for i in range(len(x)):
            j = len(x) - 1
            if x[i] != x[j]:
                return False
            j -= 1
        return True


x = 12331
y = 123454321
z = 12
solution = Solution()

print(solution.isPalindrome(x))
print(solution.isPalindrome(y))
print(solution.isPalindrome(z))