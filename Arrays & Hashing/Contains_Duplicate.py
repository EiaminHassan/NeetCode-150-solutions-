nums = [1, 2, 3, 3]
set_items = set()
def containsDuplicate(nums):
    for num in nums:
        if num in set_items:
            return True
        set_items.add(num)
    return False

ans = containsDuplicate(nums)
print(ans)

"""
Alternate solution (nlog(n) time complexity)
def containsDuplicate(nums):
    nums.sort()  # O(n log n) time
    for i in range(len(nums) - 1):  # O(n) time
        if nums[i] == nums[i + 1]:
            return True
    return False
"""
