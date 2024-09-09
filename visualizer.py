import pygame
import random
import time
import pyperclip
from algorithms.bubble_sort import bubble_sort
from algorithms.merge_sort import merge_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.quick_sort import quick_sort
from algorithms.selection_sort import selection_sort

# Pygame window settings
pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 122, 255)
GRAY = (220, 220, 220)
DARK_GRAY = (180, 180, 180)
GREEN = (50, 205, 50)
RED = (255, 69, 58)
HIGHLIGHT = (0, 150, 136)

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Visualizer")
clock = pygame.time.Clock()

# Global variables
sorting_algorithm = None
user_input_array = ""
input_active = False  # Track whether input box is active
cursor_visible = True  # For blinking cursor in the input box
cursor_timer = 0  # Timer for cursor blinking

# Helper function to render text on the screen
def render_text(window, text, size, color, pos):
    font = pygame.font.Font(None, size)
    label = font.render(text, True, color)
    window.blit(label, pos)

# Function to handle user input (array)
def handle_text_input(event, current_input):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_BACKSPACE:
            current_input = current_input[:-1]
        elif event.key == pygame.K_RETURN:
            # Process the input and start sorting
            return current_input
        elif event.key == pygame.K_v and pygame.key.get_mods() & pygame.KMOD_CTRL:
            # Paste from clipboard
            current_input += pyperclip.paste()
        elif event.unicode.isdigit() or event.unicode == ',':
            current_input += event.unicode
    return current_input

# Function to draw the input box with cursor
def draw_input_box(window, input_text, active, cursor_visible):
    font = pygame.font.Font(None, 36)
    
    # Set input box color based on active state
    color = HIGHLIGHT if active else GRAY
    
    # Draw input box
    pygame.draw.rect(window, color, (50, 50, 700, 50))
    pygame.draw.rect(window, BLACK, (50, 50, 700, 50), 2)
    
    # Render text inside input box
    render_text(window, input_text, 36, BLACK, (60, 60))
    
    # Measure the width of the text in the input box
    text_surface = font.render(input_text, True, BLACK)
    text_width = text_surface.get_width()
    
    # Draw the blinking cursor if input box is active
    if active and cursor_visible:
        cursor_x = 60 + text_width  # Set cursor position after the text
        pygame.draw.line(window, BLACK, (cursor_x, 60), (cursor_x, 90), 2)

# Function to draw the algorithm selection buttons
def draw_algorithm_buttons(window, clicked_button):
    buttons = [("Bubble Sort", 50, 150), ("Merge Sort", 250, 150), ("Insertion Sort", 450, 150),
               ("Quick Sort", 50, 220), ("Selection Sort", 250, 220)]
    
    for i, (text, x, y) in enumerate(buttons):
        button_color = DARK_GRAY if clicked_button == i else GRAY
        pygame.draw.rect(window, button_color, (x, y, 150, 40))
        pygame.draw.rect(window, BLACK, (x, y, 150, 40), 2)
        render_text(window, text, 24, BLACK, (x + 10, y + 10))
    return buttons

# Function to check if a button is clicked
def button_clicked(pos, button_rect):
    return button_rect.collidepoint(pos)

# Function to draw the "Start" button with click effect
def draw_start_button(window, is_clicked):
    button_color = DARK_GRAY if is_clicked else GREEN
    pygame.draw.rect(window, button_color, (350, 500, 100, 40))
    pygame.draw.rect(window, BLACK, (350, 500, 100, 40), 2)
    render_text(window, "Start", 30, BLACK, (370, 510))

# Function to visualize sorting
def visualize(arr):
    draw_array(arr, [BLUE] * len(arr))
    time.sleep(0.05)

# Function to draw array bars
def draw_array(arr, colors):
    window.fill(WHITE)
    bar_width = WIDTH // len(arr)
    for i, val in enumerate(arr):
        pygame.draw.rect(window, colors[i], (i * bar_width, HEIGHT - val, bar_width, val))
    pygame.display.update()

def main():
    global sorting_algorithm, user_input_array, input_active, cursor_visible, cursor_timer

    running = True
    sorting_completed = False
    arr = []
    selected_algorithm = None
    clicked_button = None
    start_button_clicked = False

    while running:
        window.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Handle input box activation
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 50 <= event.pos[0] <= 750 and 50 <= event.pos[1] <= 100:
                    input_active = True
                else:
                    input_active = False

            # Handle input for array when the input box is active
            if input_active:
                user_input_array = handle_text_input(event, user_input_array)

            # Handle button click for algorithm selection
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                # Check for button clicks
                if 50 <= pos[0] <= 200 and 150 <= pos[1] <= 190:
                    sorting_algorithm = "bubble_sort"
                    clicked_button = 0
                elif 250 <= pos[0] <= 400 and 150 <= pos[1] <= 190:
                    sorting_algorithm = "merge_sort"
                    clicked_button = 1
                elif 450 <= pos[0] <= 600 and 150 <= pos[1] <= 190:
                    sorting_algorithm = "insertion_sort"
                    clicked_button = 2
                elif 50 <= pos[0] <= 200 and 220 <= pos[1] <= 260:
                    sorting_algorithm = "quick_sort"
                    clicked_button = 3
                elif 250 <= pos[0] <= 400 and 220 <= pos[1] <= 260:
                    sorting_algorithm = "selection_sort"
                    clicked_button = 4

                # Check for start button click
                if button_clicked(pos, pygame.Rect(350, 500, 100, 40)):
                    start_button_clicked = True
                    try:
                        arr = [int(x.strip()) for x in user_input_array.split(',') if x.strip().isdigit()]
                        sorting_completed = False
                    except ValueError:
                        print("Invalid array input. Please enter valid integers.")
            else:
                start_button_clicked = False

        # Blinking cursor logic
        cursor_timer += clock.get_time()
        if cursor_timer >= 500:
            cursor_visible = not cursor_visible
            cursor_timer = 0

        # Draw the input box and the algorithm selection buttons
        draw_input_box(window, user_input_array, input_active, cursor_visible)
        draw_algorithm_buttons(window, clicked_button)
        draw_start_button(window, start_button_clicked)

        if arr and sorting_algorithm and not sorting_completed:
            if sorting_algorithm == "bubble_sort":
                bubble_sort(arr, visualize)
            elif sorting_algorithm == "merge_sort":
                merge_sort(arr, visualize)
            elif sorting_algorithm == "insertion_sort":
                insertion_sort(arr, visualize)
            elif sorting_algorithm == "quick_sort":
                quick_sort(arr, visualize)
            elif sorting_algorithm == "selection_sort":
                selection_sort(arr, visualize)
            sorting_completed = True

        # Update the screen
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
