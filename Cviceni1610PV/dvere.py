class ZamceneDvereException(Exception):
    """
    Custom exception class for representing locked doors.

    This exception is raised when an attempt is made to open locked doors.
    """

class Dvere:
    """
    The `Dvere` class represents a set of doors that can be opened or closed.

    Attributes:
        zamceno (bool): A boolean indicating whether the doors are locked (True) or unlocked (False).

    Methods:
        - `__init__(self, zamceno)`: Initializes the doors with the specified lock status.
        - `otevrit(self)`: Opens the doors, changing their status to unlocked (False).
        - `get_statement(self)`: Returns the current status of the doors (True for locked, False for unlocked).

    Usage:
    ```python
    d = Dvere(zamceno=True)  # Creates a set of locked doors.
    try:
        d.otevrit()  # Attempts to open the doors.
        if not d.get_statement():
            print("Prošel jsem")
        else:
            raise ZamceneDvereException
    except ZamceneDvereException as e:
        print("Dveře jsou zamčené, nemůžete je otevřít")
    ```
    """

    def __init__(self, zamceno):
        """
        Initializes a set of doors with the specified lock status.

        Args:
            zamceno (bool): The initial lock status of the doors (True for locked, False for unlocked).

        Raises:
            ValueError: If the provided status is not True or False, a ValueError is raised.
        """
        if zamceno is True or zamceno is False:
            self.zamceno = zamceno
        else:
            raise ValueError("Error, please provide only True or False")

    def otevrit(self):
        """
        Opens the doors, changing their status to unlocked (False).
        """
        self.zamceno = False

    def get_statement(self):
        """
        Returns the current status of the doors.

        Returns:
            bool: True if the doors are locked, False if they are unlocked.
        """
        return self.zamceno
