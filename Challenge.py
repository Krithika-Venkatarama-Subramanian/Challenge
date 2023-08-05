import sys
##main class obtains the arguments and passes it to initialize where the length of the argument is analysed
##with the length of the argument (2 to 4) it is sent to the respective classes
##when the length is 1 or more than 4 then it displays the usage message and ends the program
class main:
    def __init__(self):
        if (len(sys.argv)==1 or len(sys.argv)>4):
            print('[Usage:] python my_competition.py <result file>')
        elif (len(sys.argv)==2):
            competition.display_result('results.txt')
        elif (len(sys.argv)==3):
            competition.display_result('results.txt')
            challenge.display_error_challenge('challenges.txt')
            sys.stdout.write('\nReport competition_report.txt generated!\n')
        elif(len(sys.argv)==4):
            competition.display_result('results.txt')
            challenge.display_error_challenge('challenges.txt')
            student.display_student('students.txt')
            sys.stdout.write('\nReport competition_report.txt generated!\n')

##competition class analyses the results.txt file and displays the result 
class competition:
##read_result method reads the text file and a list holds the results.txt file data
    def read_result(file):  
        res = []
        try:
            file = open(file, "r")
            line = file.readline()##reads each line of the text file
            while line:
                res.append(line.strip().split(", "))##removes the spaces and ',' between each data in the text file
                line = file.readline()##iterates to the next line
            file.close()
            if res==[]:##if the text file is empty then this code will execute
                sys.exit("The file results.txt is empty, try a different file")
            else:##else the list is returned
                return res
        except:##except executes when there is no existing file with name results.txt
            sys.exit("Something is wrong with results.txt file")
            return None

##display_result method will display the results in the required format 
    def display_result(file):
            result=[]
            result=competition.read_result(file)
            string=''##an empty string is created to hold all the displayed details 
            print('\nCOMPETITION DASHBOARD')
            string+='\nCOMPETITION DASHBOARD\n'
            for i in result:
                sys.stdout.write('+--------+')
                string+='+--------+'
                sys.stdout.write('--------+' *(len(i)-1) + '\n')
                string+='--------+' *(len(i)-1) + '\n'
                break
            sys.stdout.write('| '+'Result' )
            string+='| '+'Result' 
            for i in range(0,len(result)):
                for j in range(0,len(result[i])):
                    if(i==0):
                        if(j!=0):
                            sys.stdout.write(' |   '+result[i][j] + ' ')##to display the challenge ID
                            string+=' |   '+result[i][j] + ' '
            sys.stdout.write(' |'+'\n')
            string+=' |'+'\n'
            for i in range(0,len(result)):
                for j in range(0,len(result[i])):
                    if(i==0):
                        if(j==0):
                            sys.stdout.write('+--------+')
                            string+='+--------+'
                            sys.stdout.write('--------+' *(len(result[i])-1) + '\n')
                            string+=('--------+' *(len(result[i])-1) + '\n')
                        else:
                            continue
                    elif(i!=0):
                        if(result[i][j]=='444' or result[i][j]=='TBA' or result[i][j]=='tba'):##to display the ongoing challenge as '--' in the displayed output
                            result[i][j]='--'
                        if(result[i][j]=='-1' or result[i][j]=='NA' or result[i][j]=='x'):##to display the not participated challenge as space ' '
                            result[i][j]=' '
                        sys.stdout.write('|   '+result[i][j] +' '*(5-len(result[i][j])))##to display student ID and time taken by each student for each challenge
                        string+=('|   '+result[i][j] +' '*(5-len(result[i][j])))
                if(i!=0):
                    sys.stdout.write('|'+'\n')
                    string+=('|'+'\n')
            for i in result:
                sys.stdout.write('+--------+')
                string+='+--------+'
                sys.stdout.write('--------+' *(len(i)-1) + '\n')
                string+=('--------+' *(len(i)-1) + '\n')
                sys.stdout.write('There are '+str(len(result)-1)+' students and '+str(len(i)-1)+' challenges.\n')##displaying the total number of students and challenges
                string+=('There are '+str(len(result)-1)+' students and '+str(len(i)-1)+' challenges.\n')
                break
            total=[]##list to hold total time taken by each student
            count=[]##list to hold count of the challenges finished by each student
            for i in range(0,len(result)):
                tot=0##initializing total to calculate total of each student
                c=0##initializing count to calculate the finished challenges
                for j in range(0,len(result[i])):
                    if(i>=1 and j!=0 and result[i][j]!='--' and result[i][j]!=' '):##to check that there should not be any ongoing or not participated challenges
                        tot+=float(result[i][j])
                        c+=1
                count.append(c)##appending count to list
                total.append(tot)##appending total to list
            avg=[]##list to hold average of each student
            value=0##to hold the student ID's position with lowest average time
            for i in range(1,len(count)):
                if(count[i]>0):
                    average=float(total[i]/count[i])##calculate average of each student
                    avg.append(average)##appending the average to list
            if(avg[0]!=' ' and avg[0]!='--'):##assuming minimum average as average of first element and that element should not be ' ' and '--'
                minimum=avg[0]
            if(len(avg)>0):##to make sure that average is not empty
                for i in range(1,len(avg)-1):
                    if (avg[i]<minimum):##calculating the minimum average
                        minimum=avg[i]
            for i in range(1,len(avg)):##to find the position of student ID with lowest average time
                    if (minimum==avg[i]):
                        value=i
            print('The top student is {:} with an average time of {:.2f} minutes.\n'.format(result[value+1][0],minimum))##displaying the top student, one who has taken minimum time to finish the challenges
            string+=('The top student is {:} with an average time of {:.2f} minutes.\n'.format(result[value+1][0],minimum))

##challenge_information class holds the value of weight of each challenge (hidden)
##the weight of each challenge is set with the help of setter and obtained by getter methods and they remain private/hidden.
class challenge_information:
    def __init__(self,weight=0):
        self.__weight=weight
    def get_weight(self):
        return self.__weight
    def set_weight(self,value):
        self.__weight=value

##challenge class displays the challenge information such as number of finished challenges,
##number of ongoing challenges and average time of each challenge
class challenge:
    def read_challenge(file):##read_challenge is to read the challenges.txt file 
        challenge = []
        try:
            file = open(file, "r")
            line = file.readline()
            while line:
                challenge.append(line.strip().split(", "))
                line = file.readline()
            file.close()
            if challenge==[]:##to find if the file is empty
                sys.exit("The file challenges.txt is empty, try a different file")
            else:
                return challenge
        except:
            sys.exit("Something is wrong with challenges.txt file")
            return None
##display_error_challenge is a method used to check whether the challenge.txt file has the special weight('S') greater than 1.0
##getters and setters from challenge_information are used to find the weight of each special challenge
##if the weight is lower than 1.0 then the program quits
    def display_error_challenge(file):
        chall=[]
        chall=challenge.read_challenge(file)
        result=[]
        result=competition.read_result('results.txt')
        for i in chall:
            if(i[1]=='S'):
                information=challenge_information(i[3])
                information.set_weight(i[3])
                val=information.get_weight()
                if (float(val)<1):
                    sys.exit('Quit... Something wrong in the challenge.txt file')
                else:
                    continue
        chal=challenge.calculate_result(result,chall)##to pass the result and challenge text file to calculate the values required

##calculate_result method calculates the average of each challenge, count of number of challenges finished and ongoing challenges
    def calculate_result(result,chall):
        dic_tot={}##empty dictionary is initialized to store the challenge ID and total of each challenge
        dic_c={}##empty dictionary is initialized to store the challenge ID and count of each challenge finished by each student
        c_on={}##empty dictionary is initialized to store the challenge ID and count of each ongoing challenge
        c_fin={}##empty dictionary is initialized to store the challenge ID and total of each finished challenge
        for i in range(0,len(result)):
            for j in range(0,len(result[i])):
                sum=0
                c=0
                count_on=0
                count_fin=0
                for k in range(0,len(result)):##to check that the elements are not '444' or '--' to calculate the total and count of each challenge
                    if (result[k][j]!='444' and result[k][j]!='NA' and result[k][j]!='x' and result[k][j]!='TBA' and result[k][j]!='tba' and result[k][j]!='-1' and result[k][j]!='' and j!=0 and k!=0):
                        sum+=float(result[k][j])
                        dic_tot[result[i][j]]=sum
                        c+=1
                        dic_c[result[i][j]]=c
                        count_fin+=1##to calcualte the number of finished challenges
                    c_fin[result[i][j]]=count_fin
                    if(result[k][j]=='444' or result[k][j]=='TBA' or result[k][j]=='tba'):##to calcualte the number of ongoing challenges
                        count_on+=1
                    c_on[result[i][j]]=count_on
            break

        avg={}##to calculate the average with total and count  
        for items1 in dic_tot:
            for items2 in dic_c:
                if(items1==items2):
                    average=float(dic_tot[items1]/dic_c[items2])
                    avg[items1]=average
        del c_fin['']##deleting the empty element 
        del c_on['']
        challenge.display_challenge(result,chall,avg,c_fin,c_on)##passing the elements to display the output   

##to display the challenge information and generate a file with name 'competition_report.txt' with results and challenge details
    def display_challenge(result,chall,avg,c_fin,c_on):
        string=''
        print('CHALLENGE INFORMATION')
        sys.stdout.write('+---------------+')
        sys.stdout.write('---------------+' *5 + '\n')
        sys.stdout.write('|   Challenge   |'+'      Name     |'+'     Weight    |'+'    Nfinish    |'+'    Nongoing   |'+'  Average time |')
        sys.stdout.write('\n+---------------+')
        sys.stdout.write('---------------+' *5 )
        empty=[]##to hold the challenges.txt information as per the required display format
        m_or_s=[]##holds the 'S' and 'M' information of the challenge
        for i in range(0,len(chall)):
                empty.append(chall[i][0])
                empty.append(chall[i][2])
                m_or_s.append(chall[i][1])
                chall[i][3]=round(float(chall[i][3]),1)
                empty.append(str(chall[i][3]))
        max_len=len(empty[0])##to find the maximum length of the string for aligning the format
        for i in range(1,len(empty)):
            if(max_len<len(empty[i])):
                max_len=len(empty[i])
        j=0
        for i in range(0,len(empty)):
            if(empty[i][0]=='C' and len(empty[i])==3):
                sys.stdout.write('\n')
            maximum_len=max_len-len(empty[i])+1
            if(len(empty[i])>3):
                maximum_len=maximum_len-1
                sys.stdout.write('| '+empty[i]+'('+ m_or_s[j] +')' +' '*(maximum_len))##to display the challenge ID,name, S or M and weight of the challenge
                j=j+1
            else:
                sys.stdout.write('|   '+empty[i] +' '*(maximum_len))
            for k in c_fin:
                if k==empty[i-2]:
                    sys.stdout.write('|     '+str(c_fin[k])+' '*(maximum_len))##to display number of finished challenges
            for k in c_on:
                if k==empty[i-2]:
                    sys.stdout.write('|     '+str(c_on[k])+' '*(maximum_len))##to display number of ongoing challenges

            maxi_len=0
            for k in avg:
                avg[k]=round(avg[k],2)
                if (maxi_len<len(str(avg[k]))):
                    maxi_len=len(str(avg[k]))##to find the maximum length for average time formatting

            aver=avg
            for k in avg:
                if k==empty[i-2]:
                    if(len(str(avg[k]))<maxi_len):
                        m_len=maxi_len+1
                        sys.stdout.write('|   '+str(avg[k])+' '*(m_len)+'  |')##to display the average time
                    else:
                        sys.stdout.write('|   '+str(avg[k])+' '*(maxi_len)+'  |')
        sys.stdout.write('\n+---------------+')
        sys.stdout.write('---------------+' *5 )
    
        max_avg=0
        name=''
        ID=''
##to calculate the highest average time taken for completion of challenge  
        for k in avg:
            if(max_avg<avg[k]):
                max_avg=avg[k]
                ID=k ##ID of the challenge is found out with the highest average time
        for i in range(0,len(empty)):
            if(ID==empty[i]):
                name=empty[i+1]##name of the challenge is found out with the ID of the challenge

        print('\nThe most difficult challenge is ',name,'(',ID,') with an average time of ',max_avg,' minutes.')

##string holds the details of the results file to display the output in the new generated file 'competition_report.txt'
        string+='\nCOMPETITION DASHBOARD\n'
        for i in result:

            string+='+--------+'
            string+='--------+' *(len(i)-1) + '\n'
            break
        string+='| '+'Result' 
        for i in range(0,len(result)):
            for j in range(0,len(result[i])):
                if(i==0):
                    if(j!=0):
                        string+=' |   '+result[i][j] + ' '
        string+=' |'+'\n'
        for i in range(0,len(result)):
            for j in range(0,len(result[i])):
                if(i==0):
                    if(j==0):
                        string+='+--------+'
                        string+=('--------+' *(len(result[i])-1) + '\n')
                    else:
                        continue
                elif(i!=0):
                    if(result[i][j]=='444' or result[i][j]=='TBA' or result[i][j]=='tba'):
                        result[i][j]='--'
                    if(result[i][j]=='-1' or result[i][j]=='NA' or result[i][j]=='x'):
                        result[i][j]=' '
                    string+=('|   '+result[i][j] +' '*(5-len(result[i][j])))
            if(i!=0):
                string+=('|'+'\n')
        for i in result:
            string+='+--------+'
            string+=('--------+' *(len(i)-1) + '\n')
            string+=('There are '+str(len(result)-1)+' students and '+str(len(i)-1)+' challenges.\n')
            break
        total=[]
        count=[]
        stud=[]
        for i in range(0,len(result)):
            tot=0
            c=0
            for j in range(0,len(result[i])):
                if(i>=1 and j!=0 and result[i][j]!='--' and result[i][j]!=' '):
                    tot+=float(result[i][j])
                    c+=1
            count.append(c)
            total.append(tot)
            stud.append(result[i][0])
        avg=[]
        value=0
        for i in range(1,len(count)):
            if(count[i]>0):
                average=float(total[i]/count[i])
                avg.append(average)
        if(avg[0]!=' ' and avg[0]!='--'):
            minimum=avg[0]
        if(len(avg)>0):
            #print(len(avg))
            for i in range(1,len(avg)-1):
                if (avg[i]<minimum):
                    minimum=avg[i]
        for i in range(1,len(avg)):
                if (minimum==avg[i]):
                    value=i
        string+=('The top student is {:} with an average time of {:.2f} minutes.\n'.format(result[value+1][0],minimum))
##new file is generated and the contents of the results file is displayed and the contents of challenges file is added and displayed in the same file.
        file=open('competition_report.txt','w')
        file.write(string)
##the process to display challenge information in command line is carried out to display the information in the newly generated file.
        file.write('\nCHALLENGE INFORMATION\n')
        file.write('+---------------+')
        file.write('---------------+' *5 + '\n')
        file.write('|   Challenge   |'+'      Name     |'+'     Weight    |'+'    Nfinish    |'+'    Nongoing   |'+'  Average time |')
        file.write('\n+---------------+')
        file.write('---------------+' *5 )
        empty=[]
        m_or_s=[]
        dic_tot={}
        dic_c={}
        c_on={}
        c_fin={}
        for i in range(0,len(chall)):
                empty.append(chall[i][0])
                empty.append(chall[i][2])
                m_or_s.append(chall[i][1])
                chall[i][3]=round(float(chall[i][3]),1)
                empty.append(str(chall[i][3]))
                
        for i in range(0,len(result)):
            for j in range(0,len(result[i])):
                sum=0
                c=0
                count_on=0
                count_fin=0
                for k in range(0,len(result)):
                    if (result[k][j]!='444' and result[k][j]!='-1' and result[k][j]!='' and j!=0 and k!=0 and result[k][j]!='--' and result[k][j]!=' ' and result[k][j]!='NA' and result[k][j]!='x' and result[k][j]!='TBA' and result[k][j]!='tba'):
                        sum+=float(result[k][j])
                        dic_tot[result[i][j]]=sum
                        c+=1
                        dic_c[result[i][j]]=c
                        count_fin+=1
                    
                    if(result[k][j]=='444' or result[k][j]=='TBA' or result[k][j]=='tba'):
                        count_on+=1
                    c_fin[result[i][j]]=count_fin
                    c_on[result[i][j]]=count_on
            break
        max_len=len(empty[0])
        for i in range(1,len(empty)):
            if(max_len<len(empty[i])):
                max_len=len(empty[i])
        j=0
        for i in range(0,len(empty)):
            if(empty[i][0]=='C' and len(empty[i])==3):
                file.write('\n')
            maximum_len=max_len-len(empty[i])+1
            if(len(empty[i])>3):
                maximum_len=maximum_len-1
                file.write('| '+empty[i]+'('+ m_or_s[j] +')' +' '*(maximum_len))
                j=j+1
            else:
                file.write('|   '+empty[i] +' '*(maximum_len))
            for k in c_fin:
                if k==empty[i-2]:
                    file.write('|     '+str(c_fin[k])+' '*(maximum_len))
            for k in c_on:
                if k==empty[i-2]:
                    file.write('|     '+str(c_on[k])+' '*(maximum_len))

            maxi_len=0
            for k in aver:
                aver[k]=round(aver[k],2)
                if (maxi_len<len(str(aver[k]))):
                    maxi_len=len(str(aver[k]))
            for k in aver:
                if k==empty[i-2]:
                    if(len(str(aver[k]))<maxi_len):
                        m_len=maxi_len+1
                        file.write('|   '+str(aver[k])+' '*(m_len)+'  |')
                    else:
                        file.write('|   '+str(aver[k])+' '*(maxi_len)+'  |')
        file.write('\n+---------------+')
        file.write('---------------+' *5 )
    
        max_avg=0
        name=''
        ID=''
        for k in aver:
            if(max_avg<aver[k]):
                max_avg=aver[k]
                ID=k
        for i in range(0,len(empty)):
            if(ID==empty[i]):
                name=empty[i+1]

        file.write('\nThe most difficult challenge is '+name)
        file.write('('+str(ID)+')' )
        file.write(' with an average time of '+str(max_avg)+' minutes.\n')
        file.write('Report competition_report.txt generated!\n')
        file.close()##after adding the above lines the file is closed

##student class takes the students.txt file to perform operations in finding the student information
##such as the number of students finishing the challenges, ongoing and the average time of each student in finishing the challenge
class student:
    def read_student(file):##to read the students.txt file 
        stud = []
        try:
            file = open(file, "r")
            line = file.readline()
            while line:
                stud.append(line.strip().split(", "))
                line = file.readline()
            file.close()
            if stud==[]:##to check if the file is empty
                sys.exit("The file students.txt is empty, try a different file")
            else:
                return stud
        except:
            sys.exit("Something is wrong with students.txt file")
            return None

##to display the student information this method is implemented
    def display_student(file):
        stud=[]
        stud=student.read_student(file)
        sys.stdout.write('\nSTUDENT INFORMATION\n')
        sys.stdout.write('+---------------+')
        sys.stdout.write('---------------+' *5 + '\n')
        sys.stdout.write('|   StudentID   |'+'      Name     |'+'     Type      |'+'    Nfinish    |'+'    Nongoing   |'+'  Average time |')
        sys.stdout.write('\n+---------------+')
        sys.stdout.write('---------------+' *5 +'\n')
        student.calculate_student_and_display(stud)##some calculations are required to display the students file and so the list is passed to a method 

##mathod to calculate the student information from the list and to display the information in the required format
    def calculate_student_and_display(stud):
        student=stud
        result=[]
        result=competition.read_result('results.txt')##the two tect files are required to process further with the calculations and hence the methods are called
        chall=challenge.read_challenge('challenges.txt')
        file=open('competition_report.txt','w')
        string=''
        ##string to hold the output of results file to be displayed in the new generated file after adding all the strings    
        string+='\nCOMPETITION DASHBOARD\n'
        for i in result:

            string+='+--------+'
            string+='--------+' *(len(i)-1) + '\n'
            break
        string+='| '+'Result' 
        for i in range(0,len(result)):
            for j in range(0,len(result[i])):
                if(i==0):
                    if(j!=0):
                        string+=' |   '+result[i][j] + ' '
        string+=' |'+'\n'
        for i in range(0,len(result)):
            for j in range(0,len(result[i])):
                if(i==0):
                    if(j==0):
                        string+='+--------+'
                        string+=('--------+' *(len(result[i])-1) + '\n')
                    else:
                        continue
                elif(i!=0):
                    if(result[i][j]=='444' or result[i][j]=='TBA' or result[i][j]=='tba'):
                        result[i][j]='--'
                    if(result[i][j]=='-1'or result[i][j]=='NA' or result[i][j]=='x'):
                        result[i][j]=' '
                    string+=('|   '+result[i][j] +' '*(5-len(result[i][j])))
            if(i!=0):
                string+=('|'+'\n')
        for i in result:
            string+='+--------+'
            string+=('--------+' *(len(i)-1) + '\n')
            string+=('There are '+str(len(result)-1)+' students and '+str(len(i)-1)+' challenges.\n')
            break
        total=[]
        count=[]
        stud=[]
        for i in range(0,len(result)):
            tot=0
            c=0
            for j in range(0,len(result[i])):
                if(i>=1 and j!=0 and result[i][j]!='--' and result[i][j]!=' '):
                    tot+=float(result[i][j])
                    c+=1
            count.append(c)
            total.append(tot)
            stud.append(result[i][0])
        avg=[]
        value=0
        for i in range(1,len(count)):
            if(count[i]>0):
                average=float(total[i]/count[i])
                avg.append(average)
        if(avg[0]!=' ' and avg[0]!='--'):
            minimum=avg[0]
        if(len(avg)>0):
            for i in range(1,len(avg)-1):
                if (avg[i]<minimum):
                    minimum=avg[i]
        for i in range(1,len(avg)):
                if (minimum==avg[i]):
                    value=i
        string+=('The top student is {:} with an average time of {:.2f} minutes.\n'.format(result[value+1][0],minimum))
        file.write(string)
        ##the challenge file output to be written in the new gernerated file
        dic_tot={}
        dic_c={}
        c_on={}
        c_fin={}
        for i in range(0,len(result)):
            for j in range(0,len(result[i])):
                sum=0
                c=0
                count_on=0
                count_fin=0
                for k in range(0,len(result)):
                    if (result[k][j]!='444' and result[k][j]!='--' and result[k][j]!='-1' and result[k][j]!=' ' and result[k][j]!='' and j!=0 and k!=0 and result[k][j]!='NA' and result[k][j]!='x' and result[k][j]!='TBA' and result[k][j]!='tba'):
                        sum+=float(result[k][j])
                        dic_tot[result[i][j]]=sum
                        c+=1
                        dic_c[result[i][j]]=c
                        count_fin+=1
                    c_fin[result[i][j]]=count_fin
                    if(result[k][j]=='444' or result[k][j]=='--' or result[k][j]=='TBA' or result[k][j]=='tba'):
                        count_on+=1
                    c_on[result[i][j]]=count_on
            break

        avg={}               
        for items1 in dic_tot:
            for items2 in dic_c:
                if(items1==items2):
                    average=float(dic_tot[items1]/dic_c[items2])
                    avg[items1]=average

        aver=avg
        file.write('\nCHALLENGE INFORMATION\n')
        file.write('+---------------+')
        file.write('---------------+' *5 + '\n')
        file.write('|   Challenge   |'+'      Name     |'+'     Weight    |'+'    Nfinish    |'+'    Nongoing   |'+'  Average time |')
        file.write('\n+---------------+')
        file.write('---------------+' *5 )
        empty=[]
        m_or_s=[]
        for i in range(0,len(chall)):
                empty.append(chall[i][0])
                empty.append(chall[i][2])
                m_or_s.append(chall[i][1])
                chall[i][3]=round(float(chall[i][3]),1)
                empty.append(str(chall[i][3]))
        max_len=len(empty[0])
        for i in range(1,len(empty)):
            if(max_len<len(empty[i])):
                max_len=len(empty[i])

        j=0
        for i in range(0,len(empty)):
            if(empty[i][0]=='C' and len(empty[i])==3):
                file.write('\n')
            maximum_len=max_len-len(empty[i])+1
            if(len(empty[i])>3):
                maximum_len=maximum_len-1
                file.write('| '+empty[i]+'('+ m_or_s[j] +')' +' '*(maximum_len))
                j=j+1
            else:
                file.write('|   '+empty[i] +' '*(maximum_len))
            for k in c_fin:
                if k==empty[i-2]:
                    file.write('|     '+str(c_fin[k])+' '*(maximum_len))
            for k in c_on:
                if k==empty[i-2]:
                    file.write('|     '+str(c_on[k])+' '*(maximum_len))

            maxi_len=0
            for k in aver:
                aver[k]=round(aver[k],2)
                if (maxi_len<len(str(aver[k]))):
                    maxi_len=len(str(aver[k]))
            for k in aver:
                if k==empty[i-2]:
                    if(len(str(aver[k]))<maxi_len):
                        m_len=maxi_len+1
                        file.write('|   '+str(aver[k])+' '*(m_len)+'  |')
                    else:
                        file.write('|   '+str(aver[k])+' '*(maxi_len)+'  |')
        max_avg=0
        name=''
        ID=''
        for k in aver:
            if(max_avg<float(aver[k])):
                max_avg=aver[k]
                ID=k

        for i in range(0,len(empty)):
            if(ID==empty[i]):
                name=empty[i+1]
        file.write('\n+---------------+')
        file.write('---------------+' *5 )
    
        
        file.write('\nThe most difficult challenge is '+str(name))
        file.write('('+str(ID)+')' )
        file.write(' with an average time of '+str(max_avg)+' minutes.\n')
        file.close()
##the files are read again to ensure that the list is same as the file 
        result=[]
        result=competition.read_result('results.txt')
        chall=[]
        dic_stud={}
        c_stud_f={}
        c_f=0
        c_stud_on={}
        c_on=0
        average={}
        chall=challenge.read_challenge('challenges.txt')
        ##to calculate the challenges ongoing and finished by each student
        for i in range(0,len(result)):
            list_stud=[]##list to hold the student's total time
            tot=0
            avg=0
            c_f=0
            c_on=0
            for j in range(0,len(result[i])):
                if(i!=0 and j!=0 and result[i][j]!='444' and result[i][j]!='-1' and result[i][j]!='NA' and result[i][j]!='x' and result[i][j]!='TBA' and result[i][j]!='tba'):
                    list_stud.append(result[i][j])
                    c_f+=1
                    tot+=float(result[i][j])
                if(result[i][j]=='444' or result[i][j]=='--' or result[i][j]=='TBA' or result[i][j]=='tba'):
                    c_on+=1
            dic_stud[result[i][0]]=list_stud##dictionary to hold the student ID and total
            c_stud_on[result[i][0]]=c_on##to hold the student ID and number of on going challenge
            c_stud_f[result[i][0]]=c_f##to hold the student ID and number of finished challenge
            if (c_f>0):##if finished challenges is greater than 0
                avg=tot/c_f
                average[result[i][0]]=avg##to calculate the average and hold it in a dictionary with student ID and average
            else:
                average[result[i][0]]=0
        del dic_stud[''] ## to remove the '' element
        del c_stud_on['']
        del c_stud_f['']
        del average['']
        for k,v in average.items():##to round off the elements to 2 decimal points 
            average[k]=(round(v,2))
        dic_stud_det={} ##dictionary to hold the {student ID:{challenge ID:[time taken for that challenge]}}
        for i in range(0,len(result)):
            chall_det={}##holds the challenge details
            for j in range(0,len(result[i])):
                if(result[0][j]!=''):
                    chall_det[result[0][j]]=result[i][j]
            if(result[i][0]!=''):
                dic_stud_det[result[i][0]]=chall_det
        dic_chall_det={}##dictionary to hold {challenge ID:Type of challenge}
        for i in range(0,len(chall)):
            for j in range(0,len(chall[i])):
                if(chall[i][j]=='M' or chall[i][j]=='S'):
                    dic_chall_det[chall[i][j-1]]=chall[i][j]
        dic_student_det={}##dictionary to hold {Student ID: education of the student(U or P)}
        for i in range(0,len(student)):
            for j in range(0,len(student[i])):
                if (student[i][j]=='U' or student[i][j]=='P'):
                    dic_student_det[student[i][j-2]]=student[i][j]
        c_under={}##to hold the count of undergraduate students finishing the S challenge
        c_post={}##to hold the count of postgraduate students finishing the S challenge
        c_mand={}##to hold the count of students finishing the M challenge
        for i,j in dic_stud_det.items():##calculations to find the count of the finished challenges
            c_u=0
            c_p=0
            c_m=0
            for o,p in j.items():
                for k,l in dic_student_det.items():
                    for m,n in dic_chall_det.items():
                            if(i==k):                               
                                if(n=='S' and o==m):
                                    if(l=='U'):
                                        if(p!='444' and p!='-1' and p!='TBA' and p!='tba' and p!='x' and p!='NA'):
                                            c_u+=1
                                            c_under[i]=c_u
                                    if(l=='P'):
                                        if(n=='S'):
                                            if(p!='444' and p!='-1' and p!='TBA' and p!='tba' and p!='x' and p!='NA'):
                                                c_p+=1
                                                c_post[i]=c_p
                                if(n=='M' and o==m):
                                    if(p!='444' and p!='-1' and p!='TBA' and p!='tba' and p!='x' and p!='NA'):
                                        c_m+=1
                                        c_mand[i]=c_m
        count_mand=0##to find the number of mandatory or M challenge
        for z in range(0,len(chall)):
            for a in range(0,len(chall[z])):
                if(chall[z][a]=='M'):
                    count_mand+=1
        count_satisfied={}##to check if the conditions are satisfied(all students - all M challenges , U students - 1 S challenge , P students - 2 S challenge)              
        temp=[]##to check there is no duplication of challenges while checking if the conditions are satisfied
        for i in (dic_stud_det):
            count_sat=0
            for j,k in dic_student_det.items():
                for y,z in c_mand.items():
                    if(z==count_mand):
                        if(i==j and k=='U'):
                            for l,m in c_under.items():
                                if(i==l and l==y):
                                    if(m>=1):
                                        count_sat+=1
                        if(i==j and k=='P'):
                            for n,o in c_post.items():
                                if(i==n):
                                    if(o>=2 and n==y):
                                        count_sat+=1
                    count_satisfied[i]=count_sat
        max_len=0 ##to calculate the maximum length for formatting the average time
        for s in student:
            if(max_len<len(str(s[1]))):
                max_len=len(str(s[1]))
        max_space=0
        max_average=0
        for a,b in average.items():
            if(max_space<len(str(b))):
               max_space=len(str(b))
        for k,v in count_satisfied.items():##to display the average time, count of finished challenges and number of ongoing challenges 
            for s in student:
                if(s[0]==k):
                    if(len(str(s[1]))<max_len):
                            leng=max_len-(len(str(s[1])))+3
                    elif(len(str(s[1]))==max_len):
                        leng=(len(str(s[1])))-3
                    sys.stdout.write('|      '+s[0]+' '*5)
                    if(v>0):
                        sys.stdout.write('|      '+s[1]+' '*leng)

                    else:
                        sys.stdout.write('|     !'+s[1]+' '*leng)
                    
                    sys.stdout.write('|      '+s[2]+' '*8)
                    if(c_stud_f[s[0]]<1):
                            sys.stdout.write('|      '+'--'+' '*7)
                    else:
                            sys.stdout.write('|      '+str(c_stud_f[s[0]])+' '*8)
                    if (c_stud_on[s[0]]<1):
                            sys.stdout.write('|      '+'--'+' '*7)
                    else:
                            sys.stdout.write('|      '+str(c_stud_on[s[0]])+' '*8)
                    leng=max_space
                
                    if(average[s[0]]!='' and average[s[0]]!=' ' and average[s[0]]!='--' and average[s[0]]!=0):
                        if((len(str(average[s[0]])))<max_space):
                            leng=max_space+1

                        sys.stdout.write('|     '+(str(average[s[0]]))+' '*leng)
                    else:
                        leng=max_space+3
                        sys.stdout.write('|     '+'--'+' '*leng)
            sys.stdout.write('|\n')
##to calculate the fastest average time or the minimum average of student required to finish the challenges
##with the minimum average time, student ID and name are found out and displayed
        max_average=100
        for a,b in average.items():
            if(max_average>b and b>0):
               max_average=b
               ID=a
        print
        for i in range(0,len(student)):
            for j in range(0,len(student[i])):
                if(ID==student[i][j]):
                    name=student[i][j+1]
        sys.stdout.write('+---------------+')
        sys.stdout.write('---------------+' *5 +'\n')
        sys.stdout.write('The student with the fastest average time is '+str(ID)+'('+str(name)+') with an average time of '+str(max_average)+' minutes.')
##new generated file is opened to display the output in the same format as the command line
        file=open('competition_report.txt','a')
        file.write('\nSTUDENT INFORMATION\n')
        file.write('+---------------+')
        file.write('---------------+' *5 + '\n')
        file.write('|   StudentID   |'+'      Name     |'+'     Type      |'+'    Nfinish    |'+'    Nongoing   |'+'  Average time |')
        file.write('\n+---------------+')
        file.write('---------------+' *5 +'\n')
        for k,v in count_satisfied.items():
            for s in student:
                    if(s[0]==k):
                        if(len(str(s[1]))<max_len):
                                leng=max_len-(len(str(s[1])))+3
                        elif(len(str(s[1]))==max_len):
                            leng=(len(str(s[1])))-3
                        file.write('|      '+s[0]+' '*5)
                        if(v>0):
                            file.write('|      '+s[1]+' '*leng)

                        else:
                            file.write('|     !'+s[1]+' '*leng)
                        
                        file.write('|      '+s[2]+' '*8)
                        if(c_stud_f[s[0]]<1):
                            file.write('|      '+'--'+' '*7)
                        else:
                            file.write('|      '+str(c_stud_f[s[0]])+' '*8)
                        if (c_stud_on[s[0]]<1):
                            file.write('|      '+'--'+' '*7)
                        else:
                            file.write('|      '+str(c_stud_on[s[0]])+' '*8)
                        leng=max_space
                        if(average[s[0]]!='' and average[s[0]]!=' ' and average[s[0]]!='--' and average[s[0]]!=0):
                            if((len(str(average[s[0]])))<max_space):
                                leng=max_space+1

                            file.write('|     '+(str(average[s[0]]))+' '*leng)
                        else:
                            leng=max_space+3
                            file.write('|     '+'--'+' '*leng)            
            file.write('|\n')
        max_average=100
        for a,b in average.items():
            if(max_average>b and b>0):
               max_average=b
               ID=a
        print
        for i in range(0,len(student)):
            for j in range(0,len(student[i])):
                if(ID==student[i][j]):
                    name=student[i][j+1]    

        file.write('+---------------+')
        file.write('---------------+' *5 +'\n')
        file.write('The student with the fastest average time is {:}({:}) with an average time of {:} minutes.'.format((str(ID)),str(name),str(max_average)))
        file.close()##the file is closed after appending the data

##start will hold the arguments obtained while running the python file in command line and gives the arguments to class main
start=main()
