import numpy as np
from sympy import latex


def task_27953():
    """
    Задача №27953 с портала https://ege.sdamgia.ru/problem?id=27953
    """

    thermal_expansion_coefficient = {
        'ABS (акрилонитрил-бутадиен-стирол) термопласт': 7.38,
        'ABS - стекло, армированное волокнами': 3.04,
        'Акриловый материал, прессованный': 23.4,
        'Алмаз': 0.11,
        'Алмаз технический': 0.12,
        'Алюминий': 2.22,
        'Ацеталь': 10.65,
        'Ацеталь , армированный стекловолокном': 3.94,
        'Ацетат целлюлозы (CA)': 13.0,
        'Ацетат бутират целлюлозы (CAB)': 2.52,
        'Барий': 2.06,
        'Бериллий': 1.15,
        'Бериллиево-медный сплав (Cu 75, Be 25)': 1.67,
        'Бетон': 1.45,
        'Бетонные структуры': 0.98,
        'Бронза': 1.8,
        'Ванадий': 0.8,
        'Висмут': 1.3,
        'Вольфрам': 0.43,
        'Гадолиний': 0.9,
        'Гафний': 0.59,
        'Германий': 0.61,
        'Гольмий': 1.12,
        'Гранит': 0.79,
        'Графит, чистый': 0.79,
        'Диспрозий': 0.99,
        'Древесина, пихта, ель': 0.37,
        'Древесина дуба, параллельно волокнам': 0.49,
        'Древесина дуба , перпендикулярно волокнам': 0.54,
        'Древесина, сосна': 0.5,
        'Европий': 3.5,
        'Железо, чистое': 1.2,
        'Железо, литое': 1.04,
        'Железо, кованое': 1.13,
        'Золото': 1.42,
        'Известняк': 0.8,
        'Инвар (сплав железа с никелем)': 0.15,
        'Инконель (сплав)': 1.26,
        'Иридий': 0.64,
        'Иттербий': 2.63,
        'Иттрий': 1.06,
        'Кадмий': 3,
        'Калий': 8.3,
        'Кальций': 2.23,
        'Каменная кладка': {'min_length': 0.47, 'max_length': 0.9},
        'Каучук, твердый': 7.7,
        'Кварц': {'min_length': 0.077, 'max_length': 0.09},
        'Керамическая плитка (черепица)': 0.59,
        'Кирпич': 0.55,
        'Кобальт': 1.2,
        'Констанан (сплав)': 1.88,
        'Корунд, спеченный': 0.65,
        'Кремний': 0.51,
        'Лантан': 1.21,
        'Латунь': 1.87,
        'Лед': 5.1,
        'Литий': 4.6,
        'Литая стальная решетка': 1.08,
        'Лютеций': 0.99,
        'Литой лист из акрилового пластика': 8.1,
        'Магний': 2.5,
        'Марганец': 2.2,
        'Медноникелевый сплав 30%': 1.62,
        'Медь': 1.66,
        'Молибден': 0.5,
        'Монель-металл (никелево-медный сплав)': 1.35,
        'Мрамор': {'min_length': 0.55, 'max_length': 1.41},
        'Мыльный камень (стеатит)': 0.85,
        'Мышьяк': 0.47,
        'Натрий': 7,
        ''





    }
    # При возрастании температуры происходит тепловое расширение
    values_list = [
        {'element': 'рельс', 'genitive_case': 'рельса', 'material': 'Железо, чистое', 'belong': 'его',
         'coefficient': 1.2, 'min_length': 1, 'max_length': 25},
        {'element': 'линейка', 'genitive_case': 'линейки', 'material': 'Сталь', 'belong': 'её', 'coefficient': 1.3,
         'step_length': [0.150, 0.300, 0.500, 1, 1.5, 2, 3]
         },
        {'element': 'рулетка', 'genitive_case': 'рулетки', 'material': 'Сталь', 'belong': 'её', 'coefficient': 1.3,
         'step_length': [3, 5, 8, 10, 15, 20, 30, 50, 60]
         },
        {'element': 'медный стержень', 'genitive_case': 'медного стержня', 'material': 'Медь', 'belong': 'его',
         'coefficient': 1.66, 'step_length': [1, 1.2, 1.5, 2, 2.2, 2.5, 3]
         },
    ]

    # случайным образом получаем сюжет задачи
    data = np.random.choice(values_list)

    element = data.get('element')
    genitive_case = data.get('genitive_case')
    belong = data.get('belong')
    coefficient = thermal_expansion_coefficient.get(data.get('material'))
    min_length = data.get('min_length')
    max_length = data.get('max_length')
    length = data.get('step_length')

    while True:
        alpha = coefficient * 10 ** (-5)

        if isinstance(coefficient, dict):
            coefficient = round(np.random.uniform(coefficient.get('min_length'), coefficient.get('max_length')), 2)

        print(coefficient)
        return

        if min_length and max_length:
            zero_length = np.random.randint(min_length, max_length)
        elif length:
            zero_length = np.random.choice(length)

        increase = np.random.randint(1, 10)
        task = (f'При температуре ' + '\(0^{\circ}C\)' + f' {element} имеет длину ' + r'\(l_{\circ}=' + latex(zero_length) + r'\)' +
                f'м. При возрастании температуры происходит тепловое расширение {genitive_case}, и {belong} длина, выраженная в '
                f'метрах, меняется по закону ' + r'\(l(t^{\circ})=l_0(1+\alpha*t^{\circ})\),' + ' где '
                + r'\(\alpha=' + latex(coefficient) + '*10^{-5}(^{\circ}C^{-1})' + r'\)' + ' — коэффициент теплового расширения, '
                + '\(t^{\circ}\)' + f' — температура (в градусах Цельсия). При какой температуре {element} '
                f'удлинится на {increase}мм? Ответ выразите в градусах Цельсия.')
        answer = round(increase * 10 ** (-3) / (alpha * zero_length))
        if 1 <= answer <= 200:
            break

    return task, answer


def task_27954():
    """
    Задача №27954 с портала https://ege.sdamgia.ru/problem?id=27954
    """
    while True:
        while True:
            p = np.random.randint(100, 5000)
            v = np.random.randint(100, 3000)
            if p >= (v * 1.6):
                break
        while True:
            f = np.random.randint(700000, 7000000)
            monthly_profit = np.random.randint(300000, 3000000)
            if f >= (monthly_profit * 1.6):
                break
        task = (f'Некоторая компания продает свою продукцию по цене \u03C1 = {p} руб. за единицу, переменные затраты '
                f'на производство одной единицы продукции составляют \u03BD = {v} руб., постоянные расходы предприятия '
                f'\u2A0D = {f} руб. в месяц. Месячная операционная прибыль предприятия (в рублях) вычисляется по '
                f'формуле \u03C0(q) = q(\u03C1 - \u03BD) - \u2A0D. Определите месячный объeм производства q '
                f'(единиц продукции), при котором месячная операционная прибыль предприятия будет равна '
                f'{monthly_profit} руб.')
        answer = round((f + monthly_profit) / (p - v))
        if 100 <= answer <= 10000:
            break

    return task, answer



if __name__ == "__main__":
    print(task_27953())
    # print(task_27954())
