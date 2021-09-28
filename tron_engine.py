from tron_bike import TronBike
import pygame


BLACK  = (0, 0, 0)
RED    = (255, 0, 0)
BLUE   = (10, 200, 255)
WHITE  = (255, 255, 255)
ORANGE = (255, 165, 0)
SLATE  = (112, 128, 144)
FPS    = (40)

FRAME_SIZE    = (800, 512)
YBUFFER       = (32)
XBUFFER       = (50)
BORDER_WIDTH  = (4)
TRAIL_WIDTH   = (2)
PLAYER1_START = (150, 300)
PLAYER2_START = (650, 300)
PLAYER1_DIREC = (1)
PLAYER2_DIREC = (3)
MAX_SCORE     = (10)


class TronEngine:


    def __init__(self):
        self.gameClock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(FRAME_SIZE)

        self.backgroundImage = pygame.image.load("Images/background.png")
        self.backgroundImage = pygame.transform.scale(self.backgroundImage, (700, 448))

        player1Image = "Images/blue_bike.png"
        player2Image = "Images/red_bike.png"
        self.player1 = TronBike(player1Image, PLAYER1_START, PLAYER1_DIREC)
        self.player2 = TronBike(player2Image, PLAYER2_START, PLAYER2_DIREC)

        self.player1Score = 0
        self.player2Score = 0

        self.allSprites = pygame.sprite.Group()
        self.allSprites.add(self.player1)
        self.allSprites.add(self.player2)

        self.player1Keys = [pygame.K_d,     pygame.K_s,    pygame.K_a,    pygame.K_w]
        self.player2Keys = [pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT, pygame.K_UP]

        self.initScoreBoard()
        self.getBorder()
        self.runGame()



    def initScoreBoard(self):
        pygame.font.init()
        self.font = pygame.font.SysFont("Trebuc.ttf", 24)


    def updateScoreBoard(self):
        player1Score = self.font.render(str(self.player1Score), True, BLUE)
        self.screen.blit(player1Score, (FRAME_SIZE[0]/2 - 15, 10))

        player2Score = self.font.render(str(self.player2Score), True, RED)
        self.screen.blit(player2Score, (FRAME_SIZE[0]/2 + 15, 10))


    def updateBoard(self):
        keys = pygame.key.get_pressed()
        self.updateBikes(keys)
        self.checkCollision()

        self.screen.fill(BLACK)
        self.screen.blit(self.backgroundImage, (50, 32))
        self.updateScoreBoard()

        pygame.draw.lines(self.screen, BLUE,   False, self.player1.trail, TRAIL_WIDTH)
        pygame.draw.lines(self.screen, ORANGE, False, self.player2.trail, TRAIL_WIDTH)

        pygame.draw.lines(self.screen, WHITE, False, self.leftBorder,  BORDER_WIDTH)
        pygame.draw.lines(self.screen, WHITE, False, self.rightBorder, BORDER_WIDTH)
        pygame.draw.lines(self.screen, WHITE, False, self.topBorder,   BORDER_WIDTH)
        pygame.draw.lines(self.screen, WHITE, False, self.botBorder,   BORDER_WIDTH)

        self.allSprites.update()
        self.allSprites.draw(self.screen)
        pygame.display.flip()



    def runGame(self):
        running = True
        while running:
            self.gameClock.tick(FPS)
            for event in pygame.event.get():
                running = False if event.type == pygame.QUIT else True

            if self.player1Score == MAX_SCORE or self.player2Score == MAX_SCORE:
                running = False

            self.updateBoard()

        pygame.quit()



    def updateBikes(self, keys):
        p1ActiveKeys = [keys[p1Key] for p1Key in self.player1Keys]
        p2ActiveKeys = [keys[p2Key] for p2Key in self.player2Keys]
        p1Directions = [p1ActiveKeys.index(activeKey) for activeKey in p1ActiveKeys if activeKey]
        p2Directions = [p2ActiveKeys.index(activeKey) for activeKey in p2ActiveKeys if activeKey]

        if len(p1Directions) != 0: self.player1.updateDirection(p1Directions[-1] + 1)
        if len(p2Directions) != 0: self.player2.updateDirection(p2Directions[-1] + 1)
        self.player1.move()
        self.player2.move()



    def checkCollision(self):
        player1Trail = self.player1.trail[1:-1]
        player2Trail = self.player2.trail[1:-1]
        player1Position = self.player1.trail[-1]
        player2Position = self.player2.trail[-1]

        if player1Position in self.player2.trail or player1Position in player1Trail : self.pointScored(2)
        if player2Position in self.player1.trail or player2Position in player2Trail : self.pointScored(1)

        if player1Position[1] < YBUFFER or player1Position[1] > FRAME_SIZE[1] - YBUFFER: self.pointScored(2)
        if player2Position[1] < YBUFFER or player2Position[1] > FRAME_SIZE[1] - YBUFFER: self.pointScored(2)
        if player2Position[0] < XBUFFER or player2Position[0] > FRAME_SIZE[0] - XBUFFER: self.pointScored(1)
        if player1Position[0] < XBUFFER or player2Position[0] > FRAME_SIZE[0] - XBUFFER: self.pointScored(1)



    def pointScored(self, winningPlayer):
        if winningPlayer == 1: self.player1Score += 1
        if winningPlayer == 2: self.player2Score += 1
        self.player1.resetBike()
        self.player2.resetBike()
        self.startLevel()



    def getBorder(self):
        windowWidth = FRAME_SIZE[0]
        windowHeight = FRAME_SIZE[1]

        self.leftBorder  = []
        self.rightBorder = []
        self.topBorder   = []
        self.botBorder   = []

        for index in range(YBUFFER, windowHeight - YBUFFER + 1):
            self.leftBorder.append((XBUFFER, index))
            self.rightBorder.append((windowWidth - XBUFFER, index))

        for index in range(XBUFFER, windowWidth - XBUFFER + 1):
            self.topBorder.append((index, windowHeight - YBUFFER))
            self.botBorder.append((index, YBUFFER))



    def startLevel(self):
        pass


