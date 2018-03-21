setwd("C:\\Users\\jiaju\\Documents\\Github\\mini_program")

source('fib_r.R')

Rcpp::sourceCpp('fibcpp.cpp')

system.time(fib_R(35))
system.time(fib_cpp_1(35))
