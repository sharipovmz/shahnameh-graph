"""CSS styles for the Streamlit app."""

from __future__ import annotations

THEMES: dict[str, dict[str, str]] = {
    "dark": {
        "app-bg": """
            radial-gradient(circle at top left, rgba(217, 164, 65, 0.16), transparent 30%),
            radial-gradient(circle at top right, rgba(121, 199, 184, 0.12), transparent 28%),
            linear-gradient(180deg, #0a1324 0%, #08111f 52%, #07101b 100%)
        """,
        "header-bg": "rgba(8, 17, 31, 0.72)",
        "sidebar-bg": """
            linear-gradient(180deg, rgba(9, 19, 35, 0.98), rgba(7, 14, 28, 0.98)),
            radial-gradient(circle at top, rgba(217, 164, 65, 0.12), transparent 26%)
        """,
        "panel-strong": "linear-gradient(145deg, rgba(18, 35, 62, 0.96), rgba(9, 18, 33, 0.96))",
        "panel-soft": "rgba(8, 18, 34, 0.72)",
        "tabs-bg": "rgba(8, 17, 31, 0.65)",
        "expander-bg": "rgba(9, 20, 38, 0.72)",
        "hero-bg": """
            radial-gradient(circle at top right, rgba(217, 164, 65, 0.24), transparent 26%),
            linear-gradient(145deg, rgba(17, 33, 58, 0.96), rgba(7, 15, 29, 0.96))
        """,
        "hero-orb": "radial-gradient(circle, rgba(121, 199, 184, 0.22), transparent 70%)",
        "hero-kicker-text": "#f7d48d",
        "hero-lead": "#d0d8e7",
        "text": "#f4f1e8",
        "muted": "#a9b7cc",
        "border": "rgba(123, 161, 214, 0.20)",
        "border-strong": "rgba(217, 164, 65, 0.22)",
        "accent": "#d9a441",
        "accent-soft": "rgba(217, 164, 65, 0.18)",
        "accent-2": "#79c7b8",
        "button-bg": "linear-gradient(135deg, rgba(217, 164, 65, 0.18), rgba(121, 199, 184, 0.12))",
        "button-border": "rgba(217, 164, 65, 0.28)",
        "tab-active-bg": "linear-gradient(135deg, rgba(217, 164, 65, 0.28), rgba(121, 199, 184, 0.22))",
        "section-pill-bg": "rgba(121, 199, 184, 0.14)",
        "section-pill-text": "#bce8df",
        "meta-label": "#8fa0ba",
        "footer-text": "#8fa0ba",
        "shadow": "0 20px 60px rgba(1, 8, 20, 0.42)",
        "table-bg": "#0d1a2c",
        "table-bg-alt": "#13243c",
        "table-header": "#102037",
        "table-text": "#f4f1e8",
        "table-text-muted": "#a9b7cc",
        "table-border": "rgba(123, 161, 214, 0.18)",
        "table-accent": "#79c7b8",
        "table-accent-soft": "rgba(121, 199, 184, 0.20)",
    },
    "light": {
        "app-bg": """
            radial-gradient(circle at top left, rgba(217, 164, 65, 0.18), transparent 24%),
            radial-gradient(circle at top right, rgba(84, 159, 200, 0.14), transparent 24%),
            linear-gradient(180deg, #f8f4ea 0%, #f4efe3 55%, #efe8d9 100%)
        """,
        "header-bg": "rgba(248, 244, 234, 0.72)",
        "sidebar-bg": """
            linear-gradient(180deg, rgba(251, 248, 242, 0.98), rgba(242, 235, 223, 0.98)),
            radial-gradient(circle at top, rgba(217, 164, 65, 0.16), transparent 26%)
        """,
        "panel-strong": "linear-gradient(145deg, rgba(255, 252, 246, 0.98), rgba(247, 240, 229, 0.98))",
        "panel-soft": "rgba(255, 251, 244, 0.85)",
        "tabs-bg": "rgba(247, 241, 232, 0.95)",
        "expander-bg": "rgba(255, 252, 246, 0.92)",
        "hero-bg": """
            radial-gradient(circle at top right, rgba(217, 164, 65, 0.20), transparent 24%),
            linear-gradient(145deg, rgba(255, 252, 245, 0.98), rgba(243, 236, 225, 0.98))
        """,
        "hero-orb": "radial-gradient(circle, rgba(121, 199, 184, 0.16), transparent 70%)",
        "hero-kicker-text": "#8b5c12",
        "hero-lead": "#4d5d73",
        "text": "#1e2b3d",
        "muted": "#607089",
        "border": "rgba(127, 100, 53, 0.16)",
        "border-strong": "rgba(217, 164, 65, 0.22)",
        "accent": "#c28a29",
        "accent-soft": "rgba(194, 138, 41, 0.12)",
        "accent-2": "#3d8f88",
        "button-bg": "linear-gradient(135deg, rgba(194, 138, 41, 0.14), rgba(61, 143, 136, 0.10))",
        "button-border": "rgba(194, 138, 41, 0.24)",
        "tab-active-bg": "linear-gradient(135deg, rgba(194, 138, 41, 0.18), rgba(61, 143, 136, 0.10))",
        "section-pill-bg": "rgba(61, 143, 136, 0.10)",
        "section-pill-text": "#2c6f68",
        "meta-label": "#7b6e57",
        "footer-text": "#6f7b8f",
        "shadow": "0 18px 42px rgba(116, 98, 69, 0.12)",
        "table-bg": "#fffaf1",
        "table-bg-alt": "#f7f0e4",
        "table-header": "#f1e6d6",
        "table-text": "#223247",
        "table-text-muted": "#62738a",
        "table-border": "rgba(127, 100, 53, 0.16)",
        "table-accent": "#3d8f88",
        "table-accent-soft": "rgba(61, 143, 136, 0.14)",
    },
}


def get_app_styles(theme: str = "dark") -> str:
    """Return the app stylesheet for the selected theme."""
    palette = THEMES.get(theme, THEMES["dark"])
    theme_vars = "\n".join(f"        --{name}: {value};" for name, value in palette.items())
    return f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Marhey:wght@500;700&family=Manrope:wght@400;500;600;700;800&display=swap');

    :root {{
{theme_vars}
        --radius-lg: 24px;
        --radius-md: 18px;
        --radius-sm: 12px;
    }}

    html, body, [class*="css"] {{
        font-family: "Manrope", sans-serif;
    }}

    .stApp {{
        background: var(--app-bg);
        color: var(--text);
    }}

    .main .block-container {{
        padding-top: 2.25rem;
        padding-bottom: 2rem;
        max-width: 1400px;
    }}

    [data-testid="stHeader"] {{
        background: var(--header-bg);
        backdrop-filter: blur(14px);
    }}

    [data-testid="stSidebar"] {{
        background: var(--sidebar-bg);
        border-right: 1px solid var(--border);
    }}

    [data-testid="stSidebar"] .block-container {{
        padding-top: 1.5rem;
    }}

    [data-testid="stMetric"] {{
        background: var(--panel-strong);
        border: 1px solid var(--border);
        border-radius: var(--radius-md);
        padding: 1rem 1.1rem;
        box-shadow: var(--shadow);
    }}

    [data-testid="stMetricLabel"] {{
        color: var(--muted) !important;
        font-size: 0.85rem !important;
        font-weight: 600 !important;
    }}

    [data-testid="stMetricValue"] {{
        color: var(--text) !important;
        font-size: 1.9rem !important;
        font-weight: 800 !important;
        letter-spacing: -0.03em;
    }}

    [data-testid="stMetricDelta"] {{
        color: var(--accent-2) !important;
    }}

    .stDataFrame, div[data-testid="stTable"] {{
        border-radius: var(--radius-md);
        overflow: hidden;
        border: 1px solid var(--border);
        box-shadow: var(--shadow);
    }}

    [data-testid="stDataFrame"],
    [data-testid="stDataFrameResizable"],
    .stDataFrameGlideDataEditor {{
        --gdg-bg-cell: var(--table-bg);
        --gdg-bg-cell-medium: var(--table-bg-alt);
        --gdg-bg-header: var(--table-header);
        --gdg-bg-header-has-focus: var(--table-header);
        --gdg-bg-header-hovered: var(--table-bg-alt);
        --gdg-bg-bubble: var(--table-bg);
        --gdg-bg-bubble-selected: var(--table-accent-soft);
        --gdg-bg-search-result: var(--table-accent-soft);
        --gdg-border-color: var(--table-border);
        --gdg-horizontal-border-color: var(--table-border);
        --gdg-drilldown-border: var(--table-border);
        --gdg-link-color: var(--table-accent);
        --gdg-accent-color: var(--table-accent);
        --gdg-accent-light: var(--table-accent-soft);
        --gdg-text-dark: var(--table-text);
        --gdg-text-medium: var(--table-text-muted);
        --gdg-text-light: var(--table-text-muted);
        --gdg-text-header: var(--table-text);
        --gdg-text-group-header: var(--table-text);
    }}

    [data-testid="stDataFrameResizable"] {{
        background: var(--table-bg);
        border-color: var(--table-border) !important;
    }}

    .stDataFrameGlideDataEditor .gdg-search-bar {{
        background: var(--table-bg-alt);
        color: var(--table-text);
        border: 1px solid var(--table-border);
    }}

    [data-testid="stDataFrame"] canvas,
    .stDataFrameGlideDataEditor canvas {{
        border-radius: var(--radius-md);
    }}

    .stTabs [data-baseweb="tab-list"] {{
        gap: 0.6rem;
        background: var(--tabs-bg);
        border: 1px solid var(--border);
        border-radius: 999px;
        padding: 0.35rem;
    }}

    .stTabs [data-baseweb="tab"] {{
        height: 44px;
        border-radius: 999px;
        color: var(--muted);
        font-weight: 700;
    }}

    .stTabs [aria-selected="true"] {{
        background: var(--tab-active-bg) !important;
        color: var(--text) !important;
    }}

    .stSlider [data-baseweb="slider"] {{
        padding-top: 0.5rem;
    }}

    .stSelectbox label, .stCheckbox label, .stSlider label, .stRadio label, .stDownloadButton button, .stButton button {{
        font-weight: 600;
        color: var(--text) !important;
    }}

    .stDownloadButton button, .stButton button {{
        min-height: 46px;
        border-radius: 14px;
        border: 1px solid var(--button-border);
        background: var(--button-bg);
        color: var(--text);
    }}

    .stExpander {{
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-md) !important;
        background: var(--expander-bg) !important;
        overflow: hidden;
    }}

    h1, h2, h3 {{
        color: var(--text) !important;
        letter-spacing: -0.03em;
    }}

    h1 {{
        font-family: "Marhey", serif;
    }}

    p, li, [data-testid="stCaptionContainer"], .stMarkdown, .stText {{
        color: var(--muted);
    }}

    .hero-card {{
        position: relative;
        overflow: hidden;
        padding: 2rem;
        border-radius: var(--radius-lg);
        background: var(--hero-bg);
        border: 1px solid var(--border-strong);
        box-shadow: var(--shadow);
        margin-bottom: 1.2rem;
    }}

    .hero-card::after {{
        content: "";
        position: absolute;
        inset: auto -10% -35% auto;
        width: 220px;
        height: 220px;
        background: var(--hero-orb);
        pointer-events: none;
    }}

    .hero-kicker {{
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.45rem 0.8rem;
        border-radius: 999px;
        background: var(--accent-soft);
        color: var(--hero-kicker-text);
        font-size: 0.82rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }}

    .hero-title {{
        margin: 0.9rem 0 0.7rem;
        font-family: "Marhey", serif;
        font-size: clamp(2.2rem, 4vw, 3.8rem);
        line-height: 1.04;
        color: var(--text);
    }}

    .hero-lead {{
        margin: 0;
        max-width: 860px;
        font-size: 1.02rem;
        line-height: 1.75;
        color: var(--hero-lead);
    }}

    .hero-meta-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 0.8rem;
        margin-top: 1.25rem;
    }}

    .hero-meta-card,
    .legend-panel,
    .sidebar-card {{
        background: var(--panel-soft);
        border: 1px solid var(--border);
        border-radius: var(--radius-md);
        box-shadow: var(--shadow);
    }}

    .hero-meta-card {{
        padding: 0.9rem 1rem;
    }}

    .meta-label {{
        display: block;
        margin-bottom: 0.28rem;
        font-size: 0.78rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: var(--meta-label);
    }}

    .meta-value {{
        color: var(--text);
        font-weight: 800;
        font-size: 1.05rem;
    }}

    .section-label {{
        display: inline-block;
        margin-bottom: 0.5rem;
        padding: 0.36rem 0.75rem;
        border-radius: 999px;
        background: var(--section-pill-bg);
        color: var(--section-pill-text);
        font-size: 0.78rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }}

    .section-title {{
        margin: 0 0 0.4rem;
        font-size: 1.45rem;
        color: var(--text);
    }}

    .section-copy {{
        margin: 0 0 1rem;
        max-width: 900px;
        color: var(--muted);
        line-height: 1.7;
    }}

    .legend-panel {{
        padding: 1rem 1.1rem;
        margin-bottom: 0.8rem;
    }}

    .legend-wrap {{
        display: flex;
        flex-wrap: wrap;
        gap: 0.8rem 1rem;
    }}

    .legend-box {{
        display: inline-flex;
        align-items: center;
        gap: 0.6rem;
        padding: 0.55rem 0.8rem;
        border-radius: 999px;
        background: rgba(255, 255, 255, 0.03);
        color: var(--text);
        font-size: 0.92rem;
        border: 1px solid var(--border);
    }}

    .legend-dot {{
        width: 14px;
        height: 14px;
        border-radius: 50%;
        display: inline-block;
        box-shadow: 0 0 0 4px rgba(255, 255, 255, 0.05);
    }}

    .legend-square {{
        width: 14px;
        height: 14px;
        display: inline-block;
        border-radius: 4px;
        box-shadow: 0 0 0 4px rgba(255, 255, 255, 0.05);
    }}

    .legend-triangle {{
        width: 0;
        height: 0;
        border-left: 7px solid transparent;
        border-right: 7px solid transparent;
        border-bottom: 14px solid;
        display: inline-block;
        filter: drop-shadow(0 0 0.2rem rgba(255, 255, 255, 0.18));
    }}

    .sidebar-card {{
        padding: 1rem;
        margin-top: 1rem;
    }}

    .sidebar-title {{
        margin: 0 0 0.35rem;
        color: var(--text);
        font-size: 1rem;
        font-weight: 800;
    }}

    .sidebar-copy {{
        margin: 0;
        color: var(--muted);
        line-height: 1.65;
        font-size: 0.92rem;
    }}

    .footer-note {{
        text-align: center;
        color: var(--footer-text);
        font-size: 0.88rem;
        padding: 1rem 0 0.5rem;
    }}

    @media (max-width: 900px) {{
        .main .block-container {{
            padding-top: 1.4rem;
        }}

        .hero-card {{
            padding: 1.4rem;
        }}

        .hero-title {{
            font-size: 2rem;
        }}
    }}
</style>
"""
