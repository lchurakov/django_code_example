from django.dispatch import Signal

user_view_signal = Signal()


def user_view_signal_handler(sender, **kwargs):
    print(f'{sender}, kwgs:{kwargs}')


user_view_signal.connect(user_view_signal_handler)
