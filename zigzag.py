import time, sys
indent =' '
asterisk = '*' * 8

def pattern_to_repeat():
    for i in range(20, -20, -1):
        if i >= 0 :
            print(indent * abs(20 - i) + asterisk)
            time.sleep(0.1)
        else: 
            print(indent * abs(20 + i) + asterisk)
            time.sleep(0.1)

try:
    while True: 
        pattern_to_repeat()
except KeyboardInterrupt:
    sys.exit()