Ausgaben=[2200,2350,2600,2130,2190]
'''
1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
'''

#1
Extraausgaben=Ausgaben[1]-Ausgaben[0]
print(Extraausgaben)

#2
Gesamtausgaben=0
for i in range(0,4):
    Gesamtausgaben += Ausgaben[i]
print(Gesamtausgaben)

#3
for i in range(0,len(Ausgaben)):
    if Ausgaben[i]==2000:
        print('JA')
    else: print('Nein')

#4
Ausgaben.append(1980)
print(Ausgaben)

#5
Ausgaben[3]-= 200
print(Ausgaben)

'''
1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
'''

heros=['spider man','thor','hulk','iron man','captain america']

#1
print('Neue Aufgabe!!')
print(len(heros))

#2
heros.append('black panther')
print(heros)
#3
heros.remove('black panther')
pos=heros.index('hulk')+1
heros.insert(pos,'black panther')
print(heros)

#4
heros[1:3]=['doctor strange']
print(heros)

#5
heros.sort()
print(heros)

'''
Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
'''

maxnum=int(input('Maximale Nummer bitte eingeben: \n'))

List=[]
for i in range(1,maxnum):
    if not i % 2:
        List.append(i)
print(List)