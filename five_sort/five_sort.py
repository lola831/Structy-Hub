def five_sort(nums):
  l, r = 0, len(nums) - 1
  
  while l < r:
    if nums[r] == 5:
      r -= 1
    elif nums[l] == 5:
      nums[l], nums[r] = nums[r], nums[l]
    else:
      l += 1
  return nums
      