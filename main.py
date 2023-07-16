from driver import HibotDriver
from action import HandAction

hibot = HibotDriver('COM3', 1152000)

hibot.do_action(HandAction.allStepToZero)