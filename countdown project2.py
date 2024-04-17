# Count time down project '2'

import time
count_down = int(input('Enter the counting number:'))

for counts in range(count_down-1,-1,-1):     # (start:stop:step)
    time.sleep(1)
    print(counts)

print('Countdown suceessfully done!')