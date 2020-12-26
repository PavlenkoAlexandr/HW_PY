import pytest

from main import is_balanced

TESTS_CASES = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}', '}{}', '{{[(])]}}', '[[{())}]']


class TestMain:

    def setup(self):
        pass

    def teardown(self):
        pass

    @pytest.mark.parametrize('case', TESTS_CASES[0:3])
    def test_positive_is_balanced(self, case):
        assert is_balanced(case)

    @pytest.mark.parametrize('case', TESTS_CASES[3:])
    def test_negative_is_balanced(self, case):
        assert not is_balanced(case)