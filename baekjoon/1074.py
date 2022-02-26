import sys

def find_section(now_width):
    global section, r, c, count
    if now_width == 1:
        print(count)
        return
    
    cent = now_width // 2

    if r < cent and c < cent:
        section = 1
    if r < cent and c >= cent:
        count += cent * cent
        c -= cent
        section = 4
    if r >= cent and c < cent:
        count += cent * cent * 2
        r -= cent
        section = 2
    if r >= cent and c >= cent:
        count += cent * cent * 3
        r -= cent
        c -= cent
        section = 3
    
    find_section(cent)

# 2^n * 2^n크기, r행, c열
n, r, c = map(int, sys.stdin.readline().split())

count = 0
section = -1

find_section(2 ** n)