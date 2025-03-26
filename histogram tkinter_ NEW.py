from tkinter import *

class HistrogramApp:
    def __init__(self):
        self.root=Tk()
        self.canvas = my_canvas
        

    def setup_window(self):
        
         root.title("Traffic data on Histogram")
        root.iconbitmap("C:/Users/hp/Downloads/traffic data/statistic_9684905.ico")
        root.geometry("700x600")
        my_canvas= Canvas(root, width=650, height=400, bg= "#F4F8D3")
        my_canvas.grid(row = 5, column = 1,padx =20, pady = 20)
        
    def draw_histogram(self):
        
        my_label = Label(root, text = " **Histogram of Vechicle Frequency per Hour(15/06/2024)**")
        my_label.config(font = ("Helvetica", 12, "bold"),anchor= W)
        my_label.grid(row = 4, column =1, pady=10,)

        #create line
        #my_canvas.create_line(x1, y1,x2,y2, fill="color")
        my_canvas.create_line(0,350,620,350, fill="black")
        my_canvas.create_line(10,20,10,350, fill="black")
        my_canvas.create_text( 300, 380 , text = "00:00 to 24:00 Hours", fill="black")

        #create text ( x= numbers hours)

        my_canvas.create_text( 25, 360 , text = "00", fill="black")
        my_canvas.create_text( 50, 360 , text = "01", fill="black")
        my_canvas.create_text( 75, 360 , text = "02", fill="black")
        my_canvas.create_text( 100, 360 , text = "03", fill="black")
        my_canvas.create_text( 125, 360 , text = "04", fill="black")
        my_canvas.create_text( 150, 360 , text = "05", fill="black")
        my_canvas.create_text( 175, 360 , text = "06", fill="black")
        my_canvas.create_text( 200, 360 , text = "07", fill="black")
        my_canvas.create_text( 225, 360 , text = "08", fill="black")
        my_canvas.create_text( 250, 360 , text = "09", fill="black")
        my_canvas.create_text( 275, 360 , text = "10", fill="black")
        my_canvas.create_text( 300, 360 , text = "11", fill="black")
        my_canvas.create_text( 325, 360 , text = "12", fill="black")
        my_canvas.create_text( 350, 360 , text = "13", fill="black")
        my_canvas.create_text( 375, 360 , text = "14", fill="black")
        my_canvas.create_text( 400, 360 , text = "15", fill="black")
        my_canvas.create_text( 425, 360 , text = "16", fill="black")
        my_canvas.create_text( 450, 360 , text = "17", fill="black")
        my_canvas.create_text( 475, 360 , text = "18", fill="black")
        my_canvas.create_text( 500, 360 , text = "19", fill="black")
        my_canvas.create_text( 525, 360 , text = "20", fill="black")
        my_canvas.create_text( 550, 360 , text = "21", fill="black")
        my_canvas.create_text( 575, 360 , text = "22", fill="black")
        my_canvas.create_text( 600, 360 , text = "23", fill="black")


        #my_canvas.create_rectangle(x1,y1,x2,y2, fil="color")
        
        my_canvas.create_rectangle(15,350,35,150, fill="red")
        my_canvas.create_rectangle(40,350,60,150, fill="red")
        my_canvas.create_rectangle(65,350,85,150, fill="red")
        my_canvas.create_rectangle(90,350,110,150, fill="red")
        my_canvas.create_rectangle(115,350,135,150, fill="red")

        my_canvas.create_rectangle(140,350,160,150, fill="red")
        my_canvas.create_rectangle(165,350,185,150, fill="red")
        my_canvas.create_rectangle(190,350,210,150, fill="red")
        my_canvas.create_rectangle(215,350,235,150, fill="red")
        my_canvas.create_rectangle(240,350,260,150, fill="red")

        my_canvas.create_rectangle(265,350,285,150, fill="red")
        my_canvas.create_rectangle(290,350,310,150, fill="red")
        my_canvas.create_rectangle(315,350,335,150, fill="red")
        my_canvas.create_rectangle(340,350,360,150, fill="red")
        my_canvas.create_rectangle(365,350,385,150, fill="red")

        my_canvas.create_rectangle(390,350,410,150, fill="red")
        my_canvas.create_rectangle(415,350,435,150, fill="red")
        my_canvas.create_rectangle(440,350,460,150, fill="red")
        my_canvas.create_rectangle(465,350,485,150, fill="red")
        my_canvas.create_rectangle(490,350,510,150, fill="red")

        my_canvas.create_rectangle(515,350,535,150, fill="red")
        my_canvas.create_rectangle(540,350,560,150, fill="red")
        my_canvas.create_rectangle(565,350,585,150, fill="red")
        my_canvas.create_rectangle(590,350,610,150, fill="red")

    def add_legend(self):
        my_canvas.create_rectangle(50,50,100,10, fill="red")
        my_canvas.create_text( 200, 30 , text = "Elm Avenue/Rabbit Road ", fill="black", font=('Helvetica 10 bold'))

    def run(self):
        self.setup_window()
        self.draw_histogram()
        self.add_legend()
        root.mainloop()

self.run()
