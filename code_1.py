import pygame
import sys
import random

pygame.init()
pygame.mixer.init()

# Constants
WIDTH, HEIGHT = 600, 600
CIRCLE_RADIUS = 250
BALL_RADIUS = 10
FPS = 60

# Sound
bounce_sound = pygame.mixer.Sound("media/bounce.wav")

# Initialise Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BOUNCING BALL")

clock = pygame.time.Clock()

def draw_circle(color):
    pygame.draw.circle(screen, color, (WIDTH // 2, HEIGHT // 2), CIRCLE_RADIUS, 2)

def main():
    ball_radius = BALL_RADIUS
    ball_position = [WIDTH // 2, HEIGHT // 2]
    ball_speed = [4, 4]
    acceleration = 0.1
    
    # Initialize colors with default values
    ball_color = (255, 255, 255)
    circle_color = (255, 255, 255)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Update ball position with acceleration
        ball_speed[0] += random.uniform(-1, 1)
        ball_speed[1] += random.uniform(-1, 1)
        
        ball_position[0] += ball_speed[0]
        ball_position[1] += ball_speed[1]
        
        # Check for collisions with circle boundaries
        distance = ((ball_position[0] - WIDTH // 2)**2 + (ball_position[1] - HEIGHT // 2)**2)**0.5
        if distance + ball_radius >= CIRCLE_RADIUS: 
            ball_speed[0] *= -1
            ball_speed[1] *= -1
            
            # Play bounce sound
            bounce_sound.play()
            
            # Increase ball size by 1 on each bounce
            ball_radius += 2
            
            # Random color for the ball and circle
            ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            circle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            
            # Ensure the ball stays within the circle boundaries
            ball_position[0] = max(CIRCLE_RADIUS, min(WIDTH - CIRCLE_RADIUS, ball_position[0]))
            ball_position[1] = max(CIRCLE_RADIUS, min(HEIGHT - CIRCLE_RADIUS, ball_position[1]))
            
            # Check if the ball completely fills the circle
            if ball_radius >= CIRCLE_RADIUS:
                pygame.quit()
                sys.exit()
        
        # Clear the screen
        screen.fill((0, 0, 0))
        
        # Draw the circle
        draw_circle(circle_color)
        
        # Draw the bouncing ball
        pygame.draw.circle(screen, ball_color, (int(ball_position[0]), int(ball_position[1])), ball_radius)
        
        # Update the display
        pygame.display.flip()
        
        # Control the frame rate
        clock.tick(FPS)

if __name__ == "__main__":
    main()
