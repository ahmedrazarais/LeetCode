def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    # farthest_reachable keeps track of the farthest index reachable from the current position
    farthest_reachable = 0

    for i in range(len(nums)):
      # If the current position is less than farthest reachable, we can move there
      if i > farthest_reachable:
        return False

      # Update farthest_reachable based on current index and jump value
      farthest_reachable = max(farthest_reachable, i + nums[i])

    # If we reach the end of the array (last index), return True
    return True

print(canJump([1,2,3,4]))