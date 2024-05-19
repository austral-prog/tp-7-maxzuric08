def enumerate_list(list):
    new_list=[]
    a=0
    for i in list:
        if i!="":
            new_indice=f'{a}. {i}'
            a+=1
            new_list.append(new_indice)
    return new_list


def enumerate_backwards(list):
    new_list=[]
    a=0
    for i in list:
        if i!="":
            new_indice=f'{a}. {i[-1::-1]}'
            a+=1
            new_list.append(new_indice)
    return new_list
