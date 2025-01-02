import math

import numpy as np
from pydantic import BaseModel, NonNegativeFloat

from neural_network_ml.inverted_pendulum.cart import Cart
from neural_network_ml.inverted_pendulum.pendulum import Pendulum

"""Equations of motion:

(m_c + m_p) x_ddot + b x_dot + m_p l_p theta_ddot cos(theta) - m_p l_p theta_dot^2 sin(theta) = Force

(I + m_p l_p^2) theta_ddot + m_p g l_p sin(theta) = -m_p l_p x_ddot cos(theta)
I = l_p * m_p^2

This can be solved for x_ddot and theta_ddot as a system of simultaneous equations at each instant in time:

k1_1 * x_ddot + k1_2 * theta_ddot = k1_3
k2_1 * x_ddot + k2_2 * theta_ddot = k2_3
"""


class Accelerations(BaseModel):
    x_ddot: float
    theta_ddot: float


def calculate_accelerations(
    pendulum: Pendulum,
    cart: Cart,
    *,
    force: float,
    drag_coefficient: NonNegativeFloat = 0.0,
) -> Accelerations:
    k1_1 = pendulum.MASS + cart.MASS
    k1_2 = pendulum.MASS * pendulum.LENGTH * math.cos(pendulum.theta)
    k1_3 = (
        force
        + pendulum.MASS
        * pendulum.LENGTH
        * pendulum.theta_dot**2
        * math.sin(pendulum.theta)
        - drag_coefficient * cart.x_dot
    )

    moment_of_inertia = pendulum.MASS * pendulum.LENGTH**2
    k2_1 = pendulum.MASS * pendulum.LENGTH * math.cos(pendulum.theta)
    k2_2 = moment_of_inertia + pendulum.MASS * pendulum.LENGTH**2
    k2_3 = -pendulum.MASS * 9.81 * pendulum.LENGTH * math.sin(pendulum.theta)

    # Solve as linear system
    A = np.array([[k1_1, k1_2], [k2_1, k2_2]])
    b = np.array([k1_3, k2_3])
    res = np.linalg.solve(A, b)
    return Accelerations(x_ddot=res[0], theta_ddot=res[1])
