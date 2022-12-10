with open("./data/input10.txt") as f:
    contents = f.read().splitlines()

SCREEN_WIDTH = 40
SCREEN_HEIGHT = 6

register = 1
cycle = 0
signal_strengths = []
screen = []


def draw_screen(cycle, register, screen):
    if abs(register - cycle % SCREEN_WIDTH) <= 1:
        screen.append("#")
    else:
        screen.append(".")


for command in contents:
    draw_screen(cycle, register, screen)
    if command.startswith("noop"):
        cycle += 1
    elif command.startswith("addx"):
        cycle += 1
        draw_screen(cycle, register, screen)
        register += int(command.split(" ")[-1])
        cycle += 1

screen_resized = "\n".join(
    [" ".join(screen[i * SCREEN_WIDTH : (i + 1) * SCREEN_WIDTH]) for i in range(SCREEN_HEIGHT)]
)
print(screen_resized)
