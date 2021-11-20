def kbig(nums, k):
    if k < 2:
        return max(nums)

    else:
        numset = set(nums)
        for _ in range(k-1):
            maxnum = max(numset)
            if nums.count(maxnum) > 1:
                for _ in range(nums.count(maxnum) - 1):
                    nums.remove(maxnum)
            else:
                numset.remove(maxnum)
    return max(numset)
