import time
from tkinter import *
from tkinter import Tk
from PIL import ImageTk, Image
import os

##############################################variables#######################################################

##############################################test 1 #########################################################
cyans = 0
blues = 0
indigos = 0
magentas = 0
purples = 0
violets = 0
reds = 0
yellows = 0
greens = 0
##############################################test 2 #########################################################
cyans1 = 0
blues1 = 0
indigos1 = 0
magentas1 = 0
purples1 = 0
violets1 = 0
reds1 = 0
yellows1 = 0
greens1 = 0
##############################################test 3 #########################################################
cyans2 = 0
blues2 = 0
indigos2 = 0
magentas2 = 0
purples2 = 0
violets2 = 0
reds2 = 0
yellows2 = 0
greens2 = 0
##############################################test 4 #########################################################
cyans3 = 0
blues3 = 0
indigos3 = 0
magentas3 = 0
purples3 = 0
violets3 = 0
reds3 = 0
yellows3 = 0
greens3 = 0
##############################################################################################################
window = Tk()
window.title('Reaction Time')
canvas = Canvas(height=500, width=500)
canvas.pack()
frame = Frame(bg='black')
frame.place(relwidth=1, relheight=1)
# image space
firstimg = Image.open("images/anotherone.png")
addimg = ImageTk.PhotoImage(firstimg)
label = Label(frame, image=addimg, bg='black', width=1, height=1)
label.place(relx=0.25, rely=0.002, relheight=0.5, relwidth=0.5)
########################################## subject details ###################################################################################################################

name_label = Label(frame, text="Input Subject's Name:", fg='white', bg='black').place(relx=0.25, rely=0.4,
                                                                                      relheight=0.05, relwidth=0.5)
name_id = StringVar()
name_input = Entry(frame, textvariable=name_id).place(relx=0.25, rely=0.45, relheight=0.05, relwidth=0.5)

age_label = Label(frame, text="Input Subject's Age:", fg='white', bg='black').place(relx=0.25, rely=0.5,
                                                                                    relheight=0.05, relwidth=0.5)
age_id = StringVar()
age_input = Entry(frame, textvariable=age_id).place(relx=0.25, rely=0.55, relheight=0.05, relwidth=0.5)

sex_label = Label(frame, text="Input Subject's Gender:", fg='white', bg='black').place(relx=0.25, rely=0.6,
                                                                                       relheight=0.05, relwidth=0.5)
sex_id = StringVar()
sex_input = Entry(frame, textvariable=sex_id).place(relx=0.25, rely=0.65, relheight=0.05, relwidth=0.5)


###############################################################################################################################################################################
########################################################################### select test page ##################################################################################


def game():
    global cyans, blues, indigos, magentas, purples, violets, yellows, reds, greens
    first = Tk()
    first.title("hello" + name_id.get())
    canvas1 = Canvas(first, height=1000, width=1000)
    canvas1.pack()
    frame1 = Frame(first, bg='white')
    frame1.place(relwidth=1, relheight=1)
    labels = Label(frame1, bg='white', text='Select Blue = b, Cyan = c, Indigo = i, Magenta = m, Purple = '
                                            'p, Violet = v, Yellow = y, Red = r, Green = g')
    labels.place(relx=0.03, rely=0.1)

    colors_change = Label(frame1, bg='cyan', width=1, height=1)
    colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

    def wrong():
        wrongs = Label(frame1, text="Incorrect Input").pack()
        pass

    def green1():
        global greens, indigos, yellows, reds, blues, cyans, magentas, violets, purples
        greens = round((time.time() - greens), 4)
        done = Label(frame1, text="TEST COMPLETED CHECK DESKTOP FOR RESULTS").pack()
        space = os.path.normpath(os.path.expanduser('~'))
        with open("%s/Desktop/%s1.txt" % (
                space, name_id.get()), 'w+') as done:
            done.write("\n" + '\n' + '\n' + '\n' + '\n')
            done.write(
                'Data for %s' % name_id.get() + '\n')
            done.write(
                'Gender %s' % sex_id.get() + '\n')
            done.write(
                'Age %s' % age_id.get() + '\n')
            done.write(
                'cyan 1: %s' % str(cyans) + '\n')
            done.write('blue 1: %s' % str(blues) + '\n')
            done.write(
                'indigo 1: %s' % str(indigos) + '\n')
            done.write(
                'magenta 1: %s' % str(magentas) + '\n')
            done.write(
                'violet 1: %s' % str(violets) + '\n')
            done.write(
                'purple 1: %s' % str(purples) + '\n')
            done.write(
                'red 1: %s' % str(reds) + '\n')
            done.write(
                'yellow 1: %s' % str(yellows) + '\n')
            done.write(
                'green 1: %s' % str(greens) + '\n')
        time.sleep(2)
        frame1.destroy()
        endingframe = Frame(first)
        endingframe.place(relwidth=1, relheight=1)
        endinglabels = Label(endingframe, bg='white',
                             text='TEST COMPLETE FIND RESULT ON DESKTOP').pack()

        pass

    def yellow1():
        global greens, yellows
        yellows = round((time.time() - yellows), 4)
        time.sleep(2)
        colors_change = Label(frame1, bg='green', width=1, height=1)
        colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

        cyan = Button(frame1, text='C', bg='blue', bd=0.01, command=wrong)
        cyan.place(relx=0.05, rely=0.9, relheight=0.05, relwidth=0.1)

        blue = Button(frame1, text='B', bg='blue', bd=0.01, command=wrong)
        blue.place(relx=0.15, rely=0.9, relheight=0.05, relwidth=0.1)

        violet = Button(frame1, text='V', bg='blue', bd=0.01, command=wrong)
        violet.place(relx=0.55, rely=0.9, relheight=0.05, relwidth=0.1)

        yellow = Button(frame1, text='Y', bg='blue', bd=0.01, command=wrong)
        yellow.place(relx=0.65, rely=0.9, relheight=0.05, relwidth=0.1)

        indigo = Button(frame1, text='I', bg='blue', bd=0.01, command=wrong)
        indigo.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.1)

        magenta = Button(frame1, text='M', bg='blue', bd=0.01, command=wrong)
        magenta.place(relx=0.35, rely=0.9, relheight=0.05, relwidth=0.1)

        purple = Button(frame1, text='P', bg='blue', bd=0.01, command=wrong)
        purple.place(relx=0.45, rely=0.9, relheight=0.05, relwidth=0.1)

        red = Button(frame1, text='R', bg='blue', bd=0.01, command=wrong)
        red.place(relx=0.75, rely=0.9, relheight=0.05, relwidth=0.1)

        green = Button(frame1, text='G', bg='blue', bd=0.01, command=green1)
        green.place(relx=0.85, rely=0.9, relheight=0.05, relwidth=0.1)

        greens = time.time()

        pass

    def red1():
        global reds, yellows
        reds = round((time.time() - reds), 4)
        time.sleep(2)
        colors_change = Label(frame1, bg='yellow', width=1, height=1)
        colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

        cyan = Button(frame1, text='C', bg='blue', bd=0.01, command=wrong)
        cyan.place(relx=0.05, rely=0.9, relheight=0.05, relwidth=0.1)

        blue = Button(frame1, text='B', bg='blue', bd=0.01, command=wrong)
        blue.place(relx=0.15, rely=0.9, relheight=0.05, relwidth=0.1)

        violet = Button(frame1, text='V', bg='blue', bd=0.01, command=wrong)
        violet.place(relx=0.55, rely=0.9, relheight=0.05, relwidth=0.1)

        yellow = Button(frame1, text='Y', bg='blue', bd=0.01, command=yellow1)
        yellow.place(relx=0.65, rely=0.9, relheight=0.05, relwidth=0.1)

        red = Button(frame1, text='R', bg='blue', bd=0.01, command=wrong)
        red.place(relx=0.75, rely=0.9, relheight=0.05, relwidth=0.1)

        green = Button(frame1, text='G', bg='blue', bd=0.01, command=wrong)
        green.place(relx=0.85, rely=0.9, relheight=0.05, relwidth=0.1)

        indigo = Button(frame1, text='I', bg='blue', bd=0.01, command=wrong)
        indigo.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.1)

        magenta = Button(frame1, text='M', bg='blue', bd=0.01, command=wrong)
        magenta.place(relx=0.35, rely=0.9, relheight=0.05, relwidth=0.1)

        purple = Button(frame1, text='P', bg='blue', bd=0.01, command=wrong)
        purple.place(relx=0.45, rely=0.9, relheight=0.05, relwidth=0.1)



        yellows = time.time()

        pass

    def violet1():
        global violets, reds
        violets = round((time.time() - violets), 4)
        time.sleep(2)
        colors_change = Label(frame1, bg='red', width=1, height=1)
        colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

        cyan = Button(frame1, text='C', bg='blue', bd=0.01, command=wrong)
        cyan.place(relx=0.05, rely=0.9, relheight=0.05, relwidth=0.1)

        blue = Button(frame1, text='B', bg='blue', bd=0.01, command=wrong)
        blue.place(relx=0.15, rely=0.9, relheight=0.05, relwidth=0.1)



        yellow = Button(frame1, text='Y', bg='blue', bd=0.01, command=wrong)
        yellow.place(relx=0.65, rely=0.9, relheight=0.05, relwidth=0.1)

        red = Button(frame1, text='R', bg='blue', bd=0.01, command=red1)
        red.place(relx=0.75, rely=0.9, relheight=0.05, relwidth=0.1)

        green = Button(frame1, text='G', bg='blue', bd=0.01, command=wrong)
        green.place(relx=0.85, rely=0.9, relheight=0.05, relwidth=0.1)

        indigo = Button(frame1, text='I', bg='blue', bd=0.01, command=wrong)
        indigo.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.1)

        magenta = Button(frame1, text='M', bg='blue', bd=0.01, command=wrong)
        magenta.place(relx=0.35, rely=0.9, relheight=0.05, relwidth=0.1)

        purple = Button(frame1, text='P', bg='blue', bd=0.01, command=wrong)
        purple.place(relx=0.45, rely=0.9, relheight=0.05, relwidth=0.1)

        violet = Button(frame1, text='V', bg='blue', bd=0.01, command=wrong)
        violet.place(relx=0.55, rely=0.9, relheight=0.05, relwidth=0.1)

        reds = time.time()

        pass

    def purple1():
        global purples, violets
        purples = round((time.time() - purples), 4)
        time.sleep(2)
        colors_change = Label(frame1, bg='violet', width=1, height=1)
        colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

        cyan = Button(frame1, text='C', bg='blue', bd=0.01, command=wrong)
        cyan.place(relx=0.05, rely=0.9, relheight=0.05, relwidth=0.1)

        blue = Button(frame1, text='B', bg='blue', bd=0.01, command=wrong)
        blue.place(relx=0.15, rely=0.9, relheight=0.05, relwidth=0.1)

        indigo = Button(frame1, text='I', bg='blue', bd=0.01, command=wrong)
        indigo.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.1)

        yellow = Button(frame1, text='Y', bg='blue', bd=0.01, command=wrong)
        yellow.place(relx=0.65, rely=0.9, relheight=0.05, relwidth=0.1)

        red = Button(frame1, text='R', bg='blue', bd=0.01, command=wrong)
        red.place(relx=0.75, rely=0.9, relheight=0.05, relwidth=0.1)

        magenta = Button(frame1, text='M', bg='blue', bd=0.01, command=wrong)
        magenta.place(relx=0.35, rely=0.9, relheight=0.05, relwidth=0.1)

        purple = Button(frame1, text='P', bg='blue', bd=0.01, command=wrong)
        purple.place(relx=0.45, rely=0.9, relheight=0.05, relwidth=0.1)

        violet = Button(frame1, text='V', bg='blue', bd=0.01, command=violet1)
        violet.place(relx=0.55, rely=0.9, relheight=0.05, relwidth=0.1)

        green = Button(frame1, text='G', bg='blue', bd=0.01, command=wrong)
        green.place(relx=0.85, rely=0.9, relheight=0.05, relwidth=0.1)

        violets = time.time()

        pass

    def magenta1():
        global magentas, purples
        magentas = round((time.time() - magentas), 4)
        time.sleep(2)
        colors_change = Label(frame1, bg='purple', width=1, height=1)
        colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

        cyan = Button(frame1, text='C', bg='blue', bd=0.01, command=wrong)
        cyan.place(relx=0.05, rely=0.9, relheight=0.05, relwidth=0.1)

        blue = Button(frame1, text='B', bg='blue', bd=0.01, command=wrong)
        blue.place(relx=0.15, rely=0.9, relheight=0.05, relwidth=0.1)

        indigo = Button(frame1, text='I', bg='blue', bd=0.01, command=wrong)
        indigo.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.1)

        yellow = Button(frame1, text='Y', bg='blue', bd=0.01, command=wrong)
        yellow.place(relx=0.65, rely=0.9, relheight=0.05, relwidth=0.1)

        red = Button(frame1, text='R', bg='blue', bd=0.01, command=wrong)
        red.place(relx=0.75, rely=0.9, relheight=0.05, relwidth=0.1)

        green = Button(frame1, text='G', bg='blue', bd=0.01, command=wrong)
        green.place(relx=0.85, rely=0.9, relheight=0.05, relwidth=0.1)

        magenta = Button(frame1, text='M', bg='blue', bd=0.01, command=wrong)
        magenta.place(relx=0.35, rely=0.9, relheight=0.05, relwidth=0.1)

        purple = Button(frame1, text='P', bg='blue', bd=0.01, command=purple1)
        purple.place(relx=0.45, rely=0.9, relheight=0.05, relwidth=0.1)

        violet = Button(frame1, text='V', bg='blue', bd=0.01, command=wrong)
        violet.place(relx=0.55, rely=0.9, relheight=0.05, relwidth=0.1)


        purples = time.time()

        pass

    def indigo1():
        global magentas, indigos
        indigos = round((time.time() - indigos), 4)
        time.sleep(2)
        colors_change = Label(frame1, bg='magenta', width=1, height=1)
        colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

        cyan = Button(frame1, text='C', bg='blue', bd=0.01, command=wrong)
        cyan.place(relx=0.05, rely=0.9, relheight=0.05, relwidth=0.1)

        blue = Button(frame1, text='B', bg='blue', bd=0.01, command=wrong)
        blue.place(relx=0.15, rely=0.9, relheight=0.05, relwidth=0.1)

        indigo = Button(frame1, text='I', bg='blue', bd=0.01, command=wrong)
        indigo.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.1)

        magenta = Button(frame1, text='M', bg='blue', bd=0.01, command=magenta1)
        magenta.place(relx=0.35, rely=0.9, relheight=0.05, relwidth=0.1)

        purple = Button(frame1, text='P', bg='blue', bd=0.01, command=wrong)
        purple.place(relx=0.45, rely=0.9, relheight=0.05, relwidth=0.1)

        violet = Button(frame1, text='V', bg='blue', bd=0.01, command=wrong)
        violet.place(relx=0.55, rely=0.9, relheight=0.05, relwidth=0.1)

        yellow = Button(frame1, text='Y', bg='blue', bd=0.01, command=wrong)
        yellow.place(relx=0.65, rely=0.9, relheight=0.05, relwidth=0.1)

        red = Button(frame1, text='R', bg='blue', bd=0.01, command=wrong)
        red.place(relx=0.75, rely=0.9, relheight=0.05, relwidth=0.1)

        green = Button(frame1, text='G', bg='blue', bd=0.01, command=wrong)
        green.place(relx=0.85, rely=0.9, relheight=0.05, relwidth=0.1)

        magentas = time.time()

        pass

    def blue1():
        global blues, indigos
        blues = round((time.time() - blues),4)
        time.sleep(2)
        colors_change = Label(frame1, bg='indigo', width=1, height=1)
        colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

        cyan = Button(frame1, text='C', bg='blue', bd=0.01, command=wrong)
        cyan.place(relx=0.05, rely=0.9, relheight=0.05, relwidth=0.1)

        blue = Button(frame1, text='B', bg='blue', bd=0.01, command=wrong)
        blue.place(relx=0.15, rely=0.9, relheight=0.05, relwidth=0.1)

        indigo = Button(frame1, text='I', bg='blue', bd=0.01, command=indigo1)
        indigo.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.1)

        magenta = Button(frame1, text='M', bg='blue', bd=0.01, command=wrong)
        magenta.place(relx=0.35, rely=0.9, relheight=0.05, relwidth=0.1)

        purple = Button(frame1, text='P', bg='blue', bd=0.01, command=wrong)
        purple.place(relx=0.45, rely=0.9, relheight=0.05, relwidth=0.1)

        violet = Button(frame1, text='V', bg='blue', bd=0.01, command=wrong)
        violet.place(relx=0.55, rely=0.9, relheight=0.05, relwidth=0.1)

        yellow = Button(frame1, text='Y', bg='blue', bd=0.01, command=wrong)
        yellow.place(relx=0.65, rely=0.9, relheight=0.05, relwidth=0.1)

        red = Button(frame1, text='R', bg='blue', bd=0.01, command=wrong)
        red.place(relx=0.75, rely=0.9, relheight=0.05, relwidth=0.1)

        green = Button(frame1, text='G', bg='blue', bd=0.01, command=wrong)
        green.place(relx=0.85, rely=0.9, relheight=0.05, relwidth=0.1)

        indigos = time.time()

        pass

    def cyan1():
        global cyans, blues
        cyans = round((time.time() - cyans),4)
        time.sleep(2)
        colors_change = Label(frame1, bg='blue', width=1, height=1)
        colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

        cyan = Button(frame1, text='C', bg='blue', bd=0.01, command=wrong)
        cyan.place(relx=0.05, rely=0.9, relheight=0.05, relwidth=0.1)

        blue = Button(frame1, text='B', bg='blue', bd=0.01, command=blue1)
        blue.place(relx=0.15, rely=0.9, relheight=0.05, relwidth=0.1)

        indigo = Button(frame1, text='I', bg='blue', bd=0.01, command=wrong)
        indigo.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.1)

        magenta = Button(frame1, text='M', bg='blue', bd=0.01, command=wrong)
        magenta.place(relx=0.35, rely=0.9, relheight=0.05, relwidth=0.1)

        purple = Button(frame1, text='P', bg='blue', bd=0.01, command=wrong)
        purple.place(relx=0.45, rely=0.9, relheight=0.05, relwidth=0.1)

        violet = Button(frame1, text='V', bg='blue', bd=0.01, command=wrong)
        violet.place(relx=0.55, rely=0.9, relheight=0.05, relwidth=0.1)

        yellow = Button(frame1, text='Y', bg='blue', bd=0.01, command=wrong)
        yellow.place(relx=0.65, rely=0.9, relheight=0.05, relwidth=0.1)

        red = Button(frame1, text='R', bg='blue', bd=0.01, command=wrong)
        red.place(relx=0.75, rely=0.9, relheight=0.05, relwidth=0.1)

        green = Button(frame1, text='G', bg='blue', bd=0.01, command=wrong)
        green.place(relx=0.85, rely=0.9, relheight=0.05, relwidth=0.1)

        blues = time.time()

        print(cyans)

        pass

    cyan = Button(frame1, text='C', bg='blue', bd=0.01, command=cyan1)
    cyan.place(relx=0.05, rely=0.9, relheight=0.05, relwidth=0.1)

    blue = Button(frame1, text='B', bg='blue', bd=0.01, command=wrong)
    blue.place(relx=0.15, rely=0.9, relheight=0.05, relwidth=0.1)

    indigo = Button(frame1, text='I', bg='blue', bd=0.01, command=wrong)
    indigo.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.1)

    magenta = Button(frame1, text='M', bg='blue', bd=0.01, command=wrong)
    magenta.place(relx=0.35, rely=0.9, relheight=0.05, relwidth=0.1)

    purple = Button(frame1, text='P', bg='blue', bd=0.01, command=wrong)
    purple.place(relx=0.45, rely=0.9, relheight=0.05, relwidth=0.1)

    violet = Button(frame1, text='V', bg='blue', bd=0.01, command=wrong)
    violet.place(relx=0.55, rely=0.9, relheight=0.05, relwidth=0.1)

    yellow = Button(frame1, text='Y', bg='blue', bd=0.01, command=wrong)
    yellow.place(relx=0.65, rely=0.9, relheight=0.05, relwidth=0.1)

    red = Button(frame1, text='R', bg='blue', bd=0.01, command=wrong)
    red.place(relx=0.75, rely=0.9, relheight=0.05, relwidth=0.1)

    green = Button(frame1, text='G', bg='blue', bd=0.01, command=wrong)
    green.place(relx=0.85, rely=0.9, relheight=0.05, relwidth=0.1)

    cyans = time.time()

    pass


def game1():
    global cyans1, blues1, indigos1, magentas1, purples1, violets1, yellows1, reds1, greens1
    first = Tk()
    first.title("hello" + name_id.get())
    canvas1 = Canvas(first, height=1000, width=1000)
    canvas1.pack()
    frame1 = Frame(first, bg='white')
    frame1.place(relwidth=1, relheight=1)
    labels = Label(frame1, bg='white', text='Select Blue = b, Cyan = c, Indigo = i, Magenta = m, Purple = '
                                            'p, Violet = v, Yellow = y, Red = r, Green = g')
    labels.place(relx=0.03, rely=0.1)

    colors_change = Label(frame1, bg='cyan', width=1, height=1)
    colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

    def wrong():
        wrongs = Label(frame1, text="Incorrect Input").pack()
        pass

    def green1():
        global greens1, indigos1, yellows1, reds1, blues1, cyans1, magentas1, violets1, purples1
        greens1 = round((time.time() - greens1), 4)
        done = Label(frame1, text="TEST COMPLETED CHECK DESKTOP FOR RESULTS").pack()
        space = os.path.normpath(os.path.expanduser('~'))
        with open("%s/Desktop/%s2.txt" % (
                space, name_id.get()), 'w+') as done:
            done.write("\n" + '\n' + '\n' + '\n' + '\n')
            done.write(
                'Data for %s' % name_id.get() + '\n')
            done.write(
                'Gender %s' % sex_id.get() + '\n')
            done.write(
                'Age %s' % age_id.get() + '\n')
            done.write(
                'cyan 2: %s' % str(cyans1) + '\n')
            done.write('blue 2: %s' % str(blues1) + '\n')
            done.write(
                'indigo 2: %s' % str(indigos1) + '\n')
            done.write(
                'magenta 2: %s' % str(magentas1) + '\n')
            done.write(
                'violet 2: %s' % str(violets1) + '\n')
            done.write(
                'purple 2: %s' % str(purples1) + '\n')
            done.write(
                'red 2: %s' % str(reds1) + '\n')
            done.write(
                'yellow 2: %s' % str(yellows1) + '\n')
            done.write(
                'green 2: %s' % str(greens1) + '\n')
        time.sleep(2)
        frame1.destroy()
        endingframe = Frame(first)
        endingframe.place(relwidth=1, relheight=1)
        endinglabels = Label(endingframe, bg='white',
                             text='TEST COMPLETE FIND RESULT ON DESKTOP').pack()

        pass

    def yellow1():
        global greens1, yellows1
        yellows1 = round((time.time() - yellows1), 4)
        time.sleep(2)
        colors_change = Label(frame1, bg='green', width=1, height=1)
        colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

        cyan = Button(frame1, text='C', bg='blue', bd=0.01, command=wrong)
        cyan.place(relx=0.05, rely=0.9, relheight=0.05, relwidth=0.1)

        blue = Button(frame1, text='B', bg='blue', bd=0.01, command=wrong)
        blue.place(relx=0.15, rely=0.9, relheight=0.05, relwidth=0.1)

        violet = Button(frame1, text='V', bg='blue', bd=0.01, command=wrong)
        violet.place(relx=0.55, rely=0.9, relheight=0.05, relwidth=0.1)

        yellow = Button(frame1, text='Y', bg='blue', bd=0.01, command=wrong)
        yellow.place(relx=0.65, rely=0.9, relheight=0.05, relwidth=0.1)

        indigo = Button(frame1, text='I', bg='blue', bd=0.01, command=wrong)
        indigo.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.1)

        magenta = Button(frame1, text='M', bg='blue', bd=0.01, command=wrong)
        magenta.place(relx=0.35, rely=0.9, relheight=0.05, relwidth=0.1)

        purple = Button(frame1, text='P', bg='blue', bd=0.01, command=wrong)
        purple.place(relx=0.45, rely=0.9, relheight=0.05, relwidth=0.1)

        red = Button(frame1, text='R', bg='blue', bd=0.01, command=wrong)
        red.place(relx=0.75, rely=0.9, relheight=0.05, relwidth=0.1)

        green = Button(frame1, text='G', bg='blue', bd=0.01, command=green1)
        green.place(relx=0.85, rely=0.9, relheight=0.05, relwidth=0.1)

        greens1 = time.time()

        pass

    def red1():
        global reds1, yellows1
        reds1 = round((time.time() - reds1), 4)
        time.sleep(2)
        colors_change = Label(frame1, bg='yellow', width=1, height=1)
        colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

        cyan = Button(frame1, text='C', bg='blue', bd=0.01, command=wrong)
        cyan.place(relx=0.05, rely=0.9, relheight=0.05, relwidth=0.1)

        blue = Button(frame1, text='B', bg='blue', bd=0.01, command=wrong)
        blue.place(relx=0.15, rely=0.9, relheight=0.05, relwidth=0.1)

        violet = Button(frame1, text='V', bg='blue', bd=0.01, command=wrong)
        violet.place(relx=0.55, rely=0.9, relheight=0.05, relwidth=0.1)

        yellow = Button(frame1, text='Y', bg='blue', bd=0.01, command=yellow1)
        yellow.place(relx=0.65, rely=0.9, relheight=0.05, relwidth=0.1)

        red = Button(frame1, text='R', bg='blue', bd=0.01, command=wrong)
        red.place(relx=0.75, rely=0.9, relheight=0.05, relwidth=0.1)

        green = Button(frame1, text='G', bg='blue', bd=0.01, command=wrong)
        green.place(relx=0.85, rely=0.9, relheight=0.05, relwidth=0.1)

        indigo = Button(frame1, text='I', bg='blue', bd=0.01, command=wrong)
        indigo.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.1)

        magenta = Button(frame1, text='M', bg='blue', bd=0.01, command=wrong)
        magenta.place(relx=0.35, rely=0.9, relheight=0.05, relwidth=0.1)

        purple = Button(frame1, text='P', bg='blue', bd=0.01, command=wrong)
        purple.place(relx=0.45, rely=0.9, relheight=0.05, relwidth=0.1)

        yellows1 = time.time()

        pass

    def violet1():
        global violets1, reds1
        violets1 = round((time.time() - violets1), 4)
        time.sleep(2)
        colors_change = Label(frame1, bg='red', width=1, height=1)
        colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

        cyan = Button(frame1, text='C', bg='blue', bd=0.01, command=wrong)
        cyan.place(relx=0.05, rely=0.9, relheight=0.05, relwidth=0.1)

        blue = Button(frame1, text='B', bg='blue', bd=0.01, command=wrong)
        blue.place(relx=0.15, rely=0.9, relheight=0.05, relwidth=0.1)

        yellow = Button(frame1, text='Y', bg='blue', bd=0.01, command=wrong)
        yellow.place(relx=0.65, rely=0.9, relheight=0.05, relwidth=0.1)

        red = Button(frame1, text='R', bg='blue', bd=0.01, command=red1)
        red.place(relx=0.75, rely=0.9, relheight=0.05, relwidth=0.1)

        green = Button(frame1, text='G', bg='blue', bd=0.01, command=wrong)
        green.place(relx=0.85, rely=0.9, relheight=0.05, relwidth=0.1)

        indigo = Button(frame1, text='I', bg='blue', bd=0.01, command=wrong)
        indigo.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.1)

        magenta = Button(frame1, text='M', bg='blue', bd=0.01, command=wrong)
        magenta.place(relx=0.35, rely=0.9, relheight=0.05, relwidth=0.1)

        purple = Button(frame1, text='P', bg='blue', bd=0.01, command=wrong)
        purple.place(relx=0.45, rely=0.9, relheight=0.05, relwidth=0.1)

        violet = Button(frame1, text='V', bg='blue', bd=0.01, command=wrong)
        violet.place(relx=0.55, rely=0.9, relheight=0.05, relwidth=0.1)

        reds1 = time.time()

        pass

    def purple1():
        global purples1, violets1
        purples1 = round((time.time() - purples1), 4)
        time.sleep(2)
        colors_change = Label(frame1, bg='violet', width=1, height=1)
        colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

        cyan = Button(frame1, text='C', bg='blue', bd=0.01, command=wrong)
        cyan.place(relx=0.05, rely=0.9, relheight=0.05, relwidth=0.1)

        blue = Button(frame1, text='B', bg='blue', bd=0.01, command=wrong)
        blue.place(relx=0.15, rely=0.9, relheight=0.05, relwidth=0.1)

        indigo = Button(frame1, text='I', bg='blue', bd=0.01, command=wrong)
        indigo.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.1)

        yellow = Button(frame1, text='Y', bg='blue', bd=0.01, command=wrong)
        yellow.place(relx=0.65, rely=0.9, relheight=0.05, relwidth=0.1)

        red = Button(frame1, text='R', bg='blue', bd=0.01, command=wrong)
        red.place(relx=0.75, rely=0.9, relheight=0.05, relwidth=0.1)

        magenta = Button(frame1, text='M', bg='blue', bd=0.01, command=wrong)
        magenta.place(relx=0.35, rely=0.9, relheight=0.05, relwidth=0.1)

        purple = Button(frame1, text='P', bg='blue', bd=0.01, command=wrong)
        purple.place(relx=0.45, rely=0.9, relheight=0.05, relwidth=0.1)

        violet = Button(frame1, text='V', bg='blue', bd=0.01, command=violet1)
        violet.place(relx=0.55, rely=0.9, relheight=0.05, relwidth=0.1)

        green = Button(frame1, text='G', bg='blue', bd=0.01, command=wrong)
        green.place(relx=0.85, rely=0.9, relheight=0.05, relwidth=0.1)

        violets1 = time.time()

        pass

    def magenta1():
        global magentas1, purples1
        magentas1 = round((time.time() - magentas1), 4)
        time.sleep(2)
        colors_change = Label(frame1, bg='purple', width=1, height=1)
        colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

        cyan = Button(frame1, text='C', bg='blue', bd=0.01, command=wrong)
        cyan.place(relx=0.05, rely=0.9, relheight=0.05, relwidth=0.1)

        blue = Button(frame1, text='B', bg='blue', bd=0.01, command=wrong)
        blue.place(relx=0.15, rely=0.9, relheight=0.05, relwidth=0.1)

        indigo = Button(frame1, text='I', bg='blue', bd=0.01, command=wrong)
        indigo.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.1)

        yellow = Button(frame1, text='Y', bg='blue', bd=0.01, command=wrong)
        yellow.place(relx=0.65, rely=0.9, relheight=0.05, relwidth=0.1)

        red = Button(frame1, text='R', bg='blue', bd=0.01, command=wrong)
        red.place(relx=0.75, rely=0.9, relheight=0.05, relwidth=0.1)

        green = Button(frame1, text='G', bg='blue', bd=0.01, command=wrong)
        green.place(relx=0.85, rely=0.9, relheight=0.05, relwidth=0.1)

        magenta = Button(frame1, text='M', bg='blue', bd=0.01, command=wrong)
        magenta.place(relx=0.35, rely=0.9, relheight=0.05, relwidth=0.1)

        purple = Button(frame1, text='P', bg='blue', bd=0.01, command=purple1)
        purple.place(relx=0.45, rely=0.9, relheight=0.05, relwidth=0.1)

        violet = Button(frame1, text='V', bg='blue', bd=0.01, command=wrong)
        violet.place(relx=0.55, rely=0.9, relheight=0.05, relwidth=0.1)

        purples1 = time.time()

        pass

    def indigo1():
        global magentas1, indigos1
        indigos1 = round((time.time() - indigos1), 4)
        time.sleep(2)
        colors_change = Label(frame1, bg='magenta', width=1, height=1)
        colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

        cyan = Button(frame1, text='C', bg='blue', bd=0.01, command=wrong)
        cyan.place(relx=0.05, rely=0.9, relheight=0.05, relwidth=0.1)

        blue = Button(frame1, text='B', bg='blue', bd=0.01, command=wrong)
        blue.place(relx=0.15, rely=0.9, relheight=0.05, relwidth=0.1)

        indigo = Button(frame1, text='I', bg='blue', bd=0.01, command=wrong)
        indigo.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.1)

        magenta = Button(frame1, text='M', bg='blue', bd=0.01, command=magenta1)
        magenta.place(relx=0.35, rely=0.9, relheight=0.05, relwidth=0.1)

        purple = Button(frame1, text='P', bg='blue', bd=0.01, command=wrong)
        purple.place(relx=0.45, rely=0.9, relheight=0.05, relwidth=0.1)

        violet = Button(frame1, text='V', bg='blue', bd=0.01, command=wrong)
        violet.place(relx=0.55, rely=0.9, relheight=0.05, relwidth=0.1)

        yellow = Button(frame1, text='Y', bg='blue', bd=0.01, command=wrong)
        yellow.place(relx=0.65, rely=0.9, relheight=0.05, relwidth=0.1)

        red = Button(frame1, text='R', bg='blue', bd=0.01, command=wrong)
        red.place(relx=0.75, rely=0.9, relheight=0.05, relwidth=0.1)

        green = Button(frame1, text='G', bg='blue', bd=0.01, command=wrong)
        green.place(relx=0.85, rely=0.9, relheight=0.05, relwidth=0.1)

        magentas1 = time.time()

        pass

    def blue1():
        global blues1, indigos1
        blues1 = round((time.time() - blues1), 4)
        time.sleep(2)
        colors_change = Label(frame1, bg='indigo', width=1, height=1)
        colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

        cyan = Button(frame1, text='C', bg='blue', bd=0.01, command=wrong)
        cyan.place(relx=0.05, rely=0.9, relheight=0.05, relwidth=0.1)

        blue = Button(frame1, text='B', bg='blue', bd=0.01, command=wrong)
        blue.place(relx=0.15, rely=0.9, relheight=0.05, relwidth=0.1)

        indigo = Button(frame1, text='I', bg='blue', bd=0.01, command=indigo1)
        indigo.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.1)

        magenta = Button(frame1, text='M', bg='blue', bd=0.01, command=wrong)
        magenta.place(relx=0.35, rely=0.9, relheight=0.05, relwidth=0.1)

        purple = Button(frame1, text='P', bg='blue', bd=0.01, command=wrong)
        purple.place(relx=0.45, rely=0.9, relheight=0.05, relwidth=0.1)

        violet = Button(frame1, text='V', bg='blue', bd=0.01, command=wrong)
        violet.place(relx=0.55, rely=0.9, relheight=0.05, relwidth=0.1)

        yellow = Button(frame1, text='Y', bg='blue', bd=0.01, command=wrong)
        yellow.place(relx=0.65, rely=0.9, relheight=0.05, relwidth=0.1)

        red = Button(frame1, text='R', bg='blue', bd=0.01, command=wrong)
        red.place(relx=0.75, rely=0.9, relheight=0.05, relwidth=0.1)

        green = Button(frame1, text='G', bg='blue', bd=0.01, command=wrong)
        green.place(relx=0.85, rely=0.9, relheight=0.05, relwidth=0.1)

        indigos1 = time.time()

        pass

    def cyan1():
        global cyans1, blues1
        cyans1 = round((time.time() - cyans1), 4)
        time.sleep(2)
        colors_change = Label(frame1, bg='blue', width=1, height=1)
        colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

        cyan = Button(frame1, text='C', bg='blue', bd=0.01, command=wrong)
        cyan.place(relx=0.05, rely=0.9, relheight=0.05, relwidth=0.1)

        blue = Button(frame1, text='B', bg='blue', bd=0.01, command=blue1)
        blue.place(relx=0.15, rely=0.9, relheight=0.05, relwidth=0.1)

        indigo = Button(frame1, text='I', bg='blue', bd=0.01, command=wrong)
        indigo.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.1)

        magenta = Button(frame1, text='M', bg='blue', bd=0.01, command=wrong)
        magenta.place(relx=0.35, rely=0.9, relheight=0.05, relwidth=0.1)

        purple = Button(frame1, text='P', bg='blue', bd=0.01, command=wrong)
        purple.place(relx=0.45, rely=0.9, relheight=0.05, relwidth=0.1)

        violet = Button(frame1, text='V', bg='blue', bd=0.01, command=wrong)
        violet.place(relx=0.55, rely=0.9, relheight=0.05, relwidth=0.1)

        yellow = Button(frame1, text='Y', bg='blue', bd=0.01, command=wrong)
        yellow.place(relx=0.65, rely=0.9, relheight=0.05, relwidth=0.1)

        red = Button(frame1, text='R', bg='blue', bd=0.01, command=wrong)
        red.place(relx=0.75, rely=0.9, relheight=0.05, relwidth=0.1)

        green = Button(frame1, text='G', bg='blue', bd=0.01, command=wrong)
        green.place(relx=0.85, rely=0.9, relheight=0.05, relwidth=0.1)

        blues1 = time.time()

        pass

    cyan = Button(frame1, text='C', bg='blue', bd=0.01, command=cyan1)
    cyan.place(relx=0.05, rely=0.9, relheight=0.05, relwidth=0.1)

    blue = Button(frame1, text='B', bg='blue', bd=0.01, command=wrong)
    blue.place(relx=0.15, rely=0.9, relheight=0.05, relwidth=0.1)

    indigo = Button(frame1, text='I', bg='blue', bd=0.01, command=wrong)
    indigo.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.1)

    magenta = Button(frame1, text='M', bg='blue', bd=0.01, command=wrong)
    magenta.place(relx=0.35, rely=0.9, relheight=0.05, relwidth=0.1)

    purple = Button(frame1, text='P', bg='blue', bd=0.01, command=wrong)
    purple.place(relx=0.45, rely=0.9, relheight=0.05, relwidth=0.1)

    violet = Button(frame1, text='V', bg='blue', bd=0.01, command=wrong)
    violet.place(relx=0.55, rely=0.9, relheight=0.05, relwidth=0.1)

    yellow = Button(frame1, text='Y', bg='blue', bd=0.01, command=wrong)
    yellow.place(relx=0.65, rely=0.9, relheight=0.05, relwidth=0.1)

    red = Button(frame1, text='R', bg='blue', bd=0.01, command=wrong)
    red.place(relx=0.75, rely=0.9, relheight=0.05, relwidth=0.1)

    green = Button(frame1, text='G', bg='blue', bd=0.01, command=wrong)
    green.place(relx=0.85, rely=0.9, relheight=0.05, relwidth=0.1)

    cyans1 = time.time()

    pass


def game2():
    global cyans2, blues2, indigos2, magentas2, purples2, violets2, yellows2, reds2, greens2
    first = Tk()
    first.title("hello" + name_id.get())
    canvas1 = Canvas(first, height=1000, width=1000)
    canvas1.pack()
    frame1 = Frame(first, bg='white')
    frame1.place(relwidth=1, relheight=1)
    labels = Label(frame1, bg='white', text='Select Blue = b, Cyan = c, Indigo = i, Magenta = m, Purple = '
                                            'p, Violet = v, Yellow = y, Red = r, Green = g')
    labels.place(relx=0.03, rely=0.1)

    colors_change = Label(frame1, bg='cyan', width=1, height=1)
    colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

    def wrong():
        wrongs = Label(frame1, text="Incorrect Input").pack()
        pass

    def green1():
        global greens2, indigos, yellows2, reds2, blues2, cyans2, magentas2, violets2, purples2
        greens2 = round((time.time() - greens2), 4)
        done = Label(frame1, text="TEST COMPLETED CHECK DESKTOP FOR RESULTS").pack()
        space = os.path.normpath(os.path.expanduser('~'))
        with open("%s/Desktop/%s3.txt" % (
                space, name_id.get()), 'w+') as done:
            done.write("\n" + '\n' + '\n' + '\n' + '\n')
            done.write(
                'Data for %s' % name_id.get() + '\n')
            done.write(
                'Gender %s' % sex_id.get() + '\n')
            done.write(
                'Age %s' % age_id.get() + '\n')
            done.write(
                'cyan 3: %s' % str(cyans2) + '\n')
            done.write('blue 3: %s' % str(blues2) + '\n')
            done.write(
                'indigo 3: %s' % str(indigos2) + '\n')
            done.write(
                'magenta 3: %s' % str(magentas2) + '\n')
            done.write(
                'violet 3: %s' % str(violets2) + '\n')
            done.write(
                'purple 3: %s' % str(purples2) + '\n')
            done.write(
                'red 3: %s' % str(reds2) + '\n')
            done.write(
                'yellow 3: %s' % str(yellows2) + '\n')
            done.write(
                'green 3: %s' % str(greens2) + '\n')
        time.sleep(2)
        frame1.destroy()
        endingframe = Frame(first)
        endingframe.place(relwidth=1, relheight=1)
        endinglabels = Label(endingframe, bg='white',
                             text='TEST COMPLETE FIND RESULT ON DESKTOP').pack()

        pass

    def yellow1():
        global greens2, yellows2
        yellows2 = round((time.time() - yellows2), 4)
        time.sleep(2)
        colors_change = Label(frame1, bg='green', width=1, height=1)
        colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

        cyan = Button(frame1, text='C', bg='blue', bd=0.01, command=wrong)
        cyan.place(relx=0.05, rely=0.9, relheight=0.05, relwidth=0.1)

        blue = Button(frame1, text='B', bg='blue', bd=0.01, command=wrong)
        blue.place(relx=0.15, rely=0.9, relheight=0.05, relwidth=0.1)

        violet = Button(frame1, text='V', bg='blue', bd=0.01, command=wrong)
        violet.place(relx=0.55, rely=0.9, relheight=0.05, relwidth=0.1)

        yellow = Button(frame1, text='Y', bg='blue', bd=0.01, command=wrong)
        yellow.place(relx=0.65, rely=0.9, relheight=0.05, relwidth=0.1)

        indigo = Button(frame1, text='I', bg='blue', bd=0.01, command=wrong)
        indigo.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.1)

        magenta = Button(frame1, text='M', bg='blue', bd=0.01, command=wrong)
        magenta.place(relx=0.35, rely=0.9, relheight=0.05, relwidth=0.1)

        purple = Button(frame1, text='P', bg='blue', bd=0.01, command=wrong)
        purple.place(relx=0.45, rely=0.9, relheight=0.05, relwidth=0.1)

        red = Button(frame1, text='R', bg='blue', bd=0.01, command=wrong)
        red.place(relx=0.75, rely=0.9, relheight=0.05, relwidth=0.1)

        green = Button(frame1, text='G', bg='blue', bd=0.01, command=green1)
        green.place(relx=0.85, rely=0.9, relheight=0.05, relwidth=0.1)

        greens2 = time.time()

        pass

    def red1():
        global reds2, yellows2
        reds2 = round((time.time() - reds2), 4)
        time.sleep(2)
        colors_change = Label(frame1, bg='yellow', width=1, height=1)
        colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

        cyan = Button(frame1, text='C', bg='blue', bd=0.01, command=wrong)
        cyan.place(relx=0.05, rely=0.9, relheight=0.05, relwidth=0.1)

        blue = Button(frame1, text='B', bg='blue', bd=0.01, command=wrong)
        blue.place(relx=0.15, rely=0.9, relheight=0.05, relwidth=0.1)

        violet = Button(frame1, text='V', bg='blue', bd=0.01, command=wrong)
        violet.place(relx=0.55, rely=0.9, relheight=0.05, relwidth=0.1)

        yellow = Button(frame1, text='Y', bg='blue', bd=0.01, command=yellow1)
        yellow.place(relx=0.65, rely=0.9, relheight=0.05, relwidth=0.1)

        red = Button(frame1, text='R', bg='blue', bd=0.01, command=wrong)
        red.place(relx=0.75, rely=0.9, relheight=0.05, relwidth=0.1)

        green = Button(frame1, text='G', bg='blue', bd=0.01, command=wrong)
        green.place(relx=0.85, rely=0.9, relheight=0.05, relwidth=0.1)

        indigo = Button(frame1, text='I', bg='blue', bd=0.01, command=wrong)
        indigo.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.1)

        magenta = Button(frame1, text='M', bg='blue', bd=0.01, command=wrong)
        magenta.place(relx=0.35, rely=0.9, relheight=0.05, relwidth=0.1)

        purple = Button(frame1, text='P', bg='blue', bd=0.01, command=wrong)
        purple.place(relx=0.45, rely=0.9, relheight=0.05, relwidth=0.1)

        yellows2 = time.time()

        pass

    def violet1():
        global violets2, reds2
        violets2 = round((time.time() - violets2), 4)
        time.sleep(2)
        colors_change = Label(frame1, bg='red', width=1, height=1)
        colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

        cyan = Button(frame1, text='C', bg='blue', bd=0.01, command=wrong)
        cyan.place(relx=0.05, rely=0.9, relheight=0.05, relwidth=0.1)

        blue = Button(frame1, text='B', bg='blue', bd=0.01, command=wrong)
        blue.place(relx=0.15, rely=0.9, relheight=0.05, relwidth=0.1)

        yellow = Button(frame1, text='Y', bg='blue', bd=0.01, command=wrong)
        yellow.place(relx=0.65, rely=0.9, relheight=0.05, relwidth=0.1)

        red = Button(frame1, text='R', bg='blue', bd=0.01, command=red1)
        red.place(relx=0.75, rely=0.9, relheight=0.05, relwidth=0.1)

        green = Button(frame1, text='G', bg='blue', bd=0.01, command=wrong)
        green.place(relx=0.85, rely=0.9, relheight=0.05, relwidth=0.1)

        indigo = Button(frame1, text='I', bg='blue', bd=0.01, command=wrong)
        indigo.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.1)

        magenta = Button(frame1, text='M', bg='blue', bd=0.01, command=wrong)
        magenta.place(relx=0.35, rely=0.9, relheight=0.05, relwidth=0.1)

        purple = Button(frame1, text='P', bg='blue', bd=0.01, command=wrong)
        purple.place(relx=0.45, rely=0.9, relheight=0.05, relwidth=0.1)

        violet = Button(frame1, text='V', bg='blue', bd=0.01, command=wrong)
        violet.place(relx=0.55, rely=0.9, relheight=0.05, relwidth=0.1)

        reds2 = time.time()

        pass

    def purple1():
        global purples2, violets2
        purples2 = round((time.time() - purples2), 4)
        time.sleep(2)
        colors_change = Label(frame1, bg='violet', width=1, height=1)
        colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

        cyan = Button(frame1, text='C', bg='blue', bd=0.01, command=wrong)
        cyan.place(relx=0.05, rely=0.9, relheight=0.05, relwidth=0.1)

        blue = Button(frame1, text='B', bg='blue', bd=0.01, command=wrong)
        blue.place(relx=0.15, rely=0.9, relheight=0.05, relwidth=0.1)

        indigo = Button(frame1, text='I', bg='blue', bd=0.01, command=wrong)
        indigo.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.1)

        yellow = Button(frame1, text='Y', bg='blue', bd=0.01, command=wrong)
        yellow.place(relx=0.65, rely=0.9, relheight=0.05, relwidth=0.1)

        red = Button(frame1, text='R', bg='blue', bd=0.01, command=wrong)
        red.place(relx=0.75, rely=0.9, relheight=0.05, relwidth=0.1)

        magenta = Button(frame1, text='M', bg='blue', bd=0.01, command=wrong)
        magenta.place(relx=0.35, rely=0.9, relheight=0.05, relwidth=0.1)

        purple = Button(frame1, text='P', bg='blue', bd=0.01, command=wrong)
        purple.place(relx=0.45, rely=0.9, relheight=0.05, relwidth=0.1)

        violet = Button(frame1, text='V', bg='blue', bd=0.01, command=violet1)
        violet.place(relx=0.55, rely=0.9, relheight=0.05, relwidth=0.1)

        green = Button(frame1, text='G', bg='blue', bd=0.01, command=wrong)
        green.place(relx=0.85, rely=0.9, relheight=0.05, relwidth=0.1)

        violets2 = time.time()

        pass

    def magenta1():
        global magentas2, purples2
        magentas2 = round((time.time() - magentas2), 4)
        time.sleep(2)
        colors_change = Label(frame1, bg='purple', width=1, height=1)
        colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

        cyan = Button(frame1, text='C', bg='blue', bd=0.01, command=wrong)
        cyan.place(relx=0.05, rely=0.9, relheight=0.05, relwidth=0.1)

        blue = Button(frame1, text='B', bg='blue', bd=0.01, command=wrong)
        blue.place(relx=0.15, rely=0.9, relheight=0.05, relwidth=0.1)

        indigo = Button(frame1, text='I', bg='blue', bd=0.01, command=wrong)
        indigo.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.1)

        yellow = Button(frame1, text='Y', bg='blue', bd=0.01, command=wrong)
        yellow.place(relx=0.65, rely=0.9, relheight=0.05, relwidth=0.1)

        red = Button(frame1, text='R', bg='blue', bd=0.01, command=wrong)
        red.place(relx=0.75, rely=0.9, relheight=0.05, relwidth=0.1)

        green = Button(frame1, text='G', bg='blue', bd=0.01, command=wrong)
        green.place(relx=0.85, rely=0.9, relheight=0.05, relwidth=0.1)

        magenta = Button(frame1, text='M', bg='blue', bd=0.01, command=wrong)
        magenta.place(relx=0.35, rely=0.9, relheight=0.05, relwidth=0.1)

        purple = Button(frame1, text='P', bg='blue', bd=0.01, command=purple1)
        purple.place(relx=0.45, rely=0.9, relheight=0.05, relwidth=0.1)

        violet = Button(frame1, text='V', bg='blue', bd=0.01, command=wrong)
        violet.place(relx=0.55, rely=0.9, relheight=0.05, relwidth=0.1)

        purples2 = time.time()

        pass

    def indigo1():
        global magentas2, indigos2
        indigos2 = round((time.time() - indigos2), 4)
        time.sleep(2)
        colors_change = Label(frame1, bg='magenta', width=1, height=1)
        colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

        cyan = Button(frame1, text='C', bg='blue', bd=0.01, command=wrong)
        cyan.place(relx=0.05, rely=0.9, relheight=0.05, relwidth=0.1)

        blue = Button(frame1, text='B', bg='blue', bd=0.01, command=wrong)
        blue.place(relx=0.15, rely=0.9, relheight=0.05, relwidth=0.1)

        indigo = Button(frame1, text='I', bg='blue', bd=0.01, command=wrong)
        indigo.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.1)

        magenta = Button(frame1, text='M', bg='blue', bd=0.01, command=magenta1)
        magenta.place(relx=0.35, rely=0.9, relheight=0.05, relwidth=0.1)

        purple = Button(frame1, text='P', bg='blue', bd=0.01, command=wrong)
        purple.place(relx=0.45, rely=0.9, relheight=0.05, relwidth=0.1)

        violet = Button(frame1, text='V', bg='blue', bd=0.01, command=wrong)
        violet.place(relx=0.55, rely=0.9, relheight=0.05, relwidth=0.1)

        yellow = Button(frame1, text='Y', bg='blue', bd=0.01, command=wrong)
        yellow.place(relx=0.65, rely=0.9, relheight=0.05, relwidth=0.1)

        red = Button(frame1, text='R', bg='blue', bd=0.01, command=wrong)
        red.place(relx=0.75, rely=0.9, relheight=0.05, relwidth=0.1)

        green = Button(frame1, text='G', bg='blue', bd=0.01, command=wrong)
        green.place(relx=0.85, rely=0.9, relheight=0.05, relwidth=0.1)

        magentas2 = time.time()

        pass

    def blue1():
        global blues2, indigos2
        blues2 = round((time.time() - blues2), 4)
        time.sleep(2)
        colors_change = Label(frame1, bg='indigo', width=1, height=1)
        colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

        cyan = Button(frame1, text='C', bg='blue', bd=0.01, command=wrong)
        cyan.place(relx=0.05, rely=0.9, relheight=0.05, relwidth=0.1)

        blue = Button(frame1, text='B', bg='blue', bd=0.01, command=wrong)
        blue.place(relx=0.15, rely=0.9, relheight=0.05, relwidth=0.1)

        indigo = Button(frame1, text='I', bg='blue', bd=0.01, command=indigo1)
        indigo.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.1)

        magenta = Button(frame1, text='M', bg='blue', bd=0.01, command=wrong)
        magenta.place(relx=0.35, rely=0.9, relheight=0.05, relwidth=0.1)

        purple = Button(frame1, text='P', bg='blue', bd=0.01, command=wrong)
        purple.place(relx=0.45, rely=0.9, relheight=0.05, relwidth=0.1)

        violet = Button(frame1, text='V', bg='blue', bd=0.01, command=wrong)
        violet.place(relx=0.55, rely=0.9, relheight=0.05, relwidth=0.1)

        yellow = Button(frame1, text='Y', bg='blue', bd=0.01, command=wrong)
        yellow.place(relx=0.65, rely=0.9, relheight=0.05, relwidth=0.1)

        red = Button(frame1, text='R', bg='blue', bd=0.01, command=wrong)
        red.place(relx=0.75, rely=0.9, relheight=0.05, relwidth=0.1)

        green = Button(frame1, text='G', bg='blue', bd=0.01, command=wrong)
        green.place(relx=0.85, rely=0.9, relheight=0.05, relwidth=0.1)

        indigos2 = time.time()

        pass

    def cyan1():
        global cyans2, blues2
        cyans2 = round((time.time() - cyans2), 4)
        time.sleep(2)
        colors_change = Label(frame1, bg='blue', width=1, height=1)
        colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

        cyan = Button(frame1, text='C', bg='blue', bd=0.01, command=wrong)
        cyan.place(relx=0.05, rely=0.9, relheight=0.05, relwidth=0.1)

        blue = Button(frame1, text='B', bg='blue', bd=0.01, command=blue1)
        blue.place(relx=0.15, rely=0.9, relheight=0.05, relwidth=0.1)

        indigo = Button(frame1, text='I', bg='blue', bd=0.01, command=wrong)
        indigo.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.1)

        magenta = Button(frame1, text='M', bg='blue', bd=0.01, command=wrong)
        magenta.place(relx=0.35, rely=0.9, relheight=0.05, relwidth=0.1)

        purple = Button(frame1, text='P', bg='blue', bd=0.01, command=wrong)
        purple.place(relx=0.45, rely=0.9, relheight=0.05, relwidth=0.1)

        violet = Button(frame1, text='V', bg='blue', bd=0.01, command=wrong)
        violet.place(relx=0.55, rely=0.9, relheight=0.05, relwidth=0.1)

        yellow = Button(frame1, text='Y', bg='blue', bd=0.01, command=wrong)
        yellow.place(relx=0.65, rely=0.9, relheight=0.05, relwidth=0.1)

        red = Button(frame1, text='R', bg='blue', bd=0.01, command=wrong)
        red.place(relx=0.75, rely=0.9, relheight=0.05, relwidth=0.1)

        green = Button(frame1, text='G', bg='blue', bd=0.01, command=wrong)
        green.place(relx=0.85, rely=0.9, relheight=0.05, relwidth=0.1)

        blues2 = time.time()

        pass

    cyan = Button(frame1, text='C', bg='blue', bd=0.01, command=cyan1)
    cyan.place(relx=0.05, rely=0.9, relheight=0.05, relwidth=0.1)

    blue = Button(frame1, text='B', bg='blue', bd=0.01, command=wrong)
    blue.place(relx=0.15, rely=0.9, relheight=0.05, relwidth=0.1)

    indigo = Button(frame1, text='I', bg='blue', bd=0.01, command=wrong)
    indigo.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.1)

    magenta = Button(frame1, text='M', bg='blue', bd=0.01, command=wrong)
    magenta.place(relx=0.35, rely=0.9, relheight=0.05, relwidth=0.1)

    purple = Button(frame1, text='P', bg='blue', bd=0.01, command=wrong)
    purple.place(relx=0.45, rely=0.9, relheight=0.05, relwidth=0.1)

    violet = Button(frame1, text='V', bg='blue', bd=0.01, command=wrong)
    violet.place(relx=0.55, rely=0.9, relheight=0.05, relwidth=0.1)

    yellow = Button(frame1, text='Y', bg='blue', bd=0.01, command=wrong)
    yellow.place(relx=0.65, rely=0.9, relheight=0.05, relwidth=0.1)

    red = Button(frame1, text='R', bg='blue', bd=0.01, command=wrong)
    red.place(relx=0.75, rely=0.9, relheight=0.05, relwidth=0.1)

    green = Button(frame1, text='G', bg='blue', bd=0.01, command=wrong)
    green.place(relx=0.85, rely=0.9, relheight=0.05, relwidth=0.1)

    cyans2 = time.time()

    pass


def game3():
    global cyans3, blues3, indigos3, magentas3, purples3, violets3, yellows3, reds3, greens3
    first = Tk()
    first.title("hello" + name_id.get())
    canvas1 = Canvas(first, height=1000, width=1000)
    canvas1.pack()
    frame1 = Frame(first, bg='white')
    frame1.place(relwidth=1, relheight=1)
    labels = Label(frame1, bg='white', text='Select letters Blue = b, Cyan = c, Indigo = i, Magenta = m, Purple = '
                                            'p, Violet = v, Yellow = y, Red = r, Green = g')
    labels.place(relx=0.03, rely=0.1)

    colors_change = Label(frame1, bg='cyan', width=1, height=1)
    colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

    def wrong():
        wrongs = Label(frame1, text="Incorrect Input").pack()
        pass

    def green1():
        global greens, indigos, yellows, reds, blues, cyans, magentas, violets, purples
        global greens2, indigos2, yellows2, reds2, blues2, cyans2, magentas2, violets2, purples2
        global greens1, indigos1, yellows1, reds1, blues1, cyans1, magentas1, violets1, purples1
        global greens3, indigos3, yellows3, reds3, blues3, cyans3, magentas3, violets3, purples3
        greens3 = round((time.time() - greens3), 4)
        avgreen = str((greens+greens1+greens2+greens3)/4)
        avgreen = round(avgreen,4)
        avred = str((reds + reds1 + reds2 + reds3) / 4)
        avred = round(avred, 4)
        avyellow = str((yellows + yellows1 + yellows2 + yellows3) / 4)
        avyellow = round(avyellow, 4)
        avindigo = str((indigos + indigos1 + indigos2 + indigos3) / 4)
        avindigo = round(avindigo, 4)
        avblue = str((blues + blues1 + blues2 + blues3) / 4)
        avblue = round(avblue, 4)
        avcyan = str((cyans + cyans1 + cyans2 + cyans3) / 4)
        avcyan = round(avcyan, 4)
        avmagenta = str((magentas + magentas1 + magentas2 + magentas3) / 4)
        avmagenta = round(avmagenta, 4)
        avviolet = str((violets + violets1 + violets2 + violets3) / 4)
        avviolet = round(avviolet, 4)
        avpurple = str((purples + purples1 + purples2 + purples3) / 4)
        avpurple = round(avpurple, 4)

        done = Label(frame1, text="TEST COMPLETED CHECK DESKTOP FOR RESULTS").pack()
        space = os.path.normpath(os.path.expanduser('~'))
        with open("%s/Desktop/%s4.txt" % (
                space, name_id.get()), 'w+') as done:
            done.write("\n" + '\n' + '\n' + '\n' + '\n')
            done.write(
                'Data for %s' % name_id.get() + '\n')
            done.write(
                'Gender %s' % sex_id.get() + '\n')
            done.write(
                'Age %s' % age_id.get() + '\n')
            done.write(
                'cyan 4: %s' % str(cyans3) + '\n')
            done.write('blue 4: %s' % str(blues3) + '\n')
            done.write(
                'indigo 4: %s' % str(indigos3) + '\n')
            done.write(
                'magenta 4: %s' % str(magentas3) + '\n')
            done.write(
                'violet 4: %s' % str(violets3) + '\n')
            done.write(
                'purple 4: %s' % str(purples3) + '\n')
            done.write(
                'red 4: %s' % str(reds3) + '\n')
            done.write(
                'yellow 4: %s' % str(yellows3) + '\n')
            done.write(
                'green 4: %s' % str(greens3) + '\n'+ '\n'+ '\n'+ '\n')
            done.write('AVERAGE FOR COLORS ARE: ' + '\n')
            done.write('GREEN: %s '% str(avgreen)+'\n'+'RED: %s'% str(avred)+'\n'+'YELLOW: %s '% str(avyellow)+'\n'+'CYAN: %s'% str(avcyan)+'\n'+'BLUE: %s '% str(avblue)+
                       '\n'+'INDIGO: %s'% str(avindigo) +'\n')
            done.write('PURPLE: %s '% str(avpurple) + '\n' + 'VIOLET: %s'% str(avviolet) + '\n' + 'MAGENTA: %s '% str(avmagenta) )
        time.sleep(2)
        frame1.destroy()
        endingframe = Frame(first)
        endingframe.place(relwidth=1, relheight=1)
        endinglabels = Label(endingframe, bg='white',
                             text='TEST COMPLETE FIND RESULT ON DESKTOP').pack()

        pass

    def yellow1():
        global greens3, yellows3
        yellows3 = round((time.time() - yellows3), 4)
        time.sleep(2)
        colors_change = Label(frame1, bg='green', width=1, height=1)
        colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

        cyan = Button(frame1, text='C', bg='blue', bd=0.01, command=wrong)
        cyan.place(relx=0.05, rely=0.9, relheight=0.05, relwidth=0.1)

        blue = Button(frame1, text='B', bg='blue', bd=0.01, command=wrong)
        blue.place(relx=0.15, rely=0.9, relheight=0.05, relwidth=0.1)

        violet = Button(frame1, text='V', bg='blue', bd=0.01, command=wrong)
        violet.place(relx=0.55, rely=0.9, relheight=0.05, relwidth=0.1)

        yellow = Button(frame1, text='Y', bg='blue', bd=0.01, command=wrong)
        yellow.place(relx=0.65, rely=0.9, relheight=0.05, relwidth=0.1)

        indigo = Button(frame1, text='I', bg='blue', bd=0.01, command=wrong)
        indigo.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.1)

        magenta = Button(frame1, text='M', bg='blue', bd=0.01, command=wrong)
        magenta.place(relx=0.35, rely=0.9, relheight=0.05, relwidth=0.1)

        purple = Button(frame1, text='P', bg='blue', bd=0.01, command=wrong)
        purple.place(relx=0.45, rely=0.9, relheight=0.05, relwidth=0.1)

        red = Button(frame1, text='R', bg='blue', bd=0.01, command=wrong)
        red.place(relx=0.75, rely=0.9, relheight=0.05, relwidth=0.1)

        green = Button(frame1, text='G', bg='blue', bd=0.01, command=green1)
        green.place(relx=0.85, rely=0.9, relheight=0.05, relwidth=0.1)

        greens3 = time.time()

        pass

    def red1():
        global reds3, yellows3
        reds3 = round((time.time() - reds3), 4)
        time.sleep(2)
        colors_change = Label(frame1, bg='yellow', width=1, height=1)
        colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

        cyan = Button(frame1, text='C', bg='blue', bd=0.01, command=wrong)
        cyan.place(relx=0.05, rely=0.9, relheight=0.05, relwidth=0.1)

        blue = Button(frame1, text='B', bg='blue', bd=0.01, command=wrong)
        blue.place(relx=0.15, rely=0.9, relheight=0.05, relwidth=0.1)

        violet = Button(frame1, text='V', bg='blue', bd=0.01, command=wrong)
        violet.place(relx=0.55, rely=0.9, relheight=0.05, relwidth=0.1)

        yellow = Button(frame1, text='Y', bg='blue', bd=0.01, command=yellow1)
        yellow.place(relx=0.65, rely=0.9, relheight=0.05, relwidth=0.1)

        red = Button(frame1, text='R', bg='blue', bd=0.01, command=wrong)
        red.place(relx=0.75, rely=0.9, relheight=0.05, relwidth=0.1)

        green = Button(frame1, text='G', bg='blue', bd=0.01, command=wrong)
        green.place(relx=0.85, rely=0.9, relheight=0.05, relwidth=0.1)

        indigo = Button(frame1, text='I', bg='blue', bd=0.01, command=wrong)
        indigo.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.1)

        magenta = Button(frame1, text='M', bg='blue', bd=0.01, command=wrong)
        magenta.place(relx=0.35, rely=0.9, relheight=0.05, relwidth=0.1)

        purple = Button(frame1, text='P', bg='blue', bd=0.01, command=wrong)
        purple.place(relx=0.45, rely=0.9, relheight=0.05, relwidth=0.1)

        yellows3 = time.time()

        pass

    def violet1():
        global violets3, reds3
        violets3 = round((time.time() - violets3), 4)
        time.sleep(2)
        colors_change = Label(frame1, bg='red', width=1, height=1)
        colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

        cyan = Button(frame1, text='C', bg='blue', bd=0.01, command=wrong)
        cyan.place(relx=0.05, rely=0.9, relheight=0.05, relwidth=0.1)

        blue = Button(frame1, text='B', bg='blue', bd=0.01, command=wrong)
        blue.place(relx=0.15, rely=0.9, relheight=0.05, relwidth=0.1)

        yellow = Button(frame1, text='Y', bg='blue', bd=0.01, command=wrong)
        yellow.place(relx=0.65, rely=0.9, relheight=0.05, relwidth=0.1)

        red = Button(frame1, text='R', bg='blue', bd=0.01, command=red1)
        red.place(relx=0.75, rely=0.9, relheight=0.05, relwidth=0.1)

        green = Button(frame1, text='G', bg='blue', bd=0.01, command=wrong)
        green.place(relx=0.85, rely=0.9, relheight=0.05, relwidth=0.1)

        indigo = Button(frame1, text='I', bg='blue', bd=0.01, command=wrong)
        indigo.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.1)

        magenta = Button(frame1, text='M', bg='blue', bd=0.01, command=wrong)
        magenta.place(relx=0.35, rely=0.9, relheight=0.05, relwidth=0.1)

        purple = Button(frame1, text='P', bg='blue', bd=0.01, command=wrong)
        purple.place(relx=0.45, rely=0.9, relheight=0.05, relwidth=0.1)

        violet = Button(frame1, text='V', bg='blue', bd=0.01, command=wrong)
        violet.place(relx=0.55, rely=0.9, relheight=0.05, relwidth=0.1)

        reds3 = time.time()

        pass

    def purple1():
        global purples3, violets3
        purples3 = round((time.time() - purples3), 4)
        time.sleep(2)
        colors_change = Label(frame1, bg='violet', width=1, height=1)
        colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

        cyan = Button(frame1, text='C', bg='blue', bd=0.01, command=wrong)
        cyan.place(relx=0.05, rely=0.9, relheight=0.05, relwidth=0.1)

        blue = Button(frame1, text='B', bg='blue', bd=0.01, command=wrong)
        blue.place(relx=0.15, rely=0.9, relheight=0.05, relwidth=0.1)

        indigo = Button(frame1, text='I', bg='blue', bd=0.01, command=wrong)
        indigo.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.1)

        yellow = Button(frame1, text='Y', bg='blue', bd=0.01, command=wrong)
        yellow.place(relx=0.65, rely=0.9, relheight=0.05, relwidth=0.1)

        red = Button(frame1, text='R', bg='blue', bd=0.01, command=wrong)
        red.place(relx=0.75, rely=0.9, relheight=0.05, relwidth=0.1)

        magenta = Button(frame1, text='M', bg='blue', bd=0.01, command=wrong)
        magenta.place(relx=0.35, rely=0.9, relheight=0.05, relwidth=0.1)

        purple = Button(frame1, text='P', bg='blue', bd=0.01, command=wrong)
        purple.place(relx=0.45, rely=0.9, relheight=0.05, relwidth=0.1)

        violet = Button(frame1, text='V', bg='blue', bd=0.01, command=violet1)
        violet.place(relx=0.55, rely=0.9, relheight=0.05, relwidth=0.1)

        green = Button(frame1, text='G', bg='blue', bd=0.01, command=wrong)
        green.place(relx=0.85, rely=0.9, relheight=0.05, relwidth=0.1)

        violets3 = time.time()

        pass

    def magenta1():
        global magentas3, purples3
        magentas3 = round((time.time() - magentas3), 4)
        time.sleep(2)
        colors_change = Label(frame1, bg='purple', width=1, height=1)
        colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

        cyan = Button(frame1, text='C', bg='blue', bd=0.01, command=wrong)
        cyan.place(relx=0.05, rely=0.9, relheight=0.05, relwidth=0.1)

        blue = Button(frame1, text='B', bg='blue', bd=0.01, command=wrong)
        blue.place(relx=0.15, rely=0.9, relheight=0.05, relwidth=0.1)

        indigo = Button(frame1, text='I', bg='blue', bd=0.01, command=wrong)
        indigo.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.1)

        yellow = Button(frame1, text='Y', bg='blue', bd=0.01, command=wrong)
        yellow.place(relx=0.65, rely=0.9, relheight=0.05, relwidth=0.1)

        red = Button(frame1, text='R', bg='blue', bd=0.01, command=wrong)
        red.place(relx=0.75, rely=0.9, relheight=0.05, relwidth=0.1)

        green = Button(frame1, text='G', bg='blue', bd=0.01, command=wrong)
        green.place(relx=0.85, rely=0.9, relheight=0.05, relwidth=0.1)

        magenta = Button(frame1, text='M', bg='blue', bd=0.01, command=wrong)
        magenta.place(relx=0.35, rely=0.9, relheight=0.05, relwidth=0.1)

        purple = Button(frame1, text='P', bg='blue', bd=0.01, command=purple1)
        purple.place(relx=0.45, rely=0.9, relheight=0.05, relwidth=0.1)

        violet = Button(frame1, text='V', bg='blue', bd=0.01, command=wrong)
        violet.place(relx=0.55, rely=0.9, relheight=0.05, relwidth=0.1)

        purples3 = time.time()

        pass

    def indigo1():
        global magentas3, indigos3
        indigos3 = round((time.time() - indigos3), 4)
        time.sleep(2)
        colors_change = Label(frame1, bg='magenta', width=1, height=1)
        colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

        cyan = Button(frame1, text='C', bg='blue', bd=0.01, command=wrong)
        cyan.place(relx=0.05, rely=0.9, relheight=0.05, relwidth=0.1)

        blue = Button(frame1, text='B', bg='blue', bd=0.01, command=wrong)
        blue.place(relx=0.15, rely=0.9, relheight=0.05, relwidth=0.1)

        indigo = Button(frame1, text='I', bg='blue', bd=0.01, command=wrong)
        indigo.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.1)

        magenta = Button(frame1, text='M', bg='blue', bd=0.01, command=magenta1)
        magenta.place(relx=0.35, rely=0.9, relheight=0.05, relwidth=0.1)

        purple = Button(frame1, text='P', bg='blue', bd=0.01, command=wrong)
        purple.place(relx=0.45, rely=0.9, relheight=0.05, relwidth=0.1)

        violet = Button(frame1, text='V', bg='blue', bd=0.01, command=wrong)
        violet.place(relx=0.55, rely=0.9, relheight=0.05, relwidth=0.1)

        yellow = Button(frame1, text='Y', bg='blue', bd=0.01, command=wrong)
        yellow.place(relx=0.65, rely=0.9, relheight=0.05, relwidth=0.1)

        red = Button(frame1, text='R', bg='blue', bd=0.01, command=wrong)
        red.place(relx=0.75, rely=0.9, relheight=0.05, relwidth=0.1)

        green = Button(frame1, text='G', bg='blue', bd=0.01, command=wrong)
        green.place(relx=0.85, rely=0.9, relheight=0.05, relwidth=0.1)

        magentas3 = time.time()

        pass

    def blue1():
        global blues3, indigos3
        blues3 = round((time.time() - blues3), 4)
        time.sleep(2)
        colors_change = Label(frame1, bg='indigo', width=1, height=1)
        colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

        cyan = Button(frame1, text='C', bg='blue', bd=0.01, command=wrong)
        cyan.place(relx=0.05, rely=0.9, relheight=0.05, relwidth=0.1)

        blue = Button(frame1, text='B', bg='blue', bd=0.01, command=wrong)
        blue.place(relx=0.15, rely=0.9, relheight=0.05, relwidth=0.1)

        indigo = Button(frame1, text='I', bg='blue', bd=0.01, command=indigo1)
        indigo.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.1)

        magenta = Button(frame1, text='M', bg='blue', bd=0.01, command=wrong)
        magenta.place(relx=0.35, rely=0.9, relheight=0.05, relwidth=0.1)

        purple = Button(frame1, text='P', bg='blue', bd=0.01, command=wrong)
        purple.place(relx=0.45, rely=0.9, relheight=0.05, relwidth=0.1)

        violet = Button(frame1, text='V', bg='blue', bd=0.01, command=wrong)
        violet.place(relx=0.55, rely=0.9, relheight=0.05, relwidth=0.1)

        yellow = Button(frame1, text='Y', bg='blue', bd=0.01, command=wrong)
        yellow.place(relx=0.65, rely=0.9, relheight=0.05, relwidth=0.1)

        red = Button(frame1, text='R', bg='blue', bd=0.01, command=wrong)
        red.place(relx=0.75, rely=0.9, relheight=0.05, relwidth=0.1)

        green = Button(frame1, text='G', bg='blue', bd=0.01, command=wrong)
        green.place(relx=0.85, rely=0.9, relheight=0.05, relwidth=0.1)

        indigos3 = time.time()

        pass

    def cyan1():
        global cyans3, blues3
        cyans3 = round((time.time() - cyans3), 4)
        time.sleep(2)
        colors_change = Label(frame1, bg='blue', width=1, height=1)
        colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

        cyan = Button(frame1, text='C', bg='blue', bd=0.01, command=wrong)
        cyan.place(relx=0.05, rely=0.9, relheight=0.05, relwidth=0.1)

        blue = Button(frame1, text='B', bg='blue', bd=0.01, command=blue1)
        blue.place(relx=0.15, rely=0.9, relheight=0.05, relwidth=0.1)

        indigo = Button(frame1, text='I', bg='blue', bd=0.01, command=wrong)
        indigo.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.1)

        magenta = Button(frame1, text='M', bg='blue', bd=0.01, command=wrong)
        magenta.place(relx=0.35, rely=0.9, relheight=0.05, relwidth=0.1)

        purple = Button(frame1, text='P', bg='blue', bd=0.01, command=wrong)
        purple.place(relx=0.45, rely=0.9, relheight=0.05, relwidth=0.1)

        violet = Button(frame1, text='V', bg='blue', bd=0.01, command=wrong)
        violet.place(relx=0.55, rely=0.9, relheight=0.05, relwidth=0.1)

        yellow = Button(frame1, text='Y', bg='blue', bd=0.01, command=wrong)
        yellow.place(relx=0.65, rely=0.9, relheight=0.05, relwidth=0.1)

        red = Button(frame1, text='R', bg='blue', bd=0.01, command=wrong)
        red.place(relx=0.75, rely=0.9, relheight=0.05, relwidth=0.1)

        green = Button(frame1, text='G', bg='blue', bd=0.01, command=wrong)
        green.place(relx=0.85, rely=0.9, relheight=0.05, relwidth=0.1)

        blues3 = time.time()

        pass

    cyan = Button(frame1, text='C', bg='blue', bd=0.01, command=cyan1)
    cyan.place(relx=0.05, rely=0.9, relheight=0.05, relwidth=0.1)

    blue = Button(frame1, text='B', bg='blue', bd=0.01, command=wrong)
    blue.place(relx=0.15, rely=0.9, relheight=0.05, relwidth=0.1)

    indigo = Button(frame1, text='I', bg='blue', bd=0.01, command=wrong)
    indigo.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.1)

    magenta = Button(frame1, text='M', bg='blue', bd=0.01, command=wrong)
    magenta.place(relx=0.35, rely=0.9, relheight=0.05, relwidth=0.1)

    purple = Button(frame1, text='P', bg='blue', bd=0.01, command=wrong)
    purple.place(relx=0.45, rely=0.9, relheight=0.05, relwidth=0.1)

    violet = Button(frame1, text='V', bg='blue', bd=0.01, command=wrong)
    violet.place(relx=0.55, rely=0.9, relheight=0.05, relwidth=0.1)

    yellow = Button(frame1, text='Y', bg='blue', bd=0.01, command=wrong)
    yellow.place(relx=0.65, rely=0.9, relheight=0.05, relwidth=0.1)

    red = Button(frame1, text='R', bg='blue', bd=0.01, command=wrong)
    red.place(relx=0.75, rely=0.9, relheight=0.05, relwidth=0.1)

    green = Button(frame1, text='G', bg='blue', bd=0.01, command=wrong)
    green.place(relx=0.85, rely=0.9, relheight=0.05, relwidth=0.1)

    cyans3 = time.time()

    pass


def buttons():
    name = name_id.get()
    age = age_id.get()
    sex = sex_id.get()

    if name != "" and name !=" " and age!="" and age.isdigit() and sex!="" and sex == 'male' or sex == 'female' :
        window.destroy()
        buttonpage = Tk()

        buttonpage.title('SELECT TEST ' + name_id.get())
        buttoncanvas = Canvas(height=500, width=500)
        buttoncanvas.pack()
        buttonframe = Frame(bg='white')
        buttonframe.place(relwidth=1, relheight=1)

        fiimg = Image.open("images/anotherone.png")
        adimg = ImageTk.PhotoImage(fiimg)
        labels = Label(buttonframe, image=adimg, bg='white', width=1, height=1)
        labels.place(relx=0.25, rely=0.002, relheight=0.5, relwidth=0.5)

        button1 = Button(buttonframe, text='TEST 1', bg='blue',fg='white', bd=0.01, command=game)

        button1.place(relx=0.1, rely=0.4, relheight=0.09, relwidth=0.3)
        button2 = Button(buttonframe, text='TEST 2', bg='blue',fg='white', bd=0.01, command=game1)

        button2.place(relx=0.1, rely=0.6, relheight=0.09, relwidth=0.3)
        button3 = Button(buttonframe, text='TEST 3', bg='blue',fg='white', bd=0.01, command=game2)

        button3.place(relx=0.6, rely=0.4, relheight=0.09, relwidth=0.3)
        button4 = Button(buttonframe, text='TEST 4', bg='blue',fg='white', bd=0.01, command=game3)

        button4.place(relx=0.6, rely=0.6, relheight=0.09, relwidth=0.3)
        buttonpage.mainloop()
    else:
        error = Label(frame, text="PLEASE INPUT SUBJECT DETAILS", fg='white', bg='black').place(relx=0.25, rely=0.1,
                                                                                                relheight=0.05,
                                                                                                relwidth=0.5)


button = Button(frame, text='Start', bg='blue', bd=0.01,fg='white', command=buttons)

button.place(relx=0.35, rely=0.8, relheight=0.09, relwidth=0.3)
eleos= Label(frame, text='eleos', bg='black',fg='white').place(relx=0.45,rely=0.97)

window.mainloop()
