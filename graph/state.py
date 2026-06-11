from typing import TypedDict

from agents.security_agent import SecurityReview
from agents.quality_agent import QualityReview


class ReviewState(TypedDict):

    diff: str

    security_result: SecurityReview | None

    quality_result: QualityReview | None

    final_review: str