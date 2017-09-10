import matplotlib.pyplot as plt


def _draw_labels(rects, ax):
    for rect in rects:
        height = rect.get_height()
        x = rect.get_x() + rect.get_width() / 2.
        y = 0.02 * height
        ax.text(x, y, '%.8f' % float(height), ha='center', va='bottom', color='w', rotation='vertical')


def show_results(interval_distribution, checking_report, numerical_characteristics):
    report_str = "{0:.10f} - Theoretical probability\n{1:.10f} - Actual probability\n{2:.10f} - Delta" \
        .format(*checking_report)

    num_chars_str = "{0:.10f} - Mathematical expectation\n{1:.10f} - Dispersion\n{2:.10f} - Mean squared deviation" \
        .format(*numerical_characteristics)

    fig, ax = plt.subplots()
    rects = ax.bar(range(len(interval_distribution)), interval_distribution.values(), align='center')
    ax.set_xticks(range(len(interval_distribution)), interval_distribution.keys())
    _draw_labels(rects, ax)

    fig.gca().set_position((.1, .2, .8, .75))
    fig.text(.02, .02, report_str)
    fig.text(.5, .02, num_chars_str)
    plt.show()
