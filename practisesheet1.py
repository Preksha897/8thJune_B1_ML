  


#Asignment sheet first by lakshita ML_8 june batch 1

#Answer 2
print(5**9)
print(3//2)
print(7//3)
print(7/3)
print(6==6)

a = 20
a += 30
a %= 3;
print(a)
print(True*False)
print(True&False)
print(True and False)
print(((6>3) and (7<4) or (18==3)) and (9>3))
print(True is False)
print('False' in 'False')
print(((True == False) or (False > True)) and (False <= True))

###################################################################


#Answer 3

s1 = "Nice to have it"
s2 = "here"
print(s1,s2)
########################

#Answer 4
a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
[1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
[1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
a[3][1][2][0]

##############################

#Answer 5
s1 = "Nice to have it"
s2 = "here"
print(s1,s2) 
a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a)
a
a.insert(0,['Nice to have it','here'])
a += 'Nice to have it','here'

###################################

#Answer 6

s1 = "Nice to have it"
s2 = "here"
print(s1,s2)

##################################

#Answer 7


def check_pangram(arg):
	if len(set('ajbxjabxshccsjhcjcjccjs') - set(arg.lower())) == 0:
		return True
	return False
user_str = input("enter a string yto check for program")
if(check_pangram(user_str)):
    print("it is a pangram string")
else:
    print("it is a not a pangram string")


#################################

# Answer 8
a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)

#################################

#Answer 9

phrase = input("Input words: ")

phrase_list = phrase.split(",")
phrase_list.sort()
print((', ').join(phrase_list))

##########################################

# Answer 10

d = {'Student': ['Rahul', 'Kishore','Vidhya', 'Raakhi'],'Marks':[57,87,67,79]}
d['Marks']
max(d['Marks'])
print(d['Student'][d['Marks'].index(max(d['Marks']))])
