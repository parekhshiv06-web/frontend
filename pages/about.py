import streamlit as st

def render():
    st.markdown("""
    <div style="margin-bottom: 2rem;">
        <h2 style="color: #2E7D32; font-size: 2rem; margin-bottom: 0.5rem;">About This Project</h2>
        <p style="color: #757575; font-size: 1rem;">Intelligent Food Product Analysis System</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: white; padding: 2rem; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); margin-bottom: 2rem; border-left: 4px solid #2E7D32;">
        <div style="font-weight: 700; color: #2E7D32; margin-bottom: 1rem; font-size: 1.2rem;">Project Overview</div>
        <div style="color: #424242; line-height: 1.8; font-size: 0.95rem;">
            <p>This application leverages cutting-edge AI and machine learning technologies to provide instant dietary analysis of food products. By combining optical character recognition with fine-tuned language models, users can quickly determine if products match their dietary requirements.</p>
            <p style="margin-top: 1rem;">The system addresses a critical gap in accessible dietary information technology by enabling real-time product analysis without requiring manual verification or external database lookups.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown("""
    <div style="font-weight: 700; color: #2E7D32; margin-bottom: 1.5rem; font-size: 1.2rem;">Technology Stack</div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="background: white; padding: 1.5rem; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); border-left: 4px solid #2E7D32;">
            <div style="font-weight: 600; color: #2E7D32; margin-bottom: 1rem;">OCR & Vision</div>
            <div style="color: #757575; font-size: 0.9rem; line-height: 1.6;">
                <p style="margin: 0.5rem 0;">Google Vision API</p>
                <p style="margin: 0.5rem 0;">Text Extraction</p>
                <p style="margin: 0.5rem 0;">85%+ Accuracy</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: white; padding: 1.5rem; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); border-left: 4px solid #81C784;">
            <div style="font-weight: 600; color: #2E7D32; margin-bottom: 1rem;">Language Model</div>
            <div style="color: #757575; font-size: 0.9rem; line-height: 1.6;">
                <p style="margin: 0.5rem 0;">Qwen2.5 1.5B</p>
                <p style="margin: 0.5rem 0;">LoRA/QLoRA Fine-tuning</p>
                <p style="margin: 0.5rem 0;">Parameter Efficient</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background: white; padding: 1.5rem; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); border-left: 4px solid #FF6B6B;">
            <div style="font-weight: 600; color: #2E7D32; margin-bottom: 1rem;">Web Framework</div>
            <div style="color: #757575; font-size: 0.9rem; line-height: 1.6;">
                <p style="margin: 0.5rem 0;">Streamlit Frontend</p>
                <p style="margin: 0.5rem 0;">Fast API Backend</p>
                <p style="margin: 0.5rem 0;">Real-time Processing</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #E8F5E9 0%, #F1F8E9 100%); padding: 2rem; border-radius: 10px; margin-bottom: 2rem;">
        <div style="font-weight: 700; color: #2E7D32; margin-bottom: 1rem; font-size: 1.2rem;">Key Features</div>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem;">
            <div style="background: white; padding: 1rem; border-radius: 8px;">
                <div style="font-weight: 600; color: #2E7D32; margin-bottom: 0.5rem;">Instant Scanning</div>
                <div style="color: #757575; font-size: 0.85rem;">Upload product images and extract ingredients in seconds using advanced OCR</div>
            </div>
            
            <div style="background: white; padding: 1rem; border-radius: 8px;">
                <div style="font-weight: 600; color: #2E7D32; margin-bottom: 0.5rem;">Smart Classification</div>
                <div style="color: #757575; font-size: 0.85rem;">AI-powered ingredient analysis for personalized dietary recommendations</div>
            </div>
            
            <div style="background: white; padding: 1rem; border-radius: 8px;">
                <div style="font-weight: 600; color: #2E7D32; margin-bottom: 0.5rem;">Allergen Detection</div>
                <div style="color: #757575; font-size: 0.85rem;">Identify hidden allergens and harmful additives with high precision</div>
            </div>
            
            <div style="background: white; padding: 1rem; border-radius: 8px;">
                <div style="font-weight: 600; color: #2E7D32; margin-bottom: 0.5rem;">Multi-Criteria Analysis</div>
                <div style="color: #757575; font-size: 0.85rem;">Check multiple dietary restrictions simultaneously</div>
            </div>
            
            <div style="background: white; padding: 1rem; border-radius: 8px;">
                <div style="font-weight: 600; color: #2E7D32; margin-bottom: 0.5rem;">Confidence Scoring</div>
                <div style="color: #757575; font-size: 0.85rem;">Each analysis comes with detailed confidence metrics</div>
            </div>
            
            <div style="background: white; padding: 1rem; border-radius: 8px;">
                <div style="font-weight: 600; color: #2E7D32; margin-bottom: 0.5rem;">Detailed Reports</div>
                <div style="color: #757575; font-size: 0.85rem;">Download comprehensive analysis reports for your records</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown("""
    <div style="background: white; padding: 2rem; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); margin-bottom: 2rem; border-left: 4px solid #81C784;">
        <div style="font-weight: 700; color: #2E7D32; margin-bottom: 1rem; font-size: 1.2rem;">Supported Dietary Categories</div>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 1rem;">
            <div style="background: #F5F5F5; padding: 1rem; border-radius: 8px; border-left: 3px solid #2E7D32;">
                <div style="font-weight: 600; color: #2E7D32;">Gluten-Free</div>
                <div style="color: #757575; font-size: 0.85rem; margin-top: 0.5rem;">Detect gluten containing grains and derivatives</div>
            </div>
            
            <div style="background: #F5F5F5; padding: 1rem; border-radius: 8px; border-left: 3px solid #2E7D32;">
                <div style="font-weight: 600; color: #2E7D32;">Lactose-Free</div>
                <div style="color: #757575; font-size: 0.85rem; margin-top: 0.5rem;">Identify dairy and lactose containing ingredients</div>
            </div>
            
            <div style="background: #F5F5F5; padding: 1rem; border-radius: 8px; border-left: 3px solid #2E7D32;">
                <div style="font-weight: 600; color: #2E7D32;">Vegetarian</div>
                <div style="color: #757575; font-size: 0.85rem; margin-top: 0.5rem;">Check for meat and animal-derived ingredients</div>
            </div>
            
            <div style="background: #F5F5F5; padding: 1rem; border-radius: 8px; border-left: 3px solid #2E7D32;">
                <div style="font-weight: 600; color: #2E7D32;">Vegan</div>
                <div style="color: #757575; font-size: 0.85rem; margin-top: 0.5rem;">Ensure zero animal products in any form</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown("""
    <div style="background: white; padding: 2rem; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); border-left: 4px solid #FF6B6B;">
        <div style="font-weight: 700; color: #2E7D32; margin-bottom: 1rem; font-size: 1.2rem;">Performance Targets</div>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 1rem;">
            <div style="text-align: center;">
                <div style="font-size: 2rem; font-weight: 700; color: #2E7D32;">85%+</div>
                <div style="color: #757575; font-size: 0.9rem;">OCR Accuracy</div>
            </div>
            
            <div style="text-align: center;">
                <div style="font-size: 2rem; font-weight: 700; color: #2E7D32;">85%+</div>
                <div style="color: #757575; font-size: 0.9rem;">Classification Accuracy</div>
            </div>
            
            <div style="text-align: center;">
                <div style="font-size: 2rem; font-weight: 700; color: #2E7D32;">&lt;5s</div>
                <div style="color: #757575; font-size: 0.9rem;">Response Time</div>
            </div>
            
            <div style="text-align: center;">
                <div style="font-size: 2rem; font-weight: 700; color: #2E7D32;">&lt;3GB</div>
                <div style="color: #757575; font-size: 0.9rem;">Model Size</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #2E7D32 0%, #81C784 100%); color: white; padding: 2rem; border-radius: 10px; text-align: center;">
        <div style="font-size: 1.2rem; font-weight: 700; margin-bottom: 0.5rem;">Data Sources</div>
        <div style="font-size: 0.95rem; line-height: 1.8; opacity: 0.95;">
            Open Food Facts Database | USDA Food Data Central | E-Numbers Database | Dubai Pulse Food Catalog
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background: white; padding: 1.5rem; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
            <div style="font-weight: 600; color: #2E7D32; margin-bottom: 0.5rem;">Development Timeline</div>
            <div style="color: #757575; font-size: 0.9rem; line-height: 1.8;">
                <p style="margin: 0.5rem 0;"><strong>Phase 1:</strong> Setup & Data (3 days)</p>
                <p style="margin: 0.5rem 0;"><strong>Phase 2:</strong> Model Fine-tuning (4 days)</p>
                <p style="margin: 0.5rem 0;"><strong>Phase 3:</strong> OCR Integration (3 days)</p>
                <p style="margin: 0.5rem 0;"><strong>Phase 4:</strong> Web Application (3 days)</p>
                <p style="margin: 0.5rem 0;"><strong>Phase 5:</strong> Testing & Documentation (4 days)</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: white; padding: 1.5rem; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
            <div style="font-weight: 600; color: #2E7D32; margin-bottom: 0.5rem;">Research Impact</div>
            <div style="color: #757575; font-size: 0.9rem; line-height: 1.8;">
                <p style="margin: 0.5rem 0;">Demonstrates modern LLM fine-tuning techniques</p>
                <p style="margin: 0.5rem 0;">Solves real-world dietary analysis problem</p>
                <p style="margin: 0.5rem 0;">Parameter-efficient AI implementation</p>
                <p style="margin: 0.5rem 0;">Accessible dietary technology</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
