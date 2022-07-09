people = {'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}
favColor = input("new favorite clour of lisa")

people['Lisa'] = favColor
keyList=[]
del people['Jenny']
print(people)
list1=[]
list1.extend(people)
list1.sort()
for key in list1:
    print(key,':',people[key])



