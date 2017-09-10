from cli import parse_args
from draw import show_results
from rng import *

if __name__ == '__main__':
    parsed = parse_args()
    rng = lehmer_random(parsed.seed, parsed.mod, parsed.mul, parsed.numbers_count)
    random_values = list(rng)

    checking_report = indirect_signs_checking(random_values)
    numerical_characteristics = numerical_characteristics_estimation(random_values)
    interval_distribution = count_interval_distribution(random_values)
    periodic_stats = aperiodic_interval_and_period(random_values)

    show_results(interval_distribution, checking_report, numerical_characteristics, periodic_stats)
