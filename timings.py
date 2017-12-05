import time
from tests import basslines, bring_AI_bach

n = 1000

print('Running Bach tests...')

start_time = time.time()

for x in xrange(n):
    for b in basslines:
        bring_AI_bach(b)

end_time = time.time()
elapsed = end_time - start_time
print('Total time elapsed: ' + str(elapsed) + ' seconds')
print('Total chorales voiced: ' + str(6 * n))
print('Average voicing time: ' + str((elapsed / 60000.) * 1000) + ' ms')
