import streamlit as st

# (Mock functions assuming they come from your local modules)
# from parser import extract_text_from_pdf
# from matcher import calculate_similarity_score
# from skills import extract_skills

# --- 1. PREMIUM PAGE SETUP ---
st.set_page_config(
    page_title="Smart Resume Screening System",
    page_icon="✨",
    layout="centered", 
    initial_sidebar_state="collapsed"
)

# --- 2. LUXURY SAAS SYSTEM CSS ---
st.markdown("""
<style>
/* -------------------------
    GLOBAL DARK THEME
------------------------- */
.stApp {
    background: linear-gradient(135deg, #020617, #0f172a, #111827);
}

/* -------------------------
    TEXT COLORS & HEADERS
------------------------- */
h1, h2, h3, h4, h5, h6 {
    color: #f8fafc !important;
    font-weight: 700 !important;
}
p, label, [data-testid="stMarkdownContainer"] p {
    color: #cbd5e1 !important;
}

/* -------------------------
    TEXT AREA & INPUTS
------------------------- */
.stTextArea textarea {
    background-color: #1e293b !important;
    color: #f8fafc !important;
    border: 1px solid #334155 !important;
    border-radius: 12px !important;
}
.stTextArea textarea:focus {
    border-color: #6366f1 !important;
    box-shadow: 0 0 0 2px rgba(99,102,241,.3) !important;
}

/* -------------------------
    FILE UPLOADER
------------------------- */
[data-testid="stFileUploader"] {
    background: #111827 !important;
    border: 2px dashed #475569 !important;
    border-radius: 16px !important;
    padding: 20px !important;
}
[data-testid="stFileUploader"] section {
    background: #111827 !important;
}

/* -------------------------
    BUTTON
------------------------- */
.stButton button {
    background: linear-gradient(90deg, #7c3aed, #2563eb) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    height: 50px !important;
    font-weight: 700 !important;
    font-size: 16px !important;
    transition: all 0.3s ease;
}
.stButton button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 20px rgba(124, 58, 237, 0.3) !important;
}

/* -------------------------
    OUTPUT DYNAMIC METRIC GRID
------------------------- */
.metric-row {
    display: flex;
    gap: 16px;
    margin: 20px 0;
    flex-wrap: wrap;
}
.metric-box {
    flex: 1;
    min-width: 150px;
    background: #1e293b;
    padding: 24px 16px;
    border-radius: 16px;
    border: 1px solid #334155;
    text-align: center;
    box-shadow: 0 4px 20px rgba(0,0,0,0.2);
}
.metric-num {
    font-size: 36px;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 4px;
}
.metric-title {
    color: #94a3b8;
    font-size: 14px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

/* -------------------------
    ALERT BANNERS
------------------------- */
.alert-banner {
    padding: 16px;
    border-radius: 12px;
    font-size: 16px;
    margin-bottom: 24px;
    border-left: 5px solid;
}
.alert-excellent { background: rgba(34,197,94,.1); border-color: #22c55e; color: #4ade80; }
.alert-good { background: rgba(59,130,246,.1); border-color: #3b82f6; color: #60a5fa; }
.alert-average { background: rgba(234,179,8,.1); border-color: #eab308; color: #fde047; }
.alert-poor { background: rgba(239,68,68,.1); border-color: #ef4444; color: #f87171; }

/* -------------------------
    SKILL PILLS STYLE
------------------------- */
.skill-pills {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 500;
    margin: 4px;
}
.pill-base { background: #334155; color: #e2e8f0; border: 1px solid #475569; }
.pill-match { background: rgba(34,197,94,.15); color: #4ade80; border: 1px solid rgba(34,197,94,.3); }
.pill-miss { background: rgba(239,68,68,.15); color: #f87171; border: 1px solid rgba(239,68,68,.3); }

/* -------------------------
    STYLING TABS
------------------------- */
.stTabs [data-baseweb="tab-list"] {
    gap: 10px;
}
.stTabs [data-baseweb="tab"] {
    background-color: #111827 !important;
    border-radius: 8px 8px 0 0 !important;
    padding: 10px 20px !important;
    color: #94a3b8 !important;
}
.stTabs [data-baseweb="tab"][aria-selected="true"] {
    color: #ffffff !important;
    background-color: #1e293b !important;
    border-bottom: 2px solid #6366f1 !important;
}
</style>
""", unsafe_allow_html=True)

# --- 3. BRAND HEADER ---
st.markdown("""
    <div style='text-align: center; padding: 10px 0 30px 0;'>
        <h1 style='font-size: 36px; font-weight: 800; color: #ffffff; margin-bottom: 8px;'>📋 Smart Resume Screening System</h1>
        <p style='color: #94a3b8; font-size: 16px;'>Verify candidate capabilities against performance benchmarks instantly.</p>
    </div>
""", unsafe_allow_html=True)

# --- 4. JOB DESCRIPTION ---
st.markdown("#### 🎯 1. Job Description Matrix")
job_description = st.text_area(
    "",
    placeholder="Enter required industry skills, frameworks, experience level, or tools...",
    height=150,
    label_visibility="collapsed"
)

# --- 5. RESUME UPLOADER ---
st.markdown("#### 📄 2. Dossier Ingestion")
uploaded_file = st.file_uploader(
    "",
    type=["pdf"],
    label_visibility="collapsed",
    help="Upload candidate resume in plain standard PDF formatting."
)

st.markdown("<br>", unsafe_allow_html=True)

# --- 6. STEP 3: ANALYSIS INITIATOR BUTTON ---
if st.button("🚀 Run Screening Analysis", type="primary", use_container_width=True):

    if not job_description:
        st.error("Operation Halted: Please input the target Job Description framework first.")
        st.stop()

    if not uploaded_file:
        st.error("Operation Halted: Missing Candidate Resume file dependency.")
        st.stop()

    # --- 7. CORE AI COMPUTATION PIPELINE ---
    with st.spinner("Executing extraction agents, parsing matrix tokens, and evaluating semantic closeness..."):
        try:
            # --- Dummy Logic (Replace with actual imports in production) ---
            resume_text = "Sample extracted resume text with python and react."
            jd_skills = ["python", "react", "aws", "docker"]
            resume_skills = ["python", "react", "git"]
            
            # --- Agar aapka components work kr rha hai toh unhide kar lein:
            # resume_text = extract_text_from_pdf(uploaded_file)
            # jd_skills = extract_skills(job_description)
            # resume_skills = extract_skills(resume_text)

            matched_skills = list(set(jd_skills) & set(resume_skills))
            missing_skills = list(set(jd_skills) - set(resume_skills))

            if len(jd_skills) > 0:
                skill_match_score = round((len(matched_skills) / len(jd_skills)) * 100, 2)
            else:
                skill_match_score = 0.0

            # Mock similarity score for representation
            similarity_score = 75.0 
            # similarity_score = round(float(calculate_similarity_score(job_description, resume_text)), 2)
            
            final_score = round((skill_match_score * 0.7) + (similarity_score * 0.3), 2)

            # --- 8. STEP 4: INTELLIGENCE RESULT REPORT (BOTTOM) ---
            st.markdown("<br><hr style='border-color: #334155;'>", unsafe_allow_html=True)
            st.markdown("### 📈 Evaluation Intelligence Report")

            # Dynamic System Decision Status Box
            if final_score >= 80:
                st.markdown(f'<div class="alert-banner alert-excellent">🟢 <b>System Consensus: Excellent Candidate Fit</b> (Score: {final_score}%)</div>', unsafe_allow_html=True)
            elif final_score >= 60:
                st.markdown(f'<div class="alert-banner alert-good">🔵 <b>System Consensus: Strong Match Contender</b> (Score: {final_score}%)</div>', unsafe_allow_html=True)
            elif final_score >= 40:
                st.markdown(f'<div class="alert-banner alert-average">🟡 <b>System Consensus: Mixed Alignment Profile</b> (Score: {final_score}%)</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="alert-banner alert-poor">🔴 <b>System Consensus: Weak Variance Correlation</b> (Score: {final_score}%)</div>', unsafe_allow_html=True)

            # Clean UI Grid Metric Blocks
            st.markdown(f"""
                <div class="metric-row">
                    <div class="metric-box" style="border-bottom: 4px solid #6366f1;">
                        <div class="metric-num">{final_score}%</div>
                        <div class="metric-title">Weighted Fit</div>
                    </div>
                    <div class="metric-box" style="border-bottom: 4px solid #22c55e;">
                        <div class="metric-num">{skill_match_score}%</div>
                        <div class="metric-title">Skill Match</div>
                    </div>
                    <div class="metric-box" style="border-bottom: 4px solid #0ea5e9;">
                        <div class="metric-num">{similarity_score}%</div>
                        <div class="metric-title">Semantic Context</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            # Tab Elements for clean compartmentalization
            tab_skills, tab_audit, tab_raw = st.tabs(["🎯 Competency Maps", "📊 Operational Logs", "📑 Text Archive"])

            with tab_skills:
                sub_left, sub_right = st.columns(2)
                
                with sub_left:
                    st.markdown("##### ✅ Intersecting Capabilities Found")
                    if matched_skills:
                        pills_html = "".join([f'<span class="skill-pills pill-match">✓ {s}</span>' for s in matched_skills])
                        st.markdown(pills_html, unsafe_allow_html=True)
                    else:
                        st.caption("No matching skill tags registered.")

                    st.markdown("<br>##### 📋 Total Job Targets Set", unsafe_allow_html=True)
                    if jd_skills:
                        pills_html = "".join([f'<span class="skill-pills pill-base">{s}</span>' for s in jd_skills])
                        st.markdown(pills_html, unsafe_allow_html=True)
                    else:
                        st.caption("No core skills mapped from JD.")

                with sub_right:
                    st.markdown("##### ❌ Identified Competency Gaps")
                    if missing_skills:
                        pills_html = "".join([f'<span class="skill-pills pill-miss">⚠️ {s}</span>' for s in missing_skills])
                        st.markdown(pills_html, unsafe_allow_html=True)
                    else:
                        st.success("Perfect coverage variance! No missing gaps found.")

                    st.markdown("<br>##### 📄 Parsed Profile Inventory", unsafe_allow_html=True)
                    if resume_skills:
                        pills_html = "".join([f'<span class="skill-pills pill-base">{s}</span>' for s in resume_skills])
                        st.markdown(pills_html, unsafe_allow_html=True)
                    else:
                        st.caption("No skills identified inside resume document.")

            with tab_audit:
                st.markdown("##### Quantitative Distribution")
                st.write(f"The profile matched **{len(matched_skills)}** out of **{len(jd_skills)}** targeted skills benchmarks.")
                
                st.markdown("<br><b>Skill Base Distribution Coverage</b>", unsafe_allow_html=True)
                st.progress(skill_match_score / 100)
                
                st.markdown("<b>Contextual Similarity Distribution Mapping</b>", unsafe_allow_html=True)
                st.progress(similarity_score / 100)

            with tab_raw:
                st.markdown("##### Secure Streamlit Text Snippet (First 5k characters)")
                st.text_area("Extracted OCR Content", value=resume_text[:5000], height=250, disabled=True, label_visibility="collapsed")

        except Exception as e:
            st.error(f"Execution Error Encountered: {str(e)}")