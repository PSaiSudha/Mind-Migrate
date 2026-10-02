import streamlit as st
import numpy as np
import pandas as pd
import time
from datetime import datetime
from utils.tips import get_wellness_tip

# Page Configuration
st.set_page_config(
    page_title="Mind Migrate | Dashboard",
    page_icon="🧠",
    layout="wide"
)

# Custom CSS for modern card styling
st.markdown("""
    <style>
    .stApp { background-color: #f8fafc; }
    .card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        border: 1px solid #e2e8f0;
    }
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; background-color: #10b981; color: white; }
    .stButton>button:hover { background-color: #059669; }
    </style>
""", unsafe_allow_html=True)

# --- TOP HEADER ---
col_h1, col_h2 = st.columns([4, 1])
with col_h1:
    st.markdown("### 🧠 Mind Migrate")
with col_h2:
    st.markdown("<p style='text-align: right; color: #64748b; font-size: 0.9rem;'>Passive Mood Intelligence</p>", unsafe_allow_html=True)

st.divider()

# --- 1. REAL-TIME MOOD STATE BANNER ---
st.markdown("""
    <div style='background: white; padding: 25px; border-radius: 12px; border: 1px solid #e2e8f0; margin-bottom: 20px;'>
        <p style='margin: 0; color: #64748b; font-size: 0.85rem; font-weight: bold; text-transform: uppercase;'>Real-Time Mood State</p>
        <h1 style='color: #0f172a; margin: 5px 0; font-size: 2rem;'>Positive & Upbeat 🌿</h1>
        <p style='margin: 0; color: #10b981; font-size: 0.9rem;'>⚡ 77% confidence &nbsp;&bull;&nbsp; <span style='color: #64748b;'>updated just now</span></p>
    </div>
""", unsafe_allow_html=True)

# --- MAIN DASHBOARD GRID (3 Columns) ---
col_left, col_mid, col_right = st.columns([1.2, 1.2, 0.9], gap="medium")

with col_left:
    st.markdown("""
        <div class='card'>
            <div style='display: flex; justify-content: space-between; align-items: center;'>
                <h4 style='margin: 0; color: #1e293b;'>Mood Classifier</h4>
                <span style='font-size: 0.8rem; background: #f1f5f9; padding: 2px 8px; border-radius: 4px; color: #475569;'>24h | 7d</span>
            </div>
            <p style='color: #64748b; font-size: 0.8rem; margin-top: 2px;'>ML-classified mood curve</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Chart representation
    chart_data = pd.DataFrame(
        np.random.randn(20, 1) * 0.5 + 5,
        columns=['Mood Score']
    )
    st.line_chart(chart_data, height=220, color="#10b981")

with col_mid:
    st.markdown("""
        <div class='card'>
            <h4 style='margin: 0; color: #1e293b;'>App & Typing Telemetry</h4>
            <p style='color: #64748b; font-size: 0.8rem; margin-top: 2px;'>Passive behavioral signals</p>
        </div>
    """, unsafe_allow_html=True)
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Keystrokes/min", "50")
    m2.metric("Backspace rate", "10%")
    m3.metric("Error rate", "4%")
    
    st.markdown("<p style='font-size: 0.85rem; color: #64748b; margin-top: 15px;'><b>Top apps - today</b> (20h 41m total)</p>", unsafe_allow_html=True)
    st.markdown("Terminal")
    st.progress(85)
    st.markdown("Spotify")
    st.progress(65)
    st.markdown("VS Code")
    st.progress(50)

with col_right:
    # Background Worker Card
    st.markdown("""
        <div style='background: #0f172a; padding: 18px; border-radius: 12px; color: white; margin-bottom: 20px;'>
            <div style='display: flex; justify-content: space-between; align-items: center;'>
                <h4 style='margin: 0; color: white; font-size: 1rem;'>Background Worker</h4>
                <span style='color: #4ade80; font-size: 0.8rem;'>● running</span>
            </div>
            <hr style='border-color: #334155; margin: 10px 0;'>
            <p style='margin: 8px 0; font-size: 0.85rem; color: #cbd5e1;'>🟢 <b>Behavior Logger</b><br><span style='color: #94a3b8; font-size: 0.75rem;'>Typing & app usage</span></p>
            <p style='margin: 8px 0; font-size: 0.85rem; color: #cbd5e1;'>🟢 <b>ML Mood Model</b><br><span style='color: #94a3b8; font-size: 0.75rem;'>scikit-learn classifier</span></p>
            <p style='margin: 8px 0; font-size: 0.85rem; color: #cbd5e1;'>🟢 <b>Schedule Worker</b><br><span style='color: #94a3b8; font-size: 0.75rem;'>Periodic background tasks</span></p>
        </div>
    """, unsafe_allow_html=True)

# --- LOWER ROW: WELLNESS TIP & PRIVACY CONTROLS ---
col_low1, col_low2 = st.columns([1.4, 1], gap="medium")

with col_low1:
    st.markdown("""
        <div class='card'>
            <h4 style='margin: 0; color: #1e293b;'>💡 Contextual Wellness Tip</h4>
            <p style='color: #64748b; font-size: 0.8rem; margin-top: 2px;'>Tailored to your current signal</p>
            <div style='background: #f8fafc; padding: 12px; border-radius: 8px; border-left: 4px solid #10b981; margin: 15px 0;'>
                <b style='color: #0f172a;'>Celebrate the win</b><br>
                <span style='color: #475569; font-size: 0.9rem;'>Positive mood detected. Consider journaling what went well today to reinforce this uplift for tomorrow.</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("🧘 Start 4-7-8 Breathing Exercise", type="primary"):
        st.success("Breathing session started! Inhale for 4s, hold for 7s, exhale for 8s.")

with col_low2:
    st.markdown("""
        <div class='card'>
            <h4 style='margin: 0; color: #1e293b; font-size: 1rem;'>🔒 Privacy & Consent</h4>
            <hr style='border-color: #e2e8f0; margin: 10px 0;'>
        </div>
    """, unsafe_allow_html=True)
    
    st.toggle("Anonymous mode (Strip identifiers)", value=True)
    st.toggle("On-device processing (Local store)", value=True)
    st.toggle("Consent to monitor telemetry", value=True)
    
    st.markdown("<p style='font-size: 0.75rem; color: #94a3b8; margin-top: 5px;'>AES-256 encrypted local store</p>", unsafe_allow_html=True)
    
    st.markdown("""
        <div style='background: #ffffff; padding: 12px; border-radius: 8px; border: 1px solid #e2e8f0; margin-top: 15px;'>
            <p style='margin: 0; font-size: 0.85rem; font-weight: bold; color: #1e293b;'>⚡ Resource Impact</p>
            <p style='margin: 5px 0 2px 0; font-size: 0.75rem; color: #64748b;'>Battery drain: 2.4 %/hr</p>
            <progress value='24' max='100' style='width:100%; height: 6px;'></progress>
            <p style='margin: 5px 0 2px 0; font-size: 0.75rem; color: #64748b;'>CPU usage: 1.8 %</p>
            <progress value='18' max='100' style='width:100%; height: 6px;'></progress>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.divider()
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 0.8rem;'>Mind Migrate Project — Professional Dashboard UI</p>", unsafe_allow_html=True)