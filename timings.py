import time
from search import bring_AI_bach
from examples import basslines

n = 1000

print('Running Bach tests...')

start_time = time.time()

for _ in xrange(n):
    for b in basslines:
        bring_AI_bach(b)

elapsed = time.time() - start_time
print('Total time elapsed: ' + str(elapsed) + ' seconds')
print('Total chorales voiced: ' + str(6 * n))
print('Average voicing time: ' + str((elapsed / (6 * n)) * 1000) + ' ms')
