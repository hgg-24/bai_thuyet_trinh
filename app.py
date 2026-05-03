import streamlit as st

# --- 1. CẤU HÌNH GIAO DIỆN ---
st.set_page_config(page_title="Đấu Trường Sinh Thái Hà Nội", page_icon="🌿", layout="centered")

st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .stApp {
        background-color: #f4fdf4;
        background-image: radial-gradient(#dcf2e3 1px, transparent 1px);
        background-size: 20px 20px;
    }

    .question-box {
        background: linear-gradient(135deg, #ffffff 0%, #f8fcf9 100%);
        padding: 25px;
        border-radius: 16px;
        border-left: 6px solid #2ecc71;
        box-shadow: 0 8px 20px rgba(0,0,0,0.06);
        margin-bottom: 25px;
        color: #2c3e50;
    }

    /* Nút bấm mặc định to và rõ ràng */
    div.stButton > button {
        border-radius: 12px;
        min-height: 75px;
        font-size: 16px;
        font-weight: 600;
        background-color: white;
        border: 2px solid #e0e6ed;
        transition: all 0.2s;
        white-space: normal;
        word-wrap: break-word;
    }
    
    div.stButton > button:hover {
        border-color: #2ecc71;
        transform: translateY(-3px);
    }
</style>
""", unsafe_allow_html=True)

# --- 2. BỘ DỮ LIỆU CHUẨN 10 CÂU ---
data = [
    {"q": "Câu 1. Hồ nào ở Hà Nội có nguồn gốc là đoạn sông Hồng cũ còn sót lại?", "opts": ["Hồ Gươm", "Hồ Tây", "Hồ Trúc Bạch", "Hồ Thiền Quang"], "ans": "Hồ Tây"},
    {"q": "Câu 2. Hiện tượng “nở hoa nước” chủ yếu do loại sinh vật nào gây ra?", "opts": ["Bèo tây", "Tảo lam", "Rong đuôi chó", "Sen"], "ans": "Tảo lam"},
    {"q": "Câu 3. Sông nào bị ô nhiễm nặng, mệnh danh là “dòng sông chết”?", "opts": ["Sông Hồng", "Sông Đuống", "Sông Tô Lịch", "Sông Nhuệ"], "ans": "Sông Tô Lịch"},
    {"q": "Câu 4. Loài thực vật nào có khả năng hấp thụ kim loại nặng, dùng xử lý nước?", "opts": ["Hoa súng", "Bèo tây", "Cây lau sậy", "Rau muống"], "ans": "Bèo tây"},
    {"q": "Câu 5. Vai trò chính của hệ thống hồ đối với đô thị Hà Nội là gì?", "opts": ["Nuôi trồng thủy sản", "Điều hòa vi khí hậu, thoát nước", "Giao thông thủy", "Khai thác du lịch"], "ans": "Điều hòa vi khí hậu, thoát nước"},
    {"q": "Câu 6. Yếu tố nào đe dọa đa dạng sinh học nhiều nhất hiện nay?", "opts": ["Thay đổi mực nước", "Xả thải sinh hoạt, lấn chiếm bờ", "Đánh bắt cá tự phát", "Thả hoa đăng"], "ans": "Xả thải sinh hoạt, lấn chiếm bờ"},
    {"q": "Câu 7. Hệ sinh thái sông Hồng khác hồ nội đô ở điểm nào?", "opts": ["Nước tĩnh", "Nước chảy, phù sa nhiều, cá đa dạng", "Không có thực vật", "Độ mặn cao"], "ans": "Nước chảy, phù sa nhiều, cá đa dạng"},
    {"q": "Câu 8. Biện pháp sinh học nào đang cải tạo sông Tô Lịch?", "opts": ["Thả cá chép", "Chế phẩm vi sinh + bèo lọc nước", "Lắp quạt sục khí", "Xây đập"], "ans": "Chế phẩm vi sinh + bèo lọc nước"},
    {"q": "Câu 9. Loài cá bản địa nào từng phổ biến Hồ Tây nay suy giảm mạnh?", "opts": ["Cá mè", "Cá chép", "Cá rô phi", "Cá trôi"], "ans": "Cá chép"},
    {"q": "Câu 10. Việc kè bờ hồ bằng bê tông gây tác động gì đến hệ sinh thái?", "opts": ["Làm nước sạch hơn", "Mất vùng đệm, giảm sinh vật trú ẩn", "Tăng oxy", "Giúp cây thủy sinh"], "ans": "Mất vùng đệm, giảm sinh vật trú ẩn"}
]

# --- 3. KHỞI TẠO BỘ NHỚ LƯU TRẠNG THÁI ---
if 'idx' not in st.session_state: st.session_state.idx = 0
if 'wrong_clicks' not in st.session_state: st.session_state.wrong_clicks = []
if 'is_correct' not in st.session_state: st.session_state.is_correct = False

# --- 4. GIAO DIỆN CHÍNH ---
st.markdown("<h2 style='text-align: center; color: #16a085; font-weight: 800;'>🌿 Khám Phá Ao Hồ Hà Nội</h2>", unsafe_allow_html=True)
st.markdown("---")

total_q = len(data)

# Màn hình chúc mừng khi hoàn thành
if st.session_state.idx >= total_q:
    st.balloons()
    st.markdown("<div class='question-box' style='text-align: center;'>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 60px;'>🏆</h1>", unsafe_allow_html=True)
    st.success("TUYỆT VỜI! BẠN ĐÃ HOÀN THÀNH BÀI TRẮC NGHIỆM!")
    st.markdown("</div>", unsafe_allow_html=True)
    
    if st.button("🔄 Chơi lại từ đầu", type="primary", use_container_width=True):
        st.session_state.idx = 0
        st.session_state.wrong_clicks = []
        st.session_state.is_correct = False
        st.rerun()

# Màn hình câu hỏi
else:
    q_data = data[st.session_state.idx]
    
    st.progress(st.session_state.idx / total_q)
    st.caption(f"Đang giải câu {st.session_state.idx + 1} / {total_q}")
    st.markdown(f'<div class="question-box"><h3>{q_data["q"]}</h3></div>', unsafe_allow_html=True)
    
    # Hàm xử lý logic khi bấm nút
    def on_click(choice):
        if choice == q_data["ans"]:
            st.session_state.is_correct = True # Đánh dấu đúng
        else:
            if choice not in st.session_state.wrong_clicks:
                st.session_state.wrong_clicks.append(choice) # Lưu lại nút đã bấm sai
    
    c1, c2 = st.columns(2)
    
    # Hàm vẽ nút bấm (Đổi icon nếu đúng/sai)
    def render_button(col, prefix, choice):
        # Mặc định text nút
        btn_text = f"{prefix}. {choice}"
        
        # Nếu đã đúng thì hiện dấu tick cho đáp án đúng
        if st.session_state.is_correct and choice == q_data["ans"]:
            btn_text = f"✅ {choice}"
            
        # Nếu đã bấm sai nút này thì hiện dấu X
        elif choice in st.session_state.wrong_clicks:
            btn_text = f"❌ {choice}"
            
        with col:
            # Khóa nút nếu đã trả lời đúng để không bấm loạn
            if st.button(btn_text, disabled=st.session_state.is_correct, use_container_width=True):
                on_click(choice)
                st.rerun()

    render_button(c1, "A", q_data["opts"][0])
    render_button(c2, "B", q_data["opts"][1])
    render_button(c1, "C", q_data["opts"][2])
    render_button(c2, "D", q_data["opts"][3])

    # Khu vực thông báo và nút chuyển câu
    st.markdown("---")
    
    if st.session_state.is_correct:
        st.success(f"🎉 CHÍNH XÁC! Đáp án đúng là: **{q_data['ans']}**")
        if st.button("Câu tiếp theo ➡️", type="primary", use_container_width=True):
            st.session_state.idx += 1
            st.session_state.wrong_clicks = []
            st.session_state.is_correct = False
            st.rerun()
    elif len(st.session_state.wrong_clicks) > 0:
        st.error("❌ Rất tiếc, bạn chọn sai rồi. Hãy thử lại các đáp án còn lại nhé!")
