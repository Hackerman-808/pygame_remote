import pygame
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

# --start venv mode-- : source venv/bin/activate

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    astfield = AsteroidField()
    # print(f"Updatable group size: {len(updatable)}")
    # print(f"Drawable group size: {len(drawable)}")
    while True:
        screen.fill((0,0,0))
        for i in updatable:
            i.update(dt)
        for i in drawable:
            i.draw(screen)
        for i in shots:
            i.draw(screen)
        for a in asteroids:
            if a.collisions(player):
                print("Game over!")
                raise SystemExit
            for s in shots:
                if a.collisions(s):
                    a.split()
                    s.kill()
                
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        clock.tick(60)
        dt = (clock.tick(60)) / 1000

main()
