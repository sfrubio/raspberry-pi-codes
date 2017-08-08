from time import sleep, time

sum_time = 0

for i in range(5):
    sleep(2)
    start = time()
    print('Quick, the Enter key')
    input()
    reaction_time = time() - start
    sum_time = sum_time + reaction_time
    print('Attempt #', i, ': You took', reaction_time, 'seconds')
print('Average time:', sum_time / 5)
