def get_neighboring_pair_easy_to_read(nums):
    if not isinstance(nums, list):
        raise TypeError
    if len(nums) == 0 or len(nums) == 1:
        return [] 
    res = []
    ptr1, ptr2 = 0, 1
    while ptr2 < len(nums):
        res.append((nums[ptr2], nums[ptr1]))
        ptr1, ptr2 = ptr1 + 1, ptr2 + 1
    return res

def get_neighboring_pair_fewest_lines(nums):
    if not isinstance(nums, list):
        raise TypeError
    if len(nums) == 0 or len(nums) == 1:
        return [] 
    return [(nums[i], nums[i - 1]) for i in range(1, len(nums))]

def get_neighboring_pair_iter(nums):
    if not isinstance(nums, list):
        raise TypeError
    if len(nums) == 0 or len(nums) == 1:
        return []
    iter1, iter2 = tee(nums)
    next(iter1, None)
    return list(zip(iter1, iter2))
