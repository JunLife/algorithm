import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    for _ in range(n):
        wear_map = dict()
        
        m = int(sys.stdin.readline())
        for _ in range(m):
            wear, position = sys.stdin.readline().strip().split()
            if not position in wear_map:
                wear_map[position] = set()
                
            wear_map[position].add(wear)

        result = 1
        for key, value in wear_map.items():
            result *= len(value) + 1
        print(result - 1)