"""
CMPS 2200  Recitation 2
"""

# the only imports needed are here
import tabulate
import time
###


def simple_work_calc(n, a, b):
    # TODO
    if n == 1:
        return 1
    else:
        return a*simple_work_calc(n//b, a, b)+n
    pass


def test_simple_work():
    """ done. """
    assert simple_work_calc(10, 2, 2) == 36
    assert simple_work_calc(20, 3, 2) == 230
    assert simple_work_calc(30, 4, 2) == 650
    assert simple_work_calc(2, 2, 2) == 4
    assert simple_work_calc(20, 4, 4) == 56
    assert simple_work_calc(40, 3, 2) == 730


def work_calc(n, a, b, f):
    # TODO
    if n == 1:
        return 1
    else:
        return a*work_calc(n//b, a, b,f)+f(n)
    pass


def span_calc(n, a, b, f):
    # TODO
    if n == 1:
        return 1
    else:
        return f(n) + span_calc(n//b, a, b, f)
    pass


def test_work():
    assert work_calc(10, 2, 2, lambda n: 1) == 15
    assert work_calc(20, 1, 2, lambda n: n*n) == 530
    assert work_calc(30, 3, 2, lambda n: n) == 300
    assert work_calc(10, 2, 2, lambda n: 2) == 22
    assert work_calc(20, 1, 2, lambda n: n*2) == 75
    assert work_calc(30, 4, 2, lambda n: n) == 650


def compare_work(work_fn1,a1,b1,f1, work_fn2,a2,b2,f2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
    """
    Compare the values of different recurrences for
    given input sizes.

    Returns:
    A list of tuples of the form
    (n, work_fn1(n), work_fn2(n), ...)

    """
    result = []
    input_sizes=sizes
    for n in input_sizes:
        result.append((
            n,
            work_fn1(n,a1,b1,f1),
            work_fn2(n,a2,b2,f2)
        ))
    return result


def print_results(results):
    """ done """
    print(tabulate.tabulate(results,
                            headers=['n', 'W_1', 'W_2'],
                            floatfmt=".3f",
                            tablefmt="github"))


def test_compare_work():
    res = compare_work(work_calc, work_calc,sizes=[10, 20, 40, 80,160, 320, 640])
    print(res)

def test_compare_span(a1,b1,f1,a2,b2,f2,sizes=[10, 20, 40, 80,160, 320, 640]):
    results = []
    for n in sizes:
        results.append((
            n,
            span_calc(n, a1,b1,f1),
            span_calc(n, a2,b2,f2)
        ))
    return results

# print_results(compare_work(work_calc, 4,2,lambda n: n**1, work_calc, 4,2,lambda n: n**3,sizes=[10, 20, 40, 80,160, 320, 640]))
# print_results(test_compare_span(2, 2, lambda n:1, 2, 2, lambda n: n,sizes=[10, 20, 40, 80,160, 320, 640]))
# print_results(compare_work(work_calc, 2,2,lambda n: 1, work_calc, 2,2,lambda n: n,sizes=[10, 20, 40, 80,160, 320, 640]))