def solution(s):
    _list = map(int, s.split())
    return str(min(_list)) + " " + str(max(_list))