"""PyVis rendering helpers."""

from __future__ import annotations

import os
import tempfile

from pyvis.network import Network

from .data import get_node_attrs


GRAPH_THEMES = {
    "dark": {
        "background": "#091221",
        "font": "#f4f1e8",
        "edge": "#79c7b8",
        "edge_font": "#a9b7cc",
    },
    "light": {
        "background": "#fbf7ef",
        "font": "#243247",
        "edge": "#4b9f9a",
        "edge_font": "#5d6f87",
    },
}


def get_node_style(node_type: str, side: str) -> tuple[str, str]:
    """Return node color and shape by type/side."""
    color = "#7ba1d6"
    shape = "dot"

    if node_type == "Шахс":
        if side == "Эрон":
            color = "#4ecb71"
        elif side == "Турон":
            color = "#e96b4c"
        else:
            color = "#91a1b8"
    elif node_type == "Макон":
        color = "#d9a441"
        shape = "square"
    elif node_type == "Ашё":
        color = "#8f7cf0"
        shape = "triangle"
    else:
        color = "#7ba1d6"

    return color, shape


def make_pyvis_graph(
    dataframe,
    metadata: dict[str, dict[str, str]],
    height: int,
    physics: bool,
    theme: str,
) -> str:
    """Create HTML for PyVis graph from filtered dataframe."""
    graph_theme = GRAPH_THEMES.get(theme, GRAPH_THEMES["dark"])
    network = Network(
        height=f"{height}px",
        width="100%",
        bgcolor=graph_theme["background"],
        font_color=graph_theme["font"],
        directed=True,
        cdn_resources="in_line",
    )
    network.barnes_hut(
        gravity=-3000,
        central_gravity=0.3,
        spring_length=200,
        spring_strength=0.01,
    )

    if not physics:
        network.toggle_physics(False)

    for _, row in dataframe.iterrows():
        source = row["Source"]
        target = row["Target"]
        relation = row["Relationship"]

        source_attrs = get_node_attrs(source, metadata)
        target_attrs = get_node_attrs(target, metadata)

        source_color, source_shape = get_node_style(
            source_attrs["type"], source_attrs["side"]
        )
        target_color, target_shape = get_node_style(
            target_attrs["type"], target_attrs["side"]
        )

        network.add_node(
            source,
            label=source,
            title=(
                f"<b>{source}</b><br>"
                f"Навъ: {source_attrs['type']}<br>"
                f"Ҷониб: {source_attrs['side']}"
            ),
            color=source_color,
            shape=source_shape,
            size=22,
            borderWidth=1.5,
            font={"size": 15, "color": graph_theme["font"], "face": "Manrope"},
        )
        network.add_node(
            target,
            label=target,
            title=(
                f"<b>{target}</b><br>"
                f"Навъ: {target_attrs['type']}<br>"
                f"Ҷониб: {target_attrs['side']}"
            ),
            color=target_color,
            shape=target_shape,
            size=22,
            borderWidth=1.5,
            font={"size": 15, "color": graph_theme["font"], "face": "Manrope"},
        )
        network.add_edge(
            source,
            target,
            title=relation,
            label=relation,
            color=graph_theme["edge"],
            width=1.7,
            font={
                "size": 11,
                "color": graph_theme["edge_font"],
                "align": "top",
                "face": "Manrope",
            },
            arrows="to",
        )

    temp_file = tempfile.NamedTemporaryFile(
        delete=False, suffix=".html", mode="w", encoding="utf-8"
    )
    network.save_graph(temp_file.name)
    temp_file.close()

    with open(temp_file.name, "r", encoding="utf-8") as handle:
        html_content = handle.read()

    os.unlink(temp_file.name)
    return html_content
