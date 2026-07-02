import streamlit as st
import os
import base64
from PIL import Image, ImageOps  # Crucial for fixing image rotation issues

# 1. Page Configuration
st.set_page_config(
    page_title="Danish's Photography Portfolio",
    page_icon="📷", #insert camera emoji
    layout="wide"
)

# ==========================================================
# GOOGLE DRIVE LARGE VIDEOS CONFIGURATION
# ==========================================================
# Replace these example link structures with your real Google Drive shared embed URLs!
# To get this link format: Open the video on Google Drive -> click Three Dots -> Open in New Window -> Click Three Dots -> Embed item...
DRIVE_VIDEOS = {
    "☀️": [
        "https://drive.google.com/file/d/1zOjcfe7pnwGk-6aGNfgbhJfnPnbkB7eh/view?usp=drive_link"
    ],
    "Alabama": [
        "https://drive.google.com/file/d/1Hf_6YXiuNpYncFvTkKhwHiLemrAeSbCX/view?usp=drive_link"
    ],
    "Alaska": [
        "https://drive.google.com/file/d/1C_nmEdlHYNwnV1UUsEhh8IocPXAyymFP/view?usp=drive_link",
        "https://drive.google.com/file/d/1l2vdDhtJfRsCfv-sQyoeoCLk9R3Cz16G/view?usp=drive_link"
    ],
    "Hawaii": [
        "https://drive.google.com/file/d/1lBEk1vqbXlwv5LudeL2YQyNBKhD_vqgS/view?usp=drive_link",
        "https://drive.google.com/file/d/1YHS8A5LMYOiwjxckKKAV4ztTGHo1Upe3/view?usp=drive_link",
        "https://drive.google.com/file/d/1urM6lJrI9n6Yaim1gyyr8QOrz0gkRdzM/view?usp=drive_link",
        "https://drive.google.com/file/d/1YpTQyBVQZX7EnpweJwSMjesbbkPbnqyx/view?usp=drive_link",
        "https://drive.google.com/file/d/1i3fBM8OTqAWMQkmV1yU2qyP9mQbdpX-j/view?usp=drive_link",
        "https://drive.google.com/file/d/1n4xkLdaMCuiefmn7yuR0vBZBdPURvPMa/view?usp=drive_link",
        "https://drive.google.com/file/d/1mSEtZCBPlTVZEzc-SpmRYgnU78uVatkn/view?usp=drive_link",
        "https://drive.google.com/file/d/1D61tzzOxGUloXs-m9g75aHa1-Rri1t2g/view?usp=drive_link"
    ],
    "Illinois": [
        "https://drive.google.com/file/d/10bUynOSq9-olE1u5NEhsIPBFYEfW1oVa/view?usp=drive_link",
        "https://drive.google.com/file/d/1kEJG9Bn2GsjVsHD76ZNQ-zaQWBVSVhr8/view?usp=drive_link",
        "https://drive.google.com/file/d/1g0qHJQsDzK2lXE5uOexY6eJCZjjdcQnY/view?usp=drive_link",
        "https://drive.google.com/file/d/1FU__6bBue7itPX7eS7YpUzCRdUiCMAjc/view?usp=drive_link"
    ],
    "Iowa": [
        "https://drive.google.com/file/d/1_125T-n-gNIWlz0s5gWBLA_MeqovJimR/view?usp=drive_link"
    ],
    "Massachusetts": [
        "https://drive.google.com/file/d/1XmbPLUQHRemta_5PE6s64UEHG322DIJ8/view?usp=drive_link",
        "https://drive.google.com/file/d/1Q10IYZKQbn7XaUZ65jUyBWRLECXVRKWC/view?usp=drive_link",
        "https://drive.google.com/file/d/1ZlPqZa98MZPG_YOqvtMHfynB-GeL3MGT/view?usp=drive_link"
    ],
    "Montana": [
        "https://drive.google.com/file/d/1mysm4Vd4o5kukprd56Rxgnb4BzF1ExvP/view?usp=drive_link"
    ],
    "Nebraska": [
        "https://drive.google.com/file/d/170nA0sDKv-SWEq7eENY1W393Rsmm53jp/view?usp=drive_link"
    ],
    "Nevada": [
        "https://drive.google.com/file/d/1-6N64Q4oZ__L0oleqG6S5vLPkf7XzwCL/view?usp=drive_link",
        "https://drive.google.com/file/d/11qz_4C4vBrCjsNo3NlytifToEzkuQyIb/view?usp=drive_link",
        "https://drive.google.com/file/d/1C9pDEwHpTtBF-o_DWO5u5kNrJIlRbVdM/view?usp=drive_link",
        "https://drive.google.com/file/d/1IRn4aQkLS1c73MxAcMztmvR7ckPIqb8i/view?usp=drive_link",
        "https://drive.google.com/file/d/1_EmT216AjHutzrGs_hjUK1iJ-QxZ-hah/view?usp=drive_link",
        "https://drive.google.com/file/d/1bWEjtsYOTrmQOrDZQZ3wxrwXAljeYM28/view?usp=drive_link",
        "https://drive.google.com/file/d/1Y7hjfMgBwwlgZ6DxJhAqmtzSYEggPKFB/view?usp=drive_link",
        "https://drive.google.com/file/d/1_UQTIDYSbDcN6ffSmtqRyembuBJDTR3s/view?usp=drive_link",
        "https://drive.google.com/file/d/1jutHlGM1qcuBabarjcPHpyzwpSCNpgsL/view?usp=drive_link",
        "https://drive.google.com/file/d/1rOlNtHxI5Jcm2cQA8lX_xZ7Vc9z8JOM5/view?usp=drive_link",
        "https://drive.google.com/file/d/1JfYMvmFHQYMD56JCOSlUwsOqnKk4Tsja/view?usp=drive_link",
        "https://drive.google.com/file/d/1i_eaVGLOZ5jTzX_xHtD4TPSCLYhG59rr/view?usp=drive_link",
        "https://drive.google.com/file/d/1L2sE9tYq-2ebDjTCH3tHXWBgVit666WT/view?usp=drive_link",
        "https://drive.google.com/file/d/1cIl7AL30uN2iAJyNseB6k4p3lgKyi4o8/view?usp=drive_link",
        "https://drive.google.com/file/d/1I2vJFfifEAxDGXsWv0HJd5ok7Li16L1R/view?usp=drive_link",
        "https://drive.google.com/file/d/1ElSEXaUOyx-4N13WgXDyQORYnhuL3dQe/view?usp=drive_link",
        "https://drive.google.com/file/d/19aySytmqH8M-7yu9FUWkdtBdpXJmUUUO/view?usp=drive_link",
        "https://drive.google.com/file/d/12fCoPp_U16Tj5gLfcXRPEXkhsZLCfKCl/view?usp=drive_link"
    ],
    "New York": [
        "https://drive.google.com/file/d/1Sg38cfelBrACsewiDluYivXEeMlMHYdi/view?usp=drive_link",
        "https://drive.google.com/file/d/1mZ0i0g_zV4CH3lL61zo8yDqPjrXQUDgM/view?usp=drive_link",
        "https://drive.google.com/file/d/1ktT4_7DzxkBXqhkPO7AbkSZlFYALHTDQ/view?usp=drive_link",
        "https://drive.google.com/file/d/1mVL-AEhZvMU7mOJ6S7UWASJdAoRmg8Pa/view?usp=drive_link"
    ],
    "Pennsylvania": [
        "https://drive.google.com/file/d/17Ee-qWYHg1oU8sqjicpEdsDg0FGUrtFQ/view?usp=drive_link",
        "https://drive.google.com/file/d/1OW5HHSu_yezve28Rv0s5fOGZfTzm1MgW/view?usp=drive_link"
    ],
    "South Dakota": [
        "https://drive.google.com/file/d/1m3gB94nZO_Feo9ijOPVPhOt9-86vwrF1/view?usp=drive_link"
    ],
    "Tennessee": [
        "https://drive.google.com/file/d/1V_L1VfzkqHwNxCWkyQHA3P2r4sTGLoOP/view?usp=drive_link",
        "https://drive.google.com/file/d/1J4ArGOZnpafp4FsqyAiA73on6TPXcKJz/view?usp=drive_link",
        "https://drive.google.com/file/d/118VgcWn1aOz0S1xpzTOzORk6xDE5bWUK/view?usp=drive_link",
        "https://drive.google.com/file/d/16zpMUPJApd4V74vkoD9WpKYbWMXiBEoZ/view?usp=drive_link",
        "https://drive.google.com/file/d/1P-GvxoVvLDTzNvWpZkHofiOgC7MAefGA/view?usp=drive_link",
        "https://drive.google.com/file/d/1SO3KXu4f-xVqg7gKPJkPEmMXjrbt4D95/view?usp=drive_link"
    ],
    "Washington": [
        "https://drive.google.com/file/d/1y8mOV4GdFucVo9FvcuOERKtRImNw59ok/view?usp=drive_link",
        "https://drive.google.com/file/d/1qRDuRRk1fbeIaVK8cnEesi9D4fb1avOp/view?usp=drive_link",
        "https://drive.google.com/file/d/1Z1GqeAEZ6_zQoAVrHfRf-wg0BeE03G_v/view?usp=drive_link",
        "https://drive.google.com/file/d/1WmDHvDxlkJvz8LxTLPYshnvA8oE5Pzjh/view?usp=drive_link",
        "https://drive.google.com/file/d/1Zu5t7WA_53GMzeiCc6sioRX9DGplFdCO/view?usp=drive_link"
    ],
    "Wyoming": [
        "https://drive.google.com/file/d/1-zjGzCuQfbILF31ZdE6uOf3RKsnXeWVR/view?usp=drive_link"
    ],
}

# PURE LAYOUT FIXED SCROLL: This invisible block forces focus to the absolute top of the page on every refresh
top_anchor = st.empty()
with top_anchor:
    st.markdown("<div id='top-of-page'></div>", unsafe_allow_html=True)

# 1.5. Function to convert local image to base64 for background
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

try:
    encoded_bg = get_base64_image("cover.jpeg")  #background image of page 

    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded_bg}");
            background-size: cover; background-position: center;
            background-repeat: no-repeat; background-attachment: fixed;
        }}
        .stApp::before {{
            content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
            background-color: rgba(0, 0, 0, 0.6); z-index: -1;
        }}
        /* Styling the album buttons to look cleaner */
        .stButton>button {{
            width: 100%;
            background-color: rgba(255, 255, 255, 0.1);
            color: magenta;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }}
        .stButton>button:hover {{
            background-color: #904bff;   /* #FF4B4B */
            color: purple;
            border-color: #904bff;      /* #FF4B4B */
        }}
        /* RESPONSIVE LAYOUT OVERRIDES (Mobile Devices smaller than 768px) */ 
        @media (max-width: 768px) {{
            .stApp {{
                background-attachment: scroll;
                background-size: cover;
            }}
            span[style*="font-size: 50px"] {{
                font-size: 32px !important;
            }}
            span[style*="font-size: 20px"] {{
                font-size: 15px !important;
            }}
            .stButton>button {{
                padding: 10px 0px !important;
                margin-bottom: 25px;
            }}
        }}
        /* 4. REMOVE STREAMLIT TABS, MENUS, HEADERS, AND BADGES COMPLETELY */
        #MainMenu, footer, header {{
            visibility: hidden !important;
            display: non !important;
        }}
        .stAppHeader, .stActionButton, div[data-testid="stStatusWidget"] {{
            display: none !important;
            visibility: hidden !important;
        }}
        </style>
    """, unsafe_allow_html=True)
except FileNotFoundError:
    st.error("Background image file not found. Check the file name path!")

# 2. Track album state using Streamlit Session State
if "current_album" not in st.session_state:
    st.session_state.current_album = "home"

# ==========================================================
# VIEW 1: THE HOME MAIN PAGE (ALBUM GRID) WITH MANUAL COVERS
# ==========================================================

if st.session_state.current_album == "home":
    st.markdown(
        '<span style="color:magenta; font-size: 45px; font-weight: bold; font-family: Brush Script MT, cursive; text-align: center; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); display: block; margin-bottom: 20px;">' 
        '💖 Photography Portfolio 💖' 
        '</span>', 
        unsafe_allow_html=True)      
    st.markdown(                                                                                                                        
        '<span style="color:magenta; background-color:pink; padding: 10px; border-radius: 0px; font-size: 20px; line-height: 1.5; font-family: Times New Roman, sans-serif;  margin-bottom: 20px; display: block; text-align: center;">'
        'Hello, I am a Malaysian raised in America with speech impairment and auditory processing disorder, and I love to travel and explore different territories with unique/beautiful scenery.''<br>''<br>'
        'I have visited all 50 states in the USA and found moments in some that inspire me to share my photography with you that reminds me of the beauty of our world.''<br>''<br>'
        'Please find my portfolio of photos that I have taken during my travels, and I hope you enjoy them as much as I enjoyed taking them!'
        '</span>',
        unsafe_allow_html=True)
    st.markdown(                                                                                                                        
        """
        <style>
        .social-link-box {
          background-color: magenta;
          padding: 6px 12px;
          border-radius: 4px;
          display: flex;
          justify-content: center;
          gap: 16px;
          flex-wrap: wrap;
          margin-bottom: 20px;
        }
        .social-link-box a {
          display: inline-flex;
          align-items: center;
          gap: 6px;
          font-size: 20px;
          text-decoration: none;
          color: pink !important;
          font-family: Times New Roman, sans-serif;
        }
        .social-link-box svg {
          width: 16px;
          height: 16px;
          fill: currentColor;
        }
        .social-link-box a:hover {
          opacity: 0.8;
        }
        </style>
        
        <div class="social-link-box">
            <a href="https://www.instagram.com/danishmurshid?igsh=bGcxb3d6dGpyYW1u" target="_blank">
                <svg viewBox="0 0 16 16"><path d="M8 0C5.829 0 5.556.01 4.703.048 3.85.088 3.269.222 2.76.42a3.9 3.9 0 0 0-1.417.923A3.9 3.9 0 0 0 .42 2.76C.222 3.268.087 3.85.048 4.7.01 5.555 0 5.827 0 8.001c0 2.172.01 2.444.048 3.297.04.852.174 1.433.372 1.942.205.526.478.972.923 1.417.444.445.89.719 1.416.923.51.198 1.09.333 1.942.372C5.555 15.99 5.827 16 8 16s2.444-.01 3.298-.048c.851-.04 1.434-.174 1.943-.372a3.9 3.9 0 0 0 1.416-.923c.445-.445.718-.891.923-1.417.197-.509.332-1.09.372-1.942C15.99 10.445 16 10.173 16 8s-.01-2.444-.048-3.299c-.04-.851-.175-1.433-.372-1.941a3.9 3.9 0 0 0-.923-1.417A3.9 3.9 0 0 0 13.24.42c-.51-.198-1.092-.333-1.943-.372C10.443.01 10.172 0 7.998 0zm-.717 1.442h.718c2.136 0 2.389.007 3.232.046.78.035 1.204.166 1.486.275.373.145.64.319.92.599s.453.546.598.92c.11.281.24.705.275 1.485.039.843.047 1.096.047 3.231s-.008 2.389-.047 3.232c-.035.78-.166 1.203-.275 1.485a2.5 2.5 0 0 1-.599.919c-.28.28-.546.453-.92.598-.28.11-.704.24-1.485.276-.843.038-1.096.047-3.232.047s-2.39-.009-3.233-.047c-.78-.036-1.203-.166-1.485-.276a2.5 2.5 0 0 1-.92-.598 2.5 2.5 0 0 1-.6-.92c-.109-.281-.24-.705-.275-1.485-.038-.843-.046-1.096-.046-3.233s.008-2.388.046-3.231c.036-.78.166-1.204.276-1.486.145-.373.319-.64.599-.92.28-.28.546-.453.92-.598.282-.11.705-.24 1.485-.276.738-.034 1.024-.044 2.515-.045zm4.988 1.328a.96.96 0 1 0 0 1.92.96.96 0 0 0 0-1.92m-4.27 1.122a4.109 4.109 0 1 0 0 8.217 4.109 4.109 0 0 0 0-8.217m0 1.441a2.667 2.667 0 1 1 0 5.334 2.667 2.667 0 0 1 0-5.334"/></svg>
                Instagram
            </a>
            <a href="https://www.linkedin.com/in/danish-murshid-wmu" target="_blank">
                <svg viewBox="0 0 16 16"><path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854zm4.943 12.248V6.169H2.542v7.225zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248S2.4 3.226 2.4 3.934c0 .694.521 1.248 1.327 1.248zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016l.016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225z"/></svg>
                LinkedIn
            </a>
            <a href="https://github.com/danishmurshid" target="_blank">
                <svg viewBox="0 0 16 16"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27s1.36.09 2 .27c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8"/></svg>
                GitHub
            </a>
            <a href="https://www.tiktok.com/@danish_plainish?_r=1&_t=ZT-97EArC7YQ6H" target="_blank">
                <svg viewBox="0 0 16 16"><path d="M9 0h1.98c.144.715.54 1.617 1.235 2.512C12.895 3.389 13.797 4 15 4v2c-1.753 0-3.07-.814-4-2.133V11A5 5 0 1 1 6 6c.525 0 1.036.083 1.5.242V8.5A3 3 0 1 0 9 11z"/></svg>
                TikTok
            </a>
        </div>
        """,
        unsafe_allow_html=True)
            
    st.divider()

    IMAGE_DIR = "images"
    
    if os.path.exists(IMAGE_DIR):
        albums = sorted([d for d in os.listdir(IMAGE_DIR) if os.path.isdir(os.path.join(IMAGE_DIR, d))])
        
        if not albums:
            st.warning("No album folders found inside your 'images/' directory!")
        else:
            album_cols = st.columns(3)
            
            # Create a uniform grid container block
            grid_container = st.container()

            for index, album_name in enumerate(albums):
                col = album_cols[index % 3]
                album_path = os.path.join(IMAGE_DIR, album_name)
                
                all_files = os.listdir(album_path)
                valid_images = [f for f in all_files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
                
                cover_candidates = [f for f in valid_images if f.lower().startswith('cover.')]
                
                if cover_candidates:
                    selected_cover = cover_candidates[0]
                elif valid_images:
                    selected_cover = valid_images[0]
                else:
                    selected_cover = None

                with col:
                    st.markdown(
                        '<span style="color:magenta; font-size: 50px; font-family: Neamants, cursive;  margin-bottom: 20px; display: block; text-align: center;">'          
                        f'{album_name}'
                        '</span>', 
                        unsafe_allow_html=True)
                    if selected_cover:
                        cover_full_path = os.path.join(album_path, selected_cover)
                        try:
                            img = Image.open(cover_full_path)
                            img = ImageOps.exif_transpose(img)
                            st.image(img, use_container_width=True)
                        except Exception:
                            st.image(cover_full_path, use_container_width=True)
                    else:
                        st.info("Empty Album")
                    
                    if st.button(f"Open {album_name} Album", key=album_name):
                        st.session_state.current_album = album_name
                        st.rerun()
    st.divider()

    st.markdown(                                                                                                                        
        '<span style="color:magenta; background-color:pink; padding: 10px; border-radius: 0px; font-size: 20px; line-height: 1.5; font-family: Times New Roman, sans-serif;  margin-bottom: 20px; display: block; text-align: center;">'
        "If you're seeing this, then you've actually bothered to look into my gallery."'<br>''<br>'
        "Cause the truth is, I'm not doing well as someone back in Chicago broke my heart without any form of closure and never truly cared about whatever career I have, and what I did to make her and I happy."'<br>''<br>'
        'Ever since then, I felt so broken and lost that I decided to leave the country for good, quit my job after my work authorization expired, and tried to find ways to cope with the heartbreak and pain, but after all this time I was never able to heal.' '<br>''<br>'
        'I was never able to move on especially since I am a hopeless romantic with an anxious attachment style.' '<br>''<br>' 
        '' '<br>''<br>'
        "And if you, the one who broke my heart, are reading this (I highly doubt you would), like I told you before:" '<br>''<br>'
        " I hope life is being kind to you lately and everything is falling into place for you..." '<br>''<br>'
        "Because it isn't for me..."
        '</span>',
        unsafe_allow_html=True)

# ==========================================================
# VIEW 2: INSIDE AN ALBUM GALLERY
# ==========================================================

else:
    chosen_album = st.session_state.current_album
    
    st.components.v1.html(
        """
        <img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" onload="
            var mainContent = window.parent.document.querySelector('section.main');
            if (mainContent) { mainContent.scrollTop = 0; }
        " style="display:none;">
        """,
        height=0,
    )

    header_col1, header_col2 = st.columns([4, 1])
    with header_col1:
        st.markdown(
        '<span style="color:magenta; font-size: 75px; font-family: Brush Script MT, cursive; text-align: left; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); display: block; margin-bottom: 20px;">' 
        f' {chosen_album}' 
        '</span>', 
        unsafe_allow_html=True)  
        if chosen_album == "Alabama":
            st.markdown(
            '<span style="color:magenta; background-color:pink; font-size: 30px; font-family: Times New Roman, sans-serif; text-align: left; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); display: block; margin-bottom: 20px;">' 
            f' Check one of these videos for Dolphins sightings!!' 
            '</span>', 
            unsafe_allow_html=True)
        if chosen_album == "Aurora":
            st.markdown(
            '<span style="color:magenta; background-color:pink; font-size: 20px; font-family: Times New Roman, sans-serif; text-align: left; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); display: block; margin-bottom: 20px;">' 
            f' The Aurora Borealis. I had the opportunity to see the northern lights four times in Chicago, Syracuse, and just above British Columbia on my trip back to Malaysia. This was a once in a lifetime experience that I will never forget.' 
            '</span>', 
            unsafe_allow_html=True)
        if chosen_album == "Michigan":
            st.markdown(
            '<span style="color:magenta; background-color:pink; font-size: 20px; font-family: Times New Roman, sans-serif; text-align: left; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); display: block; margin-bottom: 20px;">' 
            f" Yeah... There's nothing much here" 
            '</span>', 
            unsafe_allow_html=True)

    with header_col2:
        if st.button("⬅️ Back to Albums", key="top_back_btn"):
            st.session_state.current_album = "home"
            st.rerun()
            
    st.divider()
    
    target_album_dir = os.path.join("images", chosen_album)
    
    # --- UPDATED AND FIXED FILE CHECKING BLOCK ---
    extensions = ('.png', '.jpg', '.jpeg', '.webp', '.mp4', '.mov', '.webm')
    if os.path.exists(target_album_dir):
        all_files = os.listdir(target_album_dir)
        media_files = sorted([f for f in all_files if f.lower().endswith(extensions)])
        
        # This defines valid_images safely inside View 2 so the video loop can see it!
        valid_images = [f for f in all_files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')) and not f.lower().startswith('cover.')]
    else:
        media_files = []
        valid_images = [] # Keeps the code from crashing if a directory goes missing
    # ---------------------------------------------
    
    # Retrieve cloud video links assigned to this specific album
    cloud_videos = DRIVE_VIDEOS.get(chosen_album, [])
    
    if len(media_files) == 0 and len(cloud_videos) == 0:
        st.warning("This album is currently empty.")
    else:
        columns = st.columns(4)  
        grid_index = 0 

        # ----------------------------------------------------------
        # HIGHLIGHT LOGIC FOR LOCAL VIDEOS
        # ----------------------------------------------------------
        highlighted_video = "dolphin.mov"  
        target_highlight_album = "Alabama" 

        if chosen_album == target_highlight_album and highlighted_video in media_files:
            file_path = os.path.join(target_album_dir, highlighted_video)
            col = columns[grid_index % 4]
            grid_index += 1
            
            with col:
                st.video(file_path, format="video/mp4")
                st.markdown('<p style="color:magenta; text-align:center; font-weight:bold;">Check out this video for Dolphins sightings!!</p>', unsafe_allow_html=True)

        # ----------------------------------------------------------
        # MAIN GRID LOOP: LOCAL IMAGES & SMALL LOCAL MEDIA
        # ----------------------------------------------------------
        for file_name in media_files:
            if file_name.lower().startswith('cover.'):
                continue
                
            if chosen_album == target_highlight_album and file_name == highlighted_video:
                continue
                
            file_path = os.path.join(target_album_dir, file_name)
            col = columns[grid_index % 4]  
            grid_index += 1

            with col:
                if file_name.lower().endswith(('.mp4', '.mov', '.webm')):
                    #--#
                    #st.video(file_path, format="video/mp4")
                    st.video(file_path, format="video/mp4")
                    #--#
                else:  
                    try:
                        img = Image.open(file_path)
                        img = ImageOps.exif_transpose(img)
                        st.image(img, use_container_width=True)
                    except Exception:
                        st.image(file_path, use_container_width=True)

        # 1. Paste this tiny CSS snippet right before your video loop starts.
# It forces any iframe on a mobile device (screen width below 600px) to drop to 220px high 
# so it never hits the infinite loading loop freeze.
        st.markdown(
            """
            <style>
            @media (max-width: 300px) {
                div[data-testid="stHtml"] iframe, 
                div.element-container iframe {
                    height: 220px !important;
                }
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        # ----------------------------------------------------------
        # GOOGLE DRIVE VIDEO DISPLAY (STABLE ASPECT PREVIEW)
        # ----------------------------------------------------------
        for idx, embed_url in enumerate(cloud_videos):
            col = columns[grid_index % 4]
            grid_index += 1
            
            with col:
                # 1. Extract the unique file ID from your preview link
                if "/file/d/" in embed_url:
                    video_id = embed_url.split("/file/d/")[1].split("/")[0]
                else:
                    video_id = embed_url
                
                # 2. Use a standard embedded iframe layout without scaling blocks
                # This ensures Google displays its native thumbnail preview card correctly
                stable_stream_url = f"https://docs.google.com/file/d/{video_id}/preview"
                
                # We use a clean, standard height that allows the video preview title to sit nicely
                #st.components.v1.iframe(stable_stream_url, height=500, scrolling=False)              #height=450


                # 3. Direct link button right below it to allow full widescreen watching
                video_open_url = f"https://drive.google.com/file/d/{video_id}/view?usp=sharing"
                #---#
                thumbnail_url = f"https://drive.google.com/thumbnail?id={video_id}&sz=w500"
                
                # 1. Inject custom CSS rules to toggle visibility instantly based on the actual screen width
                st.markdown(
                    f"""
                    <style>
                    /* On desktop (wide screens), show the player and hide the mobile card */
                    .desktop-player-{idx} {{ display: block; }}
                    .mobile-card-{idx} {{ display: none; }}
                    
                    /* On mobile phones (screens smaller than 680px wide) */
                    @media (max-width: 680px) {{
                        .desktop-player-{idx} {{ display: none !important; }}
                        .mobile-card-{idx} {{ display: block !important; }}
                    }}
                    </style>
                    """,
                    unsafe_allow_html=True
                )
                
                # 2. OPTION A: The Desktop Iframe Player Container
                st.markdown(f'<div class="desktop-player-{idx}">', unsafe_allow_html=True)
                st.components.v1.iframe(stable_stream_url, height=500, scrolling=False)
                st.markdown('</div>', unsafe_allow_html=True)
                
                # 3. OPTION B: The Mobile Thumbnail Card Container
                st.markdown(
                    f"""
                    <div class="mobile-card-{idx}">
                        <!-- Helpful User Alert Instruction -->
                        <p style="
                            color: #ffb3ff; 
                            background-color: rgba(0, 0, 0, 0.6);
                            font-size: 14px; 
                            font-family: 'Times New Roman', serif; 
                            text-align: center; 
                            margin-bottom: 10px;
                        ">
                            ⚠️📱 If the original player above is still loading or frozen, please select the video below to watch ⬇️ 
                        </p>
                        <a href="{video_open_url}" target="_blank" style="text-decoration: none; display: block;">
                            <div style="
                                position: relative; 
                                width: 100%; 
                                height: 220px; 
                                border-radius: 8px; 
                                overflow: hidden; 
                                background-image: url('{thumbnail_url}'); 
                                background-size: cover; 
                                background-position: center;
                                border: 1px solid rgba(255, 255, 255, 0.2);
                                display: flex;
                                align-items: center;
                                justify-content: center;
                                margin-bottom: 10px;
                            ">
                                <div style="position: absolute; top:0; left:0; width:100%; height:100%; background: rgba(0,0,0,0.45); pointer-events: none;"></div>
                                <div style="
                                    position: relative;
                                    width: 55px;
                                    height: 55px;
                                    background: rgba(255, 255, 255, 0.9);
                                    border-radius: 50%;
                                    display: flex;
                                    align-items: center;
                                    justify-content: center;
                                    box-shadow: 0 4px 10px rgba(0,0,0,0.4);
                                ">
                                    <div style="
                                        width: 0; height: 0; 
                                        border-top: 10px solid transparent;
                                        border-bottom: 10px solid transparent;
                                        border-left: 16px solid #111;
                                        margin-left: 4px;
                                    "></div>
                                </div>
                            </div>
                        </a>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                #---#
                st.link_button("🔗 Open Video in New Tab", video_open_url, use_container_width=True)
            
    # ----------------------------------------------------------
    # ADDED SECTION: BOTTOM BACK BUTTON
    # ----------------------------------------------------------
    st.divider()
        
    bot_col1, bot_col2, bot_col3 = st.columns([2, 1, 2])
    with bot_col1:
        if chosen_album == "Alabama":
            st.markdown(
            '<span style="color:magenta; background-color:pink; font-size: 30px; font-family: Times New Roman, sans-serif; text-align: left; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); display: block; margin-bottom: 20px;">' 
            f' Check one of these videos for Dolphins sightings!!' 
            '</span>', 
            unsafe_allow_html=True)
        if chosen_album == "Aurora":
            st.markdown(
            '<span style="color:magenta; background-color:pink; font-size: 20px; font-family: Times New Roman, sans-serif; text-align: left; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); display: block; margin-bottom: 20px;">' 
            f' The Aurora Borealis. I had the opportunity to see the northern lights four times in Chicago, Syracuse, and just above British Columbia on my trip back to Malaysia. This was a once in a lifetime experience that I will never forget.' 
            '</span>', 
            unsafe_allow_html=True)
    with bot_col2:
        if st.button("⬅️ Back to Albums", key="bottom_back_btn"):
             st.session_state.current_album = "home"
             st.rerun()
