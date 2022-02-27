def solution(s, n):
    result = ''

    for c in s:
        if not ('a' <= c <= 'z' or 'A' <= c <= 'Z'):
            result += c
            continue

        value = ord(c) + n
        if 'a' <= c <= 'z':
            value -= ord('a')
            result += chr(value % 26 + ord('a'))
        elif 'A' <= c <= 'Z':
            value -= ord('A')
            result += chr(value % 26 + ord('A'))

    return result