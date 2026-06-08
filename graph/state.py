"""Graph state placeholder.
Holds simple state structures for workflow graphs.
"""


class State:
    def __init__(self, name: str, data: dict | None = None):
        self.name = name
        self.data = data or {}

    def __repr__(self):
        return f"State(name={self.name!r})"
