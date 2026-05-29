import streamlit as st
import requests
import time

# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------

st.set_page_config(
    page_title="Eirene AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------------------------
# ULTRA PREMIUM CSS
# ------------------------------------------------

st.markdown("""
<style>

/* ------------------------------------------------ */
/* GLOBAL */
/* ------------------------------------------------ */

html, body, [class*="css"] {

    background: #020617;
    color: #f8fafc;
    font-family: 'Inter', sans-serif;
}

/* ------------------------------------------------ */
/* MAIN APP */
/* ------------------------------------------------ */

.main {

    background:
    radial-gradient(circle at top left,
    rgba(59,130,246,0.16),
    transparent 28%),

    radial-gradient(circle at bottom right,
    rgba(168,85,247,0.12),
    transparent 24%),

    linear-gradient(
    180deg,
    #020617 0%,
    #071226 100%
    );

    min-height: 100vh;
}

/* ------------------------------------------------ */
/* TITLE */
/* ------------------------------------------------ */

.eirene-title {

    text-align: center;

    font-size: 78px;

    font-weight: 900;

    background:
    linear-gradient(
    90deg,
    #7dd3fc,
    #60a5fa,
    #818cf8
    );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;

    margin-top: 10px;

    letter-spacing: -2px;

    text-shadow:
    0 0 35px rgba(96,165,250,0.20);
}

/* ------------------------------------------------ */
/* LOGO */
/* ------------------------------------------------ */

.logo {

    text-align: center;

    font-size: 70px;

    margin-bottom: -15px;

    filter:
    drop-shadow(0 0 18px rgba(96,165,250,0.22));
}

/* ------------------------------------------------ */
/* SUBTITLE */
/* ------------------------------------------------ */

.subtitle {

    text-align: center;

    color: #cbd5e1;

    font-size: 22px;

    margin-top: 8px;

    margin-bottom: 12px;

    letter-spacing: 0.3px;
}

/* ------------------------------------------------ */
/* BRANDING */
/* ------------------------------------------------ */

.branding {

    text-align: center;

    color: #64748b;

    font-size: 13px;

    margin-bottom: 35px;
}

/* ------------------------------------------------ */
/* CHAT MESSAGE */
/* ------------------------------------------------ */

.stChatMessage {

    background:
    rgba(15,23,42,0.82);

    border:
    1px solid rgba(255,255,255,0.05);

    backdrop-filter:
    blur(24px);

    border-radius: 22px;

    padding: 20px;

    margin-bottom: 18px;

    box-shadow:
    0 0 28px rgba(0,0,0,0.22);
}

/* ------------------------------------------------ */
/* CHAT TEXT */
/* ------------------------------------------------ */

[data-testid="stChatMessageContent"] p,
[data-testid="stChatMessageContent"] div {

    color: #f8fafc !important;

    font-size: 17px !important;

    line-height: 1.92 !important;
}

/* ------------------------------------------------ */
/* SIDEBAR */
/* ------------------------------------------------ */

section[data-testid="stSidebar"] {

    background:
    linear-gradient(
    180deg,
    #010816 0%,
    #06111f 100%
    );

    border-right:
    1px solid rgba(255,255,255,0.05);
}

/* ------------------------------------------------ */
/* SIDEBAR TITLE */
/* ------------------------------------------------ */

.sidebar-title {

    color: #7dd3fc;

    font-size: 28px;

    font-weight: 800;

    margin-bottom: 20px;
}

/* ------------------------------------------------ */
/* MEMORY BLOCK */
/* ------------------------------------------------ */

.memory-block {

    background:
    rgba(255,255,255,0.03);

    border-radius: 14px;

    padding: 14px;

    margin-bottom: 12px;

    border:
    1px solid rgba(255,255,255,0.05);

    color:
    #cbd5e1;

    font-size: 14px;

    line-height: 1.5;
}

/* ------------------------------------------------ */
/* THINKING */
/* ------------------------------------------------ */

.thinking {

    color: #7dd3fc;

    font-style: italic;
}

/* ------------------------------------------------ */
/* INPUT CONTAINER */
/* ------------------------------------------------ */

.stChatInputContainer {

    background:
    rgba(15,23,42,0.94);

    border:
    1px solid rgba(125,211,252,0.12);

    border-radius: 20px;

    padding: 12px;

    box-shadow:
    0 0 25px rgba(59,130,246,0.08);
}

/* ------------------------------------------------ */
/* INPUT BOX */
/* ------------------------------------------------ */

textarea {

    color: #ffffff !important;

    background:
    rgba(2,6,23,0.92) !important;

    border-radius: 14px !important;

    font-size: 17px !important;

    caret-color: #7dd3fc !important;
}

/* ------------------------------------------------ */
/* PLACEHOLDER */
/* ------------------------------------------------ */

textarea::placeholder {

    color: #94a3b8 !important;
}

/* ------------------------------------------------ */
/* STREAMED TEXT */
/* ------------------------------------------------ */

.stMarkdown {

    color: #f8fafc !important;
}

/* ------------------------------------------------ */
/* SCROLLBAR */
/* ------------------------------------------------ */

::-webkit-scrollbar {

    width: 8px;
}

::-webkit-scrollbar-thumb {

    background:
    rgba(125,211,252,0.22);

    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------------------------
# HEADER
# ------------------------------------------------

st.markdown(
    "<div class='logo'>🧠</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='eirene-title'>Eirene AI</div>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class='subtitle'>
    Emotionally Adaptive Cognitive Intelligence
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class='branding'>
    Powered by <b>BJNEXUSAI</b>
    </div>
    """,
    unsafe_allow_html=True
)

# ------------------------------------------------
# SESSION STATE
# ------------------------------------------------

if "messages" not in st.session_state:

    st.session_state.messages = []

# ------------------------------------------------
# SIDEBAR
# ------------------------------------------------

with st.sidebar:

    st.markdown(
        "<div class='sidebar-title'>Memory</div>",
        unsafe_allow_html=True
    )

    if st.session_state.messages:

        recent_messages = st.session_state.messages[-6:]

        for msg in recent_messages:

            role = msg["role"].upper()

            content = msg["content"][:140]

            st.markdown(
                f"""
                <div class='memory-block'>
                <b>{role}</b><br><br>
                {content}
                </div>
                """,
                unsafe_allow_html=True
            )

    else:

        st.caption("No memories yet.")

# ------------------------------------------------
# CHAT HISTORY
# ------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# ------------------------------------------------
# INPUT
# ------------------------------------------------

user_input = st.chat_input(
    "Speak freely. Eirene is listening..."
)

# ------------------------------------------------
# PROCESS
# ------------------------------------------------

if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):

        st.markdown(user_input)

    with st.chat_message("assistant"):

        thinking = st.empty()

        thinking.markdown(
            "<div class='thinking'>⏳ Eirene is reflecting...</div>",
            unsafe_allow_html=True
        )

        try:

            response = requests.post(
                "http://127.0.0.1:8000/chat",
                json={
                    "message": user_input
                },
                timeout=120
            )

            data = response.json()

            ai_reply = data.get(
                "response",
                "No response generated."
            )

        except Exception as e:

            ai_reply = (
                "Eirene is momentarily recalibrating "
                "her cognitive state."
            )

            thinking.markdown(
                f"""
                <div class='thinking'
                style='color:#ef4444;'>
                ⚠️ System Alert: {str(e)}
                </div>
                """,
                unsafe_allow_html=True
            )

            time.sleep(2)

        thinking.empty()

        stream_placeholder = st.empty()

        displayed_text = ""

        for char in ai_reply:

            displayed_text += char

            stream_placeholder.markdown(
                f"{displayed_text}▌"
            )

            time.sleep(0.004)

        stream_placeholder.markdown(
            displayed_text
        )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": ai_reply
        }
    )