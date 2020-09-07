import pygame
from game import Game
pygame.init()

# generer la fenetre de notre jeu
pygame.display.set_caption("bah c'est le jeu")
screen = pygame.display.set_mode((1080, 720))

# importer de charger l'arriere plan de notre jeu
background = pygame.image.load('assets/bg.jpg')

# charger notre jeu
game = Game()

running = True

# boucle tant que cette condition est vrai
while running:

    # appliquer l'arriere plan de notre jeu
    screen.blit(background, (0, -200))

    # recuperer les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()


    # appliquer l'ensemble des images de mon groupe de projectiles
    game.player.all_projectiles.draw(screen)



    # appliquer image du joueur
    screen.blit(game.player.image, game.player.rect)

    # verifier si le joueur souhaite aller a gauche ou a droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    print(game.player.rect.x)

    #mettre a jour l'ecran
    pygame.display.flip()

    # si le joueur ferme cettre fenetre
    for event in pygame.event.get():
        # que l'event est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")
        # detecter si joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #detecter si la touche espace  est enclenchée pour lancer notre projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()



        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False