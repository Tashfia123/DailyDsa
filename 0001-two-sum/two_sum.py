# two_sum.py — LeetCode 1 (Two Sum), brute force

class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))  
    print(s.twoSum([3, 2, 4], 6))        
    print(s.twoSum([3, 3], 6))           