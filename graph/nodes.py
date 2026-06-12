from graph.state import ReviewState

from agents.security_agent import security_agent
from agents.quality_agent import quality_agent
from agents.composer_agent import composer_agent


def security_node(state: ReviewState):

    result = security_agent(
        state["diff"]
    )

    return {
        "security_result": result
    }


def quality_node(state: ReviewState):

    result = quality_agent(
        state["diff"]
    )

    return {
        "quality_result": result
    }


def composer_node(state: ReviewState):

    review = composer_agent(
        state["security_result"],
        state["quality_result"]
    )

    return {
        "final_review": review
    }
