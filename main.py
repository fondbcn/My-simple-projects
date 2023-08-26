def trap(height):
        ml=0
        mr=0
        tr=0
        l=0
        r=len(height)-1
        while l<=r:   
            if ml<mr:
                tr+=ml-height[l] if ml-height[l]>=0 else 0
                ml=max(ml,height[l])
                l+=1
            else:
                tr+=mr-height[r] if mr-height[r]>=0 else 0
                mr=max(mr,height[r])
                r-=1
        return tr
        
print(trap([4,2,3]))