import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from agents.security_agent import security_agent

diff = """
+ API_KEY = "123456"
+ PASSWORD = "admin123"
"""

result = security_agent(diff)

print(result)

print(result.severity)

for issue in result.issues:
    print(issue.type)
    print(issue.description)