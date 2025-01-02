from neural_network_ml import TIME_DELTA


class Cart:
    # Constants
    MASS: float = 1.0

    # Position constraints
    X_MAX: float = 0.9
    X_MIN: float = 0.1

    # Speed constraints
    X_DOT_MAX: float = 0.3

    # Variables
    x_dot: float
    x: float
    y: float

    def __init__(self) -> None:
        self.x = 0.5
        self.x_dot = 0.0

        self.y = 0.5

    def update(self, x_ddot: float) -> None:
        self.x_dot += x_ddot * TIME_DELTA

        if self.x_dot > self.X_DOT_MAX:
            self.x_dot = self.X_DOT_MAX
        elif self.x_dot < -self.X_DOT_MAX:
            self.x_dot = self.X_DOT_MAX

        self.x += self.x_dot * TIME_DELTA

        if self.x > self.X_MAX:
            self.x = self.X_MAX
            self.x_dot *= -0.5
        elif self.x < self.X_MIN:
            self.x = self.X_MIN
            self.x_dot *= -0.5
