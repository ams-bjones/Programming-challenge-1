def multiplelist(mults,limit):
    answer = [mults]
    term = mults
    while (mults<limit):
        term = term + mults
        answer.append(term)
    return (answer)
    
    
