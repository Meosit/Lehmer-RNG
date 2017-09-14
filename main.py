from cli import parse_args
from draw import show_results
from rng import *

RNG_GENERATORS = {
    'raw': lehmer_random,
    'uniform': uniform_random,
    'gaussian': gaussian_random,
    'exponential': exponential_random,
    'gamma': gamma_random,
    'triangle': triangle_random,
    'simpson': simpson_random
}

if __name__ == '__main__':
    parsed = parse_args()
    rng = RNG_GENERATORS[parsed.mode](vars(parsed))
    random_values = list(rng)

    checking_report = indirect_signs_checking(random_values) if parsed.mode == 'raw' else None
    numerical_characteristics = numerical_characteristics_estimation(random_values)
    interval_distribution = count_interval_distribution(random_values, parsed.intervals_count)
    periodic_stats = aperiodic_interval_and_period(random_values)

    show_results(interval_distribution, checking_report, numerical_characteristics, periodic_stats)
