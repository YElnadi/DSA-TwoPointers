def solution(s,t):
    count = 0
    for char in range(len(s)):
        if s[char].isdigit():
            new_string= s[0:char] + s[char+1:]
            if new_string < t:
                count += 1
    
    for char in range(len(t)):
        if t[char].isdigit():
            new_t= t[0:char] + t[char+1:]
            if s < new_t:
                count +=1

    return count



print(solution( "ab12c", "1zz456"))