# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):
    if len(list_to_remove_elements)>=6:
        del list_to_remove_elements[0]
        del list_to_remove_elements[3]
        del list_to_remove_elements[3]
    elif len(list_to_remove_elements)>=5:
        del list_to_remove_elements[0]
        del list_to_remove_elements[3]
    elif len(list_to_remove_elements)<=4:
        del list_to_remove_elements[0]
    print(list_to_remove_elements)


def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0,'Pink')
    list_to_add_elements.append('Yellow')
    print(list_to_add_elements)


def is_empty(list_to_check):
    if len(list_to_check)==0:
        print('La lista está vacía')
    else:
        print('No esta vacia')


def check_lists(list_to_compare1, list_to_compare2):
    if list_to_compare1[2] in list_to_compare2[2]:
        return True
    else:
        return False


def list_of_lists(list_of_lists_to_modify):
    list1=list_of_lists_to_modify[0][0:2]
    list2=list_of_lists_to_modify[1][1:4]
    list3=list_of_lists_to_modify[2][-2:]
    print([list1, list2, list3])
