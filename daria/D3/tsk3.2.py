import numpy as np

spiral = np.zeros((100,100), dtype = int)
m = (100-1)//2
spiral[m, m] = 1

n = 361527
mycoords = [(0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1) ,(1,0), (1,1) ]

#1st layer creating 
def firstLayers(m):
  for offset_ex in mycoords:
    idx = [x + y for x, y in zip([m,m], offset_ex)]     
    for offset_in in mycoords:
      idx2 = [x + y for x, y in zip(idx, offset_in)]
      spiral[idx[0],idx[1]] += spiral[idx2[0], idx2[1]]  
  return spiral

def main(firstLayers):
  r = 1
  c = 2
  layer = 3
  while True:
    while r >= - r - layer - (layer-1) and spiral[m+r,m+c] <= n:
      for offset_in in mycoords:
        idx2 = [x + y for x, y in zip([m+r,m+c], offset_in)]
        spiral[m+r,m+c] += spiral[idx2[0], idx2[1]]
      r -= 1
      
  
    r = - (layer - 1)
    c = layer - 2
    while c >= -(layer - 1) and spiral[m+r,m+c] <= n:
      for offset_in in mycoords:
        idx2 = [x + y for x, y in zip([m+r,m+c], offset_in)]
        spiral[m+r,m+c] += spiral[idx2[0], idx2[1]]
        if spiral[m+r,m+c] > n:
          return spiral[m+r,m+c] 
      c -= 1
  
    r = - (layer - 2)
    c = - (layer - 1)
    while r <= layer - 1 and spiral[m+r,m+c] <= n:
      for offset_in in mycoords:
        idx2 = [x + y for x, y in zip([m+r,m+c], offset_in)]
        spiral[m+r,m+c] += spiral[idx2[0], idx2[1]]
      r += 1
    
    r = layer - 1
    c = -(layer - 2)
    while c <= layer:
      for offset_in in mycoords:
        idx2 = [x + y for x, y in zip([m+r,m+c], offset_in)]
        spiral[m+r,m+c] += spiral[idx2[0], idx2[1]] 
      c += 1
  
    r -= 1
    c -= 1
    layer += 1
  
  
firstLayers(m)
print("THE RESULT IS", main(firstLayers))
