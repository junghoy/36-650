
library(testthat)
library(testit)


#Make_kernel_smoother function

make_kernel_smoother <- function(xs,ys,bandwidth, kernel){
  
  observed_x <- xs
  observed_y <- ys
  bandwid <- bandwidth

  #Make assertions that bandwidth > 0 and dimensions of x and y are the same
  
  assert_that(bandwidth >= 0)
  assert_that(length(observed_x) == length(observed_y))
  
  #write closure function
  
  function(input){
    
    #create an array that is the size of the input 
    result <- rep(NA, length(input))
    
    #iterate through input values 
    for(i in 1:length(input)){
      
      weight <- rep(NA, length(observed_x))
      #iterate through each observation point to calculate weight
      for(j in 1:length(observed_x)){
      
        weight[j] = kernel((observed_x[j] - input[i])/bandwid)

      }
      result[i] <- weight %*% observed_y / sum(observed_y)  
    }
    return(result)
  }
}

#Smoother_factory function
#Basically the same as make_kernel_smoother, but adds one more closure function

smoother_factory <- function(xs, ys, kernel){
  
  observed_x <- xs
  observed_y <- ys
  kernel <- kernel
  
  function(bandwidth){
    
    #Make assertions that bandwidth > 0 and dimensions of x and y are the same
    
    assert_that(bandwidth >= 0)
    assert_that(length(observed_x) == length(observed_y))
    
    function(input){
      
      result <- rep(NA, length(input))
      for(i in 1:length(input)){
        
        weight <- rep(NA, length(observed_x))
        
        for(j in 1:length(observed_x)){
          
          weight[j] = kernel((observed_x[j] - input[i])/bandwidth)
        }
        result[i] <- weight %*% observed_y / sum(observed_y)  
      }
      return(result)
    }  
  }
}

#Gaussian Kernel

gaussian <- function(s){
  return((1/sqrt(2*pi)) * exp(-s^2/2))
}

#Boxcar Kernel

boxcar <- function(s){
  if(abs(s) <= 1){
    return(1/2)
  }
  else{
    return(0)
  }
}


#Unit tests for the function

test_that('Test Smoother_factory equals make_kernel_smoother', {
  xs <- c(1,3,5,7)
  ys <- c(2,4,6,8)
  
  factory <- smoother_factory(xs,ys,dnorm)
  k1 <- factory(4)
  
  k2 <- make_kernel_smoother(xs, ys, 4, dnorm)
  
  expect_equal(k1(1.2), k2(1.2))
  print("Test1 passed")
})


test_that('Handles more than one element', {
  xs <- c(1,3,5,7)
  ys <- c(2,4,6,8)
  
  factory <- smoother_factory(xs,ys,dnorm)
  k1 <- factory(4)
  test_vector <- c(1.5,2.5,3.5,4.5)
  
  k2 <- make_kernel_smoother(xs, ys, 4, dnorm)
  expect_that(length(k1(test_vector)), equals(4))
  expect_that(length(k2(test_vector)), equals(4))
  print("Test2 passed")
  
})


test_that('Gaussian kernel test', {
  xs <- c(1:10)
  ys <- c(2:11)
  
  factory <- smoother_factory(xs,ys,gaussian)
  k1 <- factory(1)
  
  k2 <- make_kernel_smoother(xs, ys, 1, gaussian)

  expect_equal(k1(1:10), k2(1:10))
  print("Test3 passed")
    
})

test_that('Boxcar kernel test', {
  xs <- c(1:10)
  ys <- c(2:11)
  
  factory <- smoother_factory(xs,ys,boxcar)
  k1 <- factory(1)
  
  k2 <- make_kernel_smoother(xs, ys, 1, boxcar)
  
  expect_equal(k1(1:10), k2(1:10))
  print("Test4 passed")
  
})

