#  finding the intersection of two arrays.
def intersection(nums1:list[int],nums2:list[int]):
    output = []
    for i in nums1:
        if (i in nums2 and i not in output):
            output.append(i)
    return output;        
print(intersection(nums1=[33,44,1,50,77,99],nums2=[99,50,1,678,77]))