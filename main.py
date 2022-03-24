import game


def main():
    """Entry point to the app."""

    # Welcome message
    game.welcome()

    # Game loop
    while True:
        game.play_game()


if __name__ == "__main__":
    main()
