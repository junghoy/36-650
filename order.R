#!/usr/bin/env Rscript

library(testthat)

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

order=function(unsorted_array){
  return(match(unsorted_array, mergesort(unsorted_array)))
}

#Unit tests for the function


test_that('Negative number handling', {
  expect_equal(order(c(-3,-5,-7,-9)), c(4,3,2,1))
  expect_equal(order(c(3,-1,6,-8)), c(3,2,4,1))
  print("Test1 passed")
})

test_that('One element in the list', {
  expect_equal(order(51), c(1))
  print("Test2 passed")
})

test_that('Decimal numbers included', {
 expect_equal(order(c(3.5,2.5,1.5,0.5)), c(4,3,2,1)) 
 expect_equal(order(c(10,20,5,10.5)), c(2,4,1,3))
 print("Test3 passed")
})
