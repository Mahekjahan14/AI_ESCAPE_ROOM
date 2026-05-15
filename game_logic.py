import re

import streamlit as st

from data.themes import (
    BASE_LEVEL_SCORE,
    HINT_PENALTY,
    THEMES,
    TOTAL_LEVELS,
    WRONG_GUESS_PENALTY,
)


def normalize_answer(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())


def get_theme(theme_id: str | None):
    if theme_id and theme_id in THEMES:
        return THEMES[theme_id]
    return None


def reset_to_theme_select():
    keys_to_clear = [
        "theme_id",
        "current_level",
        "current_hint",
        "wrong_guesses",
        "level_points_earned",
        "game_over",
        "won",
        "last_feedback",
        "last_level_score",
    ]
    for key in keys_to_clear:
        st.session_state.pop(key, None)
    st.session_state.game_phase = "theme_select"


def initialize_game(theme_id: str):
    theme = THEMES[theme_id]
    st.session_state.theme_id = theme_id
    st.session_state.current_level = 0
    st.session_state.current_hint = 0
    st.session_state.wrong_guesses = 0
    st.session_state.score = 0
    st.session_state.game_over = False
    st.session_state.won = False
    st.session_state.game_phase = "playing"
    st.session_state.last_feedback = None
    st.session_state.last_level_score = 0
    st.session_state.hints_revealed = 0
    st.session_state.game_initialized = True


def current_room():
    theme = THEMES[st.session_state.theme_id]
    return theme["rooms"][st.session_state.current_level]


def levels_remaining() -> int:
    return TOTAL_LEVELS - st.session_state.current_level


def calculate_level_score(hints_used: int, wrong_guesses: int) -> int:
    score = BASE_LEVEL_SCORE - (hints_used * HINT_PENALTY) - (wrong_guesses * WRONG_GUESS_PENALTY)
    return max(100, score)


def reveal_hint():
    room = current_room()
    max_hint = len(room["hints"]) - 1
    if st.session_state.current_hint < max_hint:
        st.session_state.current_hint += 1
        st.session_state.hints_revealed += 1
        return True
    return False


def check_answer(guess: str) -> bool:
    room = current_room()
    accepted = {normalize_answer(room["answer"])}
    accepted.add(normalize_answer(room["answer"].replace(" ", "")))
    for alt in room.get("alt_answers", []):
        accepted.add(normalize_answer(alt))
        accepted.add(normalize_answer(alt.replace(" ", "")))
    return normalize_answer(guess) in accepted


def process_guess(guess: str):
    if not guess or not guess.strip():
        st.session_state.last_feedback = ("warning", "Enter an answer to unlock the door.")
        return

    if check_answer(guess):
        hints_used = st.session_state.current_hint
        level_score = calculate_level_score(hints_used, st.session_state.wrong_guesses)
        st.session_state.score += level_score
        st.session_state.last_level_score = level_score
        st.session_state.last_feedback = ("success", f"Correct! +{level_score} points")
        advance_level()
    else:
        st.session_state.wrong_guesses += 1
        revealed = reveal_hint()
        if revealed:
            st.session_state.last_feedback = (
                "error",
                "Wrong answer. A new hint has been unlocked — try again!",
            )
        else:
            st.session_state.last_feedback = (
                "error",
                "Wrong answer. No more hints — study what you have!",
            )


def advance_level():
    st.session_state.current_level += 1
    st.session_state.current_hint = 0
    st.session_state.wrong_guesses = 0
    st.session_state.hints_revealed = 0

    theme = THEMES[st.session_state.theme_id]
    total = len(theme["rooms"])
    if st.session_state.current_level >= total:
        st.session_state.game_over = True
        st.session_state.won = True
        st.session_state.game_phase = "complete"


def get_progress_fraction() -> float:
    return st.session_state.current_level / TOTAL_LEVELS
