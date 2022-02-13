n = int(input())

start = 666
count = 1
while True:
    if count == n:
        print(start)
        break
    start += 1
    
    if '666' in str(start):
        count += 1