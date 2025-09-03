    
def Solution1(nums1, nums2): 
    l = sorted(nums1+nums2)
        
    if len(l)%2 == 0:
        return (l[len(l)//2-1] + l[len(l)//2]) / 2
    else:
        return l[len(l)//2]


nums1 = [1,2,3]
nums2 = [1,5,7]
ans = 2.5
val_returned = Solution1(nums1, nums2)
print(f"Solution 1: Correct? - {ans == val_returned}")


    
