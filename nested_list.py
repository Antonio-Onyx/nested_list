#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

if __name__ == '__main__':
    
    nested_list = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lista = [name, score]
        nested_list.append(lista)
        
    
    #to go through every element in this list, use a nested for loop.
    score = []
    for inner in nested_list:
        score.append(inner[1])
        
    score.remove(min(score))
    pos = score.count(score[0])
    score.sort()
    
    
    names = []
    for iiner in nested_list:
        if score[pos-1] in iiner:
            print(iiner)
            names.append(iiner)
            
    names.sort()

    for i in names:
        print(i[0])        