import streamlit as st
import streamlit.components.v1 as components

from shahnameh_app.data import build_node_metadata, filter_edges, load_data
from shahnameh_app.graph_logic import (
    build_graph,
    compute_centrality_tables,
    compute_summary_metrics,
)
from shahnameh_app.ui import (
    inject_styles,
    render_centrality_tables,
    render_data_table,
    render_footer,
    render_graph_legend,
    render_header,
    render_help,
    render_metrics,
    render_section_intro,
    render_sidebar,
)
from shahnameh_app.visualization import make_pyvis_graph

st.set_page_config(
    page_title="Графи дониши «Шоҳнома»",
    page_icon="📜",
    layout="wide",
)

try:
    dataframe = load_data("data_tajik.csv")
except FileNotFoundError:
    st.error("Файли `data_tajik.csv` ёфт нашуд. Лутфан файлро ба решаи лоиҳа илова кунед.")
    st.stop()
except ValueError as exc:
    st.error(f"Хатои сохтори CSV: {exc}")
    st.stop()
except Exception as exc:  # noqa: BLE001
    st.error(f"Хатои ғайричашмдошт ҳангоми хондани додаҳо: {exc}")
    st.stop()

node_metadata = build_node_metadata(dataframe)

selected_side, selected_type, graph_height, physics_enabled, selected_theme = render_sidebar()
inject_styles(selected_theme)

filtered_dataframe = filter_edges(
    dataframe,
    metadata=node_metadata,
    side=selected_side,
    node_type=selected_type,
)
filtered_graph = build_graph(filtered_dataframe, node_metadata)

summary = compute_summary_metrics(filtered_graph)
degree_df, betweenness_df = compute_centrality_tables(filtered_graph)

render_header(
    total_rows=len(dataframe),
    filtered_rows=len(filtered_dataframe),
    side=selected_side,
    node_type=selected_type,
)
render_metrics(summary)
render_centrality_tables(degree_df, betweenness_df)

render_section_intro(
    "Граф",
    "Саҳнаи интерактивии робитаҳо",
    "Гиреҳҳоро кашед, робитаҳоро бубинед ва сохтори дохилии шабакаи «Шоҳнома»-ро аз наздик омӯзед.",
)
render_graph_legend()

if filtered_dataframe.empty:
    st.warning("⚠️ Маълумот бо ин филтрҳо ёфт нашуд. Лутфан филтрро тағйир диҳед.")
else:
    html = make_pyvis_graph(
        filtered_dataframe,
        metadata=node_metadata,
        height=graph_height,
        physics=physics_enabled,
        theme=selected_theme,
    )
    components.html(html, height=graph_height + 50, scrolling=True)

render_data_table(filtered_dataframe)
render_help()
render_footer()
