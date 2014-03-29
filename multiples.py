def multiplelist(mults,limit):
    answer = [mults]
    term = mults
    while (term < (limit-mults)):
        term = term + mults
        answer.append(term)
    return (answer)
    
def totalList(inlist):
    answer = 0
    for something in inlist:
        answer = answer + something
    return (answer)
    
top = 4000000
print (totalList(multiplelist(5, top)) + totalList(multiplelist(11,top)))
    
