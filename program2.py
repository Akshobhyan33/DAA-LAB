def binary_search(arr,low,high,search):
    while(low<=high):
        mid = low+(high-low)//2
        if(arr[mid]==search):
            return mid
        elif(arr[mid]<search):
            low=mid+1
        elif(arr[mid]>search):
            high=mid-1
    return -1

numbers=[12,23,45,54,56,57,78]
req=56
index=binary_search(numbers,0,len(numbers)-1,req)     
if(index==-1):
    print("element not found")
else:
    print("element found at index:",index)       
