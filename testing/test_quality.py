import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from agents.quality_agent import quality_agent

diff = """
+ a = 5
+ b = 10
+ c = a + b
"""

result = quality_agent(diff)

print(result)