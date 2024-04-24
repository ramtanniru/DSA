def winner(jack,jill):
    jk,ji = 0,0
    flag = True
    for i in range(len(jack)): 
        if flag:
            ele = max(jack)
            jk += ele
            jill[jack.index(ele)] = 0
            jack[jack.index(ele)] = 0
            flag = False
        else:
            ele = max(jill)
            ji += ele
            jack[jill.index(ele)] = 0
            jill[jill.index(ele)] = 0
            flag = True
    if jk>ji:
        return "Jack won"
    elif ji>jk:
        return "Jill won"
    return "It's a tie"

if __name__=='__main__':
    jack = [int(i) for i in input().split()]
    jill = [int(i) for i in input().split()]
    print(winner(jack,jill))