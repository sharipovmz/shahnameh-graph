"""Data loading, validation, node metadata, and filtering."""

from __future__ import annotations

import pandas as pd

from .constants import REQUIRED_COLUMNS


def _infer_target_attrs(target: str) -> tuple[str, str]:
    """Fallback metadata for nodes that never appear as Source."""
    if target in {"Эрон", "Турон"}:
        return "Макон", target
    return "Номаълум", "Бетараф"


def load_data(path: str = "data_tajik.csv") -> pd.DataFrame:
    """Load and validate source CSV."""
    dataframe = pd.read_csv(path, encoding="utf-8")
    dataframe.columns = dataframe.columns.str.strip()

    missing = [col for col in REQUIRED_COLUMNS if col not in dataframe.columns]
    if missing:
        missing_list = ", ".join(missing)
        raise ValueError(f"CSV сутунҳои ҳатмиро надорад: {missing_list}")

    dataframe = dataframe[list(REQUIRED_COLUMNS)].copy()
    for col in dataframe.columns:
        dataframe[col] = dataframe[col].astype(str).str.strip()

    dataframe = dataframe[
        (dataframe["Source"] != "")
        & (dataframe["Relationship"] != "")
        & (dataframe["Target"] != "")
    ].reset_index(drop=True)

    return dataframe


def build_node_metadata(dataframe: pd.DataFrame) -> dict[str, dict[str, str]]:
    """Build normalized node metadata map for both Source and Target.

    CSV semantics: Type column = Target's type; Side column = Source's side.
    """
    target_types: dict[str, str] = {}
    source_sides: dict[str, str] = {}

    for _, row in dataframe.iterrows():
        source = row["Source"]
        target = row["Target"]
        node_type = row["Type"]

        if source not in source_sides:
            source_sides[source] = row["Side"]

        # Prefer Шахс so a character who owns/builds places keeps their person type.
        if target not in target_types:
            target_types[target] = node_type
        elif node_type == "Шахс" and target_types[target] != "Шахс":
            target_types[target] = "Шахс"

    metadata: dict[str, dict[str, str]] = {}
    for node in set(source_sides) | set(target_types):
        node_type = target_types.get(node)
        node_side = source_sides.get(node)

        if node_type is None:
            node_type = "Шахс"  # source-only nodes are characters
        if node_side is None:
            _, node_side = _infer_target_attrs(node)

        metadata[node] = {"type": node_type, "side": node_side}

    return metadata


def get_node_attrs(node: str, metadata: dict[str, dict[str, str]]) -> dict[str, str]:
    attrs = metadata.get(node)
    if attrs:
        return attrs
    fallback_type, fallback_side = _infer_target_attrs(node)
    return {"type": fallback_type, "side": fallback_side}


def filter_edges(
    dataframe: pd.DataFrame,
    metadata: dict[str, dict[str, str]],
    side: str,
    node_type: str,
) -> pd.DataFrame:
    """Filter edges by node side/type for both Source and Target."""

    def _matches(node_name: str) -> bool:
        attrs = get_node_attrs(node_name, metadata)
        if side != "Ҳама" and attrs["side"] != side:
            return False
        if node_type != "Ҳама" and attrs["type"] != node_type:
            return False
        return True

    mask = dataframe.apply(
        lambda row: _matches(row["Source"]) and _matches(row["Target"]),
        axis=1,
    )
    return dataframe[mask].reset_index(drop=True)

