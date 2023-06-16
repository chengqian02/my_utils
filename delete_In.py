

import re


text = '''
In [240]: from random import normalvariate

In [241]: N = 1000000

In [242]: %timeit samples = [normalvariate(0, 1) for _ in range(N)]


In [243]: %timeit np.random.normal(size=N)
'''


text = re.sub(r'In \[\d+\]:', "", text)
print(text)