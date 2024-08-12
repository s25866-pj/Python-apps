import tkinter

def getRectColor(rect_id):
    bColor = canvas.itemcget(rect_id, 'fill')
    
    if bColor == "white":
        return 0
    else:
        return 1

def getColorAtCoords(x, y,colorToChange):
    for rect_id in rectangles:
        coords = canvas.coords(rect_id)
        if coords[0] <= x <= coords[2] and coords[1] <= y <= coords[3]:
            color =getRectColor(rect_id)
            canvas.itemconfig(rect_id,fill=colorToChange,outline=colorToChange)
            return color            
    return None

def moveOval():
    dx, dy = 5, -5
    Bdx, Bdy = 5, -5
    color1,color2="black","white"
    while True:
        canvas.move(ball1, dx, dy)
        canvas.move(ball2,Bdx,Bdy)
        window.update()
        coords = canvas.coords(ball1)
        coordsb = canvas.coords(ball2)

        left_x, left_y = coords[0], (coords[1] + coords[3]) / 2
        right_x, right_y = coords[2], (coords[1] + coords[3]) / 2
        top_x, top_y = (coords[0] + coords[2]) / 2, coords[1]
        bottom_x, bottom_y = (coords[0] + coords[2]) / 2, coords[3]

        leftB_x, leftB_y = coordsb[0], (coordsb[1] + coordsb[3]) / 2
        rightB_x, rightB_y = coordsb[2], (coordsb[1] + coordsb[3]) / 2
        topB_x, topB_y = (coordsb[0] + coordsb[2]) / 2, coordsb[1]
        bottomB_x, bottomB_y = (coordsb[0] + coordsb[2]) / 2, coordsb[3]
        
        color_left = getColorAtCoords(left_x, left_y,color1)
        color_right = getColorAtCoords(right_x, right_y,color1)
        color_top = getColorAtCoords(top_x, top_y,color1)
        color_bottom = getColorAtCoords(bottom_x, bottom_y,color1)

        colorB_left = getColorAtCoords(leftB_x, leftB_y,color2)
        colorB_right = getColorAtCoords(rightB_x, rightB_y,color2)
        colorB_top = getColorAtCoords(topB_x, topB_y,color2)
        colorB_bottom = getColorAtCoords(bottomB_x, bottomB_y,color2)
        

        if coords[2] >= 600 or coords[0] <= 0 or color_left == 0 or color_right == 0:
            dx = -dx
        if coords[3] >= 600 or coords[1] <= 0 or color_top == 0 or color_bottom == 0:
            dy = -dy

        if coordsb[2] >= 600 or coordsb[0] <= 0 or colorB_left == 1 or colorB_right == 1:
            Bdx = -Bdx
        if coordsb[3] >= 600 or coordsb[1] <= 0 or colorB_top == 1 or colorB_bottom == 1:
            Bdy = -Bdy

        window.after(50)
window = tkinter.Tk()
window.title("Yin-Yang Ping-Pong")
canvas = tkinter.Canvas(window, width=600, height=600)
canvas.pack()

rectangles = []
for i in range(12):
    if i < 6:
        for j in range(12):
            rect_id = canvas.create_rectangle(i*50, j*50, (i*50)+50, (j*50)+50, fill="black", outline="black")
            rectangles.append(rect_id)
    else:
        for j in range(12):
            rect_id = canvas.create_rectangle(i*50, j*50, (i*50)+50, (j*50)+50, fill="white", outline="white")
            rectangles.append(rect_id)

ball1 = canvas.create_oval(10, 100, 40, 130, fill="white", outline="white")
ball2 = canvas.create_oval(405, 405, 435, 435, fill="black", outline="green")
moveOval()
window.mainloop()
