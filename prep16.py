import math
def calculate_distance(x1,y1,x2,y2):
     x = x2-x1
     x*=x
     y=y2-y1
     y*=y
     total = x+ y
     total = math.sqrt(total)
     total = round(total,4)
     return total
