x, y, w, h = map(int, input().split()) # 내 위치, 직사각형의 꼭짓점

print(min(x, y, w - x, h - y))