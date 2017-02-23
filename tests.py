import unittest
from main import Board, Robot

class IngestTestCases(unittest.TestCase):
    _filename = 'test_cases.txt'

    def setUp(self):
        """
        initialize board
        :return:
        """
        self.set_variables()
        self.board = Board(self.x_max, self.y_max)

    def set_variables(self):
        self.x_max = 5
        self.y_max = 5
        self.cases = [
            {'input':["1 2 N","LMLMLMLMM"], 'output':"1 3 N"},
            {'input':["3 3 E","MMRMMRMRRM"], 'output':"5 1 E"},
            {'input':["1 1 S","RR"], 'output':"1 1 N"}
        ]

    def test_1(self):
        self.equal_test(self.cases[0])

    def test_2(self):
        self.equal_test(self.cases[1])

    def test_3(self):
        self.equal_test(self.cases[2])

    def test_4(self):
        case = self.cases[2]
        case['output'] = "2 2 R"
        self.unequal_test(case)

    def equal_test(self, case):
        test_output, control_output = self.functional_test(case)
        self.assertEqual(test_output, control_output)

    def unequal_test(self, case):
        test_output, control_output = self.functional_test(case)
        self.assertNotEquals(test_output, control_output)

    def functional_test(self, case):
        input = case['input'][0]
        x, y, r = self.parse_to_position(input)
        control_output = case['output']
        x_final, y_final, r_final = self.board.run_robot(x, y, r, case['input'][1])
        test_output = ' '.join([str(x_final), str(y_final), r_final])
        self.assertIsInstance(control_output, str)
        return test_output, control_output

    def parse_to_position(self, string_parse):
        x, y, r = tuple(string_parse.split())
        return int(x), int(y), r

if __name__ == '__main__':
    unittest.main()





