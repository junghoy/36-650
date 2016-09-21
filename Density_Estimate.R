dd <- function(u, v) {
  a <- u[1] - v[1]
  b <- u[2] - v[2]
  return( a*a + b*b )
}

nn <- function(x, X, k) {
  u <- dd(x, X[1, ])
  w <- 1
  m <- nrow(X)
  for( i in 2:m ) {
    v <- dd(x, X[i,])
    if( v < u ) {
      u <- v
      w <- i
    }
  }
  return( c(as.vector(X[w, ]), u) )
}

density_estimate <- function(x, X, k) {
  y = nn(x, X, k)
  n = len(X)
  return( k/(2.0 * n * y[3]) )
}

doit1 <- function(n, q, k=1) {
  X <- read.table(n, header=FALSE)
  y = nn(q, X, k)    
  return( as.vector(y[1:2]) )
}

doit2 <- function(n, q, k=1) {
  X <- read.table(n, header=FALSE)
  return( density_estimate(q, X, K) )
}


## 1. Give an example in the code where the choice of names obscures the code's meaning

# function nn takes in arguments x and X. This use of both lower and upper case X could
# confuse the readers. Also, names of the variables do not suggest the meaning of it

## 2. Give an example in the code where the choice of names clarifies the code's meaning

# The function name density_estimate is a good example that clarifies the meaning of the function
# From this name, we can infer that that the function is designed to estimate the density

## 3. Explain briefly what this code is designed to do

# The function 'dd' takes in two points and calculate distance squared
# The function 'nn' finds the smallest distance between one defined point and a set of points
# The function 'density_estimator' returns the measurement of how dense around the point is
# The function 'doit1' returns the point that is the shortest to the point q, with k=1
# The function 'doit2' returns the density estimate with k being set to 1

## 4. Is the source code file well named? What would you suggest?

# Source code file is named as 'doit.r' This is a terrible name. We have no idea
# the function of this script. One suggestion would be Density_Estimate


## Rewritten code 


# Calculate distance squared between two points
distance_squared <- function(point_a, point_b) {
  x_distance <- point_a[1] - point_b[1]
  y_distance <- point_a[2] - point_b[2]
  return( x_distance^2 + y_distance^2 )
}

# Find the point that is shortest to a defined point x
nearest_point <- function(def_point, set_point, k) {
  distance_sq <- distance_squared(def_point, set_point[1, ])
  
  # arbitrary random variable to be used in for loop; we define as w
  w <- 1
  
  for( ii in 2:nrow(set_point) ) {
    temp_distance_sq <- distance_squared(def_point, set_point[ii,])
    if( temp_distance_sq < distance_sq ) {
      distance_sq <- temp_distance_sq
      w <- ii
    }
  }
  return( c(as.vector(set_point[w, ]), distance_sq) )
}

# Calculate density
density_estimate <- function(def_point, set_point, k) {
  y = nearest_point(def_point, set_point, k)
  n = len(set_point)
  return( k/(2.0 * n * y[3]) )
}

# After reading table, return nearest point but omit distance sqaured
nearest_point2 <- function(def_point, file, k=1) {
  X <- read.table(file, header=FALSE)
  y = nearest_point(def_point, X, k)    
  return( as.vector(y[1:2]) )
}

# After reading table, return density estimate with k set as 1
density_estimate2 <- function(def_point, file, k=1) {
  X <- read.table(file, header=FALSE)
  return( density_estimate(def_point, X, k) )
}



