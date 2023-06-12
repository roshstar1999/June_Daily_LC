class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:return []
        arr=[]
        a=nums[0]
        b=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==b+1:
                b=nums[i]
            else:
                if a==b:
                    arr.append(str(a))
                else:
                    arr.append(str(a)+"->"+str(b))
                a=nums[i]
                b=nums[i]
        
        if a==b:
            arr.append(str(a))
        else:
            arr.append(str(a)+"->"+str(b))
                
        if not arr and len(nums)==1:
            arr.append(a)
        return arr
