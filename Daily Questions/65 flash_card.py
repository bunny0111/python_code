'''
Input:- 
'Who wrote Romeo and Juliet?'
'Shakespear'
Output:-
{'Question': 'Who wrote Romeo and Juliet?', 'Answer': 'Shakespeare'}
'''
def flash_card(question, answer):
    return{'Question':question, 'Answer':answer}

q = input("Enter question=")
a = input("Enter Answer=")
print(flash_card(q,a))