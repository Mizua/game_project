from Level import Level
from platforms.Platform import Platform
from platforms.MovingPlatform import MovingPlatform
from platforms.BoostPlatform import BoostPlatform
from PNJ.Blob import Blob

# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -1800

        # Array with width, height, x, and y of platform
        level = [[210, 70, 500, 500],
                 [210, 70, 800, 400],
                 [210, 70, 1000, 500],
                 [210, 70, 1120, 280],
                 [70, 70, 500, 550],
                 [70, 70, 100, 550],
                 [70, 70, 800, 550]
                 ]

        # Array with x, y, direction, speed of pnj
        enemies = [[500, 500, 1, 2],
                   [510, 540, 1, 2],
                   [540, 580, -1, 4]
                  ]
        for pnj in enemies:
            enemy = Blob(pnj[2],pnj[3])
            enemy.rect.x = pnj[0]
            enemy.rect.y = pnj[1]
            enemy.player=self.player
            enemy.level=self
            self.pnj_list.add(enemy)

        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        # Add an horizontal moving platform
        block = MovingPlatform(70, 40)
        block.rect.x = 1350
        block.rect.y = 380
        block.boundary_left = 1350
        block.boundary_right = 1500
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a vertical moving plateform
        block = MovingPlatform(100,20)
        block.rect.x = 1600
        block.rect.y = 300
        block.boundary_top = 300
        block.boundary_bottom = 500
        block.change_y = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a custom booster platform
        block = BoostPlatform(70, 40)
        block.rect.x = 1500
        block.rect.y = 500
        block.boost = 0.5
        block.direction = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
