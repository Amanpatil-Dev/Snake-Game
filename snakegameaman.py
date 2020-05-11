import pygame
import random
import os

# to play backgroung music
pygame.mixer.init()



# To ensure that we imported everything from python

x = pygame.init()



#colours
white =(255,255,255)

red = (255,0,0)

black= (0,0,0)

#display
screen_width = 1200
screen_height = 600
#backgroung image
bgimg = pygame.image.load("hhh.jpg")
bgimg = pygame.transform.scale(bgimg,(screen_width,screen_height))

#backgroung image for welcome screen
bgimg1 = pygame.image.load("kkk.jpg")
bgimg1 = pygame.transform.scale(bgimg1,(screen_width,screen_height))



# To  display how to make gamewindows(for some seconds)
gamewindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.update()

# TO give title to the window screen
pygame.display.set_caption("SNAKE GAME")


clock = pygame.time.Clock()
font = pygame.font.SysFont(None,55)

#check if high score file is creadted or not if not create it
if (not os.path.exists("highscore.txt")):
    with open("highscore.txt", "w") as f:
        f.write("0")

with open("highscore.txt","r")as f:
    highscore = f.read()

def text_screen(text, color, x,y):
    screen_text = font.render(text, True,color)
    gamewindow.blit(screen_text,[x,y])

def plot_snake(gamewindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gamewindow,color,[x,y,snake_size,snake_size])




# CREATING A GAME LOOP AND HANDLEING THE EVENT LIKE PRESSING KEY AND MOVING MOUSE(WINDOW CAN STOP HERE BECAUSE WE HAVE
# INITALIZE A LOOP THAT SAYS:- JAB TAK GAME OVER NA HO TAB TAK LOOP CHALNE DOO

def welcome():  #welcome window function
    exit_game = False
    while not exit_game:
        gamewindow.fill(white)
        gamewindow.blit(bgimg1, (0, 0))

        text_screen("Welcome to snakes !  ",black,260,250 )
        text_screen("Press space to play!", black,300,280)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('back.mp3.mp3')
                    pygame.mixer.music.play()


                    gameloop()
        pygame.display.update()
        clock.tick(30)





def gameloop():
    # GAME SPECIFIC  VARIABLE
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snake_size = 30

    if (not os.path.exists("highscore.txt")):
        with open("highscore.txt", "w") as f:
            f.write("0")

    with open("highscore.txt", "r") as f:
        highscore = f.read()


    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    fps = 30
    score = 0
    init_velocity = 5
    snk_list = []
    snk_length = 1

    #check if high score exist



    while not exit_game:
        if game_over:
            with open("highscore.txt", "w")as f:
                f.write(str(highscore))
                #highscore = f.read()

            gamewindow.fill(white)
            gamewindow.blit(bgimg1, (0, 0))# background image when the game is over



            text_screen("Game Over! Press Return To Continue",red, 100, 200)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game == True

                if event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_RETURN:
                       welcome()
        else:


            for event in pygame.event.get():
                if event.type == pygame.QUIT:    # to quit the game
                    exit_game == True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:   # to move the snake on x axis
                        velocity_x = 10
                        velocity_y = 0
                        #snake_x = snake_x + 20


                    elif event.key == pygame.K_LEFT:
                        velocity_x = -10
                        velocity_y = 0
                        #snake_x = snake_x - 20

                    elif event.key == pygame.K_UP:
                        velocity_y = -10
                        velocity_x = 0
                        #snake_y = snake_y - 20

                    elif event.key == pygame.K_DOWN:
                        velocity_y = 10
                        velocity_x = 0
                        #snake_y = snake_y + 20

                    elif event.key == pygame.K_q:# cheat code
                        score+=50

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y



            # sCore
            if abs(snake_x - food_x)<6 and abs(snake_y - food_y )<6:
                score +=10
                #after eating food it will randomly put food in anywhere in the screed width
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length +=5
                print(highscore)
                if score>int(highscore):
                    highscore = score



                # update with white colour
            gamewindow.fill(white)#playing window
            gamewindow.blit(bgimg,(0,0))

            text_screen("score" + str(score) + "  highscore:  "+str (highscore), red, 5, 5)
            pygame.draw.rect(gamewindow,red,[food_x,food_y,snake_size,snake_size])

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length :
                del snk_list[0]

            if head in snk_list[: -1]:# game over
                game_over = True
                pygame.mixer.music.load('gameover.mp3.wav')
                pygame.mixer.music.play()



            if snake_x<0 or snake_y> screen_width or snake_y<0 or snake_y>screen_height: #game over
                game_over = True
                print ("game over")
                pygame.mixer.music.load('gameover.mp3.wav')
                pygame.mixer.music.play()

            plot_snake(gamewindow,black,snk_list,snake_size)
        #snake
        #pygame.draw.rect(gamewindow,black,(snake_x,snake_y,snake_size,snake_size))
        #food
        #pygame.draw.rect(gamewindow, red, (food_x, food_y, snake_size, snake_size))
        pygame.display.update()
        clock.tick(fps)



    pygame.QUIT()
    quit()
welcome()
