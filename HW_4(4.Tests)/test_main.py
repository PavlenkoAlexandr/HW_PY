from unittest.mock import patch
import pytest
import main


class TestMain:

    def setup(self):
        pass

    def teardown(self):
        pass

    @pytest.mark.parametrize('number, result', [(main.documents[0]['number'], True), ('', False)])
    def test_check_document_existence(self, number, result):
        assert main.check_document_existance(number) is result

    @pytest.mark.parametrize('my_input, result', [
        (main.documents[0]['number'], (main.documents[0]['name'])),
        ('', None)
    ])
    @patch('builtins.input')
    def test_get_doc_owner_name(self, m_input, my_input, result, ):
        m_input.side_effect = [my_input]
        assert main.get_doc_owner_name() == result

    def test_get_all_doc_owners_names(self):
        assert main.get_all_doc_owners_names() == set([doc['name'] for doc in main.documents])

    def test_remove_doc_from_shelf(self,):
        shelf = list(main.directories.keys())[0]
        number = main.directories[shelf][0]
        main.remove_doc_from_shelf(number)
        assert number not in main.directories[shelf]

    @patch('builtins.input')
    def test_add_new_shelf(self, m_input):
        m_input.side_effect = ['4']
        main.add_new_shelf()
        assert '4' in main.directories.keys()

    @pytest.mark.parametrize('number, shelf', [('1', '1'), ('2', '5')])
    def test_append_doc_to_shelf(self, number, shelf):
        main.append_doc_to_shelf(number, shelf)
        assert number in main.directories[shelf]

    @patch('builtins.input')
    def test_delete_doc(self, m_input):
        number = main.documents[0]['number']
        m_input.side_effect = [number]
        main.delete_doc()
        docs = ([doc['number'] for doc in main.documents])
        assert number not in docs, main.directories.values()

    @patch('builtins.input')
    def test_get_doc_shelf(self, m_input):
        shelf = list(main.directories.keys())[0]
        number = main.directories[shelf][0]
        m_input.side_effect = [number]
        assert main.get_doc_shelf() == shelf

    @pytest.mark.parametrize('number, shelf', [(main.documents[0]['number'], '3'), (main.documents[0]['number'], '5')])
    @patch('builtins.input')
    def test_move_doc_to_shelf(self, m_input, number, shelf):
        m_input.side_effect = [number, shelf]
        main.move_doc_to_shelf()
        dirs = [direct for direct in main.directories if dir != shelf]
        assert number in main.directories[shelf] and number not in dirs

    def test_show_document_info(self):
        doc = {'type': 'type', 'number': 'number', 'name': 'name'}
        assert main.show_document_info(doc) == f'{doc["type"]} "{doc["number"]}" "{doc["name"]}"'

    @patch('builtins.input')
    def test_add_new_doc(self, m_input):
        m_input.side_effect = ['number', 'type', 'name', 'shelf']
        doc = {'type': 'type', 'number': 'number', 'name': 'name'}
        assert main.add_new_doc() == 'shelf' and doc in main.documents and 'number' in main.directories['shelf']
