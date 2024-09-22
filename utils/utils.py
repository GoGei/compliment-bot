from datetime import datetime

MAX_APOLOGIES_PER_DAY = 5
MAX_COMPLIMENTS_PER_DAY = 10
user_usage = {}


def get_user_usage(user_id):
    current_date = datetime.now().date()
    if user_id not in user_usage or user_usage[user_id]['last_date'] != current_date:
        user_usage[user_id] = {'apologies': 0, 'compliments': 0, 'last_date': current_date, 'seen': []}
    return user_usage[user_id]


def reset_user_limits():
    global user_usage
    current_date = datetime.now().date()
    for user_id in list(user_usage.keys()):
        if user_usage[user_id]['last_date'] != current_date:
            user_usage[user_id] = {'apologies': 0, 'compliments': 0, 'last_date': current_date, 'seen': []}
