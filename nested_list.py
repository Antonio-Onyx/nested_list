#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

if __name__ == '__main__':
    
    nested_list = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lista = [name, score]
        nested_list.append(lista)
        
    print(nested_list)    
    nested_list.sort()
    print(nested_list)