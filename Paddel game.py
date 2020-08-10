import turtle

wn = turtle.Screen()

wn.bgcolor("black")

wn.title("First Game")

wn.setup(width = 800, height = 600)

wn.tracer(0)


#score

score_a =0
score_b =0

#paddelA

paddel_a = turtle.Turtle()
paddel_a.speed(0)#speed of the animatiom

paddel_a.shape("square")
paddel_a.color("white")
paddel_a.shapesize(stretch_wid=5,stretch_len =1)
paddel_a.penup()
paddel_a.goto(-350,0)

#paddelb

paddel_b = turtle.Turtle()
paddel_b.speed(0)#speed of the animatiom

paddel_b.shape("square")
paddel_b.color("white")
paddel_b.shapesize(stretch_wid=5,stretch_len =1)
paddel_b.penup()
paddel_b.goto(350,0)


#ba
ball= turtle.Turtle()
ball.speed(0)#speed of the animatiom

ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_wid=1,stretch_len =1)
ball.penup()
ball.goto(0,0)

ball.dx = 0.5
ball.dy = -0.5


# pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Krishna : 0 Player B : 0 ",align = "Center", font = ("Courier",24,"normal"))





#function

def paddel_a_up():
    y = paddel_a.ycor()
    y += 20
    paddel_a.sety(y)



def paddel_a_down():
    y = paddel_a.ycor()
    y -= 20
    paddel_a.sety(y)

    

def paddel_b_up():
    y = paddel_b.ycor()
    y += 20
    paddel_b.sety(y)


def paddel_b_down():
    y = paddel_b.ycor()
    y -= 20
    paddel_b.sety(y)
    


#keyword binding

wn.listen()
wn.onkeypress(paddel_a_up,'w')
wn.onkeypress(paddel_a_down,'s')
wn.onkeypress(paddel_b_up,'Up')
wn.onkeypress(paddel_b_down,'Down')


while True:
    wn.update()

    # move the ball

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking

    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1



    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1


    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Krishna : {} Player B : {} ".format(score_a, score_b),align = "Center", font = ("Courier",24,"normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= - 1
        score_b += 1
        pen.clear()
        pen.write("Krishna : {} Player B : {} ".format(score_a, score_b),align = "Center", font = ("Courier",24,"normal"))


#paddel and ball collision

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddel_b.ycor() + 50 and ball.ycor() > paddel_b.ycor() -50):

        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddel_a.ycor() + 50 and ball.ycor() > paddel_a.ycor() -50):

        ball.setx(-340)
        ball.dx *= -1
    
        




