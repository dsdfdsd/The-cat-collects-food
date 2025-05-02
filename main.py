import pygame
import webbrowser


pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1920, 1080))


#Loading all the necessary items
bg = pygame.image.load("images/bg.png")
cat_right = [
    pygame.image.load("cat_right/cat_right1.png"),
    pygame.image.load("cat_right/cat_right2.png"),
    pygame.image.load("cat_right/cat_right3.png"),
    pygame.image.load("cat_right/cat_right4.png")
]

cat_left = [
    pygame.image.load("cat_left/cat_left1.png"),
    pygame.image.load("cat_left/cat_left2.png"),
    pygame.image.load("cat_left/cat_left3.png"),
    pygame.image.load("cat_left/cat_left4.png"),
]

cat_sleep = [
    pygame.image.load("cat_sleep_right/cat_sleep1.png"),
    pygame.image.load("cat_sleep_right/cat_sleep2.png"),
    pygame.image.load("cat_sleep_right/cat_sleep3.png"),
    pygame.image.load("cat_sleep_right/cat_sleep4.png"),
]

cat_sit = [
    pygame.image.load("cat_sit/cat_sit1.png"),
    pygame.image.load("cat_sit/cat_sit2.png"),
    pygame.image.load("cat_sit/cat_sit3.png"),
    pygame.image.load("cat_sit/cat_sit4.png"),
    pygame.image.load("cat_sit/cat_sit5.png"),
    pygame.image.load("cat_sit/cat_sit6.png"),
    pygame.image.load("cat_sit/cat_sit7.png"),
    pygame.image.load("cat_sit/cat_sit8.png"),
    pygame.image.load("cat_sit/cat_sit9.png"),
]
money = pygame.image.load("images/money.png")
foxs = [
    pygame.image.load("fox/fox1.png"),
    pygame.image.load("fox/fox2.png"),
    pygame.image.load("fox/fox3.png"),
]
losebg = pygame.image.load("images/losebg.jpg")

#Uploading fonts
label = pygame.font.Font("fonts/font.ttf", 60)
score_label = label.render("Score:", False, (0, 255, 255))
lose_label = label.render("You lose!", False, (216, 22, 22))
restart_label = label.render("Play?",False, (50, 212, 18))
restart_label_rect = restart_label.get_rect(topleft=(1000, 350))
gaid = label.render("Controls", False, (192, 192, 192))
gaid_rect = gaid.get_rect(topleft=(1500, 110))
check = label.render("Check you browser.", False, (192, 192, 192))
score = 0

#Everything for the player
player_x = 300
player_y = 740
is_jump = False
jump_count = 11
player_anim_sit = 0
player_anim_jump = 0
player_anim_sleep = 0
player_anim_count = 0
fox_anim = 0
controls_on = 0

#music
bg_sound =pygame.mixer.Sound('images/bgmusic.mp3')
jump_sound = pygame.mixer.Sound('images/jump.mp3')
moneyt = pygame.mixer.Sound('images/moneyt.mp3')
bg_sound.play(-1)

#money timer
money_timer = pygame.USEREVENT + 1
pygame.time.set_timer(money_timer, 5000)
money_list = []

#fox
fox_timer = pygame.USEREVENT + 1
pygame.time.set_timer(fox_timer, 7000)
fox_list = []

gameplay = True

running = True
while running:
    if gameplay:
        score_label2 = label.render(str(score), False, (240, 211, 19))
        player_rect = cat_left[0].get_rect(topleft=(player_x, player_y))

        screen.blit(bg, (0, 0))
        screen.blit(score_label, (100, 110))
        screen.blit(score_label2, (300, 115))
        screen.blit(gaid, gaid_rect)
        mouse = pygame.mouse.get_pos()
        if gaid_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            webbrowser.open("https://telegra.ph/Controls-05-02-7")


        if money_list:
            for (i,el) in enumerate(money_list):
                screen.blit(money, el)
                el.x -= 10

                if el.x < -10:
                    money_list.pop(i)
                if player_rect.colliderect(el):
                    score += 1
                    money_list.pop(i)
                    moneyt.play(0)

        if fox_list:
            for (i,el) in enumerate(fox_list):
                screen.blit(foxs[fox_anim // 5], el)
                el.x -= 10

                if el.x < -10:
                    fox_list.pop(i)
                if player_rect.colliderect(el):
                    bg_sound.stop()
                    lose = pygame.mixer.Sound("images/lose.mp3")
                    lose.play(0)
                    gameplay = False


        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            screen.blit(cat_right[player_anim_count], (player_x, player_y))
        elif keys[pygame.K_a]:
            screen.blit(cat_left[player_anim_count], (player_x, player_y))
        elif keys[pygame.K_s]:
            screen.blit(cat_sit[player_anim_sit // 5], (player_x, player_y))
        else:
            screen.blit(cat_sleep[player_anim_sleep // 5], (player_x, player_y))

        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True
                jump_sound.play(0)
        else:
            if jump_count >= -11:
                if jump_count > 0:
                    player_y -= (jump_count ** 2) / 2
                else:
                    player_y += (jump_count ** 2) / 2
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 11


        if keys[pygame.K_a] and player_x > 50:
            player_x -= 11
        if keys[pygame.K_d] and player_x < 1200:
            player_x += 11
        if player_anim_count == 3:
            player_anim_count = 0
        else:
            player_anim_count += 1

        if player_anim_sleep == 9:
            player_anim_sleep = 0
        else:
            player_anim_sleep += 1

        if player_anim_sit == 16:
            player_anim_sit = 0
        else:
            player_anim_sit += 1
        if fox_anim == 12:
            fox_anim = 0
        else:
            fox_anim += 1
        clock.tick(12)


        pygame.display.update()
    else:
        pygame.display.update()
        screen.blit(losebg, (0, 0))
        bg_sound.stop()
        screen.blit(lose_label, (700, 350))
        screen.blit(restart_label, restart_label_rect)
        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            bg_sound.play(-1)
            player_x = 300
            player_y = 740
            money_list.clear()
            fox_list.clear()
            score = 0
            gameplay = True



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            quit()
        if event.type == money_timer:
            money_list.append(money.get_rect(topleft=(2000, 790)))
        if event.type == fox_timer:
            fox_list.append(foxs[1].get_rect(topleft=(2300, 810)))