import math

# ---------------------------- CONSTANTS ------------------------------- #
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
   window.after_cancel(timer)
   global reps
   reps=0
   my_label = Label(text="     Timer     ", font=("TIMES NEW ROMAN", 28, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
   my_label.grid(column=1, row=0)
   my_label = Label(text="✔✔✔", fg=YELLOW, bg=YELLOW, highlightthickness=0)
   my_label.grid(column=1, row=3)
   canvas.itemconfig(timer_text, text="00:00")
   canvas.grid(column=1, row=1)

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
   global reps
   work_sec = int(WORK_MIN*60)
   short_break_sec = int(SHORT_BREAK_MIN*60)
   long_break_sec = int(LONG_BREAK_MIN*60)
   if reps%2 == 0 and reps<7:
      my_label = Label(text="Work", font=("TIMES NEW ROMAN", 28, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
      my_label.grid(column=1, row=0)
      count_down(work_sec)

   if reps%2 == 1 and reps<6:
      my_label = Label(text="Break", font=("TIMES NEW ROMAN", 28, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
      my_label.grid(column=1, row=0)
      if reps==1 :
         my_label = Label(text="✔", bg=YELLOW, highlightthickness=0)
      elif reps==3:
         my_label = Label(text="✔✔", bg=YELLOW, highlightthickness=0)
      else:
         my_label = Label(text="✔✔✔", bg=YELLOW, highlightthickness=0)
      my_label.grid(column=1, row=3)
      count_down(short_break_sec)

   if reps==7:
     my_label = Label(text="Long Break", font=("TIMES NEW ROMAN", 28, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
     my_label.grid(column=1, row=0)
     count_down(long_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
   count_min = math.floor(count/60)
   count_sec = count % 60
   if count_sec < 10:
      count_sec = "0" + str(count_sec)
   canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

   if count>0:
      global timer
      timer = window.after(1000, count_down, count-1)
   else:
      global reps
      reps += 1
      if reps<8:
         start_timer()
# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady =40, bg=YELLOW)

my_label = Label(text="")
my_label.grid(column=0,row=0)

my_label = Label(text="Timer", font=("TIMES NEW ROMAN", 28, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
my_label.grid(column=1,row=0)

button = Button(text="Start", font=("TIMES NEW ROMAN", 12, "bold"), command=start_timer)
button.grid(column=0,row=2)

canvas = Canvas(width = 200, height = 224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,112, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row = 1)

button = Button(text="Reset", font=("TIMES NEW ROMAN", 12, "bold"), command=reset_timer)
button.grid(column=2,row=2)

window.mainloop()