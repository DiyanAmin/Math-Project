#By The Numbers

#Necessary Modules
from time import sleep
import random
import customtkinter as ctk

#Global Variables
questionFont=('Times New Roman',40)
name='By The Numbers'
question=0
questionTypes=['Addition','Multiplication','Division','Subraction']

def difficultyChoice(choice):
    global num1,num2,difficultyLevel

    difficultyLevel=choice
    if choice=='Easy':
        num1=random.randint(0,100)
        num2=random.randint(0,100)

    elif choice=='Normal':
        num1=random.randint(0,300)
        num2=random.randint(0,300)

    elif choice=='Medium':
        num1=random.randint(0,500)
        num2=random.randint(0,500)

    elif choice=='Hard':
        num1=random.randint(0,1000)
        num2=random.randint(0,1000)

    elif choice=='Insane':
        num1=random.randint(0,10000)
        num2=random.randint(0,10000)

    elif choice=='???':
        num1=random.randint(0,9999999999999999999999999999999)
        num2=random.randint(0,9999999999999999999999999999999)

qnStorage=0
def startGame():

    def Once():
        qn=0
        answer=0
        for i in r.winfo_children():
            i.destroy()

        difficultyChosen=ctk.CTkLabel(r,text=f'Chosen Difficulty: {difficultyLevel}')
        difficultyChosen.pack(pady=10)

        while qn<=10:
            qn+=1

            questionType=random.choice(questionTypes)
            if questionType=='Addition':
                answer=num1+num2
                question=f'What is {num1} + {num2}'
                questionLabel=ctk.CTkLabel(r,text=f'Q-{qn}. {question}',font=questionFont)
                questionLabel.pack(pady=10)

            elif questionType=='Subtraction':
                answer=num1-num2
                question=f'What is {num1} - {num2}'
                questionLabel=ctk.CTkLabel(r,text=f'Q-{qn}. {question}',font=questionFont)
                questionLabel.pack(pady=10)
                
            elif questionType=='Multiplication':
                answer=num1*num2
                question=f'What is {num1} multiplied by {num2}'
                questionLabel=ctk.CTkLabel(r,text=f'Q-{qn}. {question}',font=questionFont)
                questionLabel.pack(pady=10)
                
            elif questionType=='Division':
                if num1<num2:
                    num1Div=num2
                    num2Div=num1
                answer=num1Div/num2Div
                question=f'What is {num1Div} divided by {num2Div}'
                questionLabel=ctk.CTkLabel(r,text=f'Q-{qn}. {question}',font=questionFont)
                questionLabel.pack(pady=10)

            global a,b,c,d
            a=(answer*num1-num2)
            b=random.randint(0,667)
            c=num2+answer/num1
            d=random.randint(400,1000)

            correctOption=random.choice(['a','b','c','d'])
            if correctOption=='a':
                a=answer
            
            elif correctOption=='b':
                b=answer
            
            elif correctOption=='c':
                c=answer
            
            elif correctOption=='d':
                d=answer

            def correctAnswer():
                sleep(0.5)
                correct=ctk.CTkToplevel()
                correct.geometry('700x250')
                correct.title('Correct Answer')

                label=ctk.CTkLabel(correct,text='Correct answer!\nClose this Window',font=('Helvetica',56))
                label.pack(pady=10)
                correct.mainloop()

                r.destroy()

            def wrongAnswer():
                for i in r.winfo_children():
                    i.destroy()

                label=ctk.CTkLabel(r,text=f'Wrong Answer',font=('Copperplate',56))
                label.pack(pady=10)
                button=ctk.CTkButton(r,text=f'Try Again',command=Once)
                button.pack(pady=10)
                r.mainloop()

            def aFunc():
                print('Option A Selected')
                if a==answer:
                    correctAnswer()
                    nextButton=ctk.CTkButton(r,text='Next',command=Once)
                    nextButton.pack(pady=10)
                    r.mainloop()
                
                else:
                    wrongAnswer()
                sleep(4)
                r.destroy()
                Once()

            def bFunc():
                print('Option B Selected')
                if b==answer:
                    correctAnswer()
                    nextButton=ctk.CTkButton(r,text='Next',command=Once)
                    nextButton.pack(pady=10)
                    r.mainloop()
                
                else:
                    wrongAnswer()
                sleep(4)
                r.destroy()
                Once()

            def cFunc():
                print('Option C Selected')
                if c==answer:
                    correctAnswer()
                    nextButton=ctk.CTkButton(r,text='Next',command=Once)
                    nextButton.pack(pady=10)
                    r.mainloop()
                
                else:
                    wrongAnswer()
                sleep(4)
                r.destroy()
                Once()

            def dFunc():
                print('Option D Selected')
                if d==answer:
                    correctAnswer()
                    nextButton=ctk.CTkButton(r,text='Next',command=Once)
                    nextButton.pack(pady=10)
                    r.mainloop()
                
                else:
                    wrongAnswer()
                sleep(4)
                r.destroy()
                Once()
                    

            optionA=ctk.CTkButton(r,height=46,text=f'A. {a}',command=aFunc)
            optionA.pack(padx=5,pady=10)

            optionB=ctk.CTkButton(r,height=46,text=f'B. {b}',command=bFunc)
            optionB.pack(pady=10)

            optionC=ctk.CTkButton(r,height=46,text=f'C. {c}',command=cFunc)
            optionC.pack(padx=5,pady=10)

            optionD=ctk.CTkButton(r,height=46,text=f'D. {d}',command=dFunc)
            optionD.pack(pady=10)

            r.mainloop()

    Once()


r=ctk.CTk()
r.title(name)
r.geometry('700x400')
#Icon here


credits=ctk.CTkLabel(r,text='Coded By Diyan. Made by all',font=('Helvetica',18))
credits.pack(pady=10)

difficulty=ctk.CTkLabel(r,text='Difficulty')
difficultyOptions=ctk.CTkComboBox(r,values=['Easy','Normal','Medium','Hard','Insane','???'],command=difficultyChoice)
difficulty.pack(pady=10)
difficultyOptions.pack(pady=10)

startButton=ctk.CTkButton(r,width=300,height=200,hover_color='green',text='Start',font=('Copperplate',46),command=startGame)
startButton.pack(pady=20)

r.mainloop()