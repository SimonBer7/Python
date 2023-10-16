class Lahev:
    """
    The `Lahev` class represents a bottle with a specific capacity.
    It can be opened and closed, and you can add liquid to it.
    The liquid can be added in milliliters using the `add_mili` method.

    Attributes:
        capacity (float): The maximum capacity of the bottle in liters.
        current_capacity (float): The current amount of liquid in the bottle in liters.
        statement (bool): A boolean indicating whether the bottle is open (True) or closed (False).

    Methods:
        - `open()`: Opens the bottle, allowing liquid to be added.
        - `close()`: Closes the bottle, preventing further additions.
        - `add(capacity)`: Adds liquid to the bottle in liters, but only if the bottle is open.
        - `add_mili(capacity)`: Adds liquid to the bottle in milliliters, but only if the bottle is open.
        - `get_capacity()`: Returns the current liquid capacity in liters.
        - `get_capacity_mili()`: Returns the current liquid capacity in milliliters.
        - `clear()`: Empties the bottle if it is open.

    Usage:
        ```python
        lahev = Lahev(5)  # Creates a bottle with a maximum capacity of 5 liters.
        lahev.open()  # Opens the bottle.
        lahev.add(2)  # Adds 2 liters of liquid to the bottle.
        print(lahev.get_capacity())  # Prints the current liquid capacity in liters.
        lahev.add_mili(1000)  # Adds 1000 milliliters (1 liter) of liquid to the bottle.
        print(lahev.get_capacity())  # Prints the updated liquid capacity in liters.
        lahev.clear()  # Empties the bottle.
        ```
    """

    def __init__(self, capacity):
        """
        Initializes a new bottle with the specified capacity.

        Args:
            capacity (float): The maximum capacity of the bottle in liters.
        """
        self.capacity = capacity
        self.current_capacity = 0
        self.statement = False

    def open(self):
        """
        Opens the bottle, allowing liquid to be added.
        """
        self.statement = True

    def close(self):
        """
        Closes the bottle, preventing further additions.
        """
        self.statement = False

    def add(self, cap):
        """
        Adds liquid to the bottle in liters, but only if the bottle is open.

        Args:
            cap (float): The amount of liquid to add in liters.

        Raises:
            Exception: If the bottle is closed, an exception is raised.
        """
        if self.statement:
            self.current_capacity += cap
        else:
            raise Exception("The bottle is closed. Open it to add liquid.")

    def add_mili(self, cap):
        """
        Adds liquid to the bottle in milliliters, but only if the bottle is open.

        Args:
            cap (float): The amount of liquid to add in milliliters.

        Raises:
            Exception: If the bottle is closed, an exception is raised.
        """
        if self.statement:
            self.current_capacity += (cap / 1000)
        else:
            raise Exception("The bottle is closed. Open it to add liquid.")

    def get_capacity(self):
        """
        Returns the current liquid capacity in liters.

        Returns:
            float: The current liquid capacity in liters.
        """
        return self.current_capacity

    def get_capacity_mili(self):
        """
        Returns the current liquid capacity in milliliters.

        Returns:
            float: The current liquid capacity in milliliters.
        """
        return self.current_capacity * 1000

    def clear(self):
        """
        Empties the bottle if it is open.
        """
        if self.statement:
            self.current_capacity = 0
