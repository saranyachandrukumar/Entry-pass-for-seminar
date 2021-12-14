#Declaring the variable
list1 = []
#intitalised the variable
intpassnumber=1
while intpassnumber<=5:
    #allowed pass until 100 member
    if intpassnumber<=4:
#Entry pass details
        strwelcome="Welcome to DSIT Seminar"
        print(strwelcome.center(50))
        strname = input("Name of Participant:")
        strplace = input("place:")
        strcategory = input("Category" + "(S)" + "tudent" + "/(E)" + "mployee/" + "(U)nEmployee:")
        # Entry pass details
        print("-------------------------------------------------------------")
        strpasstitle = "Data science in tamil"
        print(strpasstitle.center(50))
        straddress = "Anna Salai,chennai"
        print(straddress.center(50))
        strsemtitle = "Seminar on Data Science"
        print(strsemtitle.center(50))
        strenterpass = "Entry pass"
        print(strenterpass.center(50))

        print("Pass No. :" + str(intpassnumber))
        print("Name     :" + strname)
        print("Place    :" + strplace)
        print("Category :" + strcategory)

        # Each entry pass details stored into the list
        list1.append(intpassnumber)
        list1.append(strname)
        list1.append(strplace)
        list1.append(strcategory)

        #next pass creation
        intpassnumber+=1
        print("------------------------------------------------------")
        #not allowed member
    elif intpassnumber>=5:
        #Entry pass details key in for not allowed member
        strnotallowed="Welcome to DSIT Seminar"
        print(strnotallowed.center(50))
        strnameofpartnot = input("Name of Participant:")
        strplacenot = input("place:")
        strcategorynot = input("Category" + "(S)" + "tudent" + "/(E)" + "mployee/" + "(U)nEmployee:")
        #Display houseful if more than member
        print("Houseful")
        #function for houseful report
        def result():
            strresult=input("Do you want Report <Y/N>:")
            return strresult
        # Report needed get the  user input as y
        x = next("Y" if value is None else value for value in (result(),))
        if (x=="Y") or (x=="y"):
            #report detail of allowed member count
            print("------------------------------------------------------")
            title="Data Science in Tamil"
            print(title.center(50))
            address = "Anna Salai,chennai"
            print(address.center(50))
            topic = "Seminar on Data Science"
            print(topic.center(50))
            report="R E P O R T"
            print(report.center(50))

            countlist=list(list1)
            #print the countlist
            countcategoryS=countlist.count("S")
            countcategoryE=countlist.count("E")
            countcategoryUE=countlist.count("UE")
            countcategoryTotal=countcategoryS+countcategoryE+countcategoryUE
            print("No of Participants:" + str(countcategoryTotal))
            print("No of students    :" + str(countcategoryS))
            print("No of Employees   :" + str(countcategoryE))
            print("No of Un-Employee  :" + str(countcategoryUE))
            print("--------------------------------------------")
            break
        else:
            #if user no need report
            print("No report found")
            break

