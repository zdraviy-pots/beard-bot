from aiogram.fsm.state import State, StatesGroup

class NotifyState(StatesGroup):
    waiting_for_message = State() 