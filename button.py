def menu_screen():
    #you should be using a clock to limit the framerate
    FPS = 60
    clock = pygame.time.Clock()
    #no need to do this stuff every frame
    myFont = pygame.font.SysFont("", 80)
    myFont2 = pygame.font.SysFont("", 50)
    GameName = myFont.render("Educational Maze Game", 1, (GREEN))
    buttons = [Button("START GAME", myfont2, BLUE,
                              (215, 150, 400, 100), GREEN,
                              (50,200,160), game_setup)]
    
    while True:
        pos = pygame.mouse.get_pos()
        #update each button with the current mouse pos
        for button in self.buttons:
            button.update(pos)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            #pass event to each button    
            for button in buttons:
                button.get_event(event)
                            

        window.fill(BLUE)
        window.blit(GameName, (100,50))
        for button in buttons:
            button.draw(window)
        pygame.display.update()
        clock.tick(FPS)