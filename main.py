import game

from blessed import Terminal


def main() -> None:
    terminal = Terminal()
    print(terminal.clear())

    game.play_game()


if __name__ == "__main__":
    main()
