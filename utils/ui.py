import streamlit as st

from data.themes import THEMES, TOTAL_LEVELS
from game_logic import calculate_level_score, current_room, get_theme


def inject_dark_theme():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700&display=swap');

        .stApp {
            background: linear-gradient(160deg, #0c0c12 0%, #14141f 100%);
            color: #e8eaed;
            font-family: 'Outfit', sans-serif;
        }

        h1, h2, h3 {
            font-family: 'Outfit', sans-serif !important;
            color: #f5f5f5 !important;
            font-weight: 700 !important;
        }

        .block-container { padding-top: 1.5rem; max-width: 1000px; }

        .escape-hero { text-align: center; padding: 1rem 0; }
        .escape-hero p { color: #9aa0a6; font-size: 1rem; }

        .room-card {
            background: #1a1a24;
            border: 1px solid #2d2d3a;
            border-radius: 12px;
            padding: 1rem 1.25rem;
            margin: 0.75rem 0;
        }
        .room-card h3 { color: #7cb8ff !important; margin-top: 0 !important; font-size: 1.2rem !important; }
        .room-desc { color: #b8bcc4; line-height: 1.6; font-size: 0.95rem; }

        .necessity-tag {
            display: inline-block;
            background: #252532;
            border: 1px solid #3d3d4d;
            color: #c4c8d0;
            padding: 0.2rem 0.6rem;
            border-radius: 8px;
            font-size: 0.8rem;
            margin: 0.15rem 0.2rem 0.15rem 0;
        }

        .question-box {
            background: #1e2433;
            border-left: 4px solid #6ea8fe;
            padding: 0.9rem 1.1rem;
            border-radius: 8px;
            margin: 0.75rem 0;
            color: #dce3f0;
        }
        .question-box strong { color: #6ea8fe; }

        .hint-box {
            background: #252018;
            border: 1px solid #4a4030;
            border-radius: 8px;
            padding: 0.75rem 1rem;
            color: #e8c97a;
            margin: 0.4rem 0;
            font-size: 0.92rem;
        }

        /* Sidebar — Mission Control */
        div[data-testid="stSidebar"] {
            background: #111118 !important;
            border-right: 1px solid #2a2a35;
        }

        .mission-title {
            font-size: 1.35rem;
            font-weight: 700;
            color: #ffb347;
            margin: 0 0 0.25rem 0;
            letter-spacing: 0.02em;
        }

        .mission-theme {
            color: #a8b4c4;
            font-size: 0.9rem;
            margin-bottom: 1rem;
        }

        .stat-box {
            background: linear-gradient(145deg, #1c1c28, #16161f);
            border: 1px solid #333344;
            border-radius: 12px;
            padding: 0.85rem 1rem;
            margin-bottom: 0.65rem;
            text-align: center;
        }

        .stat-label {
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: #8b93a3;
            margin-bottom: 0.25rem;
        }

        .stat-value-score {
            font-size: 2rem;
            font-weight: 700;
            color: #ffd966;
            line-height: 1.1;
        }

        .stat-value-hints {
            font-size: 1.75rem;
            font-weight: 700;
            color: #7dcea0;
            line-height: 1.1;
        }

        .stat-value-level {
            font-size: 1.1rem;
            font-weight: 600;
            color: #8ec5ff;
        }

        .level-bar-wrap {
            background: #252530;
            border-radius: 999px;
            height: 8px;
            margin: 0.5rem 0 1rem;
            overflow: hidden;
        }
        .level-bar-fill {
            background: linear-gradient(90deg, #ffb347, #ffcc66);
            height: 100%;
            border-radius: 999px;
        }

        .stTextInput input {
            background: #1a1a24 !important;
            border: 1px solid #3d3d4d !important;
            color: #fff !important;
            border-radius: 8px !important;
        }

        .stButton > button {
            background: #ffb347 !important;
            color: #1a1a1a !important;
            font-weight: 600 !important;
            border: none !important;
            border-radius: 8px !important;
        }

        /* Room & theme images — aligned, same height */
        div[data-testid="stImage"] {
            display: flex;
            justify-content: center;
            margin: 0 auto 0.75rem auto;
        }
        div[data-testid="stImage"] img {
            width: 100%;
            max-height: 300px;
            object-fit: cover;
            border-radius: 12px;
            border: 1px solid #3a3a48;
            box-shadow: 0 6px 24px rgba(0,0,0,0.35);
        }
        div[data-testid="stImage"] figcaption {
            text-align: center;
            color: #9aa0a6 !important;
            font-size: 0.85rem;
            margin-top: 0.35rem;
        }

        .theme-pick img {
            max-height: 200px !important;
        }

        .room-layout {
            display: flex;
            gap: 1.25rem;
            align-items: flex-start;
            margin-bottom: 1rem;
        }

        #MainMenu, footer { visibility: hidden; }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_hero():
    st.markdown(
        """
        <div class="escape-hero">
            <h1>🔐 Escape Room</h1>
            <p>Pick a theme. Read each room like a real escape room — clues are in the story. Fewer hints = more points.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _level_total():
    if st.session_state.get("theme_id"):
        return len(THEMES[st.session_state.theme_id]["rooms"])
    return TOTAL_LEVELS


def render_sidebar():
    st.sidebar.markdown(
        '<p class="mission-title">🎮 Mission Control</p>',
        unsafe_allow_html=True,
    )

    if st.session_state.get("theme_id"):
        theme = get_theme(st.session_state.theme_id)
        total = _level_total()
        st.sidebar.markdown(
            f'<p class="mission-theme">{theme["title"]}</p>',
            unsafe_allow_html=True,
        )

        if st.session_state.get("game_phase") == "playing":
            level = st.session_state.current_level + 1
            pct = min(st.session_state.current_level / total, 1.0) * 100
            st.sidebar.markdown(
                f"""
                <div class="stat-box">
                    <div class="stat-label">Level</div>
                    <div class="stat-value-level">{level} / {total}</div>
                </div>
                <div class="level-bar-wrap">
                    <div class="level-bar-fill" style="width: {pct}%;"></div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            score = st.session_state.get("score", 0)
            room = current_room()
            hints_left = len(room["hints"]) - st.session_state.current_hint

            st.sidebar.markdown(
                f"""
                <div class="stat-box">
                    <div class="stat-label">Score</div>
                    <div class="stat-value-score">{score:,}</div>
                </div>
                <div class="stat-box">
                    <div class="stat-label">Hints left</div>
                    <div class="stat-value-hints">{hints_left}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            potential = calculate_level_score(
                st.session_state.current_hint,
                st.session_state.wrong_guesses,
            )
            st.sidebar.caption(f"Next correct answer: up to **{potential}** pts")
    else:
        st.sidebar.markdown(
            '<p class="mission-theme">Choose a theme to begin.</p>',
            unsafe_allow_html=True,
        )

    st.sidebar.markdown("---")
    if st.sidebar.button("🔄 New Game", use_container_width=True):
        from game_logic import reset_to_theme_select

        reset_to_theme_select()
        st.rerun()


def render_theme_selection():
    st.markdown("## Pick a theme")
    st.caption(f"Each theme has **{TOTAL_LEVELS} rooms**. Read the scene, then answer from the clues you see.")

    theme_ids = list(THEMES.keys())
    cols = st.columns(2)
    for i, tid in enumerate(theme_ids):
        theme = THEMES[tid]
        with cols[i % 2]:
            st.markdown('<div class="theme-pick">', unsafe_allow_html=True)
            st.image(theme["cover_image"], use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
            st.markdown(f"**{theme['title']}**")
            st.caption(theme["tagline"])
            if st.button(f"Play {theme['title']}", key=f"theme_{tid}", use_container_width=True):
                from game_logic import initialize_game

                initialize_game(tid)
                st.rerun()


def render_room_necessities(necessities: list[str]):
    tags = "".join(f'<span class="necessity-tag">{n}</span>' for n in necessities)
    st.markdown(f'<div class="room-card"><strong>Items here:</strong> {tags}</div>', unsafe_allow_html=True)


def render_room_content():
    room = current_room()
    level_num = st.session_state.current_level + 1
    total = _level_total()

    caption = f"Room {level_num} of {total} — {room['name']}"
    col_img, col_story = st.columns([1, 1], gap="large")
    with col_img:
        st.image(room["image"], use_container_width=True, caption=caption)
    with col_story:
        st.markdown(
            f'<div class="room-card"><h3>🚪 {room["name"]}</h3>'
            f'<p class="room-desc">{room["description"]}</p></div>',
            unsafe_allow_html=True,
        )
        render_room_necessities(room["necessities"])

    st.markdown(
        f'<div class="question-box"><strong>🔒 Lock puzzle:</strong> {room["question"]}</div>',
        unsafe_allow_html=True,
    )

    st.markdown("**Hints**")
    for i in range(st.session_state.current_hint + 1):
        st.markdown(f'<div class="hint-box">💡 {room["hints"][i]}</div>', unsafe_allow_html=True)

    if st.session_state.current_hint < len(room["hints"]) - 1:
        if st.button("Show next hint", key="reveal_hint"):
            from game_logic import reveal_hint

            if reveal_hint():
                st.session_state.last_feedback = ("warning", "New hint shown — score will be lower.")
            st.rerun()


def render_feedback():
    fb = st.session_state.get("last_feedback")
    if not fb:
        return
    kind, msg = fb
    if kind == "success":
        st.success(msg)
    elif kind == "error":
        st.error(msg)
    else:
        st.warning(msg)


def render_completion():
    theme = get_theme(st.session_state.theme_id)
    total = _level_total()
    st.balloons()
    st.markdown(f"## 🎉 You escaped {theme['title']}!")
    st.markdown(f"**Final score: {st.session_state.score:,}** — all {total} rooms cleared.")
    st.image(theme["cover_image"], use_container_width=True)


def render_gameplay():
    theme = get_theme(st.session_state.theme_id)
    st.markdown(f"## {theme['title']}")
    st.caption(theme["tagline"])

    if st.session_state.game_over and st.session_state.won:
        render_completion()
        return

    render_feedback()
    render_room_content()

    guess = st.text_input("Your answer", placeholder="Type here…", label_visibility="collapsed")
    if st.button("🔓 Submit answer", use_container_width=True):
        from game_logic import process_guess

        process_guess(guess)
        st.rerun()
