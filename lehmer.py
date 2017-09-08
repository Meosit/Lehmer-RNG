def _calculate_next(prev, mod, mul):
    next_seed = (prev * mul) % mod
    return next_seed


def create_lehmer_random(seed, mod, mul):
    while True:
        next_seed = _calculate_next(seed, mod, mul)
        seed = next_seed
        yield next_seed / mod
