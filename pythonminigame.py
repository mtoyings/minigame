#import modules
from tkinter import *
import random
import time
import tkinter.messagebox

root = Tk()

#display/window setting
root.title("THE CAPSTONE PROJECT") #title
root.geometry("400x200") #display size
root.configure(bg="gold") #background colour
    
#declaring variables 
timeLeft = 31
score = 0
colour= ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'black', 'brown']
randomcolour = random.choice(colour)
turnctrl = True
turncount = 0
player1 = StringVar()
player2 = StringVar()



#the complete tic-tac-toe game
def tic_tac_toe():
    time.sleep(0.01) #stop operating the code for 0.01 sec
    clear_window() 

    # activate buttons
    def BtnClick (buttons):
        global turnctrl, turncount, player2, player1 
        if buttons["text"] == " " and turnctrl == True:  # makes the button's message = X
            buttons["text"] = "X"
            

            turnctrl = False
            turncount += 1 
            player1 = player1ent.get() + " wins!!" #get name of the player 1
            player2 = player2ent.get() + " wins!!" #get name of player 2
            ResultCheck()

        elif buttons["text"] == " " and turnctrl == False: # makes the button's message = O
            buttons["text"] = "O"
            turnctrl = True
            turncount += 1
            ResultCheck()

        else: #display this message if pressed the pressed button
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "Action not available") 

    # check the result
    def ResultCheck():
        global turnctrl, turncount, player2, player1
        #check result for X
        if (button1 ['text'] == "X" and button2 ['text'] == "X" and button3 ['text'] == "X" or #horizontal line1
            button4 ['text'] == "X" and button5 ['text'] == "X" and button6 ['text'] == "X" or #horizontal line2
            button7 ['text'] == "X" and button8 ['text'] == "X" and button9 ['text'] == "X" or #horizontal line3
            button1 ['text'] == "X" and button4 ['text'] == "X" and button7 ['text'] == "X" or #diagonal top left to bottom right
            button2 ['text'] == "X" and button5 ['text'] == "X" and button8 ['text'] == "X" or #diagonal top right to bottom left
            button3 ['text'] == "X" and button6 ['text'] == "X" and button9 ['text'] == "X" or #vertical column1
            button1 ['text'] == "X" and button5 ['text'] == "X" and button9 ['text'] == "X" or #vertical column2
            button3 ['text'] == "X" and button5 ['text'] == "X" and button7 ['text'] == "X"): #vertical column3

            tkinter.messagebox.showinfo("Tic-Tac-Toe", player1)
            
            
            ResetGame()
          #check result for O  
        elif (button1 ['text'] == "O" and button2 ['text'] == "O" and button3 ['text'] == "O" or #horizontal line1
            button4 ['text'] == "O" and button5 ['text'] == "O" and button6 ['text'] == "O" or  #horizontal line2
            button7 ['text'] == "O" and button8 ['text'] == "O" and button9 ['text'] == "O" or #horizontal line3
            button1 ['text'] == "O" and button4 ['text'] == "O" and button7 ['text'] == "O" or #diagonal top left to bottom right
            button2 ['text'] == "O" and button5 ['text'] == "O" and button8 ['text'] == "O" or #diagonal top right to bottom left
            button3 ['text'] == "O" and button6 ['text'] == "O" and button9 ['text'] == "O" or #vertical column1
            button1 ['text'] == "O" and button5 ['text'] == "O" and button9 ['text'] == "O" or #vertical column2
            button3 ['text'] == "O" and button5 ['text'] == "O" and button7 ['text'] == "O"): #vertical column3
    
            tkinter.messagebox.showinfo("Tic-Tac-Toe", player2)

            
            ResetGame()

        elif turncount == 9: #display "DRAW!" when 9 turns is played (no more space left)

            tkinter.messagebox.showinfo("Tic-Tac-Toe", "DRAW!")

            
            ResetGame()

    #Restart the game
    def ResetGame():
        global turnctrl, turncount, player2, player1
        #make text in every button = " "
        button1["text"] = " "
        button2["text"] = " "
        button3["text"] = " "
        button4["text"] = " "
        button5["text"] = " "
        button6["text"] = " "
        button7["text"] = " "
        button8["text"] = " "
        button9["text"] = " "
        turnctrl = True
        turncount = 0
        player1 = StringVar()
        player2 = StringVar()

    #tic-tac-toe game structure     
    
    #title
    Label(root, text = " T i c 一", font = ("impact", 60, "bold", "italic"), bg = "gold",fg="lime green").grid(row = 0, column = 1)
    Label(root, text = "T a c 一", font = ("impact", 60, "bold", "italic"), bg = "gold",fg="lime green").grid(row = 0, column = 2)
    Label(root, text = " T o e !", font = ("impact", 60, "bold", "italic"), bg = "gold",fg="lime green").grid(row = 0, column = 3, sticky = W)

    #spacer
    Label(root, text = " ", bg = "gold").grid(row=0, column=0, pady=60)

    #label "player 1 (X)"
    player1lab = Label(root, text = "player 1 (X)", bg = "gold",fg="lime green", font = ("courier", 30))
    player1lab.grid(row=1, column=0, sticky = S, padx = 100)

    #entry to input player1's name
    player1ent = Entry(root, width = 15, font = ("courier", 35), justify = "center",fg="lime green")
    player1ent.grid(row=2, column=0, sticky=N)

    #label "player 2 (O)"
    player2lab = Label(root, text = "player 2 (O)", bg = "gold", font = ("courier", 30),fg="lime green")
    player2lab.grid(row=1, column=4, sticky = S, padx = 100)

    #entry to input player2's name
    player2ent = Entry(root, width = 15, font = ("courier", 35), justify = "center",fg="lime green")
    player2ent.grid(row=2, column=4, sticky=N)

    #back to main menu button
    mainbutton = Button(root, text = "Back to Main Menu", font = ("courier", 30) , fg = "lime green", command = mainmenu, width=20)
    mainbutton.grid(row = 4, column = 0, pady=50, sticky=W, padx=25, ipady=2)

    #exit game button
    exitbutton = Button(root, text = "Exit", font = ("courier", 30) , fg = "lime green", width=20, command = root.destroy)
    exitbutton.grid(row = 4, column = 4, sticky=E, padx=40, ipady=2, pady=50)

    
 
    #tic-tac-toe game set up: 3x3 table
    button1= Button(root, text=" ", height = 7, width = 14, font="impact, 20", command = lambda: BtnClick(button1))
    button1.grid(row=1,column=1)

    button2= Button(root, text=" ", height = 7, width = 14, font="impact, 20", command = lambda: BtnClick(button2))
    button2.grid(row=1,column=2)

    button3= Button(root, text=" ", height = 7, width = 14, font="impact, 20", command = lambda: BtnClick(button3))
    button3.grid(row=1,column=3)

    button4= Button(root, text=" ", height = 7, width = 14, font="impact, 20", command = lambda: BtnClick(button4))
    button4.grid(row=2,column=1)

    button5= Button(root, text=" ", height = 7, width = 14, font="impact, 20",command = lambda: BtnClick(button5))
    button5.grid(row=2,column=2)

    button6= Button(root, text=" ", height = 7, width = 14, font="impact, 20",command = lambda: BtnClick(button6))
    button6.grid(row=2,column=3)

    button7= Button(root, text=" ", height = 7, width = 14, font="impact, 20",command = lambda: BtnClick(button7))
    button7.grid(row=3,column=1)

    button8= Button(root, text=" ", height = 7, width = 14, font="impact, 20",command = lambda: BtnClick(button8))
    button8.grid(row=3,column=2)

    button9= Button(root, text=" ", height = 7, width = 14, font="impact, 20", command = lambda: BtnClick(button9))
    button9.grid(row=3,column=3)

    


#activate a complete game colour not the word game
def colour_word_game():
    time.sleep(0.01) #stop operating the code for 0.01 sec
    clear_window()
    initgamemain()
    

#clear all the widgets/window
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

#almost complete code of the game 
def initgamemain():
    time.sleep(0.01) #stop operating the code for 0.01 sec
    global timeLeft, score
    timeLeft = 31
    score = 0
    clear_window()
    #starts the timer + run the game
    def initgame(self):
        if timeLeft == 31:
            timer()
        mainGame()
        
    # main game code + scoring system 
    def mainGame():
        global score
        global timeLeft
        if timeLeft > 0 :
            answerEnt.focus_set()
            
            colourLabel.config(fg = colour[2], text = str(colour[0])) #display the word+colour of the word to answer
            
            if answerEnt.get() == colour[2]: # if the input word is the same as the problem
                score+=1 # increase the score by 1
            
            
                
            
                
            answerEnt.delete(0,20) # clear the input entry for next problem
            
            random.shuffle(colour) # randomize order of list of colours
            
            colourLabel.config(fg = str(colour[2]), text = str(colour[0])) #change colour+word of the problem 
            
            # update the score. 
            scoreLabel.config(text = "Score: " + str(score))
            
        else: 
            clear_window()
            #reset timer
            timeLeft = 31 

            #spacer
            Label(root, text = " \n\n\n\n\n\n\n\n\n\n\n\n", bg = "gold").pack() 

            #result of the game
            Label(root, text = "Congratulation!!\nYou scored " + str(score),fg='lime green', bg = "gold", font = ("courier", 42) ).pack(pady=30)
            
            #play again button
            Button(root, text="Play Again", fg="lime green", font=("courier", 37), command = initgamemain, width = 20).pack(ipady=3)
            
            #back to main menu button
            Button(root, text="Back to Main Menu", fg="lime green", font=("courier", 37), command = mainmenu , width = 20).pack(pady=16, ipady=3)
        


    # timer
    def timer():
        global timeLeft
        if timeLeft > 0:
            timeLeft -=1 #decrease time by one
        timeLabel.config(text= "Time: " + str(timeLeft)) #update time
        timeLabel.after(1000, timer) #re-activate this function after 1 second



    #structure of the colour not the word game: display
    
    #title
    titleLabel = Label(root, text = " # SAY THE COLOUR NOT THE WORD ", bg='gold',fg="lime green", font = ('impact', 43, 'italic', 'bold'))
    titleLabel.pack(pady=25)

    #how to play
    howtoLabel = Label(root, text= "Type the 'colour' of the word, NOT the text! \n\n\n Press ENTER to start ", bg='gold',fg="lime green", font = ('courier', 26))
    howtoLabel.pack()

    #time
    timeLabel = Label(root, text = "Time: ", bg='gold',fg="lime green", font = ('courier', 30))
    timeLabel.pack(anchor="w", pady=20, padx=80)

    #score
    scoreLabel = Label(root, text = "Score: ", bg='gold',fg="lime green", font = ('courier', 30))
    scoreLabel.pack(anchor="w", padx=80)

    #text for the problem
    colourLabel = Label(root, text = " ", font = ('impact', 64), width = 10  )
    colourLabel.pack(pady=30)

    #entry box to answer
    answerEnt = Entry (root, font = ('courier', 45),fg="lime green", justify = "center")
    answerEnt.pack(ipady=5)

    #spacer
    Label(root, text = "\n\n\n ", bg="gold").pack()
   
   #back to main menu button
    Button(root, text = "Back to Main Menu", font = ("courier", 30) , fg = "lime green", command = mainmenu, width =20).pack(anchor=W, padx=25,pady=10, ipady=3)
    #Exit Button
    Button(root, text="Exit", fg="lime green", width=20, command=root.destroy,font = ('courier', 30)).pack(ipady=3, padx=25, anchor=W)




    root.bind('<Return>', initgame)

    answerEnt.pack() 

    # set focus on the entry box 
    answerEnt.focus_set() 


#Main Menu after pressing Play Again
def mainmenu():
    global timeLeft
    clear_window()
    time.sleep(0.01) #stop operating the code for 0.01 sec
    timeLeft = 31


    #MAIN MENU when clicked PLAY AGAIN/BACK TO MAIN MENU
    Label(root, text="\n Welcome to the Python Game \n", fg="lime green", bg="gold", font = ('impact', 72)).pack(fill=X)

    #tic-tac-toe game button
    Button(root, text="Tic - Tac - Toe", width=30, fg="lime green", command= tic_tac_toe , font = ('courier', 40, 'italic')).pack(ipady=3)
    
    #colour not the word game button
    Button(root, text="Say The Colour Not The Word", fg="lime green", width=30, command=colour_word_game,font = ('courier', 40, 'italic')).pack(pady=30,ipady=3)
    
    #Exit Button
    Button(root, text="Exit", fg="lime green", width=30, command=root.destroy,font = ('courier', 40, 'italic')).pack(ipady=3)



#menu display when run code
mainmenu() 

#MAIN MENU
#Label(root, text="\n Welcome to the Python Game \n", fg="lime green", bg="gold", font = ('impact', 72)).pack(fill=X)

##Button(root, text="Tic - Tac - Toe", width=30, fg="lime green", command= tic_tac_toe , font = ('courier', 40, 'italic')).pack(ipady=3)
#Button(root, text="Colour Not The Word", fg="lime green", width=30, command=colour_word_game,font = ('courier', 40, 'italic')).pack(pady=30,ipady=3)
#Button(root, text="Exit", fg="lime green", width=30, command=root.destroy,font = ('courier', 40, 'italic')).pack(ipady=3)





root.mainloop() 


