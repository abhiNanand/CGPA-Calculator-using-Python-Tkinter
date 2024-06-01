 
#ABHISHEK ANAND

 

from tkinter import*
window=Tk()
window.title("CGPA CALCULATOR")
window.geometry("500x500")
window.configure(bg="pink")





label1=Label(window,text="  ",bg='pink')         #empty
label2=Label(window,text="Sem 1",bg='pink')      #for semester 1

grade=Label(window,text="   Grade   ",bg='cyan')
credit=Label(window,text="  Credit   ",bg='cyan')
label1.grid(row=0,column=0)
label2.grid(row=1,column=0)

grade.grid(row=8,column=15)
credit.grid(row=8,column=20)





subject1=Label(window,text="Subject 1",bg='pink')
subject2=Label(window,text="Subject 2",bg='pink')
subject3=Label(window,text="Subject 3",bg='pink')
subject4=Label(window,text="Subject 4",bg='pink')
subject5=Label(window,text="Subject 5",bg='pink')
subject6=Label(window,text="Subject 6",bg='pink')

subject1.grid(row=10,column=0)
subject2.grid(row=11,column=0)
subject3.grid(row=12,column=0)
subject4.grid(row=13,column=0)
subject5.grid(row=14,column=0)
subject6.grid(row=15,column=0)

#entries for grade (semester 1)
e1=Entry(window,width=10,borderwidth=2)
e2=Entry(window,width=10,borderwidth=2)
e3=Entry(window,width=10,borderwidth=2)
e4=Entry(window,width=10,borderwidth=2)
e5=Entry(window,width=10,borderwidth=2)
e6=Entry(window,width=10,borderwidth=2)
#position
e1.grid(row=10,column=15)
e2.grid(row=11,column=15)
e3.grid(row=12,column=15)
e4.grid(row=13,column=15)
e5.grid(row=14,column=15)
e6.grid(row=15,column=15)

#entries for credit (semester 1)
e11=Entry(window,width=10,borderwidth=2)
e21=Entry(window,width=10,borderwidth=2)
e31=Entry(window,width=10,borderwidth=2)
e41=Entry(window,width=10,borderwidth=2)
e51=Entry(window,width=10,borderwidth=2)
e61=Entry(window,width=10,borderwidth=2)
#position
e11.grid(row=10,column=20)
e21.grid(row=11,column=20)
e31.grid(row=12,column=20)
e41.grid(row=13,column=20)
e51.grid(row=14,column=20)
e61.grid(row=15,column=20)

label11=Label(window,text="  ",bg='pink')             #empty
label3=Label(window,text="Sem 2",bg='pink')           #for semester 2
grade=Label(window,text="   Grade   ",bg='cyan')
credit=Label(window,text="   Credit   ",bg='cyan')
label11.grid(row=18,column=0)
label3.grid(row=20,column=0)
grade.grid(row=23,column=15)
credit.grid(row=23,column=20)


subject1_2=Label(window,text="Subject 1",bg='pink')
subject2_2=Label(window,text="Subject 2",bg='pink')
subject3_2=Label(window,text="Subject 3",bg='pink')
subject4_2=Label(window,text="Subject 4",bg='pink')
subject5_2=Label(window,text="Subject 5",bg='pink')
subject6_2=Label(window,text="Subject 6",bg='pink')
subject1_2.grid(row=25,column=0)
subject2_2.grid(row=26,column=0)
subject3_2.grid(row=27,column=0)
subject4_2.grid(row=28,column=0)
subject5_2.grid(row=29,column=0)
subject6_2.grid(row=30,column=0)


#entries for grades (semester 2)
e13=Entry(window,width=10,borderwidth=2)
e23=Entry(window,width=10,borderwidth=2)
e33=Entry(window,width=10,borderwidth=2)
e43=Entry(window,width=10,borderwidth=2)
e53=Entry(window,width=10,borderwidth=2)
e63=Entry(window,width=10,borderwidth=2)
e13.grid(row=25,column=15)
e23.grid(row=26,column=15)
e33.grid(row=27,column=15)
e43.grid(row=28,column=15)
e53.grid(row=29,column=15)
e63.grid(row=30,column=15)


#entries for credit (semester 2)
e12=Entry(window,width=10,borderwidth=2)
e22=Entry(window,width=10,borderwidth=2)
e32=Entry(window,width=10,borderwidth=2)
e42=Entry(window,width=10,borderwidth=2)
e52=Entry(window,width=10,borderwidth=2)
e62=Entry(window,width=10,borderwidth=2)
e12.grid(row=25,column=20)
e22.grid(row=26,column=20)
e32.grid(row=27,column=20)
e42.grid(row=28,column=20)
e52.grid(row=29,column=20)
e62.grid(row=30,column=20)




    
    



#function for calculation tgpa for semester 1
def myclick():
    def gradeval(grades):
        
        grade_c = {"O":10,"A+":9,"A":8,"B+":7,"B":6, "C":5,"D":4,"E":3,"F":0}
        if grades != []:
            return grade_c[grades]
        
 
    #TAKING VALUE OF GRADES
    x1=gradeval(e1.get())
    x2=gradeval(e2.get())
    x3=gradeval(e3.get())
    x4=gradeval(e4.get())
    x5=gradeval(e5.get())
    x6=gradeval(e6.get())

    #CHANDING CREDIT TO INTERGER AND FINDING SUM OF CREDITS.
    y=int (e11.get())+int(e21.get())+int(e31.get())+int(e41.get())+int(e51.get())+int(e61.get())

    #MULTIPLYING GRADE * CREDIT AND DIVIDING BY SUM OF CREDITS.
    z=(int(x1)*int(e11.get())+int(x2)*int(e21.get())+int(x3)*int(e31.get())+int(x4)*int(e41.get())+int(x5)*int(e51.get())+int(x6)*int(e61.get()))/y
    abhi=Label(window, text = z)
    abhi.grid(row=13,column=25)

#function for calculation tgpa for semester 2
def myclick2():
    def gradevalue(grades):
        
        grade_c = {"O":10,"A+":9,"A":8,"B+":7,"B":6, "C":5,"D":4,"E":3,"F":0}
        if grades != []:
            return grade_c[grades]
        
 
    #TAKING VALUE OF GRADES
    x1=gradevalue(e13.get())
    x2=gradevalue(e23.get())
    x3=gradevalue(e33.get())
    x4=gradevalue(e43.get())
    x5=gradevalue(e53.get())
    x6=gradevalue(e63.get())

    #CHANDING CREDIT TO INTERGER AND FINDING SUM OF CREDITS.
    y=int (e12.get())+int(e22.get())+int(e32.get())+int(e42.get())+int(e52.get())+int(e62.get())

    #MULTIPLYING GRADE * CREDIT AND DIVIDING BY SUM OF CREDITS.
    z=(int(x1)*int(e12.get())+int(x2)*int(e22.get())+int(x3)*int(e32.get())+int(x4)*int(e42.get())+int(x5)*int(e52.get())+int(x6)*int(e62.get()))/y
    kartik=Label(window,text=z)
    kartik.grid(row=28,column=25)
    
    
#function for cgpa calculation
def myclick3():
    def gradeval(grades):
        
        grade_c = {"O":10,"A+":9,"A":8,"B+":7,"B":6, "C":5,"D":4,"E":3,"F":0}
        if grades != []:
            return grade_c[grades]
        
 
    #TAKING VALUE OF GRADES
    x1=gradeval(e1.get())
    x2=gradeval(e2.get())
    x3=gradeval(e3.get())
    x4=gradeval(e4.get())
    x5=gradeval(e5.get())
    x6=gradeval(e6.get())

    #CHANDING CREDIT TO INTERGER AND FINDING SUM OF CREDITS.
    y=int (e11.get())+int(e21.get())+int(e31.get())+int(e41.get())+int(e51.get())+int(e61.get())

    #MULTIPLYING GRADE * CREDIT AND DIVIDING BY SUM OF CREDITS.
    z=(int(x1)*int(e11.get())+int(x2)*int(e21.get())+int(x3)*int(e31.get())+int(x4)*int(e41.get())+int(x5)*int(e51.get())+int(x6)*int(e61.get()))/y

    def gradevalue(grades):
        
        grade_c = {"O":10,"A+":9,"A":8,"B+":7,"B":6, "C":5,"D":4,"E":3,"F":0}
        if grades != []:
            return grade_c[grades]
        
 
    #TAKING VALUE OF GRADES
    x11=gradevalue(e13.get())
    x21=gradevalue(e23.get())
    x31=gradevalue(e33.get())
    x41=gradevalue(e43.get())
    x51=gradevalue(e53.get())
    x61=gradevalue(e63.get())

    #CHANDING CREDIT TO INTERGER AND FINDING SUM OF CREDITS.
    y2=int (e12.get())+int(e22.get())+int(e32.get())+int(e42.get())+int(e52.get())+int(e62.get())

    #MULTIPLYING GRADE * CREDIT AND DIVIDING BY SUM OF CREDITS.
    z2=(int(x11)*int(e12.get())+int(x21)*int(e22.get())+int(x31)*int(e32.get())+int(x41)*int(e42.get())+int(x51)*int(e52.get())+int(x61)*int(e62.get()))/y2
    cc=(z+z2)/2
    shubham=Label(window,text=cc)
    shubham.grid(row=33,column=1)
    
#function for remark
def myclick4():
    def gradeval(grades):
        
        grade_c = {"O":10,"A+":9,"A":8,"B+":7,"B":6, "C":5,"D":4,"E":3,"F":0}
        if grades != []:
            return grade_c[grades]
        
 
    #TAKING VALUE OF GRADES
    x1=gradeval(e1.get())
    x2=gradeval(e2.get())
    x3=gradeval(e3.get())
    x4=gradeval(e4.get())
    x5=gradeval(e5.get())
    x6=gradeval(e6.get())

    #CHANDING CREDIT TO INTERGER AND FINDING SUM OF CREDITS.
    y=int (e11.get())+int(e21.get())+int(e31.get())+int(e41.get())+int(e51.get())+int(e61.get())

    #MULTIPLYING GRADE * CREDIT AND DIVIDING BY SUM OF CREDITS.
    z=(int(x1)*int(e11.get())+int(x2)*int(e21.get())+int(x3)*int(e31.get())+int(x4)*int(e41.get())+int(x5)*int(e51.get())+int(x6)*int(e61.get()))/y

    def gradevalue(grades):
        
        grade_c = {"O":10,"A+":9,"A":8,"B+":7,"B":6, "C":5,"D":4,"E":3,"F":0}
        if grades != []:
            return grade_c[grades]
        
 
    #TAKING VALUE OF GRADES
    x11=gradevalue(e13.get())
    x21=gradevalue(e23.get())
    x31=gradevalue(e33.get())
    x41=gradevalue(e43.get())
    x51=gradevalue(e53.get())
    x61=gradevalue(e63.get())

    #CHANDING CREDIT TO INTERGER AND FINDING SUM OF CREDITS.
    y2=int (e12.get())+int(e22.get())+int(e32.get())+int(e42.get())+int(e52.get())+int(e62.get())

    #MULTIPLYING GRADE * CREDIT AND DIVIDING BY SUM OF CREDITS.
    z2=(int(x11)*int(e12.get())+int(x21)*int(e22.get())+int(x31)*int(e32.get())+int(x41)*int(e42.get())+int(x51)*int(e52.get())+int(x61)*int(e62.get()))/y2
    cc=(z+z2)/2
    if cc>5:
        r="Pass"
    else:
        r="Fail"
    

    final=Label(window,text=r)
    final.grid(row=35,column=0)
        
    
    
    
    

#button
tgpa=Button(window,text="TGPA",command=myclick,bg="wheat", padx=4,pady=2)
tgpa2=Button(window,text="TGPA",command=myclick2,bg="wheat",padx=4,pady=2)
cgpa=Button(window,text="CGPA",bg="wheat",command=myclick3,padx=4,pady=2)
remark=Button(window,text="REMARK",bg="wheat",command=myclick4,padx=4,pady=2)

#buttons postitons
tgpa.grid(row=12,column=25)
tgpa2.grid(row=27,column=25)
cgpa.grid(row=33,column=0)
remark.grid(row=34,column=0)










window.mainloop()

