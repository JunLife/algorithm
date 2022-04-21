def palindromeIndex(s):
    s_len = len(s)
    
    st = 0
    ed = s_len - 1
    while st <= ed:
        if s[st] == s[ed]:
            st += 1
            ed -= 1
            continue
        
        sub_st = st + 1
        sub_ed = ed
        
        while sub_st <= sub_ed:
            if s[sub_st] == s[sub_ed]:
                sub_st += 1
                sub_ed -= 1
                continue
            
            return ed
        return st
    return -1