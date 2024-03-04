import sympy


def generate_formula(a, b, c, d, x, val):
    result = []
    for i in range(0, len(x)):
        result.append(a + b * (x[i] - val) + c * (x[i] - val)**2 + d*(x[i] - val)**3)
    return result


def check_peak(a, b, c, d, x_1, x_2):
    x, y = sympy.symbols('x y')
    y = b + 2*c*(x - x_1) + 3*d*(x - x_1)**2
    answer = sympy.solve(sympy.Eq(y, 0))
    result = []
    for i in answer:
        if i.is_real and x_1 <= i <= x_2:
            y = generate_formula(a, b, c, d, [i], x_1)
            result.append((i, y[0]))
    return result
