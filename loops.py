def index_of_by_index(word, list, index):
    for i in range(len(list)):
        if i>=index:
            if list[i]==word:
                return i
    new_list=list[index:]
    if word not in new_list:
        return -1    


def index_of_empty(list):
    for i in range(len(list)):
        a=0
        if list[i]=="" and a<1:
            a+=1
            return i
    if "" not in list:
        return -1


def index_of(word, list):
    for i in range(len(list)):
        if list[i]==word:
            return i
    if word not in list:
        return -1
    


def put(word, list):
    for i in range(len(list)):
        a=0
        if list[i]=="" and a<1:
            list[i]=word
            a+=1
            return i
    if "" not in list:
        return -1
    

def remove(word, list):
    if word in list:
        a=0
        for i in range(len(list)):
            if list[i]==word:
                list[i]=""
                a+=1
        return a
    else:
        return 0
