# # start from 01 to 10
# # #------------------task 01----------------------------------->
# #my first project with paython
# #This is multiply lines 
# #contains variables ,comments,concatenation,some basics
# #------------------------------------------------------>
# #task02
# name = "omnia" #normal name
# myAge =  30     #camel Case
# my_Counrtry = "Egypt" #snake case
# print(name , myAge , my_Counrtry)
# #task03
# name ="osama" 
# age = "38"
# country = "Egypt"
# print("\"Name : " + name + "\"")
# print("\"Age : " + age + "\"")
# print("\"Country : " + country + "\"") 
# #task 04 
# print("Hello" + "," +" "+"My"+ " " + "Name is " + name + " "+ "And" + " " + "I am" +" "+ age + " " + "years old" + " " + "and" + " " + "I live in " + " " + country )
# # task 05
# print(type(name))
# print(type(age))
# print(type(country))

#------------------------
# start from #11 to #18
#----------------------------
#task 01
myName = "Omnia"
myAge = 28
mycountry = "Egypt"
print(f"""Hello '{myName}', How You Doing \ \""" Your Age Is "{myAge}" + And your Country Is : {mycountry}""")


#task 02
print(f"""Hello '{myName}', How You Doing \ \n \""" Your Age Is "{myAge}" + \nAnd your Country Is : {mycountry}""")


#task 03
name = 'Elzero'
print(name[0:1])
print(name[2])   
print(name[-1])


#task 04
print(name[1:4]) 
print(name[::2]) 
print(name[-2::-2])  


#task 05
name1 = "#@#@Elzero#@#@"
print(name1.strip("#@"))


# task 06
num = "9"
num_1 = "15"
num_2 = "130"
num_3 = "950"
num_4 = "1500"
print(num.zfill(4))
print(num_1.zfill(4))
print(num_2.zfill(4))
print(num_3.zfill(4))
print(num_4.zfill(4))


#task 08
name_one = "OSamA"
name_two = "osaMA"
print(name_one.swapcase())
print(name_two.swapcase())

#task 09
msg = "I Love Python And Although Love Elzero Web School"
print(msg.count("Love"))


#task 10
name = "Elzero"
print(name.index("z",0,5))

#task 11
msg1 = "I <3 Python And Although <3 Elzero Web School"
print(msg1.replace("<3","Love",1))


#task 12
msg2 = "I <3 Python And Although <3 Elzero Web School"
print(msg2.replace("<3","Love"))


#task 13
name = "Osama"
age = 38
country = "Egypt"
print("My Name %s , And My Age Is %d , And My Country Is %s" %(name,age,country)) #old_way
print("My Name {} , And My Age Is {:d} , And My Country Is {}".format (name,age,country))#new_way
# Needed Output Using f""
# My Name Is Osama, And My Age Is 38, And My Country Is Egypt