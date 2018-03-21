fib_R <- function(n){
  if(n==1||n==2) return(1)
  return(fib_R(n-1)+fib_R(n-2))
}