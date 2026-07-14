import os
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

# ── Page Configuration ─────────────────────────────────────────
st.set_page_config(
    page_title="AI YouTube Script Studio",
    page_icon="🎬",
    layout="wide",
)

# ── High-Density Vintage Dashboard System ──────────────────────
st.markdown(
    """
    <style>
    /* Importing the classic elegant UI fonts along with clean handwriting typography */
    @import url('https://fonts.googleapis.com/css2?family=Delius&family=Instrument+Sans:wght@400;500;600;700&family=Playfair+Display:wght@700&display=swap');
    
    /* Core Layout & Vintage Palette Restoration */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #F9F6F0 !important;
        color: #1E2022 !important;
    }
    
    /* Global Element Compression & Layout White Space Removal */
    [data-testid="stMarkdownContainer"] {
        gap: 0px !important;
    }
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
    }
    
    /* Typography Override (Instrument Sans) */
    p, label, .stMarkdown p, [data-testid="stWidgetLabel"] p {
        font-family: 'Instrument Sans', sans-serif !important;
        color: #1E2022 !important;
        font-weight: 500;
        font-size: 14px !important;
    }
    
    /* Editorial Serif Headings (Playfair Display) */
    h1, h2, h3, h4, h5, h6, .stSubheader {
        font-family: 'Playfair Display', serif !important;
        color: #1E2022 !important;
        font-weight: 700 !important;
        margin-top: 0px !important;
        margin-bottom: 4px !important;
        letter-spacing: -0.2px;
    }
    
    /* Compact Settings Panel with Compressed Margin */
    .config-workspace-box {
        background-color: #FFFFFF;
        padding: 12px 18px;
        border-radius: 4px;
        border: 1px solid #E6DFD3;
        box-shadow: 0 4px 20px rgba(30, 32, 34, 0.03);
        margin-top: 0px !important;
        margin-bottom: 0px !important;
    }
    
    /* Script Teleprompter Canvas (Delius Font + Clean Tight Layout) */
    .script-document-canvas {
        background-color: #FCFAFA;
        border: 1px dashed #C87A65;
        border-top: 4px solid #C87A65;
        padding: 18px 22px;
        border-radius: 2px;
        margin-top: 6px;
        font-family: 'Delius', cursive;
        font-size: 16px;
        line-height: 1.5;
        color: #2C302E;
        white-space: pre-line; /* Keeps line breaks clean without massive empty gaps */
        box-shadow: 0 2px 10px rgba(0,0,0,0.01);
    }
    
    /* Explicitly lock handwriting font for script interior elements */
    .script-document-canvas * {
        font-family: 'Delius', cursive !important;
    }
    
    /* Vintage Meta Badges */
    .vintage-meta-pill {
        background: #F4EFE6;
        border-radius: 2px;
        padding: 4px 10px;
        display: inline-block;
        margin-right: 6px;
        border: 1px solid #E6DFD3;
        font-size: 11px;
        font-family: 'Instrument Sans', sans-serif;
        color: #5C6065;
        font-weight: 600;
    }

    /* Terracotta Accent Button Override */
    div.stButton > button:first-child {
        background-color: #C87A65 !important;
        border-color: #C87A65 !important;
        color: #FFFFFF !important;
        border-radius: 2px !important;
        font-family: 'Instrument Sans', sans-serif !important;
        font-weight: 600 !important;
        font-size: 14px !important;
        padding: 8px 16px;
        margin-top: 4px;
        transition: all 0.2s ease;
    }
    div.stButton > button:first-child:hover {
        background-color: #B46551 !important;
        border-color: #B46551 !important;
    }
    
    /* Layout structural tuning with minimized height gaps */
    hr {
        margin: 8px 0 !important;
    }
    
    /* Direct adjustments to shrink vertical margins inside input component groups */
    div[data-testid="stVerticalBlock"] > div {
        margin-bottom: 0px !important;
        padding-bottom: 0px !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Prompt Template ────────────────────────────────────────────
SCRIPT_TEMPLATE = """
You are an expert YouTube script writer who has written scripts for
top creators with millions of subscribers.

Write a complete, engaging YouTube script for the following:

Topic:    {topic}
Tone:     {tone}
Duration: {duration} minutes
Audience: {audience}
Keywords: {keywords}

Structure the script EXACTLY like this layout, avoiding structural double spacing or empty buffer rows:

[HOOK - 30 seconds]
(attention-grabbing opening line or question)

[INTRO - 1 minute]
(introduce yourself and what the video covers)

[SECTION 1: {section1_title}]
(detailed content for section 1)

[SECTION 2: {section2_title}]
(detailed content for section 2)

[SECTION 3: {section3_title}]
(detailed content for section 3)

[CTA - 30 seconds]
(call to action: like, subscribe, comment)

[END SCREEN]
(outro and teaser for next video)

Write naturally as if speaking to camera. Insert [PAUSE] or directional tokens cleanly directly into the dialogue rows.
"""

PROMPT = PromptTemplate(
    input_variables=[
        "topic",
        "tone",
        "duration",
        "audience",
        "keywords",
        "section1_title",
        "section2_title",
        "section3_title",
    ],
    template=SCRIPT_TEMPLATE,
)


def generate_script(topic, tone, duration, audience, keywords, s1, s2, s3):
    """Generate YouTube script using Groq Llama."""
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        return None, "System Configuration Error: Missing API key."

    try:
        llm = ChatGroq(
            api_key=api_key,
            model="llama-3.1-8b-instant",
            temperature=0.72,
            max_tokens=2500,
        )
        chain = PROMPT | llm
        response = chain.invoke(
            {
                "topic": topic,
                "tone": tone,
                "duration": duration,
                "audience": audience,
                "keywords": keywords,
                "section1_title": s1,
                "section2_title": s2,
                "section3_title": s3,
            }
        )
        return response.content, None
    except Exception as e:
        return None, str(e)


# Initialize Session State
if "generated_script" not in st.session_state:
    st.session_state.generated_script = None

# ── Dashboard Header ──────────────────────────────────────────
st.title("🎬 YouTube Script Studio")
st.markdown("<p style='margin-top:-6px; color:#5C6065; font-size:13px;'>An elegant production workspace tailored for drafting, structuring, and optimizing video narratives.</p>", unsafe_allow_html=True)
st.markdown("<hr style='border-top: 1px solid #E6DFD3;'>", unsafe_allow_html=True)


# ── Configuration Panel (Top Section) ───────────────────────────
st.markdown('<div class="config-workspace-box">', unsafe_allow_html=True)
st.markdown("### ✒️ Studio Configuration Matrix")

col1, col2 = st.columns(2, gap="large")

with col1:
    topic = st.text_input(
        "**Video Concept Topic \***",
        placeholder="e.g., The Architecture of Minimalist Living Spaces",
    )
    audience = st.text_input(
        "**Target Demographics**",
        value="Creatives and designers seeking intentional workflow adjustments",
    )
    keywords = st.text_input(
        "**SEO Tags & Search Meta**",
        placeholder="minimalist design, creative routine, space optimization",
    )

with col2:
    col_tone, col_time = st.columns(2)
    with col_tone:
        tone = st.selectbox(
            "**Narrative Style Choice**",
            [
                "Energetic and enthusiastic",
                "Professional and educational",
                "Casual and conversational",
                "Storytelling and narrative",
                "Motivational and inspiring",
                "Humorous and entertaining",
            ],
        )
    with col_time:
        duration = st.selectbox(
            "**Target Video Runtime**",
            ["5", "8", "10", "12", "15", "20"],
            index=2,
        )

    st.markdown("<div style='margin-top: 4px; margin-bottom: 2px; font-weight:700; font-size:13px; color:#1E2022;'>📍 Section Benchmarks</div>", unsafe_allow_html=True)
    
    sub_c1, sub_c2, sub_c3 = st.columns(3)
    with sub_c1:
        s1 = st.text_input("S1 Title", placeholder="Intro to Topic", label_visibility="collapsed")
    with sub_c2:
        s2 = st.text_input("S2 Title", placeholder="Core Concepts", label_visibility="collapsed")
    with sub_c3:
        s3 = st.text_input("S3 Title", placeholder="Practical Tips", label_visibility="collapsed")

    s1 = s1 or "Introduction to the Topic"
    s2 = s2 or "Core Concepts and Techniques"
    s3 = s3 or "Practical Tips and Next Steps"

compile_clicked = st.button("Generate Production Script", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)


# ── Production Teleprompter Canvas (Bottom Section) ─────────────
st.markdown("<hr style='border-top: 1px solid #E6DFD3;'>", unsafe_allow_html=True)
st.markdown("### 📄 Production Teleprompter Output")

if compile_clicked:
    if not topic.strip():
        st.error("Please assign a valid Topic entry before requesting output generation.")
    else:
        with st.spinner("Compiling structural telemetry script..."):
            script, error = generate_script(
                topic,
                tone,
                duration,
                audience,
                keywords or "creative broadcast production",
                s1,
                s2,
                s3,
            )
            if error:
                st.error(error)
            else:
                st.session_state.generated_script = script

if st.session_state.generated_script:
    word_count = len(st.session_state.generated_script.split())
    calculated_pace = round(word_count / 150, 1)

    # Clean Metadata Bar
    st.markdown(
        f"""
        <div style="margin-bottom: 6px;">
            <span class="vintage-meta-pill">📋 METRICS: {word_count} words</span>
            <span class="vintage-meta-pill">⏱️ RUNTIME PACE: {calculated_pace} min read</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Compressed Delius Script Canvas
    st.markdown(
        f'<div class="script-document-canvas">{st.session_state.generated_script}</div>',
        unsafe_allow_html=True,
    )

    st.markdown("<div style='margin-top: 8px;'></div>", unsafe_allow_html=True)

    download_filename = topic[:20].replace(" ", "_").lower() + "_studio_draft.txt"
    st.download_button(
        label="⬇️ Export Studio Transcript (.txt)",
        data=st.session_state.generated_script,
        file_name=download_filename,
        mime="text/plain",
        use_container_width=True,
    )
else:
    st.info(
        "The production desk is clear. Complete the parameter configuration matrix parameters block above to populate this workspace canvas."
    )

st.markdown("<br><hr style='border-top: 1px solid #E6DFD3;'>", unsafe_allow_html=True)
st.caption("🎬 Studio Engine Matrix Protocol · Backed by Llama Architecture Pipelines.")