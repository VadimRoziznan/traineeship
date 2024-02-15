from icecream import ic
import pymorphy2
import numpy as np
from sympy import latex


# Функция для text_tasks/
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


# Функция для text_tasks/
def get_modified_pronoun(
    word: str, сase: str, pronoun_masc=None, pronoun_femn=None, pronoun_neut=None
) -> (str, None):
    """
    Функция меняет форму указательных местоимений учитывая род переданного существительного в параметре word,
    При использовании не корректного слова в параметре word или слова которого нет в словаре pymorphy2 функция
    вернёт None.
    """

    morph = pymorphy2.MorphAnalyzer()
    gender_first_word = morph.parse(word)[0].tag.gender
    if gender_first_word == "masc" and pronoun_masc:
        new_gender_second_word = morph.parse(pronoun_masc)[0].inflect({сase}).word
        return new_gender_second_word
    elif gender_first_word == "femn" and pronoun_femn:
        new_gender_second_word = morph.parse(pronoun_femn)[0].inflect({сase}).word
        return new_gender_second_word
    elif gender_first_word == "neut" and pronoun_neut:
        new_gender_second_word = morph.parse(pronoun_neut)[0].inflect({сase}).word
        return new_gender_second_word

    return None

def get_plot_from_task_27953():
    # Сюжеты задачи.
    # Оформление:
    # "element": укажите название элемента.
    # "size_list": размер(ы) элемента, если размеры имеют стандартный шаг, замените значения start, stop, step в
    # np.arange(start, stop, step) где start - минимальная длина, stop - максимальная длина + 1 шаг, step - шаг, если
    # размеры имеют не стандартный шаг укажите их в [value1, value2, value3...].

    values_list = (
        {
            "element": "рельс",
            "size_list": np.arange(1, 25, 1),
            "thermal_expansion_coefficient": 1.3,
        },
        {
            "element": "линейка",
            "size_list": [0.15, 0.3, 0.5, 1, 1.5, 2, 3],
            "thermal_expansion_coefficient": 1.3,
        },
        {
            "element": "рулетка",
            "size_list": [3, 5, 8, 10, 15, 20, 30, 50, 60],
            "thermal_expansion_coefficient": 1.3,
        },
        {
            "element": "медный стержень",
            "size_list": np.arange(1, 3.5, 0.5),
            "thermal_expansion_coefficient": 1.66,
        },
        {
            "element": "алюминиевый потолочный карниз",
            "size_list": np.arange(1.4, 5, 0.2),
            "thermal_expansion_coefficient": 2.22,
        },
        {
            "element": "витринное стекло",
            "size_list": np.arange(1, 4.1, 0.1),
            "thermal_expansion_coefficient": 0.9,
        },
        {
            "element": "серебряная цепочка",
            "size_list": np.arange(0.35, 0.75, 0.05),
            "thermal_expansion_coefficient": 1.95,
        },
        {
            "element": "упаковочная пленка",
            "size_list": np.arange(1, 10.1, 0.1),
            "thermal_expansion_coefficient": 20,
        },
        {
            "element": "бетонная стена",
            "size_list": np.arange(1, 3.1, 0.1),
            "thermal_expansion_coefficient": 1.45,
        },
        {
            "element": "медная проволока",
            "size_list": np.arange(1, 101, 0.5),
            "thermal_expansion_coefficient": 1.66,
        },
        {
            "element": "железный мост",
            "size_list": np.arange(18.6, 32.6, 0.1),
            "thermal_expansion_coefficient": 1.04,
        },
        {
            "element": "золотая цепочка",
            "size_list": np.arange(0.35, 0.75, 0.05),
            "thermal_expansion_coefficient": 1.42,
        },
        {
            "element": "стекло армированное",
            "size_list": np.arange(1, 3.31, 0.05),
            "thermal_expansion_coefficient": 3.04,
        },
        {
            "element": "самолёт",
            "size_list": np.arange(5, 31, 1),
            "thermal_expansion_coefficient": 2.22,
        },
    )

    return np.random.choice(values_list)

def task_27953():
    """
    Задача №27953 с портала https://ege.sdamgia.ru/problem?id=27953
    """



    # Случайным образом получаем сюжет задачи
    plot = get_plot_from_task_27953()

    while True:

        zero_length = round(np.random.choice(plot.get("size_list")), 2)
        alpha = plot.get("thermal_expansion_coefficient") * 10 ** (-5)
        increase = round(np.random.uniform(0.1, 10), 1)
        task = (
            f"При температуре "
            + "\(0^{\circ}C\)"
            + f' {plot.get("element")} имеет длину '
            + r"\(l_{\circ}="
            + latex(zero_length)
            + r"\)"
            + f"м. При возрастании температуры происходит тепловое расширение "
            f'{choosing_declension_form(plot.get("element"), case="gent")}, '
            f'и {get_modified_pronoun(word=plot.get("element").split()[-1], сase="gen2", pronoun_masc="он", pronoun_femn="она", pronoun_neut="оно")} длина, выраженная в '
            f"метрах, меняется по закону "
            + r"\(l(t^{\circ})=l_0(1+\alpha{\cdot}t^{\circ})\),"
            + " где "
            + r"\(\alpha="
            + latex(plot.get("thermal_expansion_coefficient"))
            + "{\cdot}10^{-5}(^{\circ}C^{-1})"
            + r"\)"
            + " — коэффициент теплового расширения, "
            + "\(t^{\circ}\)"
            + f' — температура (в градусах Цельсия). При какой температуре {plot.get("element")} '
            f"удлинится на {increase}мм? Ответ выразите в градусах Цельсия."
        )
        answer = round(increase * 10 ** (-3) / (alpha * zero_length))
        if 1 <= answer <= 60:
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
        task = (
            f"Некоторая компания продает свою продукцию по цене \u03C1 = {p} руб. за единицу, переменные затраты "
            f"на производство одной единицы продукции составляют \u03BD = {v} руб., постоянные расходы предприятия "
            f"\u2A0D = {f} руб. в месяц. Месячная операционная прибыль предприятия (в рублях) вычисляется по "
            f"формуле \u03C0(q) = q(\u03C1 - \u03BD) - \u2A0D. Определите месячный объeм производства q "
            f"(единиц продукции), при котором месячная операционная прибыль предприятия будет равна "
            f"{monthly_profit} руб."
        )
        answer = round((f + monthly_profit) / (p - v))
        if 100 <= answer <= 10000:
            break

    return task, answer


if __name__ == "__main__":
    for el in range(1000):
        ic(task_27953())
    # print(task_27954())

