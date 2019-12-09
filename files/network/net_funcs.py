import numpy as np


def distance(x1, y1, x2, y2):
    """Calculate Euclidean distance."""
    dist = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return round(dist, 3)


def rain_attenuation(distance):
    """Calculate rain attenuation."""
    attenuation = 9 * (distance / 1000)  # convert from m to km
    return round(attenuation, 3)


def fooliage_loss(distance, frequency):
    """Calculates fooliage loss."""
    loss = 0.2 * ((frequency * 1000) ** 0.3) * ((5 / 1000) ** 0.6)
    return round(loss, 3)


def path_loss(distance, frequency, rain, fooliage):
    """Calculates path_loss."""
    path_loss = 92.4 + 20 * np.log10(distance / 1000) + 20 * np.log10(frequency) + 0.06 * (
        distance / 1000) + round(np.random.uniform(0, 1), 3) + rain + fooliage
    return round(path_loss, 3)


def received_power(power_bs, num_bs, distance, frequency, rain, fooliage):
    """Returns recieved power given the number of base stations.

    Args:
        power_bs: power of the base station.
        num_bs: number of base stations.
        distance: distance between user and base station
        frequency: the frequency at which the base station(s) operate.
        rain: rain attenuation.
        fooliage: fooliage loss.

    Returns:
        A float rounded to three decimal places representing the recieved power.
    """

    power = (10 * np.log10(power_bs / num_bs) -
             path_loss(distance, frequency, rain, fooliage)) + 30
    return round(power, 3)
