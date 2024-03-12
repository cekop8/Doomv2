import tkinter as tk
import time, pyautogui, random

class Pet:
    def __init__(self):
        self.window = tk.Tk()
        self.moveleft = [tk.PhotoImage(file='walking2.gif', format='gif -index %i' % i).subsample(2, 2) for i in range(10)]
        self.moveright = [tk.PhotoImage(file='walking.gif', format='gif -index %i' % i).subsample(2, 2) for i in range(10)]
        self.frame_index = 0
        self.status = "idle"
        self.img = self.moveleft[self.frame_index]
        self.timestamp = time.time()
        self.window.config(background='black')
        self.window.wm_attributes('-transparentcolor', 'black')
        self.window.overrideredirect(True)
        self.window.attributes('-topmost', True)
        self.label = tk.Label(self.window, bd=0, bg='black', image=self.img)
        self.label.pack()
        self.window.bind("<B1-Motion>", self.on_drag)
        self.x = random.randint(1,1800)
        self.y = random.randint(0,949)
        self.goaly = random.randint(0,949)
        self.goalx = random.randint(1,1800)
        self.directionY = -1
        self.speed = 0.5
        print(self.goalx, self.x, self.y)
        self.dir = -1
        self.window.geometry('500x500+{}+{}'.format(str(self.x), str(self.y)))
        self.window.after(0, self.update)
        self.window.mainloop()

    def changetime(self, direction):
        if time.time() > self.timestamp + 0.05:
            self.timestamp = time.time()
            self.frame_index = (self.frame_index + 1) % 5
            self.img = direction[self.frame_index]

    def changedir(self):
        self.dir = -self.dir

    def on_drag(self,event):
        self.x = pyautogui.position().x - 100
        self.y = pyautogui.position().y -60
        print(self.x,self.y)
        #print(f"Mouse dragged to ({self.x}, {self.y})")

    def go(self):
        self.x = int(self.x + self.dir)
        if self.x < self.goalx :
            self.goalx = random.randint(1,1800)

        self.y = int(self.y+ self.directionY)
        if self.y < self.goaly :
            self.goaly = random.randint(0,400)

        if self.dir < 0:
            direction = self.moveleft
        else:
            direction = self.moveright
        self.changetime(direction)

    def update(self):
        self.go()
        if self.x == self.goalx or self.x == -self.goalx or self.x > 1800:
            self.goalx = random.randint(1,1800)
            print(self.goalx , self.x, self.y)
            self.changedir()
        if self.y == self.goaly or self.y == -self.goaly:
            self.goaly = random.randint(1,1800)
            self.directionY = - self.directionY
            print(self.goaly , self.x, self.y)
            self.changedir()

        if self.y > 949:
            self.directionY = - self.directionY
        if self.y < 0:
            self.directionY = - self.directionY

        self.window.geometry('200x200+{}+{}'.format(str(self.x), str(self.y)))
        self.label.configure(image=self.img)
        self.label.pack()
        self.window.after(30, self.update)
        self.window.lift()

a = Pet()
