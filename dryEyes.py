import os, time, schedule, random
from win10toast import ToastNotifier

toaster = ToastNotifier()

tasks = [
    "Do 10 Pushups",
    "Take a walk",
    "Play A Chess Game",
    "Read 10 pages From A Book",
    "Respond to an email",
    "Make a call",
    "Feed the pets"
]

def notification():
    toaster.show_toast(
        "Next Task",
        random.choice(tasks),
        duration = 20,
        icon_path = "icons/todo.ico", 
        threaded = True,
    )

def sleeping():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

schedule.every(50).minutes.do(notification)
schedule.every(55).minutes.do(sleeping)

while True:
    schedule.run_pending()
