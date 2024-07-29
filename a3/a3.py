"""
Ella Lewis 2230313
420-LCU Computer Programming, Section # S. Hilal, instructor
Assignment 3
"""
from matplotlib import pyplot as plt

fp = open('NaturalDisasters.txt')
Types= {}
Years= {}
n=0
for line in fp:
    line=line.strip('\n')
    record=line.split(",")
    print(record)
    n+=1
    Types[record[0]]=record[1]
    Years[record[0]]=record[2]
fp.close() 

menu= """
1- How many records are there in the data file? Display all complete records in tabular format.
2- How many different types of natural disasters are reported? Print a numbered list of all types.
3- What type of Natural Disaster has been reported the most and how many times?
4- What type of Natural Disaster has been reported the least and how many times?
5- Display all the titles of the natural disasters of a requested type.
6- Display all the titles of the natural disasters of a requested year. 
7- List all the years where 2 or more natural disasters were reported.
8- List all types of natural disasters that have occurred more than 3 times.
9- List the top 5 types of natural disasters that were reported
10- Display a pie chart plot to show the distribution of titles among the top 8 types of natural disasters.
11- Exit
"""
#List for types of disasters
L=[]
for i in Types:
    if Types[i] in L:
        n+=1
    else:
        L.append(Types[i])
        dictionary= dict.fromkeys(L,0)
        for i in Types:
            if Types[i] in dictionary.keys():
                dictionary[Types[i]]+=1

#list for years occured
Y=[]
n=0
for i in Years:
    if Years[i] in Y:
        n+=1
    else:
        Y.append(Years[i])
        d=dict.fromkeys(Y,0)
        for i in Years:
            if Years[i] in d.keys():
                d[Years[i]]+=1

        
while True:
    print(menu)
    option=int(input("Enter your choice:"))
    if option==1:
        for i in Types:
            print("{:40s}{:15s}{:4s}".format(i, Types[i], Years[i]))
    if option==2:
        L=[]
        n=0
        for i in Types:
            if Types[i] in L:
                n+=1
                continue
            else:
                L.append(Types[i])
        n=1
        for i in L:
            print(n,'-',i)
            n+=1
        print("There are", n-1, "types of natural disaster")
    if option==3:
        common=max(dictionary,key=dictionary.get)
        print(common,'has been reported the most with',dictionary.get(common),'times')
    if option==4:
        least=min(dictionary,key=dictionary.get)
        print(least,'has been reported the least with', dictionary.get(least),'times')
    if option==5:
        typ=input("Enter a type:")
        if typ not in L:
            print("error")
            continue
        else:
            print("{:40s}{:4s}".format("Name", "Year"))
            for i in Types:
                if Types[i]==typ:
                    print("{:40s}{:4s}".format(i,Years[i]))
    if option==6:
        yrs=input("Enter a year:")
        for i in Years:
            if Years[i]==yrs:
                print(i)
    if option==7:
        print("{:4s}  {:s}".format("Year", "Number"))
        for key, value in d.items():
            if value>=2:
                print("{:4s}  {:s}".format(key, str(value)))
    if option==8:
        print("{:4s}  {:s}".format("Year", "Number"))
        for key, value in d.items():
            if value>=3:
                print("{:4s}  {:s}".format(key, str(value)))
    if option==9:
        sort=sorted(dictionary,key=dictionary.get)
        print(sort[:4:-1])
    if option==10:
        sort=sorted(dictionary,key=dictionary.get)
        top8=sort[:1:-1]
        plt.title("Top 8 types of natural disaster")
        plt_types=[]
        plt_number=[]
        for i in top8:
            plt_types.append(i)
            plt_number.append(Types[i])
        plt.pie(plt_number, labels= plt_types)
    if option==11:
        break
