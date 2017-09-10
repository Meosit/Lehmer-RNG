import matplotlib.pyplot as plt


def _draw_labels(rects, ax):
    for rect in rects:
        height = rect.get_height()
        x = rect.get_x() + rect.get_width() / 2.
        y = 0.02 * height
        ax.text(x, y, '%.8f' % float(height), ha='center', va='bottom', color='w', rotation='vertical')


def show_results(interval_distribution, checking_report, numerical_characteristics, periodic_stats):
    report_str = "{0:.10f} - Theoretical probability\n{1:.10f} - Actual probability\n{2:.10f} - Delta" \
        .format(*checking_report)

    num_chars_str = "{0:.10f} - Mathematical expectation\n{1:.10f} - Dispersion\n{2:.10f} - Mean squared deviation" \
        .format(*numerical_characteristics)

    periodic_stats_str = "Aperiodic interval: {0:d}, Period: {1:d}".format(*periodic_stats)

    fig, ax = plt.subplots()
    rects = ax.bar(range(len(interval_distribution)), interval_distribution.values(), align='center')
    _draw_labels(rects, ax)

    fig.gca().set_position((.1, .25, .8, .75))
    fig.canvas.set_window_title('Lehmer RNG')
    fig.text(.02, .02, report_str)
    fig.text(.52, .02, num_chars_str)
    fig.text(.25, .14, periodic_stats_str)
    plt.xticks(range(len(interval_distribution)), interval_distribution.keys())
    plt.show()
