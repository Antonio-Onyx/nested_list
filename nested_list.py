#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

if __name__ == '__main__':
    
    nested_list = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lista = [name, score]
        nested_list.append(lista)
        
    #ordenamos la lista por orden alfabetico
    #print(nested_list)    
    nested_list.sort()
    #print(nested_list)
    
    score = []
    for inner in nested_list:
        score.append(inner[1])
        
    score.sort()
    #print(score)
    cant = score.count(min(score))
    #print(cant)
    
    first_min = min(score)
    #score.remove(score[0])
    #rint(score)
    
    new_score = [s for s in score if s != first_min]
    
    #print(new_score)
    
    for v in nested_list:
        if new_score[0] in v:
            print(v[0])
    