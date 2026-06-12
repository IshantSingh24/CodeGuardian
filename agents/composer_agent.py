from agents.security_agent import SecurityReview
from agents.quality_agent import QualityReview


def composer_agent(
    security: SecurityReview,
    quality: QualityReview
):

    review = f"""
# Code Review

## Security

Severity: {security.severity}

Summary:
{security.summary}

## Quality

Score: {quality.score}/10

Summary:
{quality.summary}
"""

    return review