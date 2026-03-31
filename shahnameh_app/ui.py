"""UI rendering helpers for Streamlit."""

from __future__ import annotations

import pandas as pd
import streamlit as st

from .constants import (
    DEFAULT_GRAPH_HEIGHT,
    MAX_GRAPH_HEIGHT,
    MIN_GRAPH_HEIGHT,
    SIDE_OPTIONS,
    TYPE_OPTIONS,
)
from .styles import get_app_styles


def inject_styles(theme: str) -> None:
    st.markdown(get_app_styles(theme), unsafe_allow_html=True)


def render_sidebar() -> tuple[str, str, int, bool, str]:
    st.sidebar.markdown(
        """
        <div class="sidebar-card">
            <div class="sidebar-title">Танзимот</div>
            <p class="sidebar-copy">
                Филтрҳоро танзим кунед, андозаи саҳнаи графро интихоб намоед ва
                тарзи ҳаракати гиреҳҳоро идора кунед.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    selected_theme = st.sidebar.radio(
        "🎨 Мавзӯи намоиш:",
        ("dark", "light"),
        format_func=lambda value: "Торик" if value == "dark" else "Равшан",
    )
    selected_side = st.sidebar.selectbox("🏳️ Интихоби ҷониб:", SIDE_OPTIONS)
    selected_type = st.sidebar.selectbox("📦 Интихоби навъ:", TYPE_OPTIONS)
    graph_height = st.sidebar.slider(
        "📐 Баландии граф:",
        MIN_GRAPH_HEIGHT,
        MAX_GRAPH_HEIGHT,
        DEFAULT_GRAPH_HEIGHT,
        step=50,
    )
    physics_enabled = st.sidebar.checkbox("🔬 Физика фаъол", value=True)

    st.sidebar.markdown(
        """
        <div class="sidebar-card">
            <div class="sidebar-title">Дар бораи лоиҳа</div>
            <p class="sidebar-copy">
                Ин интерфейс барои нишон додани робитаҳои байни қаҳрамонон, маконҳо
                ва ашёҳои «Шоҳнома» сохта шудааст.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    return selected_side, selected_type, graph_height, physics_enabled, selected_theme


def render_header(total_rows: int, filtered_rows: int, side: str, node_type: str) -> None:
    st.markdown(
        f"""
        <section class="hero-card">
            <div class="hero-kicker">Мероси адабӣ • Таҳлили шабакавӣ</div>
            <h1 class="hero-title">Графи дониши «Шоҳнома»</h1>
            <p class="hero-lead">
                Интерфейси таҳлилӣ барои дидани робитаҳои байни
                <strong>қаҳрамонон</strong>, <strong>маконҳо</strong> ва
                <strong>ашёҳо</strong> дар осори Фирдавсӣ. Филтрҳо дар тарафи чап
                саҳнаи таҳлилро зуд тағйир медиҳанд ва граф марказҳои муҳими достонро
                равшан нишон медиҳад.
            </p>
            <div class="hero-meta-grid">
                <div class="hero-meta-card">
                    <span class="meta-label">Ҳолати филтр</span>
                    <span class="meta-value">{side}</span>
                </div>
                <div class="hero-meta-card">
                    <span class="meta-label">Навъи гиреҳ</span>
                    <span class="meta-value">{node_type}</span>
                </div>
                <div class="hero-meta-card">
                    <span class="meta-label">Сатрҳои намоишшуда</span>
                    <span class="meta-value">{filtered_rows} / {total_rows}</span>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_section_intro(label: str, title: str, description: str) -> None:
    st.markdown(
        f"""
        <div>
            <span class="section-label">{label}</span>
            <h2 class="section-title">{title}</h2>
            <p class="section-copy">{description}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_metrics(summary: dict[str, int]) -> None:
    render_section_intro(
        "Нишондиҳандаҳо",
        "Омори умумӣ",
        "Ин нишондиҳандаҳо ҳолати шабакаро пас аз татбиқи филтрҳо нишон медиҳанд.",
    )
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    col1.metric("🔵 Ҳамаи гиреҳҳо", summary["total_nodes"])
    col2.metric("🔗 Ҳамаи робитаҳо", summary["total_edges"])
    col3.metric("🟢 Қаҳрамонони Эрон", summary["iran_heroes"])
    col4.metric("🔴 Қаҳрамонони Турон", summary["turan_heroes"])
    col5.metric("🟡 Маконҳо", summary["places"])
    col6.metric("🟣 Ашёҳо", summary["objects"])


def render_centrality_tables(degree_df: pd.DataFrame, betweenness_df: pd.DataFrame) -> None:
    render_section_intro(
        "Марказият",
        "Қаҳрамонони калидӣ дар шабака",
        "Ҷадвалҳо нишон медиҳанд, ки кадом гиреҳҳо бештарин робита доранд ва кадомашон "
        "байни гурӯҳҳо ҳамчун миёнарав амал мекунанд.",
    )
    if degree_df.empty or betweenness_df.empty:
        st.info("Барои ҳисобкунии марказият ҳадди ақал 2 гиреҳ лозим аст.")
        return

    tab1, tab2 = st.tabs(
        ["⭐ Қаҳрамонони асосӣ", "🌉 Миёнаравҳо"]
    )

    with tab1:
        max_degree = max(float(degree_df["Degree Centrality"].max()), 1e-9)
        st.markdown(
            "**Қаҳрамонони асосӣ** — касоне, ки бештарин робитаро доранд "
            "."
        )
        st.dataframe(
            degree_df,
            column_config={
                "Degree Centrality": st.column_config.ProgressColumn(
                    "Degree Centrality",
                    format="%.4f",
                    min_value=0,
                    max_value=max_degree,
                ),
            },
            use_container_width=True,
        )

    with tab2:
        max_btw = max(float(betweenness_df["Betweenness Centrality"].max()), 1e-9)
        st.markdown(
            "**Миёнаравҳо** — касоне, ки байни гурӯҳҳо пайванд эҷод мекунанд."
        )
        st.dataframe(
            betweenness_df,
            column_config={
                "Betweenness Centrality": st.column_config.ProgressColumn(
                    "Betweenness Centrality",
                    format="%.4f",
                    min_value=0,
                    max_value=max_btw,
                ),
            },
            use_container_width=True,
        )


def render_graph_legend() -> None:
    st.markdown(
        """
        <div class="legend-panel">
            <div class="legend-wrap">
                <span class="legend-box"><span class="legend-dot" style="background:#4ecb71;"></span> Эрон (Шахс)</span>
                <span class="legend-box"><span class="legend-dot" style="background:#e96b4c;"></span> Турон (Шахс)</span>
                <span class="legend-box"><span class="legend-dot" style="background:#91a1b8;"></span> Номаълум</span>
                <span class="legend-box"><span class="legend-square" style="background:#d9a441;"></span> Макон</span>
                <span class="legend-box"><span class="legend-triangle" style="border-bottom-color:#8f7cf0;"></span> Ашё</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_data_table(dataframe: pd.DataFrame) -> None:
    render_section_intro(
        "Додаҳо",
        "Ҷадвали филтршуда",
        "Ҳамаи робитаҳои мувофиқ ба филтрро дар шакли ҷадвал бинед ва барои таҳлили баъдӣ зеркашӣ кунед.",
    )
    with st.expander("📋 Ҷадвали пурраи маълумот (натиҷа баъд аз филтр)", expanded=False):
        renamed = dataframe.rename(
            columns={
                "Source": "Сарчашма",
                "Relationship": "Робита",
                "Target": "Ҳадаф",
                "Type": "Навъ",
                "Side": "Ҷониб",
            }
        )
        st.dataframe(renamed, use_container_width=True, height=400)
        st.download_button(
            "⬇️ Зеркашӣ кардани натиҷа",
            data=dataframe.to_csv(index=False).encode("utf-8"),
            file_name="shahnameh_filtered.csv",
            mime="text/csv",
            use_container_width=True,
        )


def render_help() -> None:
    render_section_intro(
        "Шарҳ",
        "Метрикаҳо чӣ маъно доранд?",
        "Ин қисм барои хондани натиҷаҳои марказият ва фаҳмидани рамзгузории визуалӣ кӯмак мекунад.",
    )
    with st.expander("ℹ️ Тавзеҳот оид ба метрикаҳо", expanded=False):
        st.markdown(
            """
            ### 📌 Қаҳрамонони асосӣ
            Ин метрика нишон медиҳад, ки ҳар як гиреҳ (қаҳрамон) **чанд робита** дорад.
            Ҳар чӣ бештар робита бошад, ин қаҳрамон **муҳимтар** аст дар достон.

            ### 📌 Миёнаравҳо
            Ин метрика муайян мекунад, ки кадом қаҳрамон **байни гурӯҳҳо пайванд** аст.
            Масалан, агар ду гурӯҳи қаҳрамонон фақат тавассути як шахс бо ҳам робита
            дошта бошанд, он шахс **миёнарав** аст.

            ### 🎨 Рангҳо
            | Ранг | Маънӣ |
            |------|-------|
            | 🟢 Сабз | Қаҳрамонони Эрон |
            | 🔴 Сурх | Қаҳрамонони Турон |
            | 🟡 Зард | Маконҳо (шаҳрҳо, қалъаҳо) |
            | 🟣 Бунафш | Ашёҳо (аспҳо, зиреҳҳо) |
            | ⚪ Хокистарӣ | Номаълум |
            """
        )


def render_footer() -> None:
    st.markdown(
        "<div class='footer-note'>"
        "📜 Графи дониши «Шоҳнома» — Кори дипломӣ | "
        "Бо Streamlit, NetworkX ва PyVis сохта шудааст"
        "</div>",
        unsafe_allow_html=True,
    )
