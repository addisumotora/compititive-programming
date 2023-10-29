#User function Template for python3

class Solution: 
    def select(self, arr, i):
        mnItem = i
            
        for j in range(i+1, n):
            
            if arr[mnItem] > arr[j]:
                
                mnItem = j
        
        arr[i], arr[mnItem] = arr[mnItem], arr[i]
        
        return arr
        
    def selectionSort(self, arr,n):
        for i in range(n):
            arr = self.select(arr,i)
        return arr
            
            
            
