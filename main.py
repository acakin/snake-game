import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
s = Snake()
f = Food()
sb = Scoreboard()

screen.onkey(s.up, "Up")
screen.onkey(s.down, "Down")
screen.onkey(s.left, "Left")
screen.onkey(s.right, "Right")
screen.listen()



def game():

    game_is_on = True
    sb.score = 0
    sb.update_sb()
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        s.move()
        if s.head.distance(f) < 15:
            f.refresh()
            s.grow()
            sb.increase_score()

        if s.head.xcor() > 290 or s.head.xcor() < -290 or s.head.ycor() > 290 or s.head.ycor() < -290:
            sb.update()
            sb.update_sb()
            sb.game_over()
            s.reset_s()
            game_is_on = False


        for _ in range(1, len(s.s_body) - 1):
            if s.head.distance(s.s_body[_]) < 10:
                sb.update()
                sb.update_sb()
                sb.game_over()
                s.reset_s()
                game_is_on = False


game()


screen.onkeypress(game, 'space')

screen.listen()




screen.exitonclick()
