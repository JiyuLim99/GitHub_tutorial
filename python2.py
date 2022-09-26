import turtle as t

t.bgcolor("steelblue")

t.penup()
t.pencolor("mediumpurple")
t.fillcolor("mediumpurple")
t.goto(100,-500)
t.begin_fill()
t.pendown()
t.circle(500)
t.end_fill()

t.penup()
t.pencolor("orchid")
t.fillcolor("orchid")
t.goto(65,-390)
t.begin_fill()
t.pendown()
t.circle(400)
t.end_fill()

t.penup()
t.pencolor("lightcoral")
t.fillcolor("lightcoral")
t.goto(75,-400)
t.begin_fill()
t.pendown()
t.circle(350)
t.end_fill()


t.penup()
t.pencolor("orange")
t.fillcolor("orange")
t.goto(75,-370)
t.begin_fill()
t.pendown()
t.circle(300)
t.end_fill()

t.penup()
t.pencolor("gold")
t.fillcolor("gold")
t.goto(75,-170)
t.begin_fill()
t.pendown()
t.circle(170)
t.end_fill()

t.penup()
t.pencolor("olivedrab")
t.fillcolor("olivedrab")
t.goto(-500,-1100)
t.begin_fill()
t.pendown()
for i in range(4):
    t.forward(1000)
    t.left(90)
t.end_fill()

t.penup()
t.pencolor("gold")
t.fillcolor("gold")
t.goto(75,-170)
t.begin_fill()
t.pendown()
for i in range(3):
    t.forward(70)
    t.left(120) 
t.end_fill()



t.done()