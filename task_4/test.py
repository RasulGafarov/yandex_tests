import pytest
from assistant import get_user_code


class TestMakeDividerOf:
    def test_pre_check_code(self, capsys):
        try:
            from author import make_divider_of
        except SyntaxError:
            assert False, "Найдена синтаксическая ошибка, проверь отступы, запятые и скобки, возможно проблема в них"
        except AttributeError as e:
            assert False, f"Ошибка в атрибутах, проверь все ли с ними в порядке ({e})"
        except ImportError:
            assert False, "Не найдена функцию make_divider_of, возможно вы его удалили или переименовали"
        user_code = get_user_code()
        user_code_list = user_code.split("\n")
        return_list = [line for line in user_code_list if line.count("return")]
        if len(return_list) < 2:
            assert False, "Кажется вы забыли где-то добавить return"
        if return_list[1].count('('):
            assert False, "return функции make_divider_of не должен вызывать функцию, то есть не должно быть скобок"


    @pytest.mark.parametrize("denominator, numerator, expected_value",
                             [
                                 (5, [20, 10, 15.6, 0, -56, 125.56545, 1231234156486],
                                  [4.0, 2.0, 3.12, 0.0, -11.2, 25.11309, 246246831297.2]),
                                 (-8, [16, 45, 15.7, 0, -36, 1545.4568, 465748543564],
                                  [-2.0, -5.625, -1.9625, -0.0, 4.5, -193.1821, -58218567945.5]),
                                 (3.5, [45, 12, 56.0, 0, -9, 4574.155, 5467879789465],
                                  [12.857142857142858, 3.4285714285714284, 16.0, 0.0, -2.5714285714285716, 1306.9014285714286, 1562251368418.5715])
                             ])
    def test_make_divider_of(self, denominator, numerator, expected_value):
        from author import make_divider_of
        testing_div = make_divider_of(denominator)
        for i in range(len(numerator)):
            assert expected_value[i] == testing_div(numerator[i]), \
            f"Функция возвращает не верное значение (числитель: {numerator[i]}, знаменатель: {denominator}, " \
            f"ожидаемый результат: {expected_value[i]}, получен результат{testing_div(numerator[i])}"
