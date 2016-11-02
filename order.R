
#Use divide and conquer method to implement mergesort algorithm

mergesort <- function(unordered_array){
  
  #helper function to mergesort that merges two lists
  sort <- function(left, right){
    #A list that will contained sorted array 
    merged_result <- c()
    
    #Append to the sorted list until there are elements in both left and right
    while(length(left) > 0 && length(right) > 0)
    {

      #if right is greater than left, put the item in left to the result
      #After appending, remove the item from the left array
      #Similarly, if left is greater than right, put the item in right to the result
      #remove the item from the right array
      
      if(left[1] <= right[1]){
        merged_result <- c(merged_result, left[1])
        left <- left[-1]
      } 
      else{
        merged_result <- c(merged_result, right[1])
        right <- right[-1]
      }
    }
   
    #After the while loop is done, and there is still an element left in either left or right array
    #Put that last element into the result list
    
    if(length(left) > 0){
       merged_result <- c(merged_result, left)
    }
    if(length(right) > 0){
      merged_result <- c(merged_result, right)
    } 
    return(merged_result)
  }
  
  #Now, we divide the unsorted array into halves
  
  if(length(unordered_array) <= 1){
    return(unordered_array)
  } 
  else{
    middle <- length(unordered_array)/2
    left <- unordered_array[1:floor(middle)]
    right <- unordered_array[floor(middle+1):length(unordered_array)]
    
    # Recursively use the method to divide the array into halves
    left <- mergesort(left)
    right <- mergesort(right)
    
    # We order them by using our helper function sort
    if(left[length(left)] <= right[1])
    {
      c(left, right)
    } else
    {
      sort(left, right)
    }
  }
}


order_new <- function(unsorted_array){
  counter <- 1
  l <- list()
  for(item in mergesort(unsorted_array)){
    
    l[as.character(item)] <- counter
    counter = counter + 1
  }
  return(l)  
}

#Fixed duplicate issue

order_new <- function(unsorted_array){
  
  result <- match(unsorted_array, mergesort(unsorted_array))
  while(length(unique(result)) < length(unsorted_array)){
    for(i in 1:length(result)){
      if(duplicated(result)[i] == TRUE){
        result[i] <- result[i] + 1
      }
    }
  }
  return(result)
}
