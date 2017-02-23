
__author__ = "Maxwell Goldbas"

"""
This is the main structure of the untapt data challenge
2017-02-23
"""

TURN_RIGHT_TUPLE = (('N', 'E'), ('E', 'S'), ('S', 'W'), ('W', 'N'))
TURN_LEFT_TUPLE = tuple(((t[1], t[0]) for t in TURN_RIGHT_TUPLE))
TURN_RIGHT = dict(TURN_RIGHT_TUPLE)
TURN_LEFT = dict(TURN_LEFT_TUPLE)

DEBUG = True


class Board(object):
    """
    use this class to keep track of board size and number/position of robots
    """
    def __init__(self, x_max, y_max):
        self.x_max, self.y_max = x_max, y_max
        self.robots = []

    def run_robot(self, x_init, y_init, r_init, command_string ):
        """
        initialize robot and cycle thru command string
        :param x_init:
        :param y_init:
        :param r_init:
        :param command_string:
        :return: Robot object
        """
        robot = Robot(x_init, y_init, r_init)
        for command in command_string:
            robot.run_command(command)
            self.check_robot(robot)
        self.robots.append(robot)
        return robot.x, robot.y, robot.r


    def check_robot(self, robot):
        """
        check to see that robot is not outside parameter
        :return:
        """
        if DEBUG:
            position_string = "({}, {})".format(robot.x, robot.y)
            print(position_string)
        if robot.x > self.x_max:
            raise Warning('Robot Above Horizontal Bounds')
        elif robot.x < 0:
            raise Warning('Robot Below Horizontal Bounds')
        elif robot.y > self.y_max:
            raise Warning('Robot Above Vertical Bounds')
        elif robot.y < 0:
            raise Warning('Robot Below Vertical Bounds')
        pass

    def output(self):
        """
        output the location
        :return:
        """
        for robot in self.robots:
            pass

class Robot(object):
    """
    create robot and have it execute commands
    """

    def __init__(self, x_init, y_init, r_init):
        self.x = x_init
        self.y = y_init
        self.r = r_init
        self.total_distance = 0


    def run_command(self, command):
        """
        have it turn or move forward
        :param command:
        :return:
        """
        if command == "M":
            if DEBUG:
                print('Movin...')
            self.move()
            self.total_distance += 1
        elif command == "L":
            if DEBUG:
                print('Swinging a Louie...')
            self.turn_left()
        elif command == "R:":
            if DEBUG:
                print('Hard to Starboard')
            self.turn_right()
        else:
            raise Exception('Commands must be L, R, or M')


    def move(self):
        """
        understand orientation, in that direction move 1
        :return:
        """
        if self.r == 'N':
            self.y += 1
        elif self.r == 'E':
            self.x += 1
        elif self.r == 'S':
            self.y -= 1
        elif self.r == 'W':
            self.x -= 1
        else:
            print('Error in move function')

    def turn_left(self):
        self.r = TURN_LEFT[self.r]

    def turn_right(self):
        self.r = TURN_RIGHT[self.r]





