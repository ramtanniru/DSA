# Statement: Decrypt the ticket by removing 'G' and 'EF' form the ticket. 
# Note: remove E only if F follows it 
# input: "432EF12G6FE"
# output: "432126F"

def ticketDecryption(tkt):
    res = ""
    i = 0
    while i<len(tkt):
        if tkt[i]!='G' and tkt[i]!="E":
            res += tkt[i]
        if tkt[i]=='E' and i+1<len(tkt) and tkt[i+1]=="F":
            i += 1
        i += 1
    return res
if __name__=="__main__":
    tkt = input()
    print(ticketDecryption(tkt))