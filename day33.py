class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        ans = []

        for val in nums:
            for char in str(val):
                ans.append(int(char))

        return ans


# USER INPUT
nums = list(map(int, input("Enter numbers separated by space: ").split()))

# OBJECT CREATION
obj = Solution()

# FUNCTION CALL
result = obj.separateDigits(nums)

# OUTPUT
print("Separated Digits:", result)