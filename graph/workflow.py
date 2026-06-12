from langgraph.graph import START
from langgraph.graph import END
from langgraph.graph import StateGraph

from graph.state import ReviewState

from graph.nodes import (
    security_node,
    quality_node,
    composer_node
)

builder = StateGraph(
    ReviewState
)

builder.add_node(
    "security",
    security_node
)

builder.add_node(
    "quality",
    quality_node
)

builder.add_node(
    "composer",
    composer_node
)

builder.add_edge(
    START,
    "security"
)

builder.add_edge(
    START,
    "quality"
)

builder.add_edge(
    "security",
    "composer"
)

builder.add_edge(
    "quality",
    "composer"
)

builder.add_edge(
    "composer",
    END
)

graph = builder.compile()