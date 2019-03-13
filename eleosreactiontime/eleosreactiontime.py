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
##############################################test 2 #########################################################
cyans1 = 0
blues1 = 0
indigos1 = 0
magentas1 = 0
purples1 = 0
violets1 = 0
##############################################test 3 #########################################################
cyans2 = 0
blues2 = 0
indigos2 = 0
magentas2 = 0
purples2 = 0
violets2 = 0
##############################################test 4 #########################################################
cyans3 = 0
blues3 = 0
indigos3 = 0
magentas3 = 0
purples3 = 0
violets3 = 0
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
# name request
name_label = Label(frame, text="Input Subject's Name:", fg='white', bg='black').place(relx=0.25, rely=0.5,
                                                                                      relheight=0.05, relwidth=0.5)
name_id = StringVar()
name_input = Entry(frame, textvariable=name_id).place(relx=0.25, rely=0.55, relheight=0.05, relwidth=0.5)


def game():
    global cyans, blues, indigos, purples, magentas, violets
    names = name_id.get()
    # new page loop
    # confirmation if the page is correct
    if names != "":
        nextPage = Tk()
        # nextPage.geometry('900x900')
        nextPage.title('Hello: ' + names)

        canvas1 = Canvas(nextPage, height=1000, width=1000)
        canvas1.pack()
        frame1 = Frame(nextPage, bg='white')
        frame1.place(relwidth=1, relheight=1)
        labels = Label(frame1, bg='white', text='Input letters Blue = b, Cyan = c, Indigo = i, Magenta = m, Purple = '
                                                'p, Violet = v')
        labels.place(relx=0.03, rely=0.1)

        colors_change = Label(frame1, bg='cyan', width=1, height=1)
        colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

        response = Entry(frame1)
        response.place(relx=0.47, rely=0.75, relheight=0.05, relwidth=0.05)
        cyans = time.time()

        def nexts():
            global cyans, blues
            names = response.get().lower()

            if names == 'c' or names == 'b' or names == 'i' or names == 'm' or names == 'p' or names == 'v':
                if names == 'c':
                    cyans =  time.time() - cyans
                    frame1.destroy()
                    time.sleep(5)
                    cyanframe = Frame(nextPage)
                    cyanframe.place(relwidth=1, relheight=1)
                    cyanlabels = Label(cyanframe, bg='white',
                                       text='Input letters Blue = b, Cyan = c, Indigo = i, Magenta = m, Purple = '
                                            'p, Violet = v')
                    cyanlabels.place(relx=0.03, rely=0.1)
                    cyan_change = Label(cyanframe, bg='blue', width=1, height=1)
                    cyan_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)
                    cyanresponse = Entry(cyanframe)
                    cyanresponse.place(relx=0.47, rely=0.75, relheight=0.05, relwidth=0.05)
                    blues = time.time()
###############################################################################################################################################################################
################################################################################cyan function #############################################
                    def cyan():
                        global blues,indigos
                        bluenames = cyanresponse.get().lower()
                        if bluenames == 'c' or bluenames == 'b' or bluenames == 'i' or bluenames == 'm' or bluenames == 'p' or bluenames == 'v':
                            if bluenames == 'b':
                                blues = time.time() - blues
                                cyanframe.destroy()
                                time.sleep(5)
                                blueframe = Frame(nextPage)
                                blueframe.place(relwidth=1, relheight=1)
                                bluelabels = Label(blueframe, bg='white',
                                                   text='Input letters Blue = b, Cyan = c, Indigo = i, Magenta = m, Purple = '
                                                        'p, Violet = v')
                                bluelabels.place(relx=0.03, rely=0.1)
                                blue_change = Label(blueframe, bg='indigo', width=1, height=1)
                                blue_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)
                                blueresponse = Entry(blueframe)
                                blueresponse.place(relx=0.47, rely=0.75, relheight=0.05, relwidth=0.05)
                                indigos = time.time()

################################################################################### add blue button command here ################################################################
                                def blue():
                                    global indigos, magentas
                                    indigonames = blueresponse.get().lower()
                                    if indigonames == 'c' or indigonames == 'b' or indigonames == 'i' or indigonames == 'm' or indigonames == 'p' or indigonames == 'v':
                                        if indigonames == 'i':
                                            indigos = time.time() - indigos
                                            blueframe.destroy()
                                            time.sleep(5)
                                            indigoframe = Frame(nextPage)
                                            indigoframe.place(relwidth=1, relheight=1)
                                            indigolabels = Label(indigoframe, bg='white',
                                                                 text='Input letters Blue = b, Cyan = c, Indigo = i, Magenta = m, Purple = '
                                                                      'p, Violet = v')
                                            indigolabels.place(relx=0.03, rely=0.1)
                                            indigo_change = Label(indigoframe, bg='magenta', width=1, height=1)
                                            indigo_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)
                                            indigoresponse = Entry(indigoframe)
                                            indigoresponse.place(relx=0.47, rely=0.75, relheight=0.05, relwidth=0.05)
                                            magentas = time.time()
################################################################################################################################################################################
################################### add function for magenta######################################################
                                            def magenta():
                                                global magentas, violets
                                                purplenames = indigoresponse.get().lower()
                                                if purplenames == 'c' or purplenames == 'b' or purplenames == 'i' or purplenames == 'm' or purplenames == 'p' or purplenames == 'v':
                                                    if purplenames == 'm':
                                                        magentas = time.time() - magentas
                                                        indigoframe.destroy()
                                                        time.sleep(5)
                                                        purpleframe = Frame(nextPage)
                                                        purpleframe.place(relwidth=1, relheight=1)
                                                        purplelabels = Label(purpleframe, bg='white',
                                                                             text='Input letters Blue = b, Cyan = c, Indigo = i, Magenta = m, Purple = '
                                                                                  'p, Violet = v')
                                                        purplelabels.place(relx=0.03, rely=0.1)
                                                        purple_change = Label(purpleframe, bg='violet', width=1,
                                                                              height=1)
                                                        purple_change.place(relx=0.25, rely=0.2, relwidth=0.5,
                                                                            relheight=0.5)
                                                        purpleresponse = Entry(purpleframe)
                                                        purpleresponse.place(relx=0.47, rely=0.75, relheight=0.05,
                                                                             relwidth=0.05)
                                                        violets = time.time()
################################################################################################################################################################################
################################################### put purple functions here###########################################################################################
                                                        def purple():
                                                            global violets, purples
                                                            violetnames = purpleresponse.get().lower()
                                                            if violetnames == 'c' or violetnames == 'b' or violetnames == 'i' or violetnames == 'm' or violetnames == 'p' or violetnames == 'v':
                                                                if violetnames == 'v':
                                                                    violets = time.time() - violets
                                                                    purpleframe.destroy()
                                                                    time.sleep(5)
                                                                    violetframe = Frame(nextPage)
                                                                    violetframe.place(relwidth=1, relheight=1)
                                                                    violetlabels = Label(violetframe, bg='white',
                                                                                         text='Input letters Blue = b, Cyan = c, Indigo = i, Magenta = m, Purple = '
                                                                                              'p, Violet = v')
                                                                    violetlabels.place(relx=0.03, rely=0.1)
                                                                    violet_change = Label(violetframe, bg='purple',
                                                                                          width=1, height=1)
                                                                    violet_change.place(relx=0.25, rely=0.2,
                                                                                        relwidth=0.5, relheight=0.5)
                                                                    violetresponse = Entry(violetframe)
                                                                    violetresponse.place(relx=0.47, rely=0.75,
                                                                                         relheight=0.05, relwidth=0.05)
                                                                    purples = time.time()
#############################################################################################################################################################################################
###################################### add violet function ####################################################################################################################
                                                                    def fin():
                                                                        global cyans, blues, indigos, magentas, violets, purples
                                                                        purples = time.time() - purples
                                                                        cyans = round(cyans,4)
                                                                        blues = round(blues,4)
                                                                        indigos = round(indigos,4)
                                                                        magentas = round(magentas,4)
                                                                        violets = round(violets,4)
                                                                        purples = round(purples,4)
                                                                        space = os.path.normpath(os.path.expanduser('~'))
                                                                        with open("%s/Desktop/%s1.txt" % (
                                                                        space, name_id.get()), 'w+') as done:
                                                                            done.write("\n" + '\n' + '\n' + '\n' + '\n')
                                                                            done.write(
                                                                                'Data for %s' % name_id.get() + '\n')
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
                                                                        time.sleep(2)
                                                                        violetframe.destroy()
                                                                        endingframe = Frame(nextPage)
                                                                        endingframe.place(relwidth=1, relheight=1)
                                                                        endinglabels = Label(endingframe, bg='white',
                                                                                             text='TEST COMPLETE FIND RESULT ON DESKTOP').pack()

                                                                    #################################################################################################################################################################################
                                                                    violetbtn = Button(violetframe, text="NEXT",
                                                                                       bg='blue', command = fin)
                                                                    violetbtn.place(relx=0.35, rely=0.85,
                                                                                    relheight=0.09, relwidth=0.3)
                                                                else:
                                                                    put8 = Label(purpleframe, text='INCORRECT DATA')
                                                                    put8.pack()
                                                            else:
                                                                put7 = Label(purpleframe, text='INPUT A VALID DATA')
                                                                put7.pack()
                                                            pass


########################################################################################################################################################################################################

                                                        purplebtn = Button(purpleframe, text="NEXT", bg='blue',
                                                                           command=purple)
                                                        purplebtn.place(relx=0.35, rely=0.85, relheight=0.09,
                                                                        relwidth=0.3)
                                                    else:
                                                        put6 = Label(indigoframe, text='INCORRECT DATA')
                                                        put6.pack()
                                                else:
                                                    put5 = Label(indigoframe, text='INPUT A VALID DATA')
                                                    put5.pack()
                                                pass

#######################################################################################################################################################################################
                                            indigobtn = Button(indigoframe, text="NEXT", bg='blue', command=magenta)
                                            indigobtn.place(relx=0.35, rely=0.85, relheight=0.09, relwidth=0.3)
                                        else:
                                            put4 = Label(blueframe, text='INCORRECT DATA')
                                            put4.pack()
                                    else:
                                        put3 = Label(blueframe, text='INPUT A VALID DATA')
                                        put3.pack()
                                    pass


##################################################################################################################################################################################
                                bluebtn = Button(blueframe, text="NEXT", bg='blue', command=blue)
                                bluebtn.place(relx=0.35, rely=0.85, relheight=0.09, relwidth=0.3)
                            else:
                                put2 = Label(cyanframe, text='INCORRECT DATA')
                                put2.pack()
                        else:
                            put1 = Label(cyanframe, text='INPUT A VALID DATA')
                            put1.pack()

                    cyanbtn = Button(cyanframe, text="NEXT", bg='blue', command=cyan)
                    cyanbtn.place(relx=0.35, rely=0.85, relheight=0.09, relwidth=0.3)
                else:
                    put = Label(frame1, text='INCORRECT DATA')
                    put.pack()
            else:
                put = Label(frame1, text='INPUT A VALID DATA')
                put.pack()

        nexting = Button(frame1, text="NEXT", bg='blue', command=nexts)
        nexting.place(relx=0.35, rely=0.85, relheight=0.09, relwidth=0.3)

        window.destroy()
        nextPage.mainloop()
    else:
        warn = Label(text="Sorry You have to input your name")
        warn.pack()

def game1():
    global cyans1, blues1, indigos1, purples1, magentas1, violets1
    names = name_id.get()
    # new page loop
    # confirmation if the page is correct
    if names != "":
        nextPage = Tk()
        # nextPage.geometry('900x900')
        nextPage.title('Hello: ' + names)

        canvas1 = Canvas(nextPage, height=1000, width=1000)
        canvas1.pack()
        frame1 = Frame(nextPage, bg='white')
        frame1.place(relwidth=1, relheight=1)
        labels = Label(frame1, bg='white', text='Input letters Blue = b, Cyan = c, Indigo = i, Magenta = m, Purple = '
                                                'p, Violet = v')
        labels.place(relx=0.03, rely=0.1)

        colors_change = Label(frame1, bg='cyan', width=1, height=1)
        colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

        response = Entry(frame1)
        response.place(relx=0.47, rely=0.75, relheight=0.05, relwidth=0.05)
        cyans1 = time.time()

        def nexts():
            global cyans1, blues1
            names = response.get().lower()

            if names == 'c' or names == 'b' or names == 'i' or names == 'm' or names == 'p' or names == 'v':
                if names == 'c':
                    cyans1 =  time.time() - cyans1
                    frame1.destroy()
                    time.sleep(5)
                    cyanframe = Frame(nextPage)
                    cyanframe.place(relwidth=1, relheight=1)
                    cyanlabels = Label(cyanframe, bg='white',
                                       text='Input letters Blue = b, Cyan = c, Indigo = i, Magenta = m, Purple = '
                                            'p, Violet = v')
                    cyanlabels.place(relx=0.03, rely=0.1)
                    cyan_change = Label(cyanframe, bg='blue', width=1, height=1)
                    cyan_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)
                    cyanresponse = Entry(cyanframe)
                    cyanresponse.place(relx=0.47, rely=0.75, relheight=0.05, relwidth=0.05)
                    blues1 = time.time()
###############################################################################################################################################################################
################################################################################cyan function #############################################
                    def cyan():
                        global blues1,indigos1
                        bluenames = cyanresponse.get().lower()
                        if bluenames == 'c' or bluenames == 'b' or bluenames == 'i' or bluenames == 'm' or bluenames == 'p' or bluenames == 'v':
                            if bluenames == 'b':
                                blues1 = time.time() - blues1
                                cyanframe.destroy()
                                time.sleep(5)
                                blueframe = Frame(nextPage)
                                blueframe.place(relwidth=1, relheight=1)
                                bluelabels = Label(blueframe, bg='white',
                                                   text='Input letters Blue = b, Cyan = c, Indigo = i, Magenta = m, Purple = '
                                                        'p, Violet = v')
                                bluelabels.place(relx=0.03, rely=0.1)
                                blue_change = Label(blueframe, bg='indigo', width=1, height=1)
                                blue_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)
                                blueresponse = Entry(blueframe)
                                blueresponse.place(relx=0.47, rely=0.75, relheight=0.05, relwidth=0.05)
                                indigos1 = time.time()

################################################################################### add blue button command here ################################################################
                                def blue():
                                    global indigos1, magentas1
                                    indigonames = blueresponse.get().lower()
                                    if indigonames == 'c' or indigonames == 'b' or indigonames == 'i' or indigonames == 'm' or indigonames == 'p' or indigonames == 'v':
                                        if indigonames == 'i':
                                            indigos1 = time.time() - indigos1
                                            blueframe.destroy()
                                            time.sleep(5)
                                            indigoframe = Frame(nextPage)
                                            indigoframe.place(relwidth=1, relheight=1)
                                            indigolabels = Label(indigoframe, bg='white',
                                                                 text='Input letters Blue = b, Cyan = c, Indigo = i, Magenta = m, Purple = '
                                                                      'p, Violet = v')
                                            indigolabels.place(relx=0.03, rely=0.1)
                                            indigo_change = Label(indigoframe, bg='magenta', width=1, height=1)
                                            indigo_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)
                                            indigoresponse = Entry(indigoframe)
                                            indigoresponse.place(relx=0.47, rely=0.75, relheight=0.05, relwidth=0.05)
                                            magentas1 = time.time()
################################################################################################################################################################################
################################### add function for magenta######################################################
                                            def magenta():
                                                global magentas1, violets1
                                                purplenames = indigoresponse.get().lower()
                                                if purplenames == 'c' or purplenames == 'b' or purplenames == 'i' or purplenames == 'm' or purplenames == 'p' or purplenames == 'v':
                                                    if purplenames == 'm':
                                                        magentas1 = time.time() - magentas1
                                                        indigoframe.destroy()
                                                        time.sleep(5)
                                                        purpleframe = Frame(nextPage)
                                                        purpleframe.place(relwidth=1, relheight=1)
                                                        purplelabels = Label(purpleframe, bg='white',
                                                                             text='Input letters Blue = b, Cyan = c, Indigo = i, Magenta = m, Purple = '
                                                                                  'p, Violet = v')
                                                        purplelabels.place(relx=0.03, rely=0.1)
                                                        purple_change = Label(purpleframe, bg='violet', width=1,
                                                                              height=1)
                                                        purple_change.place(relx=0.25, rely=0.2, relwidth=0.5,
                                                                            relheight=0.5)
                                                        purpleresponse = Entry(purpleframe)
                                                        purpleresponse.place(relx=0.47, rely=0.75, relheight=0.05,
                                                                             relwidth=0.05)
                                                        violets1 = time.time()
################################################################################################################################################################################
################################################### put purple functions here###########################################################################################
                                                        def purple():
                                                            global violets1, purples1
                                                            violetnames = purpleresponse.get().lower()
                                                            if violetnames == 'c' or violetnames == 'b' or violetnames == 'i' or violetnames == 'm' or violetnames == 'p' or violetnames == 'v':
                                                                if violetnames == 'v':
                                                                    violets1 = time.time() - violets1
                                                                    purpleframe.destroy()
                                                                    time.sleep(5)
                                                                    violetframe = Frame(nextPage)
                                                                    violetframe.place(relwidth=1, relheight=1)
                                                                    violetlabels = Label(violetframe, bg='white',
                                                                                         text='Input letters Blue = b, Cyan = c, Indigo = i, Magenta = m, Purple = '
                                                                                              'p, Violet = v')
                                                                    violetlabels.place(relx=0.03, rely=0.1)
                                                                    violet_change = Label(violetframe, bg='purple',
                                                                                          width=1, height=1)
                                                                    violet_change.place(relx=0.25, rely=0.2,
                                                                                        relwidth=0.5, relheight=0.5)
                                                                    violetresponse = Entry(violetframe)
                                                                    violetresponse.place(relx=0.47, rely=0.75,
                                                                                         relheight=0.05, relwidth=0.05)
                                                                    purples1 = time.time()
#############################################################################################################################################################################################
###################################### add violet function ####################################################################################################################
                                                                    def fin():
                                                                        global cyans1, blues1, indigos1, magentas1, violets1, purples1
                                                                        purples1 = time.time() - purples1
                                                                        cyans1 = round(cyans1,4)
                                                                        blues1 = round(blues1,4)
                                                                        indigos1 = round(indigos1,4)
                                                                        magentas1 = round(magentas1,4)
                                                                        violets1 = round(violets1,4)
                                                                        purples1 = round(purples1,4)
                                                                        space = os.path.normpath(os.path.expanduser('~'))
                                                                        with open("%s/Desktop/%s2.txt" % (
                                                                        space, name_id.get()), 'w+') as done:
                                                                            done.write("\n" + '\n' + '\n' + '\n' + '\n')
                                                                            done.write(
                                                                                'Data for %s' % name_id.get() + '\n')
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
                                                                        time.sleep(2)
                                                                        violetframe.destroy()
                                                                        endingframe = Frame(nextPage)
                                                                        endingframe.place(relwidth=1, relheight=1)
                                                                        endinglabels = Label(endingframe, bg='white',
                                                                                             text='TEST COMPLETE FIND RESULT ON DESKTOP').pack()
#################################################################################################################################################################################
                                                                    violetbtn = Button(violetframe, text="NEXT",
                                                                                       bg='blue', command = fin)
                                                                    violetbtn.place(relx=0.35, rely=0.85,
                                                                                    relheight=0.09, relwidth=0.3)
                                                                else:
                                                                    put8 = Label(purpleframe, text='INCORRECT DATA')
                                                                    put8.pack()
                                                            else:
                                                                put7 = Label(purpleframe, text='INPUT A VALID DATA')
                                                                put7.pack()
                                                            pass


########################################################################################################################################################################################################

                                                        purplebtn = Button(purpleframe, text="NEXT", bg='blue',
                                                                           command=purple)
                                                        purplebtn.place(relx=0.35, rely=0.85, relheight=0.09,
                                                                        relwidth=0.3)
                                                    else:
                                                        put6 = Label(indigoframe, text='INCORRECT DATA')
                                                        put6.pack()
                                                else:
                                                    put5 = Label(indigoframe, text='INPUT A VALID DATA')
                                                    put5.pack()
                                                pass

#######################################################################################################################################################################################
                                            indigobtn = Button(indigoframe, text="NEXT", bg='blue', command=magenta)
                                            indigobtn.place(relx=0.35, rely=0.85, relheight=0.09, relwidth=0.3)
                                        else:
                                            put4 = Label(blueframe, text='INCORRECT DATA')
                                            put4.pack()
                                    else:
                                        put3 = Label(blueframe, text='INPUT A VALID DATA')
                                        put3.pack()
                                    pass


##################################################################################################################################################################################
                                bluebtn = Button(blueframe, text="NEXT", bg='blue', command=blue)
                                bluebtn.place(relx=0.35, rely=0.85, relheight=0.09, relwidth=0.3)
                            else:
                                put2 = Label(cyanframe, text='INCORRECT DATA')
                                put2.pack()
                        else:
                            put1 = Label(cyanframe, text='INPUT A VALID DATA')
                            put1.pack()

                    cyanbtn = Button(cyanframe, text="NEXT", bg='blue', command=cyan)
                    cyanbtn.place(relx=0.35, rely=0.85, relheight=0.09, relwidth=0.3)
                else:
                    put = Label(frame1, text='INCORRECT DATA')
                    put.pack()
            else:
                put = Label(frame1, text='INPUT A VALID DATA')
                put.pack()

        nexting = Button(frame1, text="NEXT", bg='blue', command=nexts)
        nexting.place(relx=0.35, rely=0.85, relheight=0.09, relwidth=0.3)

        window.destroy()
        nextPage.mainloop()
    else:
        warn = Label(text="Sorry You have to input your name")
        warn.pack()

def game2():
    global cyans2, blues2, indigos2, purples2, magentas2, violets2
    names = name_id.get()
    # new page loop
    # confirmation if the page is correct
    if names != "":
        nextPage = Tk()
        # nextPage.geometry('900x900')
        nextPage.title('Hello: ' + names)

        canvas1 = Canvas(nextPage, height=1000, width=1000)
        canvas1.pack()
        frame1 = Frame(nextPage, bg='white')
        frame1.place(relwidth=1, relheight=1)
        labels = Label(frame1, bg='white', text='Input letters Blue = b, Cyan = c, Indigo = i, Magenta = m, Purple = '
                                                'p, Violet = v')
        labels.place(relx=0.03, rely=0.1)

        colors_change = Label(frame1, bg='cyan', width=1, height=1)
        colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

        response = Entry(frame1)
        response.place(relx=0.47, rely=0.75, relheight=0.05, relwidth=0.05)
        cyans2 = time.time()

        def nexts():
            global cyans2, blues2
            names = response.get().lower()

            if names == 'c' or names == 'b' or names == 'i' or names == 'm' or names == 'p' or names == 'v':
                if names == 'c':
                    cyans2 =  time.time() - cyans2
                    frame1.destroy()
                    time.sleep(5)
                    cyanframe = Frame(nextPage)
                    cyanframe.place(relwidth=1, relheight=1)
                    cyanlabels = Label(cyanframe, bg='white',
                                       text='Input letters Blue = b, Cyan = c, Indigo = i, Magenta = m, Purple = '
                                            'p, Violet = v')
                    cyanlabels.place(relx=0.03, rely=0.1)
                    cyan_change = Label(cyanframe, bg='blue', width=1, height=1)
                    cyan_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)
                    cyanresponse = Entry(cyanframe)
                    cyanresponse.place(relx=0.47, rely=0.75, relheight=0.05, relwidth=0.05)
                    blues2 = time.time()
###############################################################################################################################################################################
################################################################################cyan function #############################################
                    def cyan():
                        global blues2,indigos2
                        bluenames = cyanresponse.get().lower()
                        if bluenames == 'c' or bluenames == 'b' or bluenames == 'i' or bluenames == 'm' or bluenames == 'p' or bluenames == 'v':
                            if bluenames == 'b':
                                blues2 = time.time() - blues2
                                cyanframe.destroy()
                                time.sleep(5)
                                blueframe = Frame(nextPage)
                                blueframe.place(relwidth=1, relheight=1)
                                bluelabels = Label(blueframe, bg='white',
                                                   text='Input letters Blue = b, Cyan = c, Indigo = i, Magenta = m, Purple = '
                                                        'p, Violet = v')
                                bluelabels.place(relx=0.03, rely=0.1)
                                blue_change = Label(blueframe, bg='indigo', width=1, height=1)
                                blue_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)
                                blueresponse = Entry(blueframe)
                                blueresponse.place(relx=0.47, rely=0.75, relheight=0.05, relwidth=0.05)
                                indigos2 = time.time()

################################################################################### add blue button command here ################################################################
                                def blue():
                                    global indigos2, magentas2
                                    indigonames = blueresponse.get().lower()
                                    if indigonames == 'c' or indigonames == 'b' or indigonames == 'i' or indigonames == 'm' or indigonames == 'p' or indigonames == 'v':
                                        if indigonames == 'i':
                                            indigos2 = time.time() - indigos2
                                            blueframe.destroy()
                                            time.sleep(5)
                                            indigoframe = Frame(nextPage)
                                            indigoframe.place(relwidth=1, relheight=1)
                                            indigolabels = Label(indigoframe, bg='white',
                                                                 text='Input letters Blue = b, Cyan = c, Indigo = i, Magenta = m, Purple = '
                                                                      'p, Violet = v')
                                            indigolabels.place(relx=0.03, rely=0.1)
                                            indigo_change = Label(indigoframe, bg='magenta', width=1, height=1)
                                            indigo_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)
                                            indigoresponse = Entry(indigoframe)
                                            indigoresponse.place(relx=0.47, rely=0.75, relheight=0.05, relwidth=0.05)
                                            magentas2 = time.time()
################################################################################################################################################################################
################################### add function for magenta######################################################
                                            def magenta():
                                                global magentas2, violets2
                                                purplenames = indigoresponse.get().lower()
                                                if purplenames == 'c' or purplenames == 'b' or purplenames == 'i' or purplenames == 'm' or purplenames == 'p' or purplenames == 'v':
                                                    if purplenames == 'm':
                                                        magentas2 = time.time() - magentas2
                                                        indigoframe.destroy()
                                                        time.sleep(5)
                                                        purpleframe = Frame(nextPage)
                                                        purpleframe.place(relwidth=1, relheight=1)
                                                        purplelabels = Label(purpleframe, bg='white',
                                                                             text='Input letters Blue = b, Cyan = c, Indigo = i, Magenta = m, Purple = '
                                                                                  'p, Violet = v')
                                                        purplelabels.place(relx=0.03, rely=0.1)
                                                        purple_change = Label(purpleframe, bg='violet', width=1,
                                                                              height=1)
                                                        purple_change.place(relx=0.25, rely=0.2, relwidth=0.5,
                                                                            relheight=0.5)
                                                        purpleresponse = Entry(purpleframe)
                                                        purpleresponse.place(relx=0.47, rely=0.75, relheight=0.05,
                                                                             relwidth=0.05)
                                                        violets2 = time.time()
################################################################################################################################################################################
################################################### put purple functions here###########################################################################################
                                                        def purple():
                                                            global violets2, purples2
                                                            violetnames = purpleresponse.get().lower()
                                                            if violetnames == 'c' or violetnames == 'b' or violetnames == 'i' or violetnames == 'm' or violetnames == 'p' or violetnames == 'v':
                                                                if violetnames == 'v':
                                                                    violets2 = time.time() - violets2
                                                                    purpleframe.destroy()
                                                                    time.sleep(5)
                                                                    violetframe = Frame(nextPage)
                                                                    violetframe.place(relwidth=1, relheight=1)
                                                                    violetlabels = Label(violetframe, bg='white',
                                                                                         text='Input letters Blue = b, Cyan = c, Indigo = i, Magenta = m, Purple = '
                                                                                              'p, Violet = v')
                                                                    violetlabels.place(relx=0.03, rely=0.1)
                                                                    violet_change = Label(violetframe, bg='purple',
                                                                                          width=1, height=1)
                                                                    violet_change.place(relx=0.25, rely=0.2,
                                                                                        relwidth=0.5, relheight=0.5)
                                                                    violetresponse = Entry(violetframe)
                                                                    violetresponse.place(relx=0.47, rely=0.75,
                                                                                         relheight=0.05, relwidth=0.05)
                                                                    purples2 = time.time()
#############################################################################################################################################################################################
###################################### add violet function ####################################################################################################################
                                                                    def fin():
                                                                        global cyans2, blues2, indigos2, magentas2, violets2, purples2
                                                                        purples2 = time.time() - purples2
                                                                        cyans2 = round(cyans2,4)
                                                                        blues2 = round(blues2,4)
                                                                        indigos2 = round(indigos2,4)
                                                                        magentas2 = round(magentas2,4)
                                                                        violets2 = round(violets2,4)
                                                                        purples2 = round(purples2,4)
                                                                        space = os.path.normpath(os.path.expanduser('~'))
                                                                        with open("%s/Desktop/%s3.txt"%(space,name_id.get()),'w+') as done:
                                                                            done.write("\n" + '\n' + '\n' + '\n' + '\n')
                                                                            done.write('Data for %s'%name_id.get()+'\n')
                                                                            done.write('cyan 3: %s'%str(cyans2)+'\n')
                                                                            done.write('blue 3: %s' % str(blues2) + '\n')
                                                                            done.write('indigo 3: %s' % str(indigos2) + '\n')
                                                                            done.write('magenta 3: %s' % str(magentas2) + '\n')
                                                                            done.write('violet 3: %s' % str(violets2) + '\n')
                                                                            done.write('purple 3: %s' % str(purples2) + '\n')
                                                                        time.sleep(2)
                                                                        violetframe.destroy()
                                                                        endingframe = Frame(nextPage)
                                                                        endingframe.place(relwidth=1, relheight=1)
                                                                        endinglabels = Label(endingframe, bg='white',
                                                                                             text='TEST COMPLETE FIND RESULT ON DESKTOP').pack()

 #################################################################################################################################################################################
                                                                    violetbtn = Button(violetframe, text="NEXT",
                                                                                       bg='blue', command = fin)
                                                                    violetbtn.place(relx=0.35, rely=0.85,
                                                                                    relheight=0.09, relwidth=0.3)
                                                                else:
                                                                    put8 = Label(purpleframe, text='INCORRECT DATA')
                                                                    put8.pack()
                                                            else:
                                                                put7 = Label(purpleframe, text='INPUT A VALID DATA')
                                                                put7.pack()
                                                            pass


########################################################################################################################################################################################################

                                                        purplebtn = Button(purpleframe, text="NEXT", bg='blue',
                                                                           command=purple)
                                                        purplebtn.place(relx=0.35, rely=0.85, relheight=0.09,
                                                                        relwidth=0.3)
                                                    else:
                                                        put6 = Label(indigoframe, text='INCORRECT DATA')
                                                        put6.pack()
                                                else:
                                                    put5 = Label(indigoframe, text='INPUT A VALID DATA')
                                                    put5.pack()
                                                pass

#######################################################################################################################################################################################
                                            indigobtn = Button(indigoframe, text="NEXT", bg='blue', command=magenta)
                                            indigobtn.place(relx=0.35, rely=0.85, relheight=0.09, relwidth=0.3)
                                        else:
                                            put4 = Label(blueframe, text='INCORRECT DATA')
                                            put4.pack()
                                    else:
                                        put3 = Label(blueframe, text='INPUT A VALID DATA')
                                        put3.pack()
                                    pass


##################################################################################################################################################################################
                                bluebtn = Button(blueframe, text="NEXT", bg='blue', command=blue)
                                bluebtn.place(relx=0.35, rely=0.85, relheight=0.09, relwidth=0.3)
                            else:
                                put2 = Label(cyanframe, text='INCORRECT DATA')
                                put2.pack()
                        else:
                            put1 = Label(cyanframe, text='INPUT A VALID DATA')
                            put1.pack()

                    cyanbtn = Button(cyanframe, text="NEXT", bg='blue', command=cyan)
                    cyanbtn.place(relx=0.35, rely=0.85, relheight=0.09, relwidth=0.3)
                else:
                    put = Label(frame1, text='INCORRECT DATA')
                    put.pack()
            else:
                put = Label(frame1, text='INPUT A VALID DATA')
                put.pack()

        nexting = Button(frame1, text="NEXT", bg='blue', command=nexts)
        nexting.place(relx=0.35, rely=0.85, relheight=0.09, relwidth=0.3)

        window.destroy()
        nextPage.mainloop()
    else:
        warn = Label(text="Sorry You have to input your name")
        warn.pack()

def game3():
    global cyans3, blues3, indigos3, purples3, magentas3, violets3
    names = name_id.get()
    # new page loop
    # confirmation if the page is correct
    if names != "":
        nextPage = Tk()
        # nextPage.geometry('900x900')
        nextPage.title('Hello: ' + names)

        canvas1 = Canvas(nextPage, height=1000, width=1000)
        canvas1.pack()
        frame1 = Frame(nextPage, bg='white')
        frame1.place(relwidth=1, relheight=1)
        labels = Label(frame1, bg='white', text='Input letters Blue = b, Cyan = c, Indigo = i, Magenta = m, Purple = '
                                                'p, Violet = v')
        labels.place(relx=0.03, rely=0.1)

        colors_change = Label(frame1, bg='cyan', width=1, height=1)
        colors_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)

        response = Entry(frame1)
        response.place(relx=0.47, rely=0.75, relheight=0.05, relwidth=0.05)
        cyans3 = time.time()

        def nexts():
            global cyans3, blues3
            names = response.get().lower()

            if names == 'c' or names == 'b' or names == 'i' or names == 'm' or names == 'p' or names == 'v':
                if names == 'c':
                    cyans3 =  time.time() - cyans3
                    frame1.destroy()
                    time.sleep(5)
                    cyanframe = Frame(nextPage)
                    cyanframe.place(relwidth=1, relheight=1)
                    cyanlabels = Label(cyanframe, bg='white',
                                       text='Input letters Blue = b, Cyan = c, Indigo = i, Magenta = m, Purple = '
                                            'p, Violet = v')
                    cyanlabels.place(relx=0.03, rely=0.1)
                    cyan_change = Label(cyanframe, bg='blue', width=1, height=1)
                    cyan_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)
                    cyanresponse = Entry(cyanframe)
                    cyanresponse.place(relx=0.47, rely=0.75, relheight=0.05, relwidth=0.05)
                    blues3 = time.time()
###############################################################################################################################################################################
################################################################################cyan function #############################################
                    def cyan():
                        global blues3,indigos3
                        bluenames = cyanresponse.get().lower()
                        if bluenames == 'c' or bluenames == 'b' or bluenames == 'i' or bluenames == 'm' or bluenames == 'p' or bluenames == 'v':
                            if bluenames == 'b':
                                blues3 = time.time() - blues3
                                cyanframe.destroy()
                                time.sleep(5)
                                blueframe = Frame(nextPage)
                                blueframe.place(relwidth=1, relheight=1)
                                bluelabels = Label(blueframe, bg='white',
                                                   text='Input letters Blue = b, Cyan = c, Indigo = i, Magenta = m, Purple = '
                                                        'p, Violet = v')
                                bluelabels.place(relx=0.03, rely=0.1)
                                blue_change = Label(blueframe, bg='indigo', width=1, height=1)
                                blue_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)
                                blueresponse = Entry(blueframe)
                                blueresponse.place(relx=0.47, rely=0.75, relheight=0.05, relwidth=0.05)
                                indigos3 = time.time()

################################################################################### add blue button command here ################################################################
                                def blue():
                                    global indigos3, magentas3
                                    indigonames = blueresponse.get().lower()
                                    if indigonames == 'c' or indigonames == 'b' or indigonames == 'i' or indigonames == 'm' or indigonames == 'p' or indigonames == 'v':
                                        if indigonames == 'i':
                                            indigos3 = time.time() - indigos3
                                            blueframe.destroy()
                                            time.sleep(5)
                                            indigoframe = Frame(nextPage)
                                            indigoframe.place(relwidth=1, relheight=1)
                                            indigolabels = Label(indigoframe, bg='white',
                                                                 text='Input letters Blue = b, Cyan = c, Indigo = i, Magenta = m, Purple = '
                                                                      'p, Violet = v')
                                            indigolabels.place(relx=0.03, rely=0.1)
                                            indigo_change = Label(indigoframe, bg='magenta', width=1, height=1)
                                            indigo_change.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)
                                            indigoresponse = Entry(indigoframe)
                                            indigoresponse.place(relx=0.47, rely=0.75, relheight=0.05, relwidth=0.05)
                                            magentas3 = time.time()
################################################################################################################################################################################
################################### add function for magenta######################################################
                                            def magenta():
                                                global magentas3, violets3
                                                purplenames = indigoresponse.get().lower()
                                                if purplenames == 'c' or purplenames == 'b' or purplenames == 'i' or purplenames == 'm' or purplenames == 'p' or purplenames == 'v':
                                                    if purplenames == 'm':
                                                        magentas3 = time.time() - magentas3
                                                        indigoframe.destroy()
                                                        time.sleep(5)
                                                        purpleframe = Frame(nextPage)
                                                        purpleframe.place(relwidth=1, relheight=1)
                                                        purplelabels = Label(purpleframe, bg='white',
                                                                             text='Input letters Blue = b, Cyan = c, Indigo = i, Magenta = m, Purple = '
                                                                                  'p, Violet = v')
                                                        purplelabels.place(relx=0.03, rely=0.1)
                                                        purple_change = Label(purpleframe, bg='violet', width=1,
                                                                              height=1)
                                                        purple_change.place(relx=0.25, rely=0.2, relwidth=0.5,
                                                                            relheight=0.5)
                                                        purpleresponse = Entry(purpleframe)
                                                        purpleresponse.place(relx=0.47, rely=0.75, relheight=0.05,
                                                                             relwidth=0.05)
                                                        violets3 = time.time()
################################################################################################################################################################################
################################################### put purple functions here###########################################################################################
                                                        def purple():
                                                            global violets3, purples3
                                                            violetnames = purpleresponse.get().lower()
                                                            if violetnames == 'c' or violetnames == 'b' or violetnames == 'i' or violetnames == 'm' or violetnames == 'p' or violetnames == 'v':
                                                                if violetnames == 'v':
                                                                    violets3 = time.time() - violets3
                                                                    purpleframe.destroy()
                                                                    time.sleep(5)
                                                                    violetframe = Frame(nextPage)
                                                                    violetframe.place(relwidth=1, relheight=1)
                                                                    violetlabels = Label(violetframe, bg='white',
                                                                                         text='Input letters Blue = b, Cyan = c, Indigo = i, Magenta = m, Purple = '
                                                                                              'p, Violet = v')
                                                                    violetlabels.place(relx=0.03, rely=0.1)
                                                                    violet_change = Label(violetframe, bg='purple',
                                                                                          width=1, height=1)
                                                                    violet_change.place(relx=0.25, rely=0.2,
                                                                                        relwidth=0.5, relheight=0.5)
                                                                    violetresponse = Entry(violetframe)
                                                                    violetresponse.place(relx=0.47, rely=0.75,
                                                                                         relheight=0.05, relwidth=0.05)
                                                                    purples3 = time.time()
#############################################################################################################################################################################################
###################################### add violet function ####################################################################################################################
                                                                    def fin():
                                                                        global cyans3, blues3, indigos3, magentas3, violets3, purples3
                                                                        purples3 = time.time() - purples3

                                                                        cyans3 = round(cyans3,4)
                                                                        blues3 = round(blues3,4)
                                                                        indigos3 = round(indigos3,4)
                                                                        magentas3 = round(magentas3,4)
                                                                        violets3 = round(violets3,4)
                                                                        purples3 = round(purples3,4)
                                                                        space = os.path.normpath(os.path.expanduser('~'))
                                                                        with open("%s/Desktop/%s4.txt"%(space,name_id.get()),'w+') as done:
                                                                            done.write("\n" + '\n' + '\n' + '\n' + '\n')
                                                                            done.write('Data for %s'%name_id.get()+'\n')
                                                                            done.write('cyan 4: %s'%str(cyans3)+'\n')
                                                                            done.write('blue 4: %s' % str(blues3) + '\n')
                                                                            done.write('indigo 4: %s' % str(indigos3) + '\n')
                                                                            done.write('magenta 4: %s' % str(magentas3) + '\n')
                                                                            done.write('violet 4: %s' % str(violets3) + '\n')
                                                                            done.write('purple 4: %s' % str(purples3) + '\n')
                                                                        time.sleep(2)
                                                                        violetframe.destroy()
                                                                        endingframe = Frame(nextPage)
                                                                        endingframe.place(relwidth=1, relheight=1)
                                                                        endinglabels = Label(endingframe, bg='white',
                                                                                             text='TEST COMPLETE FIND RESULT ON DESKTOP').pack()

 #################################################################################################################################################################################
                                                                    violetbtn = Button(violetframe, text="NEXT",
                                                                                       bg='blue', command = fin)
                                                                    violetbtn.place(relx=0.35, rely=0.85,
                                                                                    relheight=0.09, relwidth=0.3)
                                                                else:
                                                                    put8 = Label(purpleframe, text='INCORRECT DATA')
                                                                    put8.pack()
                                                            else:
                                                                put7 = Label(purpleframe, text='INPUT A VALID DATA')
                                                                put7.pack()
                                                            pass


########################################################################################################################################################################################################

                                                        purplebtn = Button(purpleframe, text="NEXT", bg='blue',
                                                                           command=purple)
                                                        purplebtn.place(relx=0.35, rely=0.85, relheight=0.09,
                                                                        relwidth=0.3)
                                                    else:
                                                        put6 = Label(indigoframe, text='INCORRECT DATA')
                                                        put6.pack()
                                                else:
                                                    put5 = Label(indigoframe, text='INPUT A VALID DATA')
                                                    put5.pack()
                                                pass

#######################################################################################################################################################################################
                                            indigobtn = Button(indigoframe, text="NEXT", bg='blue', command=magenta)
                                            indigobtn.place(relx=0.35, rely=0.85, relheight=0.09, relwidth=0.3)
                                        else:
                                            put4 = Label(blueframe, text='INCORRECT DATA')
                                            put4.pack()
                                    else:
                                        put3 = Label(blueframe, text='INPUT A VALID DATA')
                                        put3.pack()
                                    pass


##################################################################################################################################################################################
                                bluebtn = Button(blueframe, text="NEXT", bg='blue', command=blue)
                                bluebtn.place(relx=0.35, rely=0.85, relheight=0.09, relwidth=0.3)
                            else:
                                put2 = Label(cyanframe, text='INCORRECT DATA')
                                put2.pack()
                        else:
                            put1 = Label(cyanframe, text='INPUT A VALID DATA')
                            put1.pack()

                    cyanbtn = Button(cyanframe, text="NEXT", bg='blue', command=cyan)
                    cyanbtn.place(relx=0.35, rely=0.85, relheight=0.09, relwidth=0.3)
                else:
                    put = Label(frame1, text='INCORRECT DATA')
                    put.pack()
            else:
                put = Label(frame1, text='INPUT A VALID DATA')
                put.pack()

        nexting = Button(frame1, text="NEXT", bg='blue', command=nexts)
        nexting.place(relx=0.35, rely=0.85, relheight=0.09, relwidth=0.3)

        window.destroy()
        nextPage.mainloop()
    else:
        warn = Label(text="Sorry You have to input your name")
        warn.pack()


def buttons():
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

    button1 = Button(buttonframe, text='TEST 1', bg='blue', bd=0.01, command=game)

    button1.place(relx=0.1, rely=0.4, relheight=0.09, relwidth=0.3)
    button2 = Button(buttonframe, text='TEST 2', bg='blue', bd=0.01, command=game1)

    button2.place(relx=0.1, rely=0.6, relheight=0.09, relwidth=0.3)
    button3 = Button(buttonframe, text='TEST 3', bg='blue', bd=0.01, command=game2)

    button3.place(relx=0.6, rely=0.4, relheight=0.09, relwidth=0.3)
    button4 = Button(buttonframe, text='TEST 4', bg='blue', bd=0.01, command=game3)

    button4.place(relx=0.6, rely=0.6, relheight=0.09, relwidth=0.3)
    buttonpage.mainloop()


button = Button(frame, text='Start', bg='blue', bd=0.01, command=buttons)

button.place(relx=0.35, rely=0.7, relheight=0.09, relwidth=0.3)

window.mainloop()
