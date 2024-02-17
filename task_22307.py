# Скорость автомобиля изменяется по закону v=10+0,5⋅t, где t - время движения. Уравнение прямолинейного движения
# выглядит следующим образом: v=v0+a⋅t, где v0 - начальная скорость, t - время движения автомобиля, а a
# - ускорение. Найдите результирующую силу, действующую на автомобиль, если его масса равна 1,5т, а действие
# внешних сил описывается вторым законом Ньютона: F=m⋅a, где m - масса автомобиля, а a - его ускорение.

import pymorphy2
import numpy as np
from icecream import ic


def get_alpha(v: int, v0: int, t: int) -> float:
    """
    Данная функция не принимает участия в коде, используется для расчёта коэффициента alpha.
    Где v - конечная скорость км/час, v0 - начальная скорость км/час, t - время движения в секундах
    """

    alpha = round((v * (1000 / 3600) - v0 * (1000 / 3600)) / t, 1)
    return alpha


def choosing_declension_form(word: (str, list), case: str) -> str:
    """
    Функция подбирает правильную форму склонения переданного слова, см. https://opencorpora.org/dict.php?act=gram,
    """

    morph = pymorphy2.MorphAnalyzer()
    if len(word.split()) == 1:
        return morph.parse(word)[0].inflect({case}).word
    else:
        list_morphy = []
        for i in word.split():
            list_morphy.append(morph.parse(i)[0].inflect({case}).word)
        return " ".join(list_morphy)


def get_plot_from_task_22307():
    values_list = (
        {
            "element": "автомобиль",
            "mass": np.arange(1, 2, 0.1),
            "alpha": np.arange(1, 5, 0.1),
        },
        {
            "element": "велосипедист",
            "mass": np.arange(0.05, 0.11, 0.01),
            "alpha": np.arange(0.1, 1.1, 0.1),
        },
    )

    return np.random.choice(values_list)


def task_22307():
    """Задача №22307 с портала https://kuzovkin.info/zadachi/?exam_parametr=[124]"""

    # Случайным образом получаем сюжет задачи
    plot = get_plot_from_task_22307()

    while True:
        mass = round(np.random.choice(plot.get("mass")), 2)
        alpha = round(np.random.choice(plot.get("alpha")), 1)
        task = (
            rf"Скорость {choosing_declension_form(plot.get('element'), case='gent')} "
            + r"изменяется по закону \(v=10+"
            + f"{alpha}"
            + r"{\cdot}t\), где \(t\) - время "
            r"движения. Уравнение прямолинейного движения выглядит следующим образом: \(v=v_{0}+\alpha{\cdot}t\) где "
            r"\(v_{0}\) - начальная скорость, \(t\) - время движения "
            + f"{choosing_declension_form(plot.get('element'), case='gent')}, "
            + r"а \(\alpha\) - ускорение. "
            r"Найдите результирующую силу, действующую на "
            + f"{choosing_declension_form(plot.get('element'), case='accs')}, "
            + r"если его масса равна \("
            + f"{mass}"
            + r"\)т, "
            r"а действие внешних сил описывается вторым законом Ньютона: \(F=m{\cdot}\alpha\), где \(m\) - масса "
            f"{choosing_declension_form(plot.get('element'), case='gent')}" + r", а \(\alpha\) - его ускорение.",
        )

        answer = round(mass * 10**3 * alpha, 2)

        # Проверка на целое число, если число целое отбрасываем часть после запятой.
        answer = int(answer) if answer % 1 == 0 else answer

        if answer > 0:
            break

    return task, answer


if __name__ == "__main__":

    ic(task_22307())
