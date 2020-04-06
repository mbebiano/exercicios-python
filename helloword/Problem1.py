def likes(names):
    like = []
    listlike=0
    c=0
    a = input('Digite os números de likes: ')
    if a==0:
        print('no one like this')
    else:
        while c < a:
            like.append(input('Set names likes in the list: '))
            c+=1
        listlike=len(like)
        if listlike
'''
a=0
likes = []
#likes(0)=input('Enter the names likes: ')
while a < 5:
    likes.append(input('Set names likes in the list: '))
    a+=1

a=0
while a < 5:
    print("Aluno {}: {}".format(a, likes[a]))
    a+=1

print(likes)
print(type(likes))'''