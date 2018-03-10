def press(btn):
    if btn == "Cancel":
        app.stop()
    else:
        firstN = app.getEntry("FirstName")
        foreN = app.getEntry("Forename")
        DOB = app.getEntry("DateOfBirth")
        #        day   = app.geyEntry("Day")
        #        month = app.geyEntry("Month")
        #        year   = app.geyEntry("Year")
        Email = app.getEntry("Email")
        print("These are your details: \nFirstName:", firstN, "\nForename:", foreN, "\nDateOfBirth:", DOB,
              "\nForename:", Email, )
        app.clearEntry("FirstName")
        app.clearEntry("Forename")
        app.clearEntry("DateOfBirth")
        app.clearEntry("Forename")
        app.clearEntry("Email")


from appJar import gui

app = gui("Window")
app.setBg("#42f1f4")
app.setSticky("nw")
app.startLabelFrame("What are your details?")

app.setSticky("ew")

app.addLabel("l1", "FirstName", 0, 0)
app.addEntry("FirstName", 0, 1)
app.setSticky("w")

app.addLabel("l2", "Forename", 1, 0)
app.addEntry("Forename", 1, 1)
app.setSticky("w")

app.addLabel("l3", "DateOfBirth", 2, 0)
app.addEntry("DateOfBirth", 2, 1)
app.setSticky("w")

app.addLabel("l4", "Email", 3, 0)
app.addEntry("Email", 3, 1)
app.setSticky("w")

app.addButtons(["Submit", "Cancel"], press, 4, 0, 4)

app.stopLabelFrame()

app.go()
