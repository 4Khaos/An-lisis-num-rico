install.packages("ggplot2")
library("ggplot2")
fsin <- function(x) {
  return(sin(x))
}
fcos <- function(x) {
  return(cos(x+pi/2))
}
x=seq(0 , 9, 0.1)
ysen=c()
for(i in 1:length(x)){
  ysen[i]=sin(x[i])
}

seg <- seq.int(0, 9, length.out = 9)
segcos <- seq.int(0, 9, length.out = 9)

fx <- vector(length = length(seg))
fxcos <- vector(length = length(segcos))

for (i in 1:length(seg)) {
  fx[i] <- fsin(seg[i])
}
for (i in 1:length(segcos)) {
  fxcos[i] <- fcos(segcos[i])
}

df <- data.frame(xend = seg, 
                 y = rep(0, 9), 
                 yend = fx, 
                 yend1 = c(fx[2:9], fx[9]), 
                 xend1 = c(seg[2:9], seg[9]),
                 xendcos = segcos, 
                 ycos = rep(0, 9), 
                 yendcos = fxcos, 
                 yend1cos = c(fxcos[2:9], fxcos[9]), 
                 xend1cos = c(segcos[2:9], segcos[9]))

ggplot(data = df) + 
  stat_function(fun = fsin, size = 1.05, alpha = 0.75, color='blue') + 
  stat_function(fun = fcos, size = 1.05, alpha = 0.75, color='red') + 
  geom_segment(aes(x=xend, y=y, xend=xend, yend=yend)) + 
  geom_ribbon(aes(x=xend, ymin=y, ymax=yend), fill = 'blue', alpha = 0.3) +
  
  geom_segment(aes(x=xendcos, y=ycos, xend=xendcos, yend=yendcos)) + 
  geom_ribbon(aes(x=xendcos, ymin=ycos, ymax=yendcos), fill = 'blue', alpha = 0.3) +
  xlim(c(0, 9))
n=10
aux=91/n
y1=c()
aux1=0
sum=0
for(i in 1:n){
  if(i==n){
    y1[i]=abs(ysen[i*aux]+0)
  }else{
    y1[i]=abs(ysen[i*aux]+ysen[(i+1)*aux])
  }
  aux1=((y1[i]/2)*aux)*0.07
  print(aux1)
  sum=(sum+aux1)
}
print(sum)