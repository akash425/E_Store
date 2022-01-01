arr = [10,20,30,40,50,60,70,80,90,100]
n = 80

def fnd(arr,n):
    l =  0
    h = len(arr)-1
    mid = (l+h)//2
    
    while (l<h):
        mid = (l+h)//2
        if arr[mid]==n:
            return mid
        elif n<arr[mid]:
            h = mid-1
        elif n>arr[mid]:
            l = mid+1
            
        
        
        
        
        
    # n = 80//10
    # return n-1