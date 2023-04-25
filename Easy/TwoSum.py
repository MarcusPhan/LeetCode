from typing import List

#O(n^2) solution. Not very efficient
def twoSum(nums: List[int], target: int) -> List[int]:
    for index1 in range(0, len(nums)):
            for index2 in range(1, len(nums)):
                if index1 == index2:
                    continue

                if (nums[index1] + nums[index2]) == target:
                    a = index1
                    b = index2
    result=[]
    result.append(a)
    result.append(b)
    return result