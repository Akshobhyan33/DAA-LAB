def linear_search(arr,search):
  
 for i in range(len(arr)):
    if arr[i]==search:
     print("search element is found in index",i)

list=[1,2,3,4,5,6,7,8,9,10]
req = 6
linear_search(list,req)