import os
# task 1
print(os.listdir('./PZ_11'))
# task 2
try:
    os.mkdir('./test')
    os.mkdir('./test/test1')
except:
    pass

# task 3
os.rename('./PZ_6/1.txt', './test/1.txt')
os.rename('./PZ_6/2.txt', './test/2.txt')
os.rename('./PZ_7/3.txt', './test/test1/4.txt')

# task 4
path = os.listdir('./test')
for i in path:
    print((os.path.getsize(f'./test/{i}')), 'bytes')

# task 5
path = os.listdir('./PZ_11')
path = min(path, key=len)

print(os.path.basename(f'./PZ_11/{path}'))

# task 6-*-

os.startfile('Reports\Report_17.pdf')

# task 7
open('PZ_17/123.txt', 'w')
os.remove('PZ_17/123.txt')
