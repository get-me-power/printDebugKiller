import unittest
import sys
sys.path.append('../')
import main


class Test(unittest.TestCase):

    def source_has_no_print(self):
        input_source = """
        """

        self.assertEqual([], main.print_collector(input_source))


if __name__ == "__main__":
    unittest.main()
