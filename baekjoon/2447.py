n = int(input())

def recursion(n):
    if n == 3:
        return '***\n* *\n***'
    star = recursion(n // 3)
    
    new_star = ''
    star_split = star.split('\n')
    for e in star_split:
        new_star += e * 3 + '\n'
    
    center_star = ''
    for e in star_split:
        center_star += e + ' ' * len(e) + e + '\n'
        
    new_star = new_star + center_star + new_star
    
    return new_star.strip()

print(recursion(n))