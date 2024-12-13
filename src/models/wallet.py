class Wallet:
    def __init__(self, feedback:bool = False):
        """The class for the wallet of the player.

        Args:
            feedback (bool, optional): Send returns in the console. Defaults to False.
        """
        self.points = 0
        self.feedback = feedback
    def add_points(self, value:int):
        """Add a certain value of points to the player's wallet.

        Args:
            value (int): The number of points to add.
        """
        assert value > 0
        self.points += value
        if self.feedback:
            print(f"{value} succesfully added to the balance.")
    def remove_points(self, value:int):
        """Remove a certain value of points to the player's wallet. Set it to 0 if it's inferior to.

        Args:
            value (int): The number of points to remove.
        """
        assert value > 0
        self.points -= value
        if (self.points < 0):
            self.points = 0
        if self.feedback:
            print(f"{value} succesfully removed from the balance.")