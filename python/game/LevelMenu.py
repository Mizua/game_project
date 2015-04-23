import pygame
import constants
import routines
from Menu import Menu

class LevelMenu(Menu):

    def create_structure(self):
        Menu.create_structure(self)
        screen = self.dest_surface
        txt1 = routines.draw_text("Choose your level", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2 + 20, 50, "data/coders_crux/coders_crux.ttf", constants.WHITE)
        screen.blit(txt1[0], txt1[1])
        pygame.display.update()


    def run(self,joystick):
        menu_flag = True
        level_nbr = 0
        while menu_flag:
            for event in pygame.event.get():

                #Joystick stuff
                if event.type == pygame.JOYHATMOTION:
                    hat = joystick.get_hat(0)
                    if (0, 1) == hat:
                        self.draw(-1)
                    if (0, -1) == hat:
                        self.draw(1)
                    pygame.display.update()
                if event.type == pygame.JOYBUTTONDOWN:
                    if joystick.get_button(1) == 1:
                        if self.get_position() == 0:
                            level_nbr = 0
                        if self.get_position() == 1:
                            level_nbr = 1
                        if self.get_position() == 2:
                            level_nbr = 2

                        constants.GAME_STATUS = "level"
                        return level_nbr


                #Keyboard stuff
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.draw(-1)
                    if event.key == pygame.K_DOWN:
                        self.draw(1)
                    if event.key == pygame.K_RETURN:
                        if self.get_position() == 0:
                            level_nbr = 0
                        if self.get_position() == 1:
                            level_nbr = 1
                        if self.get_position() == 2:
                            level_nbr = 2

                        constants.GAME_STATUS = "level"
                        return level_nbr

                    if event.key == pygame.K_ESCAPE:
                        menu_flag = False
                        main_loop = False
                    pygame.display.update()
                elif event.type == pygame.QUIT:
                    constants.GAME_STATUS="exit"
                    menu_flag = False
            pygame.time.wait(8)