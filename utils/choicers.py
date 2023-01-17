import typing
import random


class Choicer(object):
    def __init__(self, choices: typing.List, with_repeat=True, default_msg='Reached end of choices'):
        self.choices = choices
        self.seen = set()
        self.with_repeat = with_repeat
        self.default_msg = default_msg

    def get_choice(self):
        while True:
            if len(self.seen) == len(self.choices):
                choice = self.default_msg
                if self.with_repeat:
                    self.seen = set()
                break

            choice = random.choice(self.choices)
            if choice not in self.seen:
                self.seen.add(choice)
                break

        return choice
