class BasePage:
    """The basis for all pages."""
    IMPLICIT_WAIT_TIME = 10
    TIMEOUT = 30

    def __init__(self, driver):
        """Base constructor.

        Sets driver, implicit wait, and timeout.
        """
        self.driver = driver
        self.driver.implicitly_wait(self.IMPLICIT_WAIT_TIME)
        self.timeout = self.TIMEOUT
