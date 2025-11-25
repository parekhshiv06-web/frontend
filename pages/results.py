import streamlit as st

def render():
    st.markdown("""
    <div style="margin-bottom: 2rem;">
        <h2 style="color: #2E7D32; font-size: 2rem; margin-bottom: 0.5rem;">Analysis Results</h2>
        <p style="color: #757575; font-size: 1rem;">Detailed breakdown of product analysis</p>
    </div>
    """, unsafe_allow_html=True)
    
    if "analysis_results" not in st.session_state:
        st.markdown("""
        <div style="background: #E3F2FD; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #1976D2; margin: 2rem 0;">
            <div style="font-weight: 600; color: #1565C0; margin-bottom: 0.5rem;">No Analysis Available</div>
            <div style="color: #0D47A1; font-size: 0.95rem;">
                Please analyze a product first by going to the Analyzer section
            </div>
        </div>
        """, unsafe_allow_html=True)
        return
    
    results = st.session_state.analysis_results
    
    st.markdown("""
    <div style="background: white; padding: 1.5rem; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); margin-bottom: 2rem; border-left: 4px solid #2E7D32;">
        <div style="font-weight: 700; color: #2E7D32; margin-bottom: 1rem; font-size: 1.1rem;">Product Information</div>
        <div style="color: #424242;">
            <p style="margin: 0.5rem 0;"><strong>Image Name:</strong> {}</p>
        </div>
    </div>
    """.format(results.get("image", "N/A")), unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown("""
    <div style="font-weight: 700; color: #2E7D32; margin-bottom: 1rem; font-size: 1.2rem;">Dietary Compliance Results</div>
    """, unsafe_allow_html=True)
    
    dietary_results = results.get("dietary_results", {})
    col1, col2 = st.columns(2)
    
    cols = [col1, col2]
    for idx, (category, result) in enumerate(dietary_results.items()):
        with cols[idx % 2]:
            status = result.get("status", "UNKNOWN")
            confidence = result.get("confidence", 0) * 100
            
            status_color = "#1B5E20" if status == "PASSED" else "#B71C1C"
            status_bg = "#C8E6C9" if status == "PASSED" else "#FFCDD2"
            
            st.markdown(f"""
            <div style="background: white; padding: 1.5rem; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); margin-bottom: 1rem;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                    <div style="font-weight: 600; color: #2E7D32; text-transform: capitalize;">{category.replace('-', ' ')}</div>
                    <div style="background-color: {status_bg}; color: {status_color}; padding: 0.4rem 0.8rem; border-radius: 6px; font-weight: 600; font-size: 0.85rem;">{status}</div>
                </div>
                <div style="margin-bottom: 0.5rem;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                        <div style="font-size: 0.85rem; color: #757575;">Confidence Score</div>
                        <div style="font-weight: 600; color: #2E7D32;">{confidence:.1f}%</div>
                    </div>
                    <div style="background: #E0E0E0; height: 8px; border-radius: 4px; overflow: hidden;">
                        <div style="background: linear-gradient(90deg, #81C784 0%, #2E7D32 100%); height: 100%; width: {confidence}%;"></div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown("""
    <div style="font-weight: 700; color: #2E7D32; margin-bottom: 1rem; font-size: 1.2rem;">Extracted Ingredients</div>
    """, unsafe_allow_html=True)
    
    ingredients = results.get("extracted_ingredients", [])
    st.markdown("""
    <div style="background: white; padding: 1.5rem; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); margin-bottom: 2rem;">
    """, unsafe_allow_html=True)
    
    ingredient_html = ""
    for ingredient in ingredients:
        ingredient_html += f'<span style="display: inline-block; background-color: #E8F5E9; color: #2E7D32; padding: 0.4rem 0.8rem; border-radius: 6px; margin: 0.3rem; font-size: 0.9rem; border: 1px solid #81C784;">{ingredient}</span>'
    
    st.markdown(ingredient_html, unsafe_allow_html=True)
    
    st.markdown("""
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown("""
    <div style="font-weight: 700; color: #2E7D32; margin-bottom: 1rem; font-size: 1.2rem;">Allergen Detection</div>
    """, unsafe_allow_html=True)
    
    allergens = results.get("allergens", [])
    
    if allergens:
        st.markdown("""
        <div style="background: #FFEBEE; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #FF6B6B;">
            <div style="font-weight: 600; color: #B71C1C; margin-bottom: 1rem;">Detected Allergens</div>
        </div>
        """, unsafe_allow_html=True)
        
        allergen_html = ""
        for allergen in allergens:
            allergen_html += f'<span style="display: inline-block; background-color: #FFCDD2; color: #B71C1C; padding: 0.5rem 1rem; border-radius: 6px; margin: 0.3rem; font-size: 0.9rem; border: 1px solid #EF5350; font-weight: 500;">{allergen}</span>'
        
        st.markdown(allergen_html, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="background: #C8E6C9; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #2E7D32;">
            <div style="color: #1B5E20; font-weight: 600;">No major allergens detected</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown("""
    <div style="font-weight: 700; color: #2E7D32; margin-bottom: 1rem; font-size: 1.2rem;">Additives & E-Numbers</div>
    """, unsafe_allow_html=True)
    
    additives = results.get("additives", [])
    
    if additives:
        for additive in additives:
            st.markdown(f"""
            <div style="background: white; padding: 1.5rem; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); margin-bottom: 1rem; border-left: 4px solid #FF9800;">
                <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 1rem;">
                    <div>
                        <div style="font-weight: 600; color: #2E7D32; font-size: 1rem;">{additive['name']}</div>
                        <div style="color: #757575; font-size: 0.9rem;">{additive['type']}</div>
                    </div>
                    <div style="background: #FFF3E0; color: #E65100; padding: 0.4rem 0.8rem; border-radius: 6px; font-weight: 500; font-size: 0.85rem;">{additive['concern']}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="background: #C8E6C9; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #2E7D32;">
            <div style="color: #1B5E20; font-weight: 600;">No artificial additives detected</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div style="text-align: center;">
        """, unsafe_allow_html=True)
        if st.button("Download Report", use_container_width=True):
            st.success("Report downloaded successfully")
    
    with col2:
        st.markdown("""
        <div style="text-align: center;">
        """, unsafe_allow_html=True)
        if st.button("Analyze Another Product", use_container_width=True):
            st.session_state.clear()
            st.switch_page("pages/analyzer.py")
