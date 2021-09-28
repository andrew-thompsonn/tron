import pygame

# TODO: - "Boost" feature

class TronBike(pygame.sprite.Sprite):

    def __init__(self, imagePath, coordinates, direction, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.startDirection = direction
        self.startCoords = coordinates
        self.trail = [coordinates]
        self.dimensions = (43, 48)
        self.movementDist = 5
        self.vectors = {1:(1, 0), 2:(0, 1), 3:(-1, 0), 4:(0, -1)}
        self.angles = {1:-90, 2:180, 3:90, 4:0}
        self.direction = None

        self.rawImage = pygame.image.load(imagePath)
        self.rawImage = pygame.transform.scale(self.rawImage, self.dimensions)
        self.image = self.rawImage

        self.rect = self.image.get_rect()
        self.rect.center = self.trail[0]

        self.updateDirection(direction)


    def updateDirection(self, direction):
        self.direction = self.vectors[direction]
        angle = self.angles[direction]
        self.rotateCenter(self.rect.center, angle)


    def rotateCenter(self, center, angle):
        self.image = pygame.transform.rotate(self.rawImage, angle)
        self.rect = self.image.get_rect(center = self.image.get_rect(center = center).center)


    def move(self):
        coordinates = self.trail[-1]
        for distance in range(1, self.movementDist + 1):
            xMovement = self.direction[0]*distance
            yMovement = self.direction[1]*distance

            coordinate = (coordinates[0] + xMovement, coordinates[1] + yMovement)
            self.trail.append(coordinate)

        self.rect.center = self.trail[-1]


    def resetBike(self):
        self.trail.clear()
        self.trail.append(self.startCoords)
        self.trail.append(self.startCoords)
        self.updateDirection(self.startDirection)
