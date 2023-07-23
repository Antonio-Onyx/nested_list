#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

if __name__ == '__main__':
    
    nested_list = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lista = [name, score]
        nested_list.append(lista)
        
    #ordenamos la lista por orden alfabetico
    print(nested_list)    
    nested_list.sort()
    print(nested_list)
    
    val = []
    for inner in nested_list:
        val.append(inner[1])
        
    mini = min(val)
    for v in nested_list:
        if v[1] == mini:
            nested_list.remove(v)
            
    
    print(nested_list)        