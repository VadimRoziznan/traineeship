from difflib import SequenceMatcher
import pymorphy2
import numpy as np
from sympy import latex


def choosing_declension_form(word: (str, list), case: str) -> str:
    """
    Функция подбирает правильную форму склонения переданного слова, см. https://opencorpora.org/dict.php?act=gram,
    по умолчанию слово пропишется в родительном падеже
    """

    morph = pymorphy2.MorphAnalyzer()
    if len(word.split()) == 1:
        return morph.parse(word)[0].inflect({case}).word
    else:
        list_morphy = []
        for i in word.split():
            list_morphy.append(morph.parse(i)[0].inflect({case}).word)
        return " ".join(list_morphy)


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


def task_27953():
    """
    Задача №27953 с портала https://ege.sdamgia.ru/problem?id=27953
    """

    # Температурные коэффициенты линейного расширения.
    # Примечание: источниками справочных данных являются публикации в Интернете, поэтому они не могут считаться
    # «официальными» и «абсолютно точными».
    list_thermal_expansion_coefficient = {
        "ABS (акрилонитрил-бутадиен-стирол) термопласт": 7.38,
        "ABS - стекло, армированное волокнами": 3.04,
        "Акриловый материал, прессованный": 23.4,
        "Алмаз": 0.11,
        "Алмаз технический": 0.12,
        "Алюминий": 2.22,
        "Ацеталь": 10.65,
        "Ацеталь , армированный стекловолокном": 3.94,
        "Ацетат целлюлозы (CA)": 13.0,
        "Ацетат бутират целлюлозы (CAB)": 2.52,
        "Барий": 2.06,
        "Бериллий": 1.15,
        "Бериллиево-медный сплав (Cu 75, Be 25)": 1.67,
        "Бетон": 1.45,
        "Бетонные структуры": 0.98,
        "Бронза": 1.8,
        "Ванадий": 0.8,
        "Висмут": 1.3,
        "Вольфрам": 0.43,
        "Гадолиний": 0.9,
        "Гафний": 0.59,
        "Германий": 0.61,
        "Гольмий": 1.12,
        "Гранит": 0.79,
        "Графит, чистый": 0.79,
        "Диспрозий": 0.99,
        "Древесина, пихта, ель": 0.37,
        "Древесина дуба, параллельно волокнам": 0.49,
        "Древесина дуба , перпендикулярно волокнам": 0.54,
        "Древесина, сосна": 0.5,
        "Европий": 3.5,
        "Железо, чистое": 1.2,
        "Железо, литое": 1.04,
        "Железо, кованое": 1.13,
        "Золото": 1.42,
        "Известняк": 0.8,
        "Инвар (сплав железа с никелем)": 0.15,
        "Инконель (сплав)": 1.26,
        "Иридий": 0.64,
        "Иттербий": 2.63,
        "Иттрий": 1.06,
        "Кадмий": 3,
        "Калий": 8.3,
        "Кальций": 2.23,
        "Каменная кладка": {"min_length": 0.47, "max_length": 0.9},
        "Каучук, твердый": 7.7,
        "Кварц": {"min_length": 0.077, "max_length": 0.09},
        "Керамическая плитка (черепица)": 0.59,
        "Кирпич": 0.55,
        "Кобальт": 1.2,
        "Констанан (сплав)": 1.88,
        "Корунд, спеченный": 0.65,
        "Кремний": 0.51,
        "Лантан": 1.21,
        "Латунь": 1.87,
        "Лед": 5.1,
        "Литий": 4.6,
        "Литая стальная решетка": 1.08,
        "Лютеций": 0.99,
        "Литой лист из акрилового пластика": 8.1,
        "Магний": 2.5,
        "Марганец": 2.2,
        "Медноникелевый сплав 30%": 1.62,
        "Медь": 1.66,
        "Молибден": 0.5,
        "Монель-металл (никелево-медный сплав)": 1.35,
        "Мрамор": {"min_length": 0.55, "max_length": 1.41},
        "Мыльный камень (стеатит)": 0.85,
        "Мышьяк": 0.47,
        "Натрий": 7,
        "Нейлон, универсальный": 7.2,
        "Нейлон, Тип 11 (Type 11)": 10,
        "Нейлон, Тип 12 (Type 12)": 8.05,
        "Нейлон литой , Тип 6 (Type 6)": 8.5,
        "Нейлон, Тип 6/6 (Type 6/6), формовочный состав": 8,
        "Неодим": 0.96,
        "Никель": 1.30,
        "Ниобий (Columbium)": 0.7,
        "Нитрат целлюлозы (CN)": 10,
        "Окись алюминия": 0.54,
        "Олово": 2.34,
        "Осмий": 0.5,
        "Палладий": 1.18,
        "Песчаник": 1.16,
        "Платина": 0.9,
        "Плутоний": 5.4,
        "Полиалломер": 9.15,
        "Полиамид (PA)": 11,
        "Поливинилхлорид (PVC)": 5.04,
        "Поливинилденфторид (PVDF)": 12.78,
        "Поликарбонат (PC)": 7.02,
        "Поликарбонат - армированный стекловолокном": 2.15,
        "Полипропилен - армированный стекловолокном": 3.2,
        "Полистирол (PS)": 7,
        "Полисульфон (PSO)": 5.58,
        "Полиуретан (PUR), жесткий": 5.76,
        "Полифенилен - армированный стекловолокном": 3.58,
        "Полифенилен (PP), ненасыщенный": 9.05,
        "Полиэстер": 12.35,
        "Полиэстер, армированный стекловолокном": 2.5,
        "Полиэтилен (PE)": 20,
        "Полиэтилен - терефталий (PET)": 5.94,
        "Празеодимий": 0.67,
        "Припой 50 - 50": 2.4,
        "Прометий": 1.1,
        "Рений": 0.67,
        "Родий": 0.8,
        "Рутений": 0.91,
        "Самарий": 1.27,
        "Свинец": 2.8,
        "Свинцово-оловянный сплав": 1.16,
        "Селен": 0.38,
        "Серебро": 1.95,
        "Скандий": 1.02,
        "Слюда": 0.3,
        "Сплав твердый (Hard alloy) K20": 0.6,
        "Сплав хастелой (Hastelloy) C": 1.13,
        "Сталь": 1.3,
        "Сталь нержавеющая аустенитная (304)": 1.73,
        "Сталь нержавеющая аустенитная (310)": 1.44,
        "Сталь нержавеющая аустенитная (316)": 1.6,
        "Сталь нержавеющая ферритная (410)": 0.99,
        "Стекло витринное (зеркальное, листовое)": 0.9,
        "Стекло пирекс, пирекс": 0.4,
        "Стекло тугоплавкое": 0.59,
        "Строительный (известковый) раствор": {"min_length": 0.73, "max_length": 1.35},
        "Стронций": 2.25,
        "Сурьма": 1.04,
        "Таллий": 2.99,
        "Тантал": 0.65,
        "Теллур": 3.69,
        "Тербий": 1.03,
        "Титан": 0.86,
        "Торий": 1.2,
        "Тулий": 1.33,
        "Уран": 1.39,
        "Фарфор": {"min_length": 0.36, "max_length": 0.45},
        "Фенольно-альдегидный полимер без добавок": 8,
        "Фторэтилен пропилен (FEP)": 13.5,
        "Хлорированный поливинилхлорид (CPVC)": 6.66,
        "Хром": 0.62,
        "Цемент": 1,
        "Церий": 0.52,
        "Цинк": 2.97,
        "Цирконий": 0.57,
        "Шифер": 1.04,
        "Штукатурка": 1.64,
        "Эбонит": 7.66,
        "Эпоксидная смола , литая резина и незаполненные продукты из них": 5.5,
        "Эрбий": 1.22,
        "Этилен винилацетат (EVA)": 18,
        "Этилен и этилакрилат (EEA)": 20.5,
        "Эфир виниловый": {"min_length": 1.6, "max_length": 2.2},
        "test": (432, 500, 1),
    }

    # Сюжеты задачи
    values_list = (
        {
            "element": "рельс",
            "size_list": np.arange(1, 25, 1),
            "thermal_expansion_coefficient": list_thermal_expansion_coefficient.get(
                "Сталь"
            ),
            "test_coefficient": {
                "starting_value": 1.3,
                "final_value": 2,
                "step_value": 1,
            },
        },
        {
            "element": "линейка",
            "size_list": [0.15, 0.3, 0.5, 1, 1.5, 2, 3],
            "thermal_expansion_coefficient": list_thermal_expansion_coefficient.get(
                "Сталь"
            ),
            "test_coefficient": {
                "starting_value": 1.3,
                "final_value": 2,
                "step_value": 1,
            },
        },
        {
            "element": "рулетка",
            "size_list": [3, 5, 8, 10, 15, 20, 30, 50, 60],
            "thermal_expansion_coefficient": list_thermal_expansion_coefficient.get(
                "Сталь"
            ),
            "test_coefficient": {
                "starting_value": 1.3,
                "final_value": 2,
                "step_value": 1,
            },
        },
        {
            "element": "медный стержень",
            "size_list": np.arange(1, 3.5, 0.5),
            "thermal_expansion_coefficient": list_thermal_expansion_coefficient.get(
                "Медь"
            ),
            "test_coefficient": {
                "starting_value": 1.66,
                "final_value": 2,
                "step_value": 1,
            },
        },
        {
            "element": "алюминиевый потолочный карниз",
            "size_list": np.arange(1.4, 5, 0.2),
            "thermal_expansion_coefficient": list_thermal_expansion_coefficient.get(
                "Алюминий"
            ),
            "test_coefficient": {
                "starting_value": 2.22,
                "final_value": 3,
                "step_value": 1,
            },
        },
        {
            "element": "витринное стекло",
            "size_list": np.arange(1, 4.1, 0.1),
            "thermal_expansion_coefficient": list_thermal_expansion_coefficient.get(
                "Стекло витринное (зеркальное, листовое)"
            ),
            "test_coefficient": {
                "starting_value": 0.9,
                "final_value": 1,
                "step_value": 1,
            },
        },
        {
            "element": "серебряная цепочка",
            "size_list": np.arange(0.35, 0.75, 0.05),
            "thermal_expansion_coefficient": list_thermal_expansion_coefficient.get(
                "Серебро"
            ),
            "test_coefficient": {
                "starting_value": 1.92,
                "final_value": 2,
                "step_value": 1,
            },
        },
        {
            "element": "упаковочная пленка",
            "size_list": np.arange(1, 10.1, 0.1),
            "thermal_expansion_coefficient": list_thermal_expansion_coefficient.get(
                "Полиэтилен (PE)"
            ),
            "test_coefficient": {
                "starting_value": 20,
                "final_value": 21,
                "step_value": 1,
            },
        },
        {
            "element": "бетонная стена",
            "size_list": np.arange(1, 3.1, 0.1),
            "thermal_expansion_coefficient": list_thermal_expansion_coefficient.get(
                "Бетон"
            ),
            "test_coefficient": {
                "starting_value": 1.45,
                "final_value": 2,
                "step_value": 1,
            },
        },
        {
            "element": "медная проволока",
            "size_list": np.arange(1, 101, 0.5),
            "thermal_expansion_coefficient": list_thermal_expansion_coefficient.get(
                "Медь"
            ),
            "test_coefficient": {
                "starting_value": 1.66,
                "final_value": 2,
                "step_value": 1,
            },
        },
        {
            "element": "железный мост",
            "size_list": np.arange(18.6, 32.6, 0.1),
            "thermal_expansion_coefficient": list_thermal_expansion_coefficient.get(
                "Железо, литое"
            ),
            "test_coefficient": {
                "starting_value": 1.04,
                "final_value": 2,
                "step_value": 1,
            },
        },
        {
            "element": "золотая цепочка",
            "size_list": np.arange(0.35, 0.75, 0.05),
            "thermal_expansion_coefficient": list_thermal_expansion_coefficient.get(
                "Золото"
            ),
            "test_coefficient": {
                "starting_value": 1.42,
                "final_value": 2,
                "step_value": 1,
            },
        },
        {
            "element": "стекло армированное",
            "size_list": np.arange(1, 3.31, 0.05),
            "thermal_expansion_coefficient": list_thermal_expansion_coefficient.get(
                "ABS - стекло, армированное волокнами"
            ),
            "test_coefficient": {
                "starting_value": 3.04,
                "final_value": 4,
                "step_value": 1,
            },
        },
        {
            "element": "самолёт",
            "size_list": np.arange(5, 31, 1),
            "thermal_expansion_coefficient": list_thermal_expansion_coefficient.get(
                "Алюминий"
            ),
            "test_coefficient": {
                "starting_value": 2.22,
                "final_value": 3,
                "step_value": 1,
            },
        },
    )

    # print(np.random.choice([20, 4, 6]))
    t = values_list[-1].get("test_coefficient")
    # k = np.random.choice(np.array(t))
    # print(t)
    # print(np.arange(20, 1, 1))

    # Случайным образом получаем сюжет задачи
    data = np.random.choice(values_list)

    test = round(
        np.random.choice(
            np.arange(
                data.get("test_coefficient").get("starting_value"),
                data.get("test_coefficient").get("final_value"),
                data.get("test_coefficient").get("step_value"),
            )
        ),
        2,
    )

    print(data.get("element"), test)

    # Получаем температурный коэффициент линейного расширения
    coefficient = data.get("thermal_expansion_coefficient")

    while True:
        if isinstance(coefficient, dict):
            coefficient = round(
                np.random.uniform(
                    coefficient.get("min_length"), coefficient.get("max_length")
                ),
                2,
            )

        zero_length = round(np.random.choice(data.get("size_list")), 2)
        alpha = coefficient * 10 ** (-5)
        increase = round(np.random.uniform(0.1, 10), 1)
        task = (
            f"При температуре "
            + "\(0^{\circ}C\)"
            + f' {data.get("element")} имеет длину '
            + r"\(l_{\circ}="
            + latex(zero_length)
            + r"\)"
            + f"м. При возрастании температуры происходит тепловое расширение "
            f'{choosing_declension_form(data.get("element"), case="gent")}, '
            f'и {get_modified_pronoun(word=data.get("element").split()[-1], сase="gen2", pronoun_masc="он", pronoun_femn="она", pronoun_neut="оно")} длина, выраженная в '
            f"метрах, меняется по закону "
            + r"\(l(t^{\circ})=l_0(1+\alpha{\cdot}t^{\circ})\),"
            + " где "
            + r"\(\alpha="
            + latex(coefficient)
            + "{\cdot}10^{-5}(^{\circ}C^{-1})"
            + r"\)"
            + " — коэффициент теплового расширения, "
            + "\(t^{\circ}\)"
            + f' — температура (в градусах Цельсия). При какой температуре {data.get("element")} '
            f"удлинится на {increase}мм? Ответ выразите в градусах Цельсия."
        )
        answer = round(increase * 10 ** (-3) / (alpha * zero_length))
        if 1 <= answer <= 60:
            break

    def checking_plot(name: str, checklist: list, correction_percentage: int) -> list:
        """
        Функция возвращает отчет в котором указывается номер элемента и в каком процентном соотношении совпадает
        строка переданная в name с элементом каждого сценария, в функции есть настраиваемый параметр
        correction_percentage, при необходимости измените процент коррекции.
        """
        report = []

        for index, plot in enumerate(checklist):
            matcher = round(
                SequenceMatcher(None, name.lower(), plot.get("element")).ratio() * 100
            )

            if matcher > correction_percentage:
                report.append(f"Элемент с номером {index} имеет совпадение {matcher}")

        return report

    # При необходимости проверить сюжеты на вхождение имени раскомментировать код, измените значение name на необходимый,
    # при необходимости измените процент коррекции.
    # pprint(checking_plot(name='медные Стержни', checklist=values_list, correction_percentage=50))

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

    print(task_27953())
    # print(task_27954())
