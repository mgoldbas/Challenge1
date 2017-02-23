import unittest
from main import Board, Robot

class IngestTestCases(unittest.TestCase):
    filename = 'test_cases.txt'

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
            {'input':["3 3 E","MMRMMRMRRM"], 'output':"5 1 E"}
        ]



    def test_robots(self):
        count = 0
        for case in self.cases:
            print('ROBOT:' +str(count))
            count += 1
            input = case['input'][0]
            x, y, r = self.parse_to_position(input)
            control_output = case['output']
            x_final, y_final, r_final = self.board.run_robot(x, y, r, case['input'][1])
            test_output = ' '.join([str(x_final), str(y_final), r_final])
            self.assertEqual(test_output, control_output)



    def parse_to_position(self, string_parse):
        x, y, r = tuple(string_parse.split())
        return int(x), int(y), r

if __name__ == '__main__':
    unittest.main()





