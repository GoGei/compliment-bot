COMMANDS = {
    'handle_welcome': {
        'description': 'Начать общаться с ботом',
        'decorator_kwargs': {
            'commands': ['start'],
        }
    },
    'handle_compliment': {
        'description': 'Чтобы получить комплимент',
        'decorator_kwargs': {
            'commands': ['compliment'],
        }
    },
    'handle_apologize': {
        'description': 'Чтобы получить извинения',
        'decorator_kwargs': {
            'commands': ['apologize'],
        }
    }
}
