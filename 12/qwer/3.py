import os

print(os.listdir('../qwe'))

try:

    os.mkdir('../../test')
    os.mkdir('../../test/test1')
except:
    pass

# os.rename('../qwe/1.txt', '../test/1.txt')
# os.rename('../qwe/negri.py', '../test/negri.py')
# os.rename('../qwert/123.txt', '../test/test1/1234.txt')

os.getsize('../test')