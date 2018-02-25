
def press(button):
    if button == "Cancel":
        app.stop()
    else:
        usr = app.getEntry("Username")
        pwd = app.getEntry("Password")
        print("These are your details: \nUsername:", usr, "Password:", pwd)
        app.stop()

from appJar import gui

app=gui("Login Window")
app.setBg("#4286f4")
app.setSticky("sw")
app.startLabelFrame("Login Details")

app.setSticky("ew")

app.addLabel("l1", "Username", 0, 0)
app.addEntry("Username", 0, 1)
app.addLabel("l2", "Password", 1, 0)
app.addSecretEntry("Password", 1, 1)
app.addButtons(["Submit", "Cancel"], press, 2, 0, 2)

app.stopLabelFrame()

app.go()
