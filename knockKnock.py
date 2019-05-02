import random #allows random.randint(x,y)

#intro
name = input("Hello, What is your name? ") #Asks user for name and stores in name
menu = ["1. Knock, Knock", "2. Punch line", "3. Riddles", "4. Q/A", "5. Quit"] #declares the different kind of jokes in the menu
jokeType="0" #intialize jokeType for while loop

while(jokeType != "5"): #ask jokes until user wants to quit
    print("\nHey "+ name + ",What kind of joke would you like to hear?") #conversate to user for type of joke
    for y in menu: #loop for amount of y in menu
        print(y) # print y
    jokeType = input("\nEnter number: ") #save jokeType from user input
   

#knock knock
    
    if jokeType is "1":   #user wants a knockknock joke
        print("\nAlright here's your joke, " + name +"\n") #begins telling joke using name
        choice = random.randint(1,3) #chooses random joke
        #knock1
        if choice is 1:
            input("Knock Knock\n") #joke
            x=0 #delcare x for loop to run correctly
            for x in range(0,3): #give the responses to user and ignore input
                input("Banana\n") #joke
                input("Knock Knock\n") #joke
                x = x+1 #increment x so the loop exits successfully

            input("Orange\n")  #joke
            print("Orange you glad I didn't say Banana\n") #joke
        #knock2
        if choice is 2:
            input("Knock Knock\n") #joke
            input("Broken Pencil\n") #joke
            print("Nevermind, it's pointless\n") #joke
        #knock3
        if choice is 3:
            input("Knock Knock\n") #joke
            input("Cows go\n") #joke
            print("No, silly. Cows go Moo!") #joke


#punch line
    if jokeType is "2": #user wants a punch line
        print("\nAlright here's your joke, " + name +"\n") #begins telling joke using name
        choice = random.randint(1,3) #chooses random joke
        #punch1
        if choice is 1:
            print("A farmer in the field with his cows counted 196 of them, but when he rounded them up he had 200\n") #joke
        #punch2
        if choice is 2:
            print("The midget fortune teller who kills his customers is a small medium at large \n") #joke
        #punch3
        if choice is 3:
            print("The dyslexic devil worshipper sold his soul to Santa\n") #joke


#Riddles
    if jokeType is "3": #user wants a riddle
        print("\nAlright here's your joke, " + name +"\n") #begins telling joke using name
        choice = random.randint(1,3) #chooses random joke
        #riddle1
        if choice is 1:
            input("What is Black, White and Red all over?")#joke
            print("A Newspaper\n")#joke
        #riddle2
        if choice is 2:
            input("What begins with T, ends with T and has T in it?")#joke
            print("Teapot\n")#joke
        #riddle3
        if choice is 3:
            input("Where do fish keep their money?")#joke
            print("Riverbank\n")#joke
        
        
#Q/A
    if jokeType is "4": #user wants a Q/A
        print("\nAlright here's your joke, " + name +"\n") #begins telling joke using name
        choice = random.randint(1,3) #chooses random joke
        #Q/A1
        if choice is 1:
            input("What looks like half an apple?")#joke
            print("The other half\n")#joke
        #Q/A2
        if choice is 2:
            input("What do diapers and Politicians have in common?")#joke
            print("They both need changing regularly - for exactly the same reason\n")#joke
        #Q/A3
        if choice is 3:
            input("What is a cow with no legs called?")#joke
            print("Ground Beef\n")#joke

        
#ask user if they want another for another
    newJoke =input("would you like another joke? (y/n):") #ask for another
    if newJoke is "y": #dont quit early
        jokeType = 0 # resets jokeType so it doesnt quit
    else:
        quiT = input("Are you sure you want to quit? (y/n):") #final confirm
        if quiT is "y": #if yes
            jokeType="5" #end loop
            print("Have a marvelous day " + name +"!") #say goodbye
        else:
            jokeType = 0 #repeat while jokeType !=5
            
            
            
        





                
