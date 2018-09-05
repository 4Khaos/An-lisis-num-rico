install.packages("PolynomF")

require(PolynomF)
lagrange = function(x,y,a){
  n = length(x)
  if(a < min(x) || max(x) < a) stop("No está interpolando")
  X = matrix(rep(x, times=n), n, n, byrow=T)
  mN = a - X; diag(mN) = 1
  mD = X - t(X); diag(mD) = 1
  Lnk = apply(mN, 1, prod)/apply(mD, 2, prod)
  sum(y*Lnk)
}

t = c(100,200,300,400,500,600)
b = c(-160,-35,-4.2,9.0,16.9,21.3)

datx = t[1:6]; daty = b[1:6]
datx
daty
polyAjuste = poly.calc(datx,daty)
polyAjuste
plot(datx,daty, pch=19, cex=1, col = "red", asp=1) 
curve(polyAjuste,add=T)

lagrange(x[1:6],y[1:6], 450)
polyAjuste(450) #Evaluar la ecuacion en 450
