import typing
import random
from .utils import get_user_usage


class Choicer(object):
    def __init__(self,
                 choices: typing.List,
                 stats_key: str,
                 day_limit: int,
                 with_repeat: bool = True,
                 default_msg: str = 'Reached end of choices',
                 limited_msg: str = 'Reached limited number of choices',
                 ):
        self.choices = choices
        self.with_repeat = with_repeat
        self.default_msg = default_msg
        self.limited_msg = limited_msg
        self.stats_key = stats_key
        self.day_limit = day_limit

    def get_random_choice(self, seen: list) -> str:
        difference = set(self.choices) - set(seen)
        choice = random.choice(list(difference))
        if choice not in seen:
            seen.append(choice)
        return choice

    def get_choice(self, user_id: str) -> str:
        while True:
            data = get_user_usage(user_id)
            seen: list = data['seen']
            if len(seen) == len(self.choices):
                if self.with_repeat:
                    data['seen'] = []
                    seen = []
                    choice = self.get_random_choice(seen)
                    return choice
                else:
                    return self.default_msg

            return self.get_random_choice(seen)

    def get_limited_choice(self, user_id: str) -> str:
        user_stats = get_user_usage(user_id)

        if user_stats[self.stats_key] < self.day_limit:
            choice = self.get_choice(user_id)
            user_stats[self.stats_key] += 1
        else:
            choice = self.limited_msg

        return choice
