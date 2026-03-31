"""Graph creation and analytics."""

from __future__ import annotations

import networkx as nx
import pandas as pd

from .data import get_node_attrs


def build_graph(
    dataframe: pd.DataFrame,
    metadata: dict[str, dict[str, str]],
) -> nx.DiGraph:
    """Build directed graph with normalized node attributes."""
    graph = nx.DiGraph()

    for _, row in dataframe.iterrows():
        source = row["Source"]
        target = row["Target"]
        relation = row["Relationship"]

        source_attrs = get_node_attrs(source, metadata)
        target_attrs = get_node_attrs(target, metadata)

        graph.add_node(source, type=source_attrs["type"], side=source_attrs["side"])
        graph.add_node(target, type=target_attrs["type"], side=target_attrs["side"])
        graph.add_edge(source, target, relationship=relation)

    return graph


def compute_summary_metrics(graph: nx.DiGraph) -> dict[str, int]:
    """Compute top-level metrics from currently visible graph."""
    return {
        "total_nodes": graph.number_of_nodes(),
        "total_edges": graph.number_of_edges(),
        "iran_heroes": sum(
            1
            for _, attrs in graph.nodes(data=True)
            if attrs.get("type") == "Шахс" and attrs.get("side") == "Эрон"
        ),
        "turan_heroes": sum(
            1
            for _, attrs in graph.nodes(data=True)
            if attrs.get("type") == "Шахс" and attrs.get("side") == "Турон"
        ),
        "places": sum(
            1 for _, attrs in graph.nodes(data=True) if attrs.get("type") == "Макон"
        ),
        "objects": sum(
            1 for _, attrs in graph.nodes(data=True) if attrs.get("type") == "Ашё"
        ),
    }


def _to_ranked_df(
    graph: nx.DiGraph,
    values: dict[str, float],
    metric_name: str,
    top_n: int,
) -> pd.DataFrame:
    if not values:
        return pd.DataFrame(columns=["Қаҳрамон", metric_name])

    ranked = [
        (node, value)
        for node, value in sorted(values.items(), key=lambda item: item[1], reverse=True)
        if graph.nodes[node].get("type") == "Шахс"
    ][:top_n]

    if not ranked:
        return pd.DataFrame(columns=["Қаҳрамон", metric_name])

    dataframe = pd.DataFrame(ranked, columns=["Қаҳрамон", metric_name])
    dataframe.index = range(1, len(dataframe) + 1)
    dataframe.index.name = "№"
    dataframe[metric_name] = dataframe[metric_name].round(4)
    return dataframe


def compute_centrality_tables(
    graph: nx.DiGraph,
    top_n: int = 10,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Compute degree and betweenness centrality top tables."""
    if graph.number_of_nodes() < 2:
        empty_deg = pd.DataFrame(columns=["Қаҳрамон", "Degree Centrality"])
        empty_btw = pd.DataFrame(columns=["Қаҳрамон", "Betweenness Centrality"])
        return empty_deg, empty_btw

    degree_values = nx.degree_centrality(graph)
    betweenness_values = nx.betweenness_centrality(graph)

    degree_df = _to_ranked_df(graph, degree_values, "Degree Centrality", top_n)
    betweenness_df = _to_ranked_df(
        graph, betweenness_values, "Betweenness Centrality", top_n
    )
    return degree_df, betweenness_df
