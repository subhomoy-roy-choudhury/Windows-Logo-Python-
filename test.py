import tkinter
import turtle
import tkinter.messagebox
from PIL import Image

window = tkinter.Tk()

canvas = tkinter.Canvas(master = window, width = 800, height = 800)
canvas.grid(padx=2, pady=2, row=0, column=0, rowspan=10, columnspan=10) # , sticky='nsew')
#draw = turtle.Turtle()
draw = turtle.RawTurtle(canvas)
entry1 = tkinter.Text(window) 
canvas.create_window(0, 500, window=entry1)
# entry2 = tkinter.Text(window) 
# canvas.create_window(200, 800, window=entry2)

result = tkinter.Text(master = window)
result.config(fg="black")
result.grid(padx=2, pady=2, row=0, column=11, sticky='nsew')

def Button_click ():
    tkinter.messagebox.showinfo("Game", "Tic Tac Toe")

def run():
    code = entry1.get("1.0",'end-1c')
    print(type(code))
    print(code)
    result.insert("1.0",code)
    if "fd" in code :
        code_num = int(code[3:])
        print(code_num)
        entry1.delete("1.0", "end-1c")
        draw.forward(code_num)
    elif "bk" in code :
        code_num = int(code[3:])
        print(code_num)
        entry1.delete("1.0", "end-1c")
        draw.backward(code_num)
    elif "rt" in code :
        code_num = int(code[3:])
        print(code_num)
        entry1.delete("1.0", "end-1c")
        draw.right(code_num)
    elif "lt" in code :
        code_num = int(code[3:])
        print(code_num)
        entry1.delete("1.0", "end-1c")
        draw.left(code_num)
    elif "cs" in code :
        entry1.delete("1.0", "end-1c")
        result.delete("1.0", "end-1c")
        draw.setx(0)
        draw.sety(0)
        draw.clear()
    elif "ht" in code :
        entry1.delete("1.0", "end-1c")
        draw.hideturtle()
    elif "dt" in code :
        entry1.delete("1.0", "end-1c")
        draw.showturtle()
    elif "pu" in code :
        entry1.delete("1.0", "end-1c")
        draw.penup()
    elif "pd" in code :
        entry1.delete("1.0", "end-1c")
        draw.pendown()
    elif "setpensize" in code :
        code_num = int(code[11:])
        print(code_num)
        entry1.delete("1.0", "end-1c")
        draw.pensize(code_num)

# def save_img():
#     fileName = "image"
#     draw .getscreen().getcanvas().postscript(file= fileName+'.eps')
#     img = Image.open(fileName + '.eps') 
#     # fig = img.convert('RGBA')
#     # image_png= 'logo-rgb.png'
#     # fig.save(image_png, lossless = True)
#     img.save(fileName + '.jpg', "JPEG")


menu_bar = tkinter.Menu(window)
run_bar = tkinter.Menu(menu_bar, tearoff=0)
save_bar = tkinter.Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run', command=run)
# run_bar.add_command(label='Save', command=save_img)
menu_bar.add_cascade(label='Run', menu=run_bar)
window.config(menu=menu_bar)

window.bind('<Return>',lambda event:run())
window.mainloop()