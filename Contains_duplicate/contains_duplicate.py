def contains_duplicate(nums) :
    return len(nums) != len(set(nums))

if __name__ == "__main__" :
    nums1 = [1,2,3,3]   
    nums2 = [1,2,3,4]

    print(contains_duplicate(nums1))
    print(contains_duplicate(nums2))