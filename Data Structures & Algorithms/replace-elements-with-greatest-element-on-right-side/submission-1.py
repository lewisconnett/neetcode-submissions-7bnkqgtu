class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        greatest_num = -1

        for i in range(len(arr)-1, -1, -1):
            val = arr[i]
            arr[i] = greatest_num
            if val > greatest_num:
                greatest_num = val
        
        return arr