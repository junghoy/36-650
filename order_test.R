
#!/usr/bin/env Rscript

source("order.r")

library(testthat)

#Unit tests for the function

test_that('Negative number handling', {
  expect_equal(order_new(c(-3,-5,-7,-9)), c(4,3,2,1))
  expect_equal(order_new(c(3,-1,6,-8)), c(3,2,4,1))
  print("Test1 passed")
})

test_that('One element in the list', {
  expect_equal(order_new(51), c(1))
  print("Test2 passed")
})

test_that('Decimal numbers included', {
  expect_equal(order_new(c(3.5,2.5,1.5,0.5)), c(4,3,2,1)) 
  expect_equal(order_new(c(10,20,5,10.5)), c(2,4,1,3))
  print("Test3 passed")
})

test_that('Duplicate values', {
  expect_equal(order_new(c(3,5,5,5,1,2)), c(3,4,5,6,1,2))
  expect_equal(order_new(c(10,9,8,1,1,1)), c(6,5,4,1,2,3))  
  print("Test4 passed")
})
