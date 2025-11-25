import streamlit as st
from PIL import Image
import io
import time
from utils.backend_client import BackendClient

def render():
    st.markdown("""
    <style>
        .section-title {
            font-size: 1.3rem;
            font-weight: 600;
            color: #333;
            margin: 1rem 0 0.8rem 0;
            border-bottom: 2px solid #667eea;
            padding-bottom: 0.5rem;
        }
        .analysis-card {
            background: white;
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            margin-bottom: 1rem;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-title">Product Image Upload</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        uploaded_file = st.file_uploader(
            "Choose a product image",
            type=["jpg", "jpeg", "png", "webp"],
            help="Clear, straight-on photos work best"
        )
        
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, use_column_width=True, caption="Uploaded Product Image")
            
    
    with col2:
        st.markdown('<div class="section-title">Dietary Requirement</div>', unsafe_allow_html=True)
        
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
                "Analyze Product",
                use_container_width=True,
                type="primary"
            )
        
        if analyze_button:
            try:
                backend = BackendClient()
                
                if not backend.health_check():
                    st.error(" Backend server is not available. Please ensure the backend server is running.")
                    return
                
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
                        st.success("Analysis completed successfully")
                    
                    except Exception as e:
                        st.error(f" Analysis failed: {str(e)}")
            
            except Exception as e:
                st.error(f" Error: {str(e)}")
    
    elif uploaded_file is None:
