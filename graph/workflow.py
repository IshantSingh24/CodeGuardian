"""Workflow placeholder.
Defines simple transitions or orchestration helpers.
"""

from .state import State


class Workflow:
    def __init__(self, states: list[State]):
        self.states = states

    def start(self):
        return self.states[0] if self.states else None
