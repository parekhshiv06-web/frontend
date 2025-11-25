import streamlit as st
from PIL import Image
import io
import time
from utils.backend_client import BackendClient

st.set_page_config(
    page_title="Food Product Analyzer",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
/* Radio buttons */
[data-baseweb="radio"] > div > div [aria-checked="true"] {
    background: linear-gradient(90deg, #764ba2 0%, #667eea 100%) !important;
    border-color: #764ba2 !important;
}
[data-baseweb="radio"] > div > div [aria-checked="true"] svg {
    color: #fff !important;
}

/* Checkboxes */
[data-baseweb="checkbox"] [aria-checked="true"] {
    background: linear-gradient(90deg, #764ba2 0%, #667eea 100%) !important;
    border-color: #764ba2 !important;
}
[data-baseweb="checkbox"] [aria-checked="true"] svg {
    color: #fff !important;
}

/* Select/Dropdown */
[data-baseweb="select"] [aria-selected="true"] {
    background: linear-gradient(90deg, #764ba2 0%, #667eea 100%) !important;
    color: #fff !important;
}
[data-baseweb="menu"] [aria-selected="true"] {
    background: linear-gradient(90deg, #764ba2 0%, #667eea 100%) !important;
    color: #fff !important;
}

/* Buttons */
.stButton > button, .stButton > button:focus {
    background: linear-gradient(90deg, #764ba2 0%, #667eea 100%) !important;
    color: #fff !important;
    border: none !important;
    box-shadow: 0 2px 8px rgba(102,126,234,0.15);
}
.stButton > button:hover {
    background: linear-gradient(90deg, #667eea 0%, #764ba2 100%) !important;
    color: #fff !important;
    box-shadow: 0 4px 12px rgba(102,126,234,0.25) !important;
}
.stButton > button:active, .stButton > button:focus-visible {
    outline: 2px solid #764ba2 !important;
    color: #fff !important;
}

/* Progress bar */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #764ba2 0%, #667eea 100%) !important;
}
    .jumbotron {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 2rem;
        border-radius: 12px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .jumbotron h1 {
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0 0 0.5rem 0;
        letter-spacing: -0.5px;
    }
    .jumbotron p {
        font-size: 1.2rem;
        margin: 0;
        opacity: 0.95;
    }
    .feature-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        border-left: 4px solid #667eea;
        margin-bottom: 1rem;
    }
    .feature-card h3 {
        color: #667eea;
        margin-top: 0;
    }
    .section-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: #333;
        margin-bottom: 1rem;
        border-bottom: 2px solid #667eea;
        padding-bottom: 0.5rem;
    }
</style>
<style>
/* File uploader browse button */
.stFileUploader > label span[data-testid="stFileUploadDropzone"] > div {
    background: linear-gradient(90deg, #764ba2 0%, #667eea 100%) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 6px !important;
    box-shadow: 0 2px 8px rgba(102,126,234,0.10);
}
.stFileUploader > label span[data-testid="stFileUploadDropzone"] > div:hover {
    background: linear-gradient(90deg, #667eea 0%, #764ba2 100%) !important;
    color: #fff !important;
    box-shadow: 0 4px 12px rgba(102,126,234,0.25) !important;
}
.stFileUploader > label span[data-testid="stFileUploadDropzone"] > div:active {
    outline: 2px solid #764ba2 !important;
    color: #fff !important;
}

/* File uploader input button */
.stFileUploader [data-testid="stFileUploaderDropZone"] button {
    background: linear-gradient(90deg, #764ba2 0%, #667eea 100%) !important;
    color: #fff !important;
    border: none !important;
}
.stFileUploader [data-testid="stFileUploaderDropZone"] button:hover {
    background: linear-gradient(90deg, #667eea 0%, #764ba2 100%) !important;
    color: #fff !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="jumbotron">
    <h1>Food Product Analyzer</h1>
    <p>Scan product labels and get instant dietary compliance analysis</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="feature-card">
    <h3>How It Works</h3>
    <p>Upload a clear photo of your product label, select your dietary requirement, and get instant analysis of ingredients against your dietary needs.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown('<div class="section-title">Step 1: Upload Product Image</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        "Choose a product image",
        type=["jpg", "jpeg", "png", "webp"],
        help="Clear, straight-on photos work best"
    )
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, use_column_width=True, caption="Uploaded Product Image")
        

with col2:
    st.markdown('<div class="section-title">Step 2: Select Dietary Requirement</div>', unsafe_allow_html=True)
    
    dietary_needs = []
    
    selected_option = st.radio(
        "Select a dietary requirement:",
        ["Gluten-Free", "Lactose-Free", "Vegetarian", "None"],
        horizontal=True,
        help="Choose one dietary requirement to check"
    )
    
    if selected_option == "Gluten-Free":
        dietary_needs.append("gluten-free")
    elif selected_option == "Lactose-Free":
        dietary_needs.append("lactose-free")
    elif selected_option == "Vegetarian":
        dietary_needs.append("vegetarian")
    
    if not dietary_needs:
        pass
    
st.divider()


if uploaded_file is not None and dietary_needs:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        analyze_button = st.button(
            " Analyze Product",
            use_container_width=True,
            type="primary"
        )
    
    if analyze_button:
        try:
            backend = BackendClient()
            print(f"Backend URL: {backend.base_url}")
            
            if not backend.health_check():
                st.error(" Backend server is not available. Please ensure the backend server is running.")
            else:
                with st.spinner("Processing image and analyzing ingredients..."):
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                    
                    image_bytes = io.BytesIO()
                    pil_image = Image.open(uploaded_file)
                    
                    if pil_image.mode in ('RGBA', 'LA', 'P'):
                        background = Image.new('RGB', pil_image.size, (255, 255, 255))
                        if pil_image.mode == 'P':
                            pil_image = pil_image.convert('RGBA')
                        background.paste(pil_image, mask=pil_image.split()[-1] if pil_image.mode == 'RGBA' else None)
                        pil_image = background
                    
                    pil_image.save(image_bytes, format='JPEG')
                    image_bytes.seek(0)
                    
                    progress_bar.progress(20)
                    status_text.text("Sending image to backend...")
                    
                    try:
                        analysis_results = backend.analyze_product(
                            image_bytes.getvalue(),
                            dietary_needs,
                            uploaded_file.name
                        )
                        
                        progress_bar.progress(100)
                        status_text.text("Analysis complete")
                        
                        st.session_state.analysis_results = analysis_results
                        
                        time.sleep(0.5)
                        st.success("Analysis completed successfully!")

                    
                    except Exception as e:
                        st.error(f" Analysis failed: {str(e)}")
        
        except Exception as e:
            st.error(f" Error: {str(e)}")

else:
    if uploaded_file is None:
        pass

st.divider()


if "analysis_results" in st.session_state and st.session_state.analysis_results is not None:
    results = st.session_state.analysis_results
    
    st.markdown('<div class="section-title">Analysis Results</div>', unsafe_allow_html=True)
    
    extracted_text = results.get("extracted_text", "")
    if extracted_text:
        st.markdown('<div class="section-title" style="font-size: 1.2rem; border-bottom: 1px solid #ddd; padding-bottom: 0.3rem;">Extracted Text from Label</div>', unsafe_allow_html=True)
        escaped_text = extracted_text[:500].replace("<", "&lt;").replace(">", "&gt;")
        ellipsis = "..." if len(extracted_text) > 500 else ""
        st.markdown(f"""
        <div style="background: #f5f5f5; padding: 1rem; border-radius: 8px; border-left: 3px solid #667eea;">
            <pre style="margin: 0; white-space: pre-wrap; word-wrap: break-word; font-family: monospace; font-size: 0.9rem;">{escaped_text}{ellipsis}</pre>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown('<div class="section-title" style="font-size: 1.2rem; border-bottom: 1px solid #ddd; padding-bottom: 0.3rem;">Dietary Compliance Analysis</div>', unsafe_allow_html=True)
    
    dietary_analysis = results.get("dietary_analysis", {})
    
    if dietary_analysis:
        cols = st.columns(len(dietary_analysis)) if len(dietary_analysis) > 0 else [st.columns(1)[0]]
        
        for idx, (category, analysis) in enumerate(dietary_analysis.items()):
            with cols[idx]:
                compliant = analysis.get("compliant", False)
                warnings = analysis.get("warnings", [])
                status_color = "#764ba2" if compliant else "#D32F2F"
                status_text = "COMPLIANT" if compliant else "NOT COMPLIANT"
                bg_color = "#ede7f6" if compliant else "#FFEBEE"
                border_color = "#b39ddb" if compliant else "#EF5350"
                warnings_html = f'<div style="font-size: 0.85rem; color: #666;">Warnings: {', '.join(warnings)}</div>' if warnings else '<div style="font-size: 0.85rem; color: #764ba2;">No concerning ingredients found</div>'
                
                st.markdown(f"""
                <div style="background: {bg_color}; padding: 1rem; border-radius: 8px; border-left: 4px solid {border_color}; text-align: center;">
                    <div style="font-weight: 600; color: #333; margin-bottom: 0.5rem; text-transform: capitalize;">{category.replace('-', ' ')}</div>
                    <div style="font-size: 1.2rem; font-weight: 700; color: {status_color}; margin-bottom: 0.5rem;">{status_text}</div>
                    {warnings_html}
                </div>
                """, unsafe_allow_html=True)
    
    st.divider()
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Analyze Another Product", use_container_width=True):
            st.session_state.analysis_results = None
            st.rerun()
