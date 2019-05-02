from tkinter import *
import random #allows random.randint(x,y)

class App(Tk):
    def __init__(self):
        Tk.__init__(self)

        #declare variables
        self.__teams=["ATL","BOS","BRK","CHA","CHI","CLE","DAL",
                      "DEN","DET","GS","HOU","IND","LAC","LAL",
                      "MEM","MIA","MIL","MIN","NO","NYK","OKC",
                      "ORL","PHI","PHX","POR","SAC","SA","TOR","UTA","WAS"]
        self.__choices=[False]*30
        self.__p1Choices=[False]*30
        self.__p2Choices=[False]*30
        self.__series=1
        self.__gameNumber=1
        self.__p1Wins=0
        self.__p1SeriesWins=0
        self.__p2Wins=0
        self.__p2SeriesWins=0
        self.__lastGame="No last game played"
        self.__counter1=0
        self.__counter2=0
        self.__switch = False
        self.__switchOver = False

        self.addGui()
        self.mainloop()


    def updateData(self):
        #create Toplevel for updating statistics
        self.win1 = Toplevel()
        self.win1.title('Import')
        self.win1.geometry('210x200')
        self.win1.resizable(False,False)
        
        #create some labels that end in Lab
        self.p1SeriesWinsLab = Label(self.win1,text="P1 total series wins:")
        self.p2SeriesWinsLab = Label(self.win1,text="P2 total series wins:")
        self.p1WinsLab = Label(self.win1,text="P1 wins for current series: (0-3)")
        self.p2WinsLab = Label(self.win1,text="P2 wins for current series: (0-3)")
        self.infoLab = Label(self.win1,text="")

        #create some entries that end in New
        self.p1SeriesWinsNew = Entry(self.win1, width = 5)
        self.p2SeriesWinsNew = Entry(self.win1, width = 5)
        self.p1WinsNew = Entry(self.win1, width = 5)
        self.p2WinsNew = Entry(self.win1, width = 5)

        #create optionmenu
        self.teamsMenuVar = StringVar(self)
        self.teamsMenuVar.set("Already played")
        self.teamsMenu = OptionMenu(self.win1,self.teamsMenuVar, *self.getTeams())
        self.teamsMenu.config(state="disabled")

        #add buttons
        self.updateDataButton = Button(self.win1,text="Update",command = self.checkUpdate)
        self.teamsMenuBtn = Button(self.win1,text="Select team",state="disabled",command=self.updateChoices)
        
        #add everything to toplevel
        self.p1SeriesWinsLab.grid(row=0,columnspan=3)
        self.p2SeriesWinsLab.grid(row=1,columnspan=3)
        self.p1WinsLab.grid(row=2,columnspan=3)
        self.p2WinsLab.grid(row=3,columnspan=3)
        self.p1SeriesWinsNew.grid(row=0,column=3)
        self.p2SeriesWinsNew.grid(row=1,column=3)
        self.p1WinsNew.grid(row=2,column=3)
        self.p2WinsNew.grid(row=3,column=3)
        self.updateDataButton.grid(row=4,columnspan=4)
        self.teamsMenu.grid(row=5,columnspan=4)
        self.teamsMenuBtn.grid(row=6,columnspan=4)
        self.infoLab.grid(row=7,columnspan=4)

    def checkUpdate(self):
        try:
            #make sure values are ints
            p1SWN = int(self.getp1SeriesWinsNew()) 
            p2SWN = int(self.getp2SeriesWinsNew())
            p1WINS = int(self.getp1WinsNew())
            p2WINS = int(self.getp2WinsNew())
            if(p1WINS<4 and p2WINS<4 and p1WINS>=0 and p2WINS>=0 and p1SWN>=0 and p2SWN>=0):
                #update variables
                self.setUpdate(p1SWN,p2SWN,p1WINS,p2WINS)
                self.infoLab.config(text="P1 played teams")
                #active/disable some labels and entries
                self.p1SeriesWinsNew.config(state="disabled")
                self.p2SeriesWinsNew.config(state="disabled")
                self.p1WinsNew.config(state="disabled")
                self.p2WinsNew.config(state="disabled")
                self.updateDataButton.config(state="disabled")
                self.teamsMenuBtn.config(state="active")
                self.teamsMenu.config(state="normal")
                total = self.getp1Wins()+self.getp2Wins()
                if(total == 0):
                    self.win1.destroy()
        except ValueError:
            pass
    
    def setUpdate(self,p1SWN,p2SWN,p1WINS,p2WINS):
        #if series has played 6 than or less game 
        self.__series=p1SWN+p2SWN+1
        self.__gameNumber=p1WINS+p2WINS+1
        self.__p1Wins=p1WINS
        self.__p1SeriesWins=p1SWN
        self.__p2Wins=p2WINS
        self.__p2SeriesWins=p2SWN
        self.__p1Choices=[False]*30 #reset choices for p1 for new series
        self.__p2Choices=[False]*30 #reset choices for p2 for new series

        #update original gui
        #clean up when refreshing
        self.p1Menu.grid_forget()
        self.p2Menu.grid_forget()
        self.p1selectedLabel.grid_forget()
        self.p2selectedLabel.grid_forget()
        self.lastGame.grid_forget()
        self.addGui()

    def updateChoices(self):
        teamsPerPerson = self.getp1Wins()+self.getp2Wins() #counter for total games player already in series
        team = self.teamsMenuVar.get() #grab string var
        #if stringvar is changed and counters are less than games in series and right player
        if(team != "Already played" and self.getCounter2() < teamsPerPerson and self.getSwitch() == True and self.getSwitchOver()== False):   
            team = self.teamsMenuVar.get() #gather team from stringvar
            teamNum=self.getTeams().index(team) #get index of team
            if(self.getp2Choices()[teamNum] == False): #if player hasnt selected team yet
                self.setp2Choices(teamNum) #select team for player
                print("p2: {}".format(team)) #testing line
                self.addCounter2() #add 1 to counter
                if(self.getCounter2()==teamsPerPerson): #if player selected all teams
                    self.toggleSwitch() #toggle switch back to true for next time
                    self.toggleSwitchOver() # toggle switchover to end method
                    self.resetCounters() #reset counter for next time
                    self.infoLab.config(text="")
                    #clean up self and destroy import window
                    self.p1Menu.grid_forget()
                    self.p2Menu.grid_forget()
                    self.p1selectedLabel.grid_forget()
                    self.p2selectedLabel.grid_forget()
                    self.lastGame.grid_forget()
                    self.addGui()
                    self.win1.destroy()
        #if stringvar is changed and counters are less than games in series and right player
        if(team != "Already played" and self.getCounter1() < teamsPerPerson and self.getSwitch() == False and self.getSwitchOver()== False):
            team = self.teamsMenuVar.get() #gather team from stringVar
            teamNum=self.getTeams().index(team) #get index of team
            if(self.getp1Choices()[teamNum] == False): #if player hasnt selected team yet
                self.setp1Choices(teamNum) #select team for player
                print("p1: {}".format(team)) #testing line
                self.addCounter1() #add 1 to counter
                if(self.getCounter1()==teamsPerPerson): #if player has selected all teams
                    self.toggleSwitch() #toggle switch to true to pick teams for pl2
                    self.infoLab.config(text="P2 played teams")
                    
    def exportData(self):
        text_file = open("Output.txt", "w") #file for writing to
        text_file.truncate() #delete all current text in file
        #add wins and series wins
        text_file.write("Player 1 series wins: {}\n".format(self.getp1SeriesWins()))
        text_file.write("Player 2 series wins: {}\n".format(self.getp2SeriesWins()))
        text_file.write("Player 1 current wins: {}\n".format(self.getp1Wins()))
        text_file.write("Player 2 current wins: {}\n".format(self.getp2Wins()))
        total = self.getp1Wins()+self.getp2Wins()
        teams1 = [""]*total #string list for return
        c1=0
        #for all teams check if they have every been if yes add to teams1 string
        for x in range(0,30):
            if(self.getp1Choices()[x]==True):
                teams1[c1]= self.getTeams()[x]
                c1+=1
        text_file.write("Player 1 has been: {}\n".format(teams1))        
        teams2 = [""]*total #string list for return
        c2=0
        #for all teams check if they have every been if yes add to teams2 string
        for y in range(0,30):
            if(self.getp2Choices()[y]==True):
                teams2[c2]= self.getTeams()[y]
                c2+=1
        text_file.write("Player 2 has been: {}\n".format(teams2))
        text_file.close()
        
    def addGui(self):
        #name gui
        self.title("NBA 2K Randoms Series App")

        #create MenuBar for importing data
        self.menuBar = Menu(self)
        self.fileMenu = Menu(self, tearoff=0)
        self.fileMenu.add_command(label="Import Data",command=self.updateData)
        self.fileMenu.add_command(label="Export Data",command=self.exportData)
        #self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Close",command=self.destroy)
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)
        

        #create labels for player1, player2, vs., selectedTeams,home/away,gameNumber, series number
        self.p1Label = Label(self,text="Player 1")
        self.p2Label = Label(self,text="Player 2")
        self.p1winsLabel = Label(self,text="Wins: {}".format(self.getp1SeriesWins()))
        self.p2winsLabel = Label(self,text="Wins: {}".format(self.getp2SeriesWins()))
        self.gameLabel = Label(self,text="Game: {}".format(self.getGame()))
        self.seriesLabel = Label(self,text="Series: {}".format(self.getSeries()))
        self.series1Label = Label(self,text="Series score")
        self.seriesRecord = Label(self,text="{0}-{1}".format(self.getp1Wins(),self.getp2Wins()))
        self.vsLabel = Label(self,text="vs.")
        self.p1selectedLabel = Label(self,text="(blank)")
        self.p2selectedLabel = Label(self,text="(blank)")
        self.homeLabel = Label(self,text="Home")
        self.awayLabel = Label(self,text="Away")
        self.scoresLabel=Label(self,text="Final Score:")
        self.mvpLabel=Label(self,text="MVP:")
        self.lastGame=Label(self,text="{}".format(self.getLastGame()))
    
        #declare random teams option menus for away and home users
        #set stringVar for p1 and p2
        self.p1stringVar = StringVar(self)
        self.p1stringVar.set("Randoms")
        self.p2stringVar = StringVar(self)
        self.p2stringVar.set("Randoms")
        p1Teams =self.assignTeams(1)
        self.p1Menu = OptionMenu(self,self.p1stringVar, p1Teams[0],p1Teams[1],p1Teams[2])
        p2Teams =self.assignTeams(2)
        self.p2Menu = OptionMenu(self,self.p2stringVar, p2Teams[0],p2Teams[1],p2Teams[2])
        
        #declare confirm and suicide bottoms for both users and a start game button
        self.confirm1 = Button(self,text="Select",command=self.selected1)
        self.suicide1btn = Button(self,text="Suicide",command=self.suicide1)
        self.confirm2 = Button(self,text="Select",command=self.selected2)
        self.suicide2btn = Button(self,text="Suicide",command=self.suicide2)
        self.readyBtn = Button(self,text="Start Game",command=self.ready)
        self.finishBtn = Button(self,text="Game Over",command=self.gameOver,state="disabled")

        #declare textbox for scores
        self.p1Score = Entry(self,state="disabled",width = 5)
        self.p2Score = Entry(self,state="disabled",width = 5)
        self.mvpPlayer = Entry(self,state="disabled",width = 18)

        #send all labels,buttons, and option menus to grid
        self.config(menu=self.menuBar)
        self.p1Label.grid(row=0,column=0)
        self.seriesLabel.grid(row=0,column=1,columnspan=3)
        self.p2Label.grid(row=0,column=4)
        self.p1winsLabel.grid(row=1,column=0)
        self.gameLabel.grid(row=1,column=1,columnspan=3)
        self.p2winsLabel.grid(row=1,column=4)
        self.p1Menu.grid(row=2,column=0)
        self.series1Label.grid(row=2,column=1,columnspan=3)
        self.p2Menu.grid(row=2,column=4)
        self.confirm1.grid(row=3,column=0)
        self.seriesRecord.grid(row=3,column=1,columnspan=3)
        self.confirm2.grid(row=3,column=4)
        self.suicide1btn.grid(row=4,column=0)
        self.suicide2btn.grid(row=4,column=4)
        self.p1selectedLabel.grid(row=5,column=1)
        self.vsLabel.grid(row=5,column=2,)
        self.p2selectedLabel.grid(row=5,column=3)
        self.readyBtn.grid(row=4,column=1,columnspan=3)
        self.scoresLabel.grid(row=7,column=0)
        self.p1Score.grid(row=7,column=1)
        self.p2Score.grid(row=7,column=3)
        self.mvpLabel.grid(row=8,column=1)
        self.mvpPlayer.grid(row=8,column=2)
        self.finishBtn.grid(row=9,column=1,columnspan=3)
        self.lastGame.grid(row=10,column=0,columnspan=5)
        
    def assignTeams(self, who):
        teams = [""]*3 #string list for return
        x=0 #until 3 teams are picked
        while(x < 3): #pick 3 teams
            num = random.randint(0,29) #pick random team 0-29
            if(who==1): #if player1
                if(self.getChoices()[num] == False and self.getp1Choices()[num] == False): #if not in current choices and player hasnt been in series
                    teams[x] = self.getTeams()[num] #add team to list for 3 random teams
                    self.setChoices(num) #set choices at num to true so cant pick team again this game
                    x=x+1 #count team added
                if(self.getp1Choices()[num] == True):
                    print("player1 already {} in series".format(self.getTeams()[num]))
            if(who==2): #if player2
                if(self.getChoices()[num] == False and self.getp2Choices()[num] == False): #if not in current choices and player hasnt been in series
                    teams[x] = self.getTeams()[num]#add team to list for 3 random teams
                    self.setChoices(num)#set choices at num to true so cant pick team again this game
                    x=x+1 #count team added
                if(self.getp2Choices()[num] == True):
                    print("player2 already {} in series".format(self.getTeams()[num]))

        print(teams)
        return teams
    
    def gameOver(self):#check bottom
        cGame = ""
        try:
            p1 = int(self.getp1Score()) #make sure scores are ints
            p2 = int(self.getp2Score())
            cGame = self.whoWon(p1,p2) #send scores to see who won
        except ValueError:
            pass
        if((cGame == "p1" or cGame == "p2") and self.getmvpPlayer().isalpha() == True ): # if given a winner and mvp is text
            #update lastGame string with data from last game
            self.setLastGame(p1,self.getp1selectedLabel(),p2,self.getp2selectedLabel(),self.getmvpPlayer()) 
            #disable some entrys and btns
            self.setGameSeries(cGame)#check for winner of series(4 wins), if so start new series and add win to player
        else:
            print("Final score only accepts ints and MVP only accepts all text")

    def ready(self): #check top/open bottom
        #if choices arent set catch ValueError
        try:
            self.setplayerChoices()
            #close ready btn
            self.readyBtn.config(state="disabled")#disable button
            #activate btn and open entries for text
            self.finishBtn.config(state="active")
            self.p1Score.config(state="normal")
            self.p2Score.config(state="normal")
            self.mvpPlayer.config(state="normal")
        except ValueError:
            print("Teams are not set for both teams")        
  
    def selected1(self):
        if(self.p1stringVar.get() != "Randoms"): #if stringVar is changed from default 
            team = self.p1stringVar.get() #get selected team
            self.p1selectedLabel.config(text=team) #set label to team
            self.suicide1btn.config(state="disabled") #disable button
            self.confirm1.config(state="disabled") #disable button
            self.p1Menu.config(state="disabled") #disable button

    def selected2(self):
        if(self.p2stringVar.get() != "Randoms"): #if stringVar is changed from default 
            team = self.p2stringVar.get() #get selected team
            self.p2selectedLabel.config(text=team) #set label to team
            self.suicide2btn.config(state="disabled") #disable button
            self.confirm2.config(state="disabled") #disable button
            self.p2Menu.config(state="disabled") #disable button

    def setGameSeries(self,winner):
        self.setGameNumber() #update gameNumber
        self.setWin(winner) #add win to p1 or p2 total wins in current series
        if(self.getp1Wins()==4 or self.getp2Wins()==4): #if p1 or p2 won their 4th game set new series
            self.setNoWins() #clear current series wins for both player
            self.setSeries(winner) #give series win to winner

        #forgot some from grid to clean it up
        self.p1Menu.grid_forget()
        self.p2Menu.grid_forget()
        self.p1selectedLabel.grid_forget()
        self.p2selectedLabel.grid_forget()
        self.lastGame.grid_forget()
        self.addGui()

    def setplayerChoices(self):
        team1 = self.getp1selectedLabel() #get team from label
        num1 = self.getTeams().index(team1) #find index of that team in teams
        self.setp1Choices(num1) #say player1 was team
        team2 = self.getp2selectedLabel() #get team from label
        num2 = self.getTeams().index(team2) #find index of that team in teams
        self.setp2Choices(num2) #say player2 was team
        self.__choices=[False]*30 #reset game choices for next game
 
    def suicide1(self):
        team = "" #string for return
        x=0 #until 1 teams are picked
        while(x < 1): #pick 1 teams
            num = random.randint(0,29) #pick random team 0-29
            if(self.getChoices()[num] == False and self.getp1Choices()[num] == False): #if not in current choices and player hasnt been in series
                team = self.getTeams()[num] #set string to selected string
                self.setChoices(num) #set choices at num to true so cant pick team again this game
                x=x+1 #count team added
        print(team)
                
        #disable buttons and set selected label    
        self.suicide1btn.config(state="disabled")
        self.confirm1.config(state="disabled")
        self.p1Menu.config(state="disabled")
        self.p1selectedLabel.config(text=team)

    def suicide2(self):
        team = "" #string for return
        x=0 #until 1 teams are picked
        while(x < 1): #pick 1 teams
            num = random.randint(0,29) #pick random team 0-29
            if(self.getChoices()[num] == False and self.getp2Choices()[num] == False): #if not in current choices and player hasnt been in series
                team = self.getTeams()[num] #set string to selected string
                self.setChoices(num) #set choices at num to true so cant pick team again this game
                x=x+1 #count team added
        print(team)
                
        #disable buttons and set selected label    
        self.suicide2btn.config(state="disabled")
        self.confirm2.config(state="disabled")
        self.p2Menu.config(state="disabled")
        self.p2selectedLabel.config(text=team)

    def whoWon(self, p1, p2):
        completeGame = ""
        if(p1>p2): #if player one scored more
            completeGame = "p1" #game has a winner
        elif(p1<p2):
            completeGame = "p2" #game has a winner
        return completeGame #return winner


    #GET METHODS   
    def getGame(self):
        return self.__gameNumber #return game variable
    def getmvpPlayer(self):
        return self.mvpPlayer.get() #return mvp player from entry box
    def getChoices(self):
        return self.__choices #return choices variable
    def getLastGame(self):
        return self.__lastGame #return lastGame string
    def getp1Choices(self):
        return self.__p1Choices #return p1Choices variable
    def getp2Choices(self):
        return self.__p2Choices #return p2Choices variable
    def getp1Score(self):
        return self.p1Score.get() #return p1score from entry box
    def getp2Score(self):
        return self.p2Score.get() #return p2score from entry box
    def getp1selectedLabel(self):
        return self.p1selectedLabel.cget("text") #return p1 team from p1selected label
    def getp2selectedLabel(self):
        return self.p2selectedLabel.cget("text") #return p2 team from p2selected label
    def getp1SeriesWins(self):
        return self.__p1SeriesWins #return p1Wins variable
    def getp2SeriesWins(self):
        return self.__p2SeriesWins #return p2Wins variable
    def getp1Wins(self):
        return self.__p1Wins #return p1Wins variable
    def getp2Wins(self):
        return self.__p2Wins #return p2Wins variable
    def getSeries(self):
        return self.__series #return series variable
    def getTeams(self):
        return self.__teams #return teams variable

    #Get methods for Toplevel
    def getp1SeriesWinsNew(self):
        return self.p1SeriesWinsNew.get() #return p1 series wins from user
    def getp2SeriesWinsNew(self):
        return self.p2SeriesWinsNew.get() #return p2 series wins from user
    def getp1WinsNew(self):
        return self.p1WinsNew.get() #return p1 wins for current series
    def getp2WinsNew(self):
        return self.p2WinsNew.get() #return p2 wins for current series
    def getCounter1(self):
        return self.__counter1
    def getCounter2(self):
        return self.__counter2
    def getSwitch(self):
        return self.__switch
    def getSwitchOver(self):
        return self.__switchOver

    def toggleSwitch(self):
        if(self.getSwitch() == True):
            self.__switch = False
            print("switch to False")
        else:
            self.__switch = True
            print("switch to True")

    def toggleSwitchOver(self):
        if(self.getSwitchOver() == False):
            self.__switchOver = True
            print("ending loop")
        else:
            self.__switchOver = False
    
    
    def addCounter1(self):
        self.__counter1 += 1
    def addCounter2(self):
        self.__counter2 += 1

    def resetCounters(self):
        self.__counter1=0
        self.__counter2=0
        
    def setChoices(self,num):
        self.__choices[num] = True #set choices at num variable to true

    def setLastGame(self,p1score,p1team,p2score,p2team,mvp):
        gameInfo="{1} {0} vs. {3} {2}   MVP: {4}".format(p1score,p1team,p2score,p2team,mvp.upper())
        self.__lastGame = gameInfo
        
    def setp1Choices(self,num):
        self.__p1Choices[num] = True #set p1choices at num variable to true
    def setp2Choices(self,num):
        self.__p2Choices[num] = True #set p2choices at num variable to true
        
    def setWin(self,who):
        if(who == "p1"): #if player one wins
            print("player 1 wins game!")
            self.__p1Wins +=1 #add one win to p1 win total
        if(who == "p2"): #if player two wins
            print("player 2 wins game!")
            self.__p2Wins +=1 #add one win to p2 win total

    def setNoWins(self):
        self.__p1Wins =0#no wins in new series
        self.__p2Wins =0#no wins in new series
        self.__gameNumber=1 #game 1 for new series
        
    def setGameNumber(self):
        self.__gameNumber +=1 #add one to game number
        
    def setSeries(self,who):
        self.__series +=1 #add one to total series number
        if(who == "p1"):
            self.__p1SeriesWins+=1 #add win to series total for p1
            print("player 1 wins series!")
        if(who == "p2"):
            self.__p2SeriesWins+=1 #add win to series total for p2
            print("player 2 wins series!")
        self.__p1Choices=[False]*30 #reset choices for p1 for new series
        self.__p2Choices=[False]*30 #reset choices for p2 for new series
        

def main():
  app = App()

if __name__ == "__main__":
  main()
