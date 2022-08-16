from typing import List


class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i in range(len(nums)):
            if target - nums[i] in numMap:
                return [numMap.get(target - nums[i]),i]
            else:
                numMap[nums[i]] = i

         # print("123")

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([1,2,4,7],8))