import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from graph.workflow import graph

state = {
    "diff": """
+ API_KEY = "123456"
+ password = "admin"
+ a = 5
+ b = 10
"""
}

result = graph.invoke(
    state
)

print(result["final_review"])