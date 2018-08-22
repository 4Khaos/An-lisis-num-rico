f <- function(x)
{
  log( x + 2 )
}
g <- function(x)
{
  sin(x)
}
E = 0.0000001

x0 = 0
x1 = 300


if (f(x1)*f(x0)<0)
{
  x2 = x1 - (( f(x1)/( f(x1) - f(x0) ) )*(x1-x0))
  if (f(x2)*f(x1) < 0)
  {
    x2 = x1
    x1 = x0
  } else
  {
    x2 = x1
  }
}

