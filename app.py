import streamlit as st
import time

# --- CẤU HÌNH TRANG VIP ---
st.set_page_config(page_title="Sinh Thái Ao Hồ Hà Nội", page_icon="🌿", layout="centered")

# --- CSS TỐI ƯU HÓA: ĐẸP & CHỐNG LAG ---
st.markdown("""
<style>
    /* Ẩn các menu mặc định của Streamlit để web nhẹ và giống App thật hơn */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Background pattern chấm bi chìm nhẹ nhàng */
    .stApp {
        background-color: #f4fdf4;
        background-image: radial-gradient(#dcf2e3 1px, transparent 1px);
        background-size: 20px 20px;
    }

    /* Khung câu hỏi hiện đại, đổ bóng mượt */
    .question-box {
        background: linear-gradient(135deg, #ffffff 0%, #f8fcf9 100%);
        padding: 25px;
        border-radius: 16px;
        border-left: 6px solid #2ecc71; /* Viền xanh lá cây sinh thái */
        box-shadow: 0 8px 20px rgba(0,0,0,0.06);
        margin-bottom: 25px;
        margin-top: 10px;
        color: #2c3e50;
    }

    /* Hiệu ứng Nút bấm A B C D */
    .stButton>button {
        border-radius: 12px;
        min-height: 70px;
        height: auto;
        font-size: 16px;
        font-weight: 500;
        color: #34495e;
        background-color: #ffffff;
        border: 2px solid #e0e6ed;
        transition: all 0.2s ease-in-out; /* Chuyển động mượt, không lag */
        white-space: normal;
        word-wrap: break-word;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    
    .stButton>button:hover {
        border-color: #2ecc71;
        color: #2ecc71;
        transform: translateY(-3px); /* Hiệu ứng nảy lên khi di chuột */
        box-shadow: 0 8px 15px rgba(46, 204, 113, 0.15);
    }
    
    /* Chỉnh cho ảnh bo góc */
    img {
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# --- NGÂN HÀNG CÂU HỎI (Đã thêm link ảnh minh họa tối ưu dung lượng) ---
danh_sach_cau_hoi = [
    {
        "cau_hoi": "Câu 1. Hồ nào ở Hà Nội có nguồn gốc là đoạn sông Hồng cũ còn sót lại?",
        "dap_an": ["Hồ Gươm", "Hồ Tây", "Hồ Trúc Bạch", "Hồ Thiền Quang"],
        "dap_an_dung": "Hồ Tây",
        "anh_minh_hoa": "https://images.unsplash.com/photo-1596422846543-75c6fc197f07?auto=format&fit=crop&w=800&q=80"
    },
    {
        "cau_hoi": "Câu 2. Hiện tượng “nở hoa nước” ở hồ Hà Nội chủ yếu do loại sinh vật nào gây ra?",
        "dap_an": ["Bèo tây", "Tảo lam", "Rong đuôi chó", "Sen"],
        "dap_an_dung": "Tảo lam",
        "anh_minh_hoa": "https://images.unsplash.com/photo-1620054794695-81232822a106?auto=format&fit=crop&w=800&q=80"
    },
    {
        "cau_hoi": "Câu 3. Sông nào ở Hà Nội hiện bị ô nhiễm nặng, được mệnh danh là “dòng sông chết”?",
        "dap_an": ["Sông Hồng", "Sông Đuống", "Sông Tô Lịch", "Sông Nhuệ"],
        "dap_an_dung": "Sông Tô Lịch",
        "anh_minh_hoa": "https://images.unsplash.com/photo-1611273426858-450d8e3c9cce?auto=format&fit=crop&w=800&q=80"
    },
    {
        "cau_hoi": "Câu 4. Loài thực vật thủy sinh nào có khả năng hấp thụ kim loại nặng, thường dùng xử lý nước hồ?",
        "dap_an": ["Hoa súng", "Bèo tây", "Cây lau sậy", "Rau muống"],
        "dap_an_dung": "Bèo tây",
        "anh_minh_hoa": "https://images.unsplash.com/photo-1632223709673-d8dbcf51246c?auto=format&fit=crop&w=800&q=80"
    },
    {
        "cau_hoi": "Câu 5. Vai trò chính của hệ thống hồ Hà Nội đối với đô thị là gì?",
        "dap_an": ["Nuôi trồng thủy sản", "Điều hòa vi khí hậu, thoát nước chống ngập", "Giao thông đường thủy", "Khai thác du lịch tâm linh"],
        "dap_an_dung": "Điều hòa vi khí hậu, thoát nước chống ngập",
        "anh_minh_hoa": "https://images.unsplash.com/photo-1579782522718-e325608823f6?auto=format&fit=crop&w=800&q=80"
    },
    {
        "cau_hoi": "Câu 6. Yếu tố nào đe dọa đa dạng sinh học ở hồ Hà Nội nhiều nhất hiện nay?",
        "dap_an": ["Thay đổi mực nước theo mùa", "Xả thải sinh hoạt, đô thị hóa lấn chiếm bờ hồ", "Đánh bắt cá tự phát", "Du khách thả hoa đăng"],
        "dap_an_dung": "Xả thải sinh hoạt, đô thị hóa lấn chiếm bờ hồ",
        "anh_minh_hoa": "https://images.unsplash.com/photo-1518005020951-eccb494ad742?auto=format&fit=crop&w=800&q=80"
    },
    {
        "cau_hoi": "Câu 7. Hệ sinh thái sông Hồng đoạn qua Hà Nội khác hồ nội đô ở điểm nào?",
        "dap_an": ["Nước tĩnh, nghèo oxy", "Nước chảy, phù sa nhiều, đa dạng cá sông hơn", "Không có thực vật thủy sinh", "Độ mặn cao"],
        "dap_an_dung": "Nước chảy, phù sa nhiều, đa dạng cá sông hơn",
        "anh_minh_hoa": "https://images.unsplash.com/photo-1470075446540-333e691ec552?auto=format&fit=crop&w=800&q=80"
    },
    {
        "cau_hoi": "Câu 8. Biện pháp sinh học nào đang được thử nghiệm để cải tạo sông Tô Lịch?",
        "dap_an": ["Thả cá chép", "Dùng chế phẩm vi sinh + thả bèo, thủy sinh", "Lắp quạt sục khí", "Xây đập ngăn dòng"],
        "dap_an_dung": "Dùng chế phẩm vi sinh + thả bèo, thủy sinh",
        "anh_minh_hoa": "https://images.unsplash.com/photo-1542385151-efd9000785a0?auto=format&fit=crop&w=800&q=80"
    },
    {
        "cau_hoi": "Câu 9. Loài cá bản địa nào từng rất phổ biến ở Hồ Tây nhưng nay đã suy giảm mạnh?",
        "dap_an": ["Cá mè", "Cá chép", "Cá rô phi", "Cá trôi"],
        "dap_an_dung": "Cá chép",
        "anh_minh_hoa": "https://images.unsplash.com/photo-1522069169874-c58ec4b76be1?auto=format&fit=crop&w=800&q=80"
    },
    {
        "cau_hoi": "Câu 10. Việc kè bờ hồ bằng bê tông ở Hà Nội gây tác động tiêu cực gì đến hệ sinh thái?",
        "dap_an": ["Làm nước hồ sạch hơn", "Mất vùng đệm ven bờ, giảm sinh vật trú ẩn", "Tăng lượng oxy hòa tan", "Giúp cây thủy sinh phát triển"],
        "dap_an_dung": "Mất vùng đệm ven bờ, giảm sinh vật trú ẩn",
        "anh_minh_hoa": "https://images.unsplash.com/photo-1527488975949-5f21469e5746?auto=format&fit=crop&w=800&q=80"
    }
]

# --- KHỞI TẠO BỘ NHỚ TRẠNG THÁI ---
if 'cau_hien_tai' not in st.session_state:
    st.session_state.cau_hien_tai = 0
if 'diem_so' not in st.session_state:
    st.session_state.diem_so = 0

# --- GIAO DIỆN CHÍNH ---
st.markdown("<h1 style='text-align: center; color: #2ecc71;'>🌿 Khám Phá Sinh Thái Hà Nội</h1>", unsafe_allow_html=True)
st.markdown("---")

total_q = len(danh_sach_cau_hoi)

# Nếu chưa làm hết câu hỏi
if st.session_state.cau_hien_tai < total_q:
    cau_hoi_data = danh_sach_cau_hoi[st.session_state.cau_hien_tai]
    
    # 1. Hiển thị thanh tiến trình
    progress = st.session_state.cau_hien_tai / total_q
    st.progress(progress)
    st.caption(f"Đang giải câu {st.session_state.cau_hien_tai + 1} / {total_q}")
    
    # 2. Hiển thị ảnh minh họa (Dùng st.image mượt mà)
    st.image(cau_hoi_data["anh_minh_hoa"], use_container_width=True)
    
    # 3. Hiển thị câu hỏi trong hộp màu
    st.markdown(f'<div class="question-box"><h3>{cau_hoi_data["cau_hoi"]}</h3></div>', unsafe_allow_html=True)
    
    # 4. Chia cột cho đáp án
    col1, col2 = st.columns(2)
    dap_an_list = cau_hoi_data["dap_an"]
    
    with col1:
        btn_A = st.button(f"A. {dap_an_list[0]}", use_container_width=True)
        btn_C = st.button(f"C. {dap_an_list[2]}", use_container_width=True)
        
    with col2:
        btn_B = st.button(f"B. {dap_an_list[1]}", use_container_width=True)
        btn_D = st.button(f"D. {dap_an_list[3]}", use_container_width=True)

    # 5. Logic kiểm tra đúng sai
    lua_chon = None
    if btn_A: lua_chon = dap_an_list[0]
    if btn_B: lua_chon = dap_an_list[1]
    if btn_C: lua_chon = dap_an_list[2]
    if btn_D: lua_chon = dap_an_list[3]

    if lua_chon:
        if lua_chon == cau_hoi_data["dap_an_dung"]:
            st.success("🎉 Chính xác! Đang chuyển trang...")
            st.session_state.diem_so += 10
            time.sleep(0.8) # Đã giảm thời gian chờ xuống 0.8s để bớt cảm giác lag
            st.session_state.cau_hien_tai += 1
            st.rerun()
        else:
            st.error("❌ Rất tiếc, chưa chính xác. Hãy chọn lại nhé!")

# Nếu đã làm xong hết
else:
    st.progress(1.0)
    st.balloons()
    st.markdown("<div class='question-box'>", unsafe_allow_html=True)
    st.success(f"🏆 TUYỆT VỜI! BẠN ĐÃ HOÀN THÀNH BÀI TRẮC NGHIỆM!")
    st.info(f"Tổng điểm của bạn: **{st.session_state.diem_so}** / {total_q * 10}")
    st.markdown("</div>", unsafe_allow_html=True)
    
    if st.button("🔄 Chơi lại từ đầu", type="primary", use_container_width=True):
        st.session_state.cau_hien_tai = 0
        st.session_state.diem_so = 0
        st.rerun()
