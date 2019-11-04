from tkinter import *
from tkinter import ttk
from finalprojectturtle import *
from turtle import *




def interface():
    global Final_Label_1
    def get_number(event):
        global num1, num2, num3, num4, num5, num6, num7, num8, num9, num10, num11, num12, num13, num14, num15, numlist

        try:
            num1 = int(numAEntry.get())
            num2 = int(numBEntry.get())
            num3 = int(numCEntry.get())
            num4 = int(numDEntry.get())
            num5 = int(numEEntry.get())
            num6 = int(numFEntry.get())
            num7 = int(numGEntry.get())
            num8 = int(numHEntry.get())
            num9 = int(numIEntry.get())
            num10 = int(numJEntry.get())
            num11 = int(numKEntry.get())
            num12 = int(numLEntry.get())
            num13 = int(numMEntry.get())
            num14 = int(numNEntry.get())
            num15 = int(numOEntry.get())

            valid = True

            numlist = [num3, num2, num1, num6, num5, num4, num9, num8, num7, num12, num11, num10, num15, num14, num13]
            for x in numlist:
                if x < 0 or x > 10:
                    valid = False

            if valid:
                Final_Label_1.configure(text='Diagram below shows')
                a_big_pizza_filling_color(numlist)


            else:
                Final_Label_1.configure(text='Invalid input, try again')

        except:
            Final_Label_1.configure(text='Invalid input, try again')



    interfaces = Tk()

    Label(interfaces, text="Hot Spot", font=("Arial", 20)).grid(row=0, column=0)
    Label(interfaces, text=" Shooting", font=("Arial", 20)).grid(row=0, column=1, sticky=W)

    Label(interfaces, text="Enter the number of").grid(row=1, column=0, sticky=W)
    Label(interfaces, text="makes at each corresponding spot.").grid(row=1, column=1, sticky=W)

    Label(interfaces, text="Spot 1").grid(row=2, column=0, sticky=W)
    numAEntry = Entry(interfaces)
    numAEntry.grid(row=2, column=1, sticky=W)

    Label(interfaces, text="Spot 2").grid(row=3, column=0, sticky=W)
    numBEntry = Entry(interfaces)
    numBEntry.grid(row=3, column=1, sticky=W)

    Label(interfaces, text="Spot 3").grid(row=4, column=0, sticky=W)
    numCEntry = Entry(interfaces)
    numCEntry.grid(row=4, column=1, sticky=W)

    Label(interfaces, text="Spot 4").grid(row=5, column=0, sticky=W)
    numDEntry = Entry(interfaces)
    numDEntry.grid(row=5, column=1, sticky=W)

    Label(interfaces, text="Spot 5").grid(row=6, column=0, sticky=W)
    numEEntry = Entry(interfaces)
    numEEntry.grid(row=6, column=1, sticky=W)

    Label(interfaces, text="Spot 6").grid(row=7, column=0, sticky=W)
    numFEntry = Entry(interfaces)
    numFEntry.grid(row=7, column=1, sticky=W)

    Label(interfaces, text="Spot 7").grid(row=8, column=0, sticky=W)
    numGEntry = Entry(interfaces)
    numGEntry.grid(row=8, column=1, sticky=W)

    Label(interfaces, text="Spot 8").grid(row=9, column=0, sticky=W)
    numHEntry = Entry(interfaces)
    numHEntry.grid(row=9, column=1, sticky=W)

    Label(interfaces, text="Spot 9").grid(row=10, column=0, sticky=W)
    numIEntry = Entry(interfaces)
    numIEntry.grid(row=10, column=1, sticky=W)

    Label(interfaces, text="Spot 10").grid(row=11, column=0, sticky=W)
    numJEntry = Entry(interfaces)
    numJEntry.grid(row=11, column=1, sticky=W)

    Label(interfaces, text="Spot 11").grid(row=12, column=0, sticky=W)
    numKEntry = Entry(interfaces)
    numKEntry.grid(row=12, column=1, sticky=W)

    Label(interfaces, text="Spot 12").grid(row=13, column=0, sticky=W)
    numLEntry = Entry(interfaces)
    numLEntry.grid(row=13, column=1, sticky=W)

    Label(interfaces, text="Spot 13").grid(row=14, column=0, sticky=W)
    numMEntry = Entry(interfaces)
    numMEntry.grid(row=14, column=1, sticky=W)

    Label(interfaces, text="Spot 14").grid(row=15, column=0, sticky=W)
    numNEntry = Entry(interfaces)
    numNEntry.grid(row=15, column=1, sticky=W)

    Label(interfaces, text="Spot 15").grid(row=16, column=0, sticky=W)
    numOEntry = Entry(interfaces)
    numOEntry.grid(row=16, column=1, sticky=W)

    Final_Label_1 = Label(interfaces, text='')
    Final_Label_1.grid(row=17, column=0, sticky=W)

    submitButton = Button(interfaces, text="Track You're Shots!")
    submitButton.bind("<Button-1>", get_number)
    submitButton.grid(row=18, column=1, sticky=E)

    interfaces.mainloop()

def semicircle(radius):
   circle(radius,180)
   return

def rectangle(short_leg, long_leg):
   forward(short_leg/2)
   left(90)
   forward(long_leg)
   left(90)
   forward(short_leg)
   left(90)
   forward(long_leg)
   left(90)
   forward(short_leg/2)
   return

def basketball_court():
   pencolor('green')
   width(2)
   forward(160)
   left(90)
   forward(75)
   semicircle(160)
   forward(75)
   left(90)
   forward(160)
   rectangle(90, 140)
   forward(45)
   left(90)
   forward(140)
   semicircle(45)
   forward(140)
   left(90)
   forward(45)
   width(1)
   pencolor('black')
   rectangle (520,300)
   return





def pizza_pie_position_direction(r, pos):
   # left(ang_in)
   # begin_fill("salmon")
   penup()
   forward(r-25)
   left(90)
   circle(r-25, 22)
   pendown()
   color('red')
   width(3)
   write(pos, font = (10))
   penup()
   circle(r-25, 14)
   left(90)
   forward(r-25)
   left(144)
   pendown()


   forward(r)
   left(90)
   circle(r, 36)
   left(90)
   forward(r)
   left(144)
   # end_fill()
   return


def avr_list(makes_list: list) -> list:

   avr_list = []
   for i in range(len(makes_list)):
       avr_list = avr_list + [makes_list[i]/10]

   return list(map(lambda x: x*100, avr_list))


def spot_color(percentage: int) -> object:

   if percentage <= 30:
       return 'gray30'
   if 30 < percentage <= 65:
       return 'gray69'
   if percentage > 65:
       return 'gray89'

def spot_color_for_all(numlist):
    average_list = avr_list(numlist)
    return list(map(lambda x: spot_color(x), average_list))



def instruction_rectangle(pencolor,fillcolor):
   color(pencolor,fillcolor)
   begin_fill()
   forward(15)
   left(90)
   forward(10)
   left(90)
   forward(15)
   left(90)
   forward(10)
   left(90)
   end_fill()

   return

def draw_instructions():
    left(90)
    penup()
    forward(50)
    pendown()
    left(90)
    instruction_rectangle("black", "gray30")
    penup()
    forward(25)
    pendown()
    write('shooting ratio: 0% ~ 30%', font = (10))
    penup()
    backward(25)

    right(90)
    penup()
    forward(50)
    pendown()
    left(90)
    instruction_rectangle("black", "gray69")
    penup()
    forward(25)
    pendown()
    write('shooting ratio: 30% ~ 65%', font=(10))
    penup()
    backward(25)

    right(90)
    penup()
    forward(50)
    pendown()
    left(90)
    instruction_rectangle("black", "gray89")
    penup()
    forward(25)
    pendown()
    write('shooting ratio: 65% ~ 100%', font =(10))
    penup()
    backward(25)
    left(90)
    forward(150)
    left(90)


    hideturtle()


def instruction_in_shooting_position():
    color('black')
    penup()
    forward(300)
    left(90)
    forward(50)
    left(90)
    pendown()
    write('1. shoot from position 1 to position 15 according ', font = (10))
    penup()
    right(90)
    forward(35)
    left(90)
    pendown()
    write('     to the basketball court picture instruction.', font = (10))
    penup()
    right(90)
    forward(35)
    pendown()
    left(90)
    write('2. input your scores to the matched entry', font = (10))
    penup()
    right(90)
    forward(35)
    pendown()
    left(90)
    write('    submit and check your hot spot picture!', font = (10))
    penup()
    left(90)
    forward(155)
    right(90)
    forward(300)
    left(180)
    pendown()



def pizza_pie_filling_color(r, color):
   begin_fill()
   forward(r)
   left(90)
   circle(r, 36)
   left(90)
   forward(r)
   end_fill()
   left(144)
   return


def a_big_pizza_filling_color(numlist):
    right(180)
    count = 0
    for i in range(5):
        for (r) in (260, 160, 80):
            index = count
            pizza_pie_filling_color(r, color(spot_color_for_all(numlist)[index]))
            count += 1
        left(36)

    right(180)
    basketball_court()
    a_big_pizza_position_direction()
    instruction_in_shooting_position()
    draw_instructions()
    update()


def a_big_pizza_position_direction():
    count = 0
    for i in range(5):
        for (r) in (80, 160, 260):
            count += 1
            pos = count
            pizza_pie_position_direction(r, pos)
        left(36)

def main():
    basketball_court()
    a_big_pizza_position_direction()
    instruction_in_shooting_position()
    update()
    interface()
    update()



if __name__ == '__main__':
    tracer(0)
    try:
        main()
        done()
    except:
        pass

