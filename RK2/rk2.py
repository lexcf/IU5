import unittest
from unittest.mock import patch
from io import StringIO
from operator import itemgetter

class ProgrammingLanguage:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class SyntaticConstruction:
    def __init__(self, id, name, usage_frequency, pl_id):
        self.id = id
        self.name = name
        self.usage_frequency = usage_frequency
        self.pl_id = pl_id

class PlSc:
    def __init__(self, pl_id, sc_id):
        self.pl_id = pl_id
        self.sc_id = sc_id

languages = [
    ProgrammingLanguage(1, 'Java'),
    ProgrammingLanguage(2, 'C++'),
    ProgrammingLanguage(3, 'C#'),
]

constructions = [
    SyntaticConstruction(1, 'Идентификатор', 100, 1),
    SyntaticConstruction(2, 'Константа', 50, 1),
    SyntaticConstruction(3, 'Переменная', 100, 2),
    SyntaticConstruction(4, 'Тип', 80, 3),
    SyntaticConstruction(5, 'Метка', 20, 3),
]

languages_constructions = [
    PlSc(1, 1),
    PlSc(1, 2),
    PlSc(2, 3),
    PlSc(3, 4),
    PlSc(3, 5),
]

def main():
    one_to_many = [(c.name, c.usage_frequency, l.name)
                   for c in constructions
                   for l in languages
                   if c.pl_id == l.id]

    many_to_many_temp = [(l.name, lc.pl_id, lc.sc_id)
                         for l in languages
                         for lc in languages_constructions
                         if l.id == lc.pl_id]

    many_to_many = [(c.name, c.usage_frequency, language_name)
                    for language_name, language_id, construction_id in many_to_many_temp
                    for c in constructions
                    if c.id == construction_id]

    print('Задание Б1')
    res_11 = sorted(one_to_many, key=itemgetter(0))
    print(res_11)

    print('\nЗадание Б2')
    language_construction_count = {}

    for l in languages:
        language_name = l.name
        constructions_count = sum(1 for c in one_to_many if c[2] == language_name)
        language_construction_count[language_name] = constructions_count

    sorted_language_construction_count = sorted(language_construction_count.items(), key=lambda x: x[1], reverse=True)

    for language, count in sorted_language_construction_count:
        print(f'{language}: {count} конструкций')

    print('\nЗадание Б3')
    filtered_many_to_many = [(c_name, language_name) for c_name, _, language_name in many_to_many if c_name.endswith('а')]

    for syntax, language in filtered_many_to_many:
        print(f'{syntax} ({language})')



class TestProgrammingLanguage(unittest.TestCase):
    def test_programming_language_attributes(self):
        lang = ProgrammingLanguage(1, 'Python')
        self.assertEqual(lang.id, 1)
        self.assertEqual(lang.name, 'Python')

class TestSyntaticConstruction(unittest.TestCase):
    def test_syntatic_construction_attributes(self):
        construction = SyntaticConstruction(1, 'Variable', 80, 2)
        self.assertEqual(construction.id, 1)
        self.assertEqual(construction.name, 'Variable')
        self.assertEqual(construction.usage_frequency, 80)
        self.assertEqual(construction.pl_id, 2)

class TestPlSc(unittest.TestCase):
    def test_pl_sc_attributes(self):
        pl_sc = PlSc(1, 3)
        self.assertEqual(pl_sc.pl_id, 1)
        self.assertEqual(pl_sc.sc_id, 3)

class TestMainFunction(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_task_B1(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            main_output = mock_stdout.getvalue().strip()

        self.assertTrue("Задание Б1" in main_output)
        self.assertTrue("Идентификатор" in main_output)
        self.assertTrue("Константа" in main_output)
        self.assertTrue("Переменная" in main_output)
        self.assertTrue("Тип" in main_output)
        self.assertTrue("Метка" in main_output)

    def test_task_B2(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            main_output = mock_stdout.getvalue().strip()

        self.assertTrue("Задание Б2" in main_output)
        self.assertTrue("Java: " in main_output)
        self.assertTrue("C#: " in main_output)
        self.assertTrue("C++: " in main_output)

    def test_task_B3(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            main_output = mock_stdout.getvalue().strip()

        expected_output = [
            'Константа (Java)',
            'Метка (C#)'
        ]

        for output in expected_output:
            self.assertIn(output, main_output)


if __name__ == '__main__':
    unittest.main()
