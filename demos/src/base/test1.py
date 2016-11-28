from math import sqrt

score = 15
if score < 60 :
    print 'passed'
    print 'in pass'
elif score < 80 :
    print 'not good'
else :
    print 'good'
    
L = [75, 92, 59, 68]

sum1 = 0.0
for x in L:
    sum1 = sum1 + x
print sum1 / 4.0
    
print 'over'

s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s:
    print x[0] + ':', x[1]

print "--------------"
def tSqrt(i=9):
    print "i = ", i
    if(i <= 0) :
        return 0
    res = sqrt(i)
    return res, -res

res = tSqrt()
if len(res) < 2 :
    print  "input error : " , res
else :
    print res[0], res[1]
   
print "--------------" 

    
