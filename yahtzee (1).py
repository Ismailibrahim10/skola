from die import Die

class YahtzeeMainClass:
    def __init__(self):
        self.dice = [Die() for _ in range(5)]
        self.keep_playing = True
        
        while self.keep_playing:
            self.play_round()

    def play_round(self):
        """Play a single round of Yahtzee."""
        turn = 0
        print("Welcome to Yahtzee!")
        
        while turn < 3:
            print(f"Starting turn: {turn+1} of 3, rolling dice")
            self.roll_dice()
            self.display_dice()
            if self.check_yahtzee():
                print(f"You got YAHTZEE! in {self.dice[0].value}'s")
                return
            if turn < 2:
                if not self.prompt_continue("Want to throw again? (y for yes, anything else for no) "):
                    break
            else:
                if not self.prompt_continue("Game over! Want to play again? (y for yes, anything else for no) "):
                    break
            turn += 1

    def roll_dice(self):
        """Roll all dice."""
        for die in self.dice:
            die.roll()

    def display_dice(self):
        """Display the current values of all dice."""
        for i, die in enumerate(self.dice):
            print(f"{i}: {die}")

    def check_yahtzee(self):
        """Check if all dice have the same value (Yahtzee)."""
        first_value = self.dice[0].value
        return all(die.value == first_value for die in self.dice)

    @staticmethod
    def prompt_continue(prompt):
        """Prompt the player to continue or stop the game."""
        return input(prompt).strip().lower() == 'y'

def main():
    YahtzeeMainClass()

if __name__ == '__main__':
    main()
