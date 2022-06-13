import pytest
from assistant import get_user_code


class TestContact:
    @pytest.mark.parametrize("print_line_1, print_line_2",
                             [("Михаил Булгаков — адрес: Россия, Москва, Большая Пироговская,"
                               " дом 35б, кв. 6, телефон: 2-03-27, день рождения: 15.05.1891",
                               "Владимир Маяковский — адрес: Россия, Москва, Лубянский проезд, "
                               "д. 3, кв. 12, телефон: 73-88, день рождения: 19.07.1893")])
    def test_pre_check_code(self, capsys, print_line_1, print_line_2):
        try:
            from author import Contact
        except SyntaxError:
            assert False, "Найдена синтаксическая ошибка, проверь отступы, запятые и скобки, возможно проблема в них"
        except AttributeError as e:
            assert False, f"Ошибка в атрибутах, проверь все ли с ними в порядке ({e})"
        except ImportError:
            assert False, "Не найден класс Contact, возможно вы его удалили или переименовали"
        if "show_contact" not in Contact.__dict__:
            assert False, "У класса Contact не найден метод show_contact"
        user_code = get_user_code()
        if user_code.count("def print_contact"):
            assert False, "Кажется вы забыли удалить функцию print_contact"
        outer, err = capsys.readouterr()
        outer_list = outer.split("\n")
        if print_line_1 not in outer_list and print_line_2 not in outer_list():
            assert False, "Похоже вы не вызвали метод show_contact для объектов mike и vlad"
        if len(outer_list) != 5:
            assert False, "Вы вывели слишком много строк, в show_contact должен быть только один print"

    @pytest.mark.parametrize("name, phone, birthday, address, expected_result", [
        ("Саша", "+79991320798", "15.05.1895", "Россия, Уфа, Большая Пироговская, дом 35б, кв. 6",
         "Саша — адрес: Россия, Уфа, Большая Пироговская, дом 35б, кв. 6,"
         " телефон: +79991320798, день рождения: 15.05.1895"),
        ("Лена", "+79991547898", "13.05.2000", "Россия, Москва, Донецкая, дом 13, кв. 4",
         "Лена — адрес: Россия, Москва, Донецкая, дом 13, кв. 4, телефон: +79991547898, день рождения: 13.05.2000"),
        ("Настя", "+79865452112", "14.03.1986", "Россия, Казань, Донецкая, дом 3",
         "Настя — адрес: Россия, Казань, Донецкая, дом 3, телефон: +79865452112, день рождения: 14.03.1986")
    ])
    def test_show_contact(self, capsys, name, phone, birthday, address, expected_result):
        try:
            from author import Contact
        except SyntaxError:
            assert False, "Найдена синтаксическая ошибка, проверь отступы, запятые и скобки, возможно проблема в них"
        except AttributeError as e:
            assert False,  f"Ошибка в атрибутах, проверь все ли с ними в порядке ({e})"
        except ImportError:
            assert False, "Не найден метод Contact, возможно вы его удалили или переименовали"
        try:
            contact = Contact(name, phone, birthday, address)
        except TypeError:
            assert False, "Не удается создать объект класса Contact, ошибка в параметрах инициализации"
        if "show_contact" not in Contact.__dict__:
            assert False, "У метода Contact не найдена функция show_contact"
        capsys.readouterr()
        try:
            contact.show_contact()
        except TypeError:
            assert False
        out, err = capsys.readouterr()
        output_list = out.split("\n")
        assert output_list[0] == expected_result, f"Метод show_contact вывел '{output_list[1]}'," \
                                                  f"  а должен был '{expected_result}'"
