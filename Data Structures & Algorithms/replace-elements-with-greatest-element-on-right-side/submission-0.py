class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        for i in range(0, len(arr)):
            greatest_element = 0
            for j in range(i+1, len(arr)):
                if arr[j] > greatest_element:
                    greatest_element = arr[j]
            
            arr[i] = greatest_element

        arr[len(arr) - 1] = -1

        return arr