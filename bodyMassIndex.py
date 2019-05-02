from tkinter import *

class App(Tk):
    def __init__(self):
        Tk.__init__(self)

        #name gui
        self.title("Unit Converter")

        #set window size and make it unadjustable
        #self.geometry('20x140')
        self.resizable(width=False, height=False)
    
        #create labels for distance,temp,volume
        self.tempLabel = Label(self,text="Temperature:")
        self.tempAnsLabel = Label(self,text="Please enter a number and unit to convert to all temperatures")
        self.distanceLabel = Label(self,text="Distance:")
        self.distAnsLabel = Label(self,text="Please enter a number and unit to convert to all distances")
        self.volLabel = Label(self,text="Volume:")
        self.volAnsLabel = Label(self,text="Please enter a number and unit to convert to all volumes")
        
        #create text boxes for distance,temp,volume
        self.tempTextbox = Entry(self)
        self.distTextbox = Entry(self)
        self.volTextbox = Entry(self)


        #create optionmenu bar
        self.tempstringVar = StringVar(self)
        self.tempstringVar.set("units")
        self.tempMenu = OptionMenu(self,self.tempstringVar, "°Kelvin","°Celsius","°Fahrenheit")
        self.diststringVar = StringVar(self)
        self.diststringVar.set("units")
        self.distMenu = OptionMenu(self,self.diststringVar, "Meters","Feet","Miles")
        self.volstringVar = StringVar(self)
        self.volstringVar.set("units")
        self.volMenu = OptionMenu(self,self.volstringVar, "Pints","Quarts","Gallons")

        #create calculations button
        self.calctempBtn = Button(self,text="Convert Temperatures",command=self.calcTemp)
        self.calcdistBtn = Button(self,text="Convert Distances",command=self.calcDist)
        self.calcvolBtn = Button(self,text="Convert Volumes",command=self.calcVol)

        #add labels,textboxes and button to grid
        self.tempLabel.grid(row=0,column=0)
        self.tempTextbox.grid(row=0,column=1)
        self.tempMenu.grid(row=0,column=2)
        self.tempAnsLabel.grid(row=1,columnspan=3)
        self.calctempBtn.grid(row=2,column=1)
        self.distanceLabel.grid(row=3,column=0)
        self.distTextbox.grid(row=3,column=1)
        self.distMenu.grid(row=3,column=2)
        self.distAnsLabel.grid(row=4,columnspan=3)
        self.calcdistBtn.grid(row=5,column=1)
        self.volLabel.grid(row=6,column=0)
        self.volTextbox.grid(row=6,column=1)
        self.volMenu.grid(row=6,column=2)
        self.volAnsLabel.grid(row=7,columnspan=3)
        self.calcvolBtn.grid(row=8,column=1)
        
        #keep running
        self.mainloop()
    def calcDist(self):
        distUsed = self.getdistStringVar() #returns stringvar in temp menu
        newData="Please enter a number and unit to convert to all distances" #data for updating label 
        try:
            num = self.getdistTextbox() #returns disttextbox
            num = float(num)
            #calc dist given m
            if(distUsed == "Meters"):
                ft=num*3.2808398950131
                mi=num*0.00062137119223733
                newData = "Meters: {0:.2f}, Feet: {1:.2f}, Miles: {2:.4f}".format(num,ft,mi)    
            #calc dist given ft
            elif(distUsed == "Feet"):
                m=num*0.3048
                mi=num*0.00018939393939394
                newData = "Meters: {0:.2f}, Feet: {1:.2f}, Miles: {2:.4f}".format(m,num,mi)
            #calc dist given miles
            elif(distUsed == "Miles"):
                m=num*1609.344
                ft=num*5280
                newData = "Meters: {0:.2f}, Feet: {1:.2f}, Miles: {2:.4f}".format(m,ft,num)
        except TypeError and ValueError:
            pass
        self.distAnsLabel.config(text=newData)
            
    def calcTemp(self):
        tempUsed = self.gettempStringVar() #returns stringvar in temp menu
        newData="Please enter a number and unit to convert to all temperatures" #data for updating label 
        try:
            num = self.gettempTextbox() #returns temptextbox
            num = float(num)
            #calc temps given k
            if(tempUsed=="°Kelvin"):
                f = (num-273.15)*1.8+32
                c = num-273.15
                newData="Kelvin: {0:.2f}, Celsius: {1:.2f}, Fahrenheit: {2:.2f}".format(num,c,f)
            #calc temps given c
            elif(tempUsed=="°Celsius"):
                f = (num*1.8)+32
                k = num +273.15
                newData="Kelvin: {0:.2f}, Celsius: {1:.2f}, Fahrenheit: {2:.2f}".format(k,num,f)
            #calc temps given f 
            elif(tempUsed=="°Fahrenheit"):
                c = (num-32)*(5/9)
                k  = (num-32)*(5/9)+273.15
                newData="Kelvin: {0:.2f}, Celsius: {1:.2f}, Fahrenheit: {2:.2f}".format(k,c,num)
        except TypeError and ValueError:
            pass
        self.tempAnsLabel.config(text=newData)

    def calcVol(self):
        volUsed = self.getvolStringVar() #returns stringvar in vol menu
        newData="Please enter a number and unit to convert to all volumes" #data for updating label 
        try:
            num = self.getvolTextbox() #returns voltextbox
            num = float(num)
            #calc temps given p
            if(volUsed=="Pints"):
                q = num*.5
                g = num*.125
                newData="Pints: {0:.2f}, Quarts: {1:.2f}, Gallons: {2:.3f}".format(num,q,g)
            #calc temps given q
            elif(volUsed=="Quarts"):
                p = num*2
                g = num*.25
                newData="Pints: {0:.2f}, Quarts: {1:.2f}, Gallons: {2:.3f}".format(p,num,g)
            #calc temps given g 
            elif(volUsed=="Gallons"):
                p = num*8
                q  = num*4
                newData="Pints: {0:.2f}, Quarts: {1:.2f}, Gallons: {2:.3f}".format(p,q,num)
        except TypeError and ValueError:
            pass
        self.volAnsLabel.config(text=newData)
            
    def getdistStringVar(self):
        return self.diststringVar.get() #returns string variable in dist menu
    def getdistTextbox(self):
        return self.distTextbox.get() #returns value inside of distTextbox
    def gettempStringVar(self):
        return self.tempstringVar.get() #returns string variable in temp menu
    def gettempTextbox(self):
        return self.tempTextbox.get() #returns value inside of tempTextbox
    def getvolStringVar(self):
        return self.volstringVar.get() #returns string variable in vol menu
    def getvolTextbox(self):
        return self.volTextbox.get() #returns value inside of volTextbox
        
def main():
  app = App()

if __name__ == "__main__":
  main()
