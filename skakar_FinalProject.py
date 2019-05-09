'''
Fall 2016
CSCI 230
Final Project : Game
Made by Sundeep Kakar
'''

from tkinter import *                       #importing module  

class Game(Tk):                                                                                                         #Class Game 

    def __init__(self):                     #init function to create all widgets in the tk window
        Tk.__init__(self)

        global count
        count = True                                                                                                                        
        
        Label(self, text = "=-=-=-=-=-HUNT FOR KING REBET!-=-=-=-=-=", font=("Times New Roman", 30)).grid(row = 0, column = 0, columnspan = 2)  #Label displays game name

        self.story = StringVar()                                                                                            #This is done so it can be updated later in the program
        self.story.set("Welcome to the game. Your aim is to find King Rebet, who stole your shrink ray and get it back.")
        Label(self, textvariable = self.story).grid(row = 1, column = 0, columnspan = 2)                    #creating label for story
        
        self.story2 = StringVar()
        self.story2.set("(Make a choice from the given options and Click *Continue* twice)")
        Label(self, textvariable = self.story2).grid(row = 2, column = 0, columnspan = 2)                   #creating label for story (line 2)

        global ch1                          #This is done so the radio button text values can be updated later in the program
        ch1 = StringVar()
        ch1.set("Play")
        global ch2
        ch2 = StringVar()
        ch2.set(" ")
        global ch3
        ch3 = StringVar()
        ch3.set(" ")

        self.ask = StringVar()
        self.ask.set("What do you do :")
        Label(self, textvariable = self.ask).grid(row = 4, column = 0)                                              #creating radio buttons
        self.chVar = IntVar()
        choice1 = self.radRadio1 = Radiobutton(self, textvariable = ch1, variable = self.chVar, value = 1)
        self.radRadio1.grid(row = 4, column = 1, columnspan = 2)
        choice2 = self.radRadio2 = Radiobutton(self, textvariable = ch2, variable = self.chVar, value = 2)
        self.radRadio2.grid(row = 5, column = 1, columnspan = 2)
        choice3 = self.radRadio3 = Radiobutton(self, textvariable = ch3, variable = self.chVar, value = 3)
        self.radRadio3.grid(row = 6, column = 1, columnspan = 2)


        self.contB = self.btnButtonB2 = Button(self, text = "Continue", command = self.Intro)           #creating Continue button
        self.btnButtonB2.grid(row = 9, column = 0, columnspan = 2)

        self.btnButtonQ = Button(self, text = "Quit", command = self.Quit)                              #creating quit button
        self.btnButtonQ.grid(row = 9, column = 1, columnspan = 2)

        Label(self, text = "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=", font=("Times New Roman", 30)).grid(row = 10, column = 0, columnspan = 2)
        
        self.mainloop()

    def Quit(self):         #Function destroys tk window
        self.destroy()

    def Get_Choice(self):   #Function gets and returns value of the radio button chosen
        a = self.chVar.get()
        return str(a)            

    def Intro(self):                                                                                                                                                    #Function called when user clicks Play 
        self.story.set("You have ventured out to the Planet Xenos. You are in search of the dreaded King Rebet who stole your SHRINK RAY.")                             #Set story
        self.story2.set("You get out of your ship to find yourself on a cliff side. Your spaceship is overheating and you can't fly it for the rest of the trip.")      

        ch1.set("Check BackPack")                                                                                                                                       #Set all the choices
        ch2.set("Inspect Spaceship")
        ch3.set("Look around")

        self.Desel()
        choice = self.Get_Choice()
        if choice == '1':                                                                                                                               #if elif statements execute for valid radio button entry 
            self.story.set("Your Backpack contains rations, a Photon Rifle, some extra cartridges, a small lightsaber dagger, and your hover skates.")
            self.story2.set(" ")
        elif choice == '2':
            self.story.set("Your spaceship, despite being brand new, is steaming like hot soup!")
            self.story2.set("You just have to give it a rest and continue on foot, for now.")
        elif choice == '3':
            self.contB.grid_forget()                                                                        #previous continue button is deleted and replaced by a new one with different command
            self.contB = self.btnButtonB2 = Button(self, text = "Continue", command = self.Lookaround)
            self.btnButtonB2.grid(row = 9, column = 0, columnspan = 2)

    def Desel(self):                                                                                #This function stops the previous radio button value from going through when a new function is called.
        global count                
        if count == True:                       #If the value of the previous radio button has gone through once, the if statement just changes value of count 
            if str(self.chVar.get()) == '1':        #If statements to deselect previously selected radio button
                self.radRadio1.deselect()
            elif str(self.chVar.get()) == '2':
                self.radRadio2.deselect()
            elif str(self.chVar.get()) == '3':
                self.radRadio3.deselect()
            count = False                           #Count is set to False at last so that the same value doesn't go through twice.
        else:
            count = True                            

    def Lookaround(self):
        self.story.set("There are three paths you see. One leads to a small Village, another leads to a Lake,")         #Update the story
        self.story2.set("and the last one leads up to the Gromsby Mountains")
        ch1.set("Walk to the Lake")                                                                                     #Update all the choices
        ch2.set("Hike up the Gromsby Mountains")
        ch3.set("Go to the Village")
        self.Desel()                                                                                                    #Function called to deselect previously selected radio button
        choice = self.Get_Choice()
        if choice == '1':    
            self.contB.grid_forget()                                                                #previous continue button is deleted and replaced by a new one with different command
            self.contB = self.btnButtonB2 = Button(self, text = "Continue", command = self.Lake)            
            self.btnButtonB2.grid(row = 9, column = 0, columnspan = 2)
        elif choice == '2':
            self.contB.grid_forget()
            self.contB = self.btnButtonB2 = Button(self, text = "Continue", command = self.Mount)
            self.btnButtonB2.grid(row = 9, column = 0, columnspan = 2)
        elif choice == '3':
            self.contB.grid_forget()
            self.contB = self.btnButtonB2 = Button(self, text = "Continue", command = self.Village)
            self.btnButtonB2.grid(row = 9, column = 0, columnspan = 2)

    def Village(self):
        print("Village")
        self.story.set("You reach the Village. It's small and simple. One cannot see many people on the streets. There is an armory.")  #Update the story
        self.story2.set("There is a podium where the hologram of the Mayor stands. He's open for questions. ")
        ch1.set("Talk to Mayor")                                                                                                        #Update all the choices
        ch2.set("Go to the Armory")
        ch3.set("Go back")
        self.Desel()
        choice = self.Get_Choice()
        if choice == '1':    
            self.contB.grid_forget()                                                                    #previous continue button is deleted and replaced by a new one with different command
            self.contB = self.btnButtonB2 = Button(self, text = "Continue", command = self.Mayor)
            self.btnButtonB2.grid(row = 9, column = 0, columnspan = 2)
        elif choice == '2':
            self.contB.grid_forget()
            self.contB = self.btnButtonB2 = Button(self, text = "Continue", command = self.Mount)
            self.btnButtonB2.grid(row = 9, column = 0, columnspan = 2)
        elif choice == '3':
            self.contB.grid_forget()
            self.contB = self.btnButtonB2 = Button(self, text = "Continue", command = self.Lookaround)
            self.btnButtonB2.grid(row = 9, column = 0, columnspan = 2)

    def Mayor(self):
        self.story.set("You walk up to the Mayor. He says cheerfully, 'Hello and welcome to the Village of Xen'ja! Can I help you with something?'")        #Update the story
        self.story2.set("You question the hologram about Rebet's whereabouts. His smile turns upside down and suggests you to look beyond the Mountains.")
        ch1.set("Walk to the Mountains")                                                                                                                    #Update all the choices
        ch2.set("Go to the Armory")
        ch3.set("Go back")
        self.Desel()
        choice = self.Get_Choice()
        if choice == '1':    
            self.contB.grid_forget()                                                                    #previous continue button is deleted and replaced by a new one with different command
            self.contB = self.btnButtonB2 = Button(self, text = "Continue", command = self.Mount)
            self.btnButtonB2.grid(row = 9, column = 0, columnspan = 2)
        elif choice == '2':
            self.contB.grid_forget()
            self.contB = self.btnButtonB2 = Button(self, text = "Continue", command = self.Armory)
            self.btnButtonB2.grid(row = 9, column = 0, columnspan = 2)
        elif choice == '3':
            self.contB.grid_forget()
            self.contB = self.btnButtonB2 = Button(self, text = "Continue", command = self.Lookaround)
            self.btnButtonB2.grid(row = 9, column = 0, columnspan = 2)
    
    def Armory(self):
        #print("Armory")
        self.story.set("You make your way to the front of the Armory. There is a humanoid robot standing. He greets you,'Hello Sir. What can I do for you?'")           #Update the story
        self.story2.set("You take a look at all the stuff you can purchase. You just have enough for one item. You might need something to help you against Rebet.")
        ch1.set("Buy LaserVest and progress to the mountains")                                                                                                          #Update all the choices
        ch2.set("Buy Incendiary bullets for your Photon Rifle and progress to the mountains")
        ch3.set("Leave without purchase")
        self.Desel()
        choice = self.Get_Choice()
        if choice == '1':
            self.contB.grid_forget()                                                                    #previous continue button is deleted and replaced by a new one with different command
            self.contB = self.btnButtonB2 = Button(self, text = "Continue", command = self.Mount)
            self.btnButtonB2.grid(row = 9, column = 0, columnspan = 2)
        elif choice == '2':
            self.contB.grid_forget()
            self.contB = self.btnButtonB2 = Button(self, text = "Continue", command = self.Mount)
            self.btnButtonB2.grid(row = 9, column = 0, columnspan = 2)
        elif choice == '3':
            self.contB.grid_forget()
            self.contB = self.btnButtonB2 = Button(self, text = "Continue", command = self.Mayor)
            self.btnButtonB2.grid(row = 9, column = 0, columnspan = 2)
        
    def Lake(self):
        #print("Lake")
        self.story.set("The Lake is highly acidic. There's a very old laser bridge going across. Looks like ancient technology from 2090")      #Update the story
        self.story2.set("You look through your bag. ")
        ch1.set("Use the Bridge")                                                                                                               #Update all the choices
        ch2.set("Use hover boots")
        ch3.set("Go back")
        self.Desel()
        choice = self.Get_Choice()
        if choice == '1':    
            self.contB.grid_forget()                                                                    #previous continue button is deleted and replaced by a new one with different command
            self.contB = self.btnButtonB2 = Button(self, text = "Continue", command = self.Bridge)
            self.btnButtonB2.grid(row = 9, column = 0, columnspan = 2)
        elif choice == '2':
            self.contB.grid_forget()
            self.contB = self.btnButtonB2 = Button(self, text = "Continue", command = self.Boots)
            self.btnButtonB2.grid(row = 9, column = 0, columnspan = 2)
        elif choice == '3':
            self.contB.grid_forget()
            self.contB = self.btnButtonB2 = Button(self, text = "Continue", command = self.Lookaround)
            self.btnButtonB2.grid(row = 9, column = 0, columnspan = 2)

    def Boots(self):
        #print("Boots")
        self.story.set("Since you chose to use your boots instead of the Bridge, you attempt to hover inches over the acidic lake. Your boots seem to be malfunctioning.")      #Update the story
        self.story2.set("The liquid seems to be corroding your boots. Just inches before the shore, your boots give up and you fall in the acidic lake. You Die.")
        self.ask.set("YOU LOST! WELL PLAYED")
        ch1.set("Thanks For Playing!")                                                                                                                                          #Update all the choices
        ch2.set("Game by : SUNDEEP KAKAR")
        ch3.set("CSCI 230 - Professor : A.Harris")  
        self.contB.grid_forget()                        #To hide Continue button since the game ended for the user

    def Bridge(self):
        #print("Bridge")
        self.story.set("Just as you observed, the Bridge was rickety and unstable. You reach the middle of the Bridge before the Laser web collapses.")     #Update the story
        self.story2.set("You fall into the acidic lake and slowly decay off into the deadly grey liquid.")
        self.ask.set("YOU LOST! WELL PLAYED")
        ch1.set("Thanks For Playing!")                                                                                                                      #Update all the choices
        ch2.set("Game by : SUNDEEP KAKAR")
        ch3.set("CSCI 230 - Professor : A.Harris") 
        self.contB.grid_forget()                        #To hide Continue button since the game ended for the user
       
    def Valley(self):
        #print("Bridge")
        self.story.set("You start your journey through the valley. Half way, you feel the ground shake. You see robotic limbs coming out the ground.")      #Update the story
        self.story2.set("This, infact, is a robot graveyard. You try to run but they catch you and pull you down. You're dead.")
        self.ask.set("YOU LOST! WELL PLAYED")
        ch1.set("Thanks For Playing!")                                                                                                                      #Update all the choices
        ch2.set("Game by : SUNDEEP KAKAR")
        ch3.set("CSCI 230 - Professor : A.Harris")  
        self.contB.grid_forget()                    #To hide Continue button since the game ended for the user

    def Mount(self):
        #print("Mount")
        self.story.set("You walk to the great Gromsby Mountain. There is nothing to be seen but stone and rubble around you. On walking a bit further, you spot something.")                    #Update the story
        self.story2.set("There is a huge Valley in front of you. There's something about it that you find fishy, but that's the shortest route. There is a climber's way up the mountain too.")
        ch1.set("Climb the Mountain")                                                                                                                                                           #Update all the choices
        ch2.set("Go through the Valley")
        ch3.set("Go back")
        self.Desel()
        choice = self.Get_Choice()
        if choice == '1':    
            self.contB.grid_forget()                                                                        #previous continue button is deleted and replaced by a new one with different command
            self.contB = self.btnButtonB2 = Button(self, text = "Continue", command = self.ClimbMount)
            self.btnButtonB2.grid(row = 9, column = 0, columnspan = 2)
        elif choice == '2':
            self.contB.grid_forget()
            self.contB = self.btnButtonB2 = Button(self, text = "Continue", command = self.Valley)
            self.btnButtonB2.grid(row = 9, column = 0, columnspan = 2)
        elif choice == '3':
            self.contB.grid_forget()
            self.contB = self.btnButtonB2 = Button(self, text = "Continue", command = self.Village)
            self.btnButtonB2.grid(row = 9, column = 0, columnspan = 2)

    def ClimbMount(self):
        #print("Mount")
        self.story.set("You climb up the Mountain. There's a cave which leads down to somewhere. You look down the cave, and suddenly, you hear Rebet's Roar.")         #Update the story
        self.story2.set("You know you have to go down there.")
        ch1.set("Go in the Cave")                                                                                                                                       #Update all the choices
        ch2.set("Go back to the Valley")
        ch3.set("Go back")
        self.Desel()
        choice = self.Get_Choice()
        if choice == '1':    
            self.contB.grid_forget()                                                                    #previous continue button is deleted and replaced by a new one with different command
            self.contB = self.btnButtonB2 = Button(self, text = "Continue", command = self.Cave)
            self.btnButtonB2.grid(row = 9, column = 0, columnspan = 2)
        elif choice == '2':
            self.contB.grid_forget()
            self.contB = self.btnButtonB2 = Button(self, text = "Continue", command = self.Valley)
            self.btnButtonB2.grid(row = 9, column = 0, columnspan = 2)
        elif choice == '3':
            self.contB.grid_forget()
            self.contB = self.btnButtonB2 = Button(self, text = "Continue", command = self.Village)
            self.btnButtonB2.grid(row = 9, column = 0, columnspan = 2)

    def Cave(self):
        #print("Cave")
        self.story.set("You slide down the cave. The cave opens up into a huge swamp. You land in the slime covered mud, inches away from the actual acid water.")              #Update the story
        self.story2.set("You look in front of you and you spot the Giant Frog-like creature they call KING REBET! He's 20 ft big and he looks at you with his huge eyes...")
        ch1.set("Stand up cautiously")                                                                                                                                          #Update all the choices
        ch2.set("Reach for your Photon Rifle")
        ch3.set("Look around")
        self.Desel()
        choice = self.Get_Choice()
        if choice == '1':    
            self.contB.grid_forget()                                                                    #previous continue button is deleted and replaced by a new one with different command
            self.contB = self.btnButtonB2 = Button(self, text = "Continue", command = self.Standup)
            self.btnButtonB2.grid(row = 9, column = 0, columnspan = 2)
        elif choice == '2':
            self.contB.grid_forget()
            self.contB = self.btnButtonB2 = Button(self, text = "Continue", command = self.Rifle)
            self.btnButtonB2.grid(row = 9, column = 0, columnspan = 2)
        elif choice == '3':
            self.contB.grid_forget()
            self.contB = self.btnButtonB2 = Button(self, text = "Continue", command = self.Standup)
            self.btnButtonB2.grid(row = 9, column = 0, columnspan = 2)

    def Standup(self):
        #print("Stand up Cautiously")
        self.story.set("The monster looks at you and giggles,'I remember you. You're the kid who graciously gave me his Shrink Ray'")                                       #Update the story
        self.story2.set("You shout back 'You stole it frome me! Give it back!' You notice a huge stack of gold behind Rebet, on top of which is your Shrink Ray.")
        ch1.set("Reach for your Photon Rifle")                                                                                                                              #Update all the choices
        ch2.set("Sneak out your dagger from your Bag.")
        ch3.set("Do Nothing")
        self.Desel()
        choice = self.Get_Choice()
        if choice == '1':    
            self.contB.grid_forget()                                                                    #previous continue button is deleted and replaced by a new one with different command
            self.contB = self.btnButtonB2 = Button(self, text = "Continue", command = self.Rifle)
            self.btnButtonB2.grid(row = 9, column = 0, columnspan = 2)
        elif choice == '2':
            self.contB.grid_forget()
            self.contB = self.btnButtonB2 = Button(self, text = "Continue", command = self.Standup2)
            self.btnButtonB2.grid(row = 9, column = 0, columnspan = 2)
        elif choice == '3':
            self.contB.grid_forget()
            self.contB = self.btnButtonB2 = Button(self, text = "Continue", command = self.Standup2)
            self.btnButtonB2.grid(row = 9, column = 0, columnspan = 2)

    def Standup2(self):
        #print("Stand up 2")
        self.story.set("'Your best chance at survival is to hand me any weapons you have. Forget your Shrink Ray. Surrender and I'll let you live.'")                   #Update the story
        self.story2.set("You shout back 'You stole it frome me! Give it back!' You notice a huge stack of gold behind Rebet, on top of which is your Shrink Ray.")
        ch1.set("Surrender")                                                                                                                                            #Update all the choices
        ch2.set("Pretend to surrender")
        ch3.set("Shoot him down with your Photon Rifle")
        self.Desel()
        choice = self.Get_Choice()
        if choice == '1':    
            self.contB.grid_forget()                                                                    #previous continue button is deleted and replaced by a new one with different command
            self.contB = self.btnButtonB2 = Button(self, text = "Continue", command = self.Surrender)
            self.btnButtonB2.grid(row = 9, column = 0, columnspan = 2)
        elif choice == '2':
            self.contB.grid_forget()
            self.contB = self.btnButtonB2 = Button(self, text = "Continue", command = self.PreSurr)
            self.btnButtonB2.grid(row = 9, column = 0, columnspan = 2)
        elif choice == '3':
            self.contB.grid_forget()
            self.contB = self.btnButtonB2 = Button(self, text = "Continue", command = self.Rifle)
            self.btnButtonB2.grid(row = 9, column = 0, columnspan = 2)

    def Rifle(self):
        #print("Photon Rifle")
        self.story.set("You grab your Photon Rifle and shoot straight at Rebets Face. Rebet anticipated this. He jumps out of the way and shoots a ball of acidic slime back at you.")  #Update the story
        self.story2.set("The slime hits your feet and slowly starts crawling up your body. You try to shoot the slime but it engulfs you. 'No one tries to fight King Rebet!' he says")
        self.ask.set("YOU LOST! WELL PLAYED")
        ch1.set("Thanks For Playing!")                                                                                                                                                  #Update all the choices
        ch2.set("Game by : SUNDEEP KAKAR")
        ch3.set("CSCI 230 - Professor : A.Harris") 
        self.contB.grid_forget()                            #To hide Continue button since the game ended for the user
    
    def PreSurr(self):
        #print("Act Surrender")
        self.story.set("'He holds his hand out to take your weapons. You pretend to hand them over, but as soon as you put your dagger in his hand, you pick up the Rifle.")    #Update the story
        self.story2.set("You aim straight for his eyes and with one shot you blind his right eye. He screeches loudly and falls back.")
        ch1.set("Go for your Shrink Ray")                                                                                                                                       #Update all the choices
        ch2.set("Finish him off first")
        ch3.set("Do nothing.")
        self.Desel()
        choice = self.Get_Choice()
        if choice == '1':    
            self.contB.grid_forget()                                                                    #previous continue button is deleted and replaced by a new one with different command
            self.contB = self.btnButtonB2 = Button(self, text = "Continue", command = self.ShrinkRay)
            self.btnButtonB2.grid(row = 9, column = 0, columnspan = 2)
        elif choice == '2':
            self.contB.grid_forget()
            self.contB = self.btnButtonB2 = Button(self, text = "Continue", command = self.AttRebet)
            self.btnButtonB2.grid(row = 9, column = 0, columnspan = 2)
        elif choice == '3':
            self.contB.grid_forget()
            self.contB = self.btnButtonB2 = Button(self, text = "Continue", command = self.Nothing)
            self.btnButtonB2.grid(row = 9, column = 0, columnspan = 2)

    def ShrinkRay(self):
        #print("Shrink Ray")
        self.story.set("You run towards the pile of gold. Just before you get there, Rebet crashes into you like a mad bull. He jumps onto the pile of gold. His paln is to gobble up the gold.")                           #Update the story
        self.story2.set("He gobbles up the whole pile including the shrink ray, but the shrink ray goes off in his stomach and his body starts to rapidly shrink. His tiny body explodes leaving you just the gun.")
        self.ask.set("YOU WIN! WELL PLAYED")
        ch1.set("Thanks For Playing!")                                                                                                                                                                                      #Update all the choices
        ch2.set("Game by : SUNDEEP KAKAR")
        ch3.set("CSCI 230 - Professor : A.Harris") 
        self.contB.grid_forget()                                        #To hide Continue button since the game ended for the user

    def AttRebet(self):
        #print("Attack Rebet")
        self.story.set("Rebet tries to make a run for the gold. You throw your dagger at him, and when it reaches his face, you shoot the dagger. The dagger explodes and Rebet is blown out of the cave.") #Update the story
        self.story2.set("Rebet is unconscious. You got your Shrink Ray back and you also got to keep all that gold.")
        self.ask.set("YOU WIN! WELL PLAYED")
        ch1.set("Thanks For Playing!")                                                                                                                                                                      #Update all the choices
        ch2.set("Game by : SUNDEEP KAKAR")
        ch3.set("CSCI 230 - Professor : A.Harris") 
        self.contB.grid_forget()                                        #To hide Continue button since the game ended for the user


    def Surrender(self):
        #print("Surrender")
        self.story.set("You hand him your backpack and all of your weapons. He laughs at you and throughs your belongings in the acid. 'Goodbye, buddy', he says before")       #Update the story
        self.story2.set("he frog-leaps onto the gold pile, gobbles it all up, and leaps out of the cave into his portal. Sadly, you fail to get your Shrink Ray back.")
        self.ask.set("YOU LOST! WELL PLAYED")
        ch1.set("Thanks For Playing!")                                                                                                                                          #Update all the choices
        ch2.set("Game by : SUNDEEP KAKAR")
        ch3.set("CSCI 230 - Professor : A.Harris") 
        self.contB.grid_forget()                                        #To hide Continue button since the game ended for the user


def main():                                                             #Main function creates class object
    game = Game()                                                       #Creating object for class Game

if __name__ == "__main__":                          #This stops program from executing if its opened as a file in a different program
 main()

                        
