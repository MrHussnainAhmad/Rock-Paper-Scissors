# Rock-Paper-Scissors
    determine_winner Function:
        This function takes two parameters: user_choice and computer_choice.
        It determines the winner based on the choices made by the user and the computer.
        If both choices are the same, it's a tie. Otherwise, it checks the combinations of choices to determine the winner.

    display_result Function:
        This function takes three parameters: user_choice, computer_choice, and result.
        It simply prints out the user's choice, computer's choice, and the result of the game.

    play_game Function:
        This function is the main function to play the game.
        It prompts the user to enter their choice (rock, paper, scissors) or 'q' to quit.
        It validates the user's input and generates the computer's choice randomly.
        It then determines the winner using the determine_winner function, updates the scores, displays the result, and increments the game count.
        If the user chooses to quit, it returns False to signal the end of the game loop.

    Game Loop:
        The game loop continuously calls the play_game function until the user chooses to quit.

    Final Scores Display:
        After the game ends, the final scores (user's score, computer's score, and the number of games played) are displayed.
