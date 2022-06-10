import pytest
from assistant import get_user_code


class TestCacheArgs:
    def test_pre_check_code(self):
        try:
            from author import long_heavy, cache_args
        except SyntaxError:
            assert False, "Найдена синтаксическая ошибка, проверь отступы, запятые и скобки, возможно проблема в них"
        except AttributeError as e:
            assert False, f"Ошибка в атрибутах, проверь все ли с ними в порядке ({e})"
        except ImportError:
            assert False, "Не найдена функция cache_args или long_heavy, возможно вы её удалили или переименовали"
        user_code = get_user_code()
        if not user_code.find("@time_check"):
            assert False, "Кто-то удалил декоратор @time_check"
        elif not user_code.find("@cache_args"):
            assert False, "Кто-то удалил декоратор @cache_args"

    @pytest.mark.parametrize("input, output_time, output_value",
                             [
                                 ((8, 6, 9, 6), (1, 1, 1, 0), (16, 12, 18, 12))
                              ])
    def test_cache_args(self, capsys, input, output_time, output_value):
        from author import long_heavy
        capsys.readouterr()
        for i in range(len(input)):
            value = long_heavy(input[i])
            out, err = capsys.readouterr()
            out_list = out.split("\n")
            if len(out_list) < 2:
                assert False, "Вы ничего не выводите"
            elif len(out_list) > 2:
                assert False, "Вы выводите слишком много строк"
            elif value != output_value[i]:
                assert False, f"Похоже вы сломали функцию long_heavy (ожидается: '{output_value[i]}'," \
                              f" получено: '{out_list[1]}'"
            elif out_list[0] != f"Время выполнения функции: {str(output_time[i])}.0 с.":
                test = f"Время выполнения функции: {str(output_time[i])}.0 с."
                assert False, f"Не правильно возвращается время действия функции"
