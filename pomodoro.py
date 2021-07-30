from tkinter import *
import time
# import threading
# import multiprocessing

WIDTH = 600
HEIGHT = 400

root = Tk()
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(False,False)
root.title("Pomodoro")

label_work = Label(root, text = "Pomodoro Time" ,font = ("cascadia", 24)) 
label_work.place(x = 80 + 125, y = 50)

label_time_tracker = Label(root, text = "work/break (in minutes)" ,font = ("cascadia", 24)) 
label_time_tracker.place(x = 80 + 70, y = 100 )

label_seperator = Label(root, text = "/" ,font = ("cascadia", 28)) 
label_seperator.place(x = WIDTH//2-2, y = HEIGHT//2-55)

work_min_entry = Entry(root, width  = 2, bg  = "white", fg = "black" ,font = ("arial", 20), insertontime=0)
work_min_entry.place(x = WIDTH//2-50, y = HEIGHT//2-50)
work_min_entry.insert(-1,"50")

break_min_entry = Entry(root, width  = 2, bg  = "white", fg = "black" ,font = ("arial", 20), insertontime=0)
break_min_entry.place(x = WIDTH//2+30, y = HEIGHT//2-50)
break_min_entry.insert(-1, "10")

counting_down = True
def countdown():
    global counting_down
    label_time_tracker.place(x = 80 + 120, y = 100)
    work_t = int(work_min_entry.get())*60
    label_work.configure(text = "Work")
    label_work.place(x = WIDTH//2-30, y = 50)
    while counting_down:
        if work_t == 0:
            break
        mins, secs = divmod(work_t, 60)
        time = f"min: {mins} sec: {secs}"
        # time = f"{mins}:{secs}"
        label_time_tracker.config(text = time)
        root.update()
        root.after(1000)
        work_t -= 1
        
    break_t = int(break_min_entry.get())*60
    if counting_down:
        label_work.configure(text = "break")
    while counting_down:
        if break_t == 0:
            break
        mins, secs = divmod(break_t, 60)
        time = f"min: {mins} sec: {secs}"
        label_time_tracker.config(text = time)
        root.update()
        root.after(1000)
        break_t -= 1
    if counting_down: countdown()
    print("done")
    return True

# I COULDN´T DO IT WITH THREADING or MULTIPROCESSING IN ORDER TO MAKE COUNTDOWN COUNTINUE  WHILE DRAGING THE WINDOW
# th = threading.Thread(target=countdown)
# process = multiprocessing.Process(target=countdown)
def start():
    global counting_down
    try:
        int(work_min_entry.get())
        int(break_min_entry.get())
        counting_down = True
        countdown()
        # th.start()
        # process.start()
        return True

    except ValueError:
        label_time_tracker.configure(text = "Invalid input")
        return False

def stop():
    global counting_down
    counting_down = False
    label_work.configure(text = "Pomodoro Time")
    label_work.place(x = 80 + 125, y = 50)

    label_time_tracker.config(text = "work/break (in minutes)")
    label_time_tracker.place(x = 80 + 70, y = 100)
    # th.terminate()
    # process.terminate()

start_btn = Button(root, text = "start", bg  = "white", fg  = "black" ,command = start, padx = 5, pady = 2, font = ("cascadia", 13))
start_btn.place(x = WIDTH//2-20, y = HEIGHT//2)

cancel_btn = Button(root, text = "cancel", bg  = "white", fg  = "black" ,command = stop, padx = 5, pady = 2, font = ("cascadia", 13))
cancel_btn.place(x = WIDTH//2-28, y = HEIGHT//2+40)

root.mainloop()
