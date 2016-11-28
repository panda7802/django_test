

L = ['Adam', 'Lisa', 'Bart', 'Paul']
for t in enumerate(L):
    index = t[0]
    name = t[1]
    print index, '-', name

print "-------------"

print range(1, len(L) + 15, 2)
       
for index, name in zip(range(1, len(L) + 1), L):
    print index, '-', name    

print "-------------"


d = { 'Adam': 95, 'Lisa': 85, 'Bart': 74 }
print d.values()
print d.itervalues()
# [85, 95, 59]
# for v in d.keys():
#     print d[v]
#     
sSum = 0.0
for v in d.itervalues():
    sSum = sSum + v
print sSum / len(d)

sSum = 0.0
for v in d.values() :
    sSum = sSum + v
print sSum / len(d)

print "-------------"

print [x * (x + 1) for x in range(1, 10, 2)]

print "-------------"
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }

def generate_tr(name, score):
    if score < 60 :
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    else :
        return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)

tds = [generate_tr(name, score) for name, score in d.iteritems()]
print '<table border="1">'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'


print [100 * n1 + 10 * n2 + n3 for n1 in range(1, 3) for n2 in range(3) for n3 in range(3) if n1 == n3]
