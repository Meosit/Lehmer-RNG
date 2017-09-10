from functools import reduce
from itertools import repeat
from math import pi, fabs, sqrt, isclose
from statistics import mean

from helper import min_max

THEORETICAL_PROBABILITY = pi / 4


def _calculate_next(prev, mod, mul):
    next_seed = (prev * mul) % mod
    return next_seed


def lehmer_random(seed, mod, mul, size=None):
    assert size is None or size > 0
    random_range = repeat(0) if size is None else range(size)
    for _ in random_range:
        next_seed = _calculate_next(seed, mod, mul)
        seed = next_seed
        yield next_seed / mod


def indirect_signs_checking(random_values):
    pairs = zip(random_values[::2], random_values[1::2])
    valid_pair_count = sum(a ** 2 + b ** 2 < 1.0 for a, b in pairs)
    actual_probability = valid_pair_count * 2 / len(random_values)
    delta = fabs(THEORETICAL_PROBABILITY - actual_probability)
    return THEORETICAL_PROBABILITY, actual_probability, delta


def numerical_characteristics_estimation(random_values):
    mate_expectation = mean(random_values)
    coefficient = 1 / (len(random_values) - 1)
    dispersion = coefficient * reduce(lambda acc, x: acc + (x - mate_expectation) ** 2, random_values, 0)
    mean_squared_deviation = sqrt(dispersion)
    return mate_expectation, dispersion, mean_squared_deviation


def count_interval_distribution(random_values, interval_count=20):
    # FIXME: invalid last interval distribution
    _min, _max = min_max(random_values)
    interval = float(_max - _min) / (interval_count - 1)
    interval_distribution = {k: 0 for k in range(interval_count)}
    for value in random_values:
        interval_index = int((value - _min) / interval)
        interval_distribution[interval_index] += 1

    def normalize(v): return v / float(len(random_values))

    interval_distribution = {k: normalize(v) for k, v in interval_distribution.items()}
    return interval_distribution


def aperiodic_interval_and_period(random_values):
    test_value = random_values[-1]
    first_occurrence_index = -1
    period = 0
    for i, value in enumerate(random_values, start=0):
        if isclose(value, test_value):
            if first_occurrence_index == -1:
                first_occurrence_index = i
            else:
                period = i - first_occurrence_index
                break
    aperiodic_interval = -1
    for i in range(len(random_values)):
        if isclose(random_values[i], random_values[i + period]):
            aperiodic_interval = i + period
            break
    return aperiodic_interval, period
