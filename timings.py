import time
import sys
import os
from tqdm import tqdm
from search import bring_AI_bach
from hill import hill_climb
from examples import basslines

# Disable printing
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore printing
def enablePrint():
    sys.stdout = sys.__stdout__

n = 1000

print('Running Bach tests...')

start_time = time.time()

for _ in tqdm(xrange(n)):
    for b in basslines:
        bring_AI_bach(b)

elapsed = time.time() - start_time
print('Total time elapsed: ' + str(elapsed) + ' seconds')
print('Total chorales voiced: ' + str(6 * n))
print('Average voicing time: ' + str((elapsed / (6 * n)) * 1000) + ' ms')

n = 100
reps = 1000

print('Running hill-climbing tests...')

start_time = time.time()

blockPrint()
for x in tqdm(xrange(n)):
    for bass in basslines:
        hill_climb(bass, reps)
enablePrint()

elapsed = time.time() - start_time
print('Total time elapsed: ' + str(elapsed) + 'seconds')
print('Total hill-climbing runs: ' + str(6 * n))
print('Total voicing attempts: ' + str(6 * n * reps))
print('Average hill-climbing time: ' + str((elapsed / (6 * n)) * 1000) + ' ms')
print('Average voicing attempt time: ' +
      str((elapsed / (6 * n * reps)) * 1000) + ' ms')
