import streamlit as st
import time

# --- CẤU HÌNH TRANG VIP ---
st.set_page_config(page_title="Đấu Trường Trí Tuệ", page_icon="🌿", layout="centered")

# CSS Tùy chỉnh cho giao diện xịn hơn (Nút bấm bo góc, màu sắc hiện đại)
st.markdown("""
<style>
    .stButton>button {
        border-radius: 8px;
        min-height: 60px;
        height: auto;
        font-size: 16px;
        font-weight: 600;
        transition: all 0.3s ease;
        white-space: normal;
        word-wrap: break-word;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .question-box {
        background-color: #f0f2f6;
        padding: 25px;
        border-radius: 10px;
        border-left: 5px solid #00b4d8;
        margin-bottom: 25px;
    }
</style>
""", unsafe_allow_html=True)

# --- NGÂN HÀNG CÂU HỎI (Bộ 10 câu) ---
danh_sach_cau_hoi = [
    {
        "cau_hoi": "Câu 1. Hồ nào ở Hà Nội có nguồn gốc là đoạn sông Hồng cũ còn sót lại?",
        "dap_an": ["Hồ Gươm", "Hồ Tây", "Hồ Trúc Bạch", "Hồ Thiền Quang"],
        "dap_an_dung": "Hồ Tây"
    },
    {
        "cau_hoi": "Câu 2. Hiện tượng “nở hoa nước” ở hồ Hà Nội chủ yếu do loại sinh vật nào gây ra?",
        "dap_an": ["Bèo tây", "Tảo lam", "Rong đuôi chó", "Sen"],
        "dap_an_dung": "Tảo lam"
    },
    {
        "cau_hoi": "Câu 3. Sông nào ở Hà Nội hiện bị ô nhiễm nặng, được mệnh danh là “dòng sông chết”?",
        "dap_an": ["Sông Hồng", "Sông Đuống", "Sông Tô Lịch", "Sông Nhuệ"],
        "dap_an_dung": "Sông Tô Lịch"
    },
    {
        "cau_hoi": "Câu 4. Loài thực vật thủy sinh nào sau đây có khả năng hấp thụ kim loại nặng, thường dùng để xử lý nước hồ?",
        "dap_an": ["Hoa súng", "Bèo tây", "Cây lau sậy", "Rau muống"],
        "dap_an_dung": "Bèo tây"
    },
    {
        "cau_hoi": "Câu 5. Vai trò chính của hệ thống hồ Hà Nội đối với đô thị là gì?",
        "dap_an": ["Nuôi trồng thủy sản", "Điều hòa vi khí hậu, thoát nước chống ngập", "Giao thông đường thủy", "Khai thác du lịch tâm linh"],
        "dap_an_dung": "Điều hòa vi khí hậu, thoát nước chống ngập"
    },
    {
        "cau_hoi": "Câu 6. Yếu tố nào đe dọa đa dạng sinh học ở hồ Hà Nội nhiều nhất hiện nay?",
        "dap_an": ["Thay đổi mực nước theo mùa", "Xả thải sinh hoạt, đô thị hóa lấn chiếm bờ hồ", "Đánh bắt cá tự phát", "Du khách thả hoa đăng"],
        "dap_an_dung": "Xả thải sinh hoạt, đô thị hóa lấn chiếm bờ hồ"
    },
    {
        "cau_hoi": "Câu 7. Hệ sinh thái sông Hồng đoạn qua Hà Nội khác hồ nội đô ở điểm nào?",
        "dap_an": ["Nước tĩnh, nghèo oxy", "Nước chảy, phù sa nhiều, đa dạng cá sông hơn", "Không có thực vật thủy sinh", "Độ mặn cao"],
        "dap_an_dung": "Nước chảy, phù sa nhiều, đa dạng cá sông hơn"
    },
    {
        "cau_hoi": "Câu 8. Biện pháp sinh học nào đang được thử nghiệm để cải tạo sông Tô Lịch?",
        "dap_an": ["Thả cá chép", "Dùng chế phẩm vi sinh + thả bèo, thủy sinh để lọc nước", "Lắp quạt sục khí", "Xây đập ngăn dòng"],
        "dap_an_dung": "Dùng chế phẩm vi sinh + thả bèo, thủy sinh để lọc nước"
    },
    {
        "cau_hoi": "Câu 9. Loài cá bản địa nào từng rất phổ biến ở Hồ Tây nhưng nay đã suy giảm mạnh?",
        "dap_an": ["Cá mè", "Cá chép", "Cá rô phi", "Cá trôi"],
        "dap_an_dung": "Cá chép"
    },
    {
        "cau_hoi": "Câu 10. Việc kè bờ hồ bằng bê tông ở Hà Nội gây tác động tiêu cực gì đến hệ sinh thái?",
        "dap_an": ["Làm nước hồ sạch hơn", "Mất vùng đệm ven bờ, giảm nơi trú ẩn cho sinh vật", "Tăng lượng oxy hòa tan", "Giúp cây thủy sinh phát triển mạnh"],
        "dap_an_dung": "Mất vùng đệm ven bờ, giảm nơi trú ẩn cho sinh vật"
    }
]

# --- KHỞI TẠO BỘ NHỚ TRẠNG THÁI ---
if 'cau_hien_tai' not in st.session_state:
    st.session_state.cau_hien_tai = 0
if 'diem_so' not in st.session_state:
    st.session_state.diem_so = 0

# --- GIAO DIỆN CHÍNH ---
st.title("🌿 Trắc nghiệm: Sinh thái Ao Hồ Hà Nội")
st.markdown("---")

total_q = len(danh_sach_cau_hoi)

# Nếu chưa làm hết câu hỏi
if st.session_state.cau_hien_tai < total_q:
    # Thanh tiến trình
    progress = st.session_state.cau_hien_tai / total_q
    st.progress(progress)
    st.caption(f"Câu hỏi {st.session_state.cau_hien_tai + 1} / {total_q}")
    
    cau_hoi_data = danh_sach_cau_hoi[st.session_state.cau_hien_tai]
    
    # Hiển thị câu hỏi trong hộp màu
    st.markdown(f'<div class="question-box"><h3>{cau_hoi_data["cau_hoi"]}</h3></div>', unsafe_allow_html=True)
    
    # Chia 2 cột cho 4 đáp án cho đẹp
    col1, col2 = st.columns(2)
    
    dap_an_list = cau_hoi_data["dap_an"]
    
    # Cột 1 chứa A và C
    with col1:
        btn_A = st.button(f"A. {dap_an_list[0]}", use_container_width=True)
        btn_C = st.button(f"C. {dap_an_list[2]}", use_container_width=True)
        
    # Cột 2 chứa B và D
    with col2:
        btn_B = st.button(f"B. {dap_an_list[1]}", use_container_width=True)
        btn_D = st.button(f"D. {dap_an_list[3]}", use_container_width=True)

    # Logic kiểm tra đúng sai
    lua_chon = None
    if btn_A: lua_chon = dap_an_list[0]
    if btn_B: lua_chon = dap_an_list[1]
    if btn_C: lua_chon = dap_an_list[2]
    if btn_D: lua_chon = dap_an_list[3]

    if lua_chon:
        if lua_chon == cau_hoi_data["dap_an_dung"]:
            st.success("🎉 Chính xác! Chuẩn bị sang câu tiếp theo...")
            st.session_state.diem_so += 10
            time.sleep(1.2) # Dừng 1.2s để người chơi thấy thông báo báo đúng
            st.session_state.cau_hien_tai += 1
            st.rerun()
        else:
            st.error("❌ Rất tiếc, sai rồi! Hãy thử suy nghĩ và chọn lại nhé.")

# Nếu đã làm xong hết
else:
    st.progress(1.0)
    st.balloons()
    st.success(f"🏆 CHÚC MỪNG BẠN ĐÃ HOÀN THÀNH XUẤT SẮC!")
    st.info(f"Tổng điểm của bạn: **{st.session_state.diem_so}** / {total_q * 10}")
    
    if st.button("🔄 Chơi lại từ đầu", type="primary", use_container_width=True):
        st.session_state.cau_hien_tai = 0
        st.session_state.diem_so = 0
        st.rerun()