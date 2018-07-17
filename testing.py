import unittest
import unittest.mock

import worklog
from worklog import Entry
import add_entry
import search


class TestWorkLog(unittest.TestCase):

    def setUp(self):
        self.entries = worklog.Entry.select().order_by(Entry.timestamp.desc())

    def test_get_name(self):
        options = ["my_name"]
        with unittest.mock.patch('builtins.input', side_effect=options):
            self.assertEqual(add_entry.get_name(), "my_name")

    def test_get_task(self):
        options = ["my_task"]
        with unittest.mock.patch('builtins.input', side_effect=options):
            self.assertEqual(add_entry.get_task(), "my_task")

    def test_get_time(self):
        options = [10]
        with unittest.mock.patch('builtins.input', side_effect=options):
            self.assertEqual(add_entry.get_time(), 10)

    def test_get_notes(self):
        options = ["my_notes"]
        with unittest.mock.patch('builtins.input', side_effect=options):
            self.assertEqual(add_entry.get_notes(), "my_notes")

    def test_employee_search(self):
        options = ["user name"]
        with unittest.mock.patch('builtins.input', side_effect=options):
            self.assertEqual(search.employee_search(self.entries), "user name")

    def test_date_search(self):
        options = ["20/06/2018"]
        with unittest.mock.patch('builtins.input', side_effect=options):
            self.assertEqual(search.date_search(self.entries), "20/06/2018")

    def test_time_search(self):
        options = [35]
        with unittest.mock.patch('builtins.input', side_effect=options):
            self.assertEqual(search.time_search(self.entries), 35)

    def test_search_term(self):
        options = ["my notes"]
        with unittest.mock.patch('builtins.input', side_effect=options):
            self.assertEqual(search.search_term(self.entries), "my notes")


if __name__ == '__main__':
    unittest.main()
