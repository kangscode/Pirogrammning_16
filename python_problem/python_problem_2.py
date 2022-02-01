
info = list()

def Menu1(st) :
    student = dict()
    student['name'] = st[0]
    student['midScore'] = st[1]
    student['finalScore'] = st[2]
    info.append(student)

def Menu2() :
    for i in info:
        if 'grade' in i:
            continue
        else:
            grade = (i['midScore'] + i['finalScore']) / 2
            if grade >= 90:
                i['grade'] = "A"
            elif grade >= 80:
                i['grade'] = "B"
            elif grade >= 70:
                i['grade'] = "C"
            else:
                i['grade'] = "D"

def Menu3() :
    print("----------------------------")
    print("name\tmid\tfinal\tgrade")
    print("----------------------------")
    for i in info:
        print("{0}\t{1}\t{2}\t{3}"
        .format(i['name'], i['midScore'], i['finalScore'], i['grade']))

def Menu4(name):
    for i in range(len(info)):
        if info[i]['name'] == name:
            del info[i]
            break    

#학생 정보를 저장할 변수 초기화
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")

while True :
    flag = False
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        st = list(input("Enter name mid-score final-score : ").split())
        if len(st) != 3:
            print("Num of data is not 3!")
            continue
        st[1] = float(st[1])
        st[2] = float(st[2])
        if st[1] < 0 or st[2] < 0 or st[1] != int(st[1]) or st[2] != int(st[2]):
            print("Score is not positive integer!")
            continue
        st[1] == int(st[1])
        st[2] == int(st[2])
        for i in info:
            if i.get('name') == st[0]:
                print("Already exist name!")
                flag = True
                break
        if flag:
            continue
        Menu1(st)
        
    elif choice == "2" :
        if len(info) == 0:
            print("no student data!")
            continue
        count = 0
        for i in info:
            if 'grade' in i:
                count += 1
        if len(info) == count:
            continue
        Menu2()         
        print("Grading to all students.")

    elif choice == "3" :
        if len(info) == 0:
            print("no student data!")
            continue
        count = 0
        for i in info:
            if 'grade' in i:
                count += 1
        if len(info) != count:
            print("There is a student who didn't get grade.")
            continue
        Menu3()

    elif choice == "4" :
        if len(info) == 0:
            print("no student data!")
            continue
        name = input("Enter the name to delete : ")
        for i in info:
            if i['name'] == name:
                Menu4(name)
                print(name, "student information is deleted.")
                flag = True
                break
        if flag:
            continue
        print("Not exist name!")

    elif choice == "5" :
        print("Exit Program!")
        exit(0)

    else :
        print("Wrong number. Choose again.")