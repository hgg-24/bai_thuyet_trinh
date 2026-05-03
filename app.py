import streamlit as st
import time

# --- 1. CẤU HÌNH TRANG VÀ GIAO DIỆN (UI/CSS) ---
st.set_page_config(page_title="Trắc Nghiệm Sinh Thái Hà Nội", page_icon="🌿", layout="centered")

# --- CSS NÂNG CAO CHO NÚT BẤM CÓ MÀU ĐÚNG/SAI ---
st.markdown("""
<style>
    /* Ẩn các menu mặc định của Streamlit để web giống App thật hơn */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Background pattern nhẹ nhàng */
    .stApp {
        background-color: #f6fff6;
        background-image: radial-gradient(#d4eed9 0.5px, transparent 0.5px);
        background-size: 10px 10px;
    }

    /* Tiêu đề chính đẹp hơn */
    .title-text {
        text-align: center;
        color: #16a085;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-weight: 800;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        padding-bottom: 20px;
    }

    /* Khung câu hỏi hiện đại */
    .question-box {
        background: white;
        padding: 30px;
        border-radius: 20px;
        border-left: 8px solid #2ecc71;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        margin-bottom: 30px;
        margin-top: 10px;
        color: #34495e;
    }
    
    .question-box h3 {
        font-weight: 700;
        line-height: 1.4;
    }

    /* TÙY CHỈNH NÚT BẤM (NÚT CHỌN ĐÁP ÁN) */
    div.stButton > button {
        border-radius: 15px;
        min-height: 80px;
        height: auto;
        font-size: 18px;
        font-weight: 600;
        color: #34495e;
        background-color: white;
        border: 2px solid #e0e6ed;
        transition: all 0.2s ease-in-out;
        white-space: normal;
        word-wrap: break-word;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    }
    
    /* Hiệu ứng nảy khi di chuột */
    div.stButton > button:hover {
        border-color: #2ecc71;
        color: #2ecc71;
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(46, 204, 113, 0.1);
    }
    
    /* MÀU ĐỎ KHI CHỌN SAI */
    div.stButton > button.incorrect {
        background-color: #ffcccc !important;
        border-color: #ff4d4d !important;
        color: #b30000 !important;
    }
    
    /* MÀU XANH KHI CHỌN ĐÚNG */
    div.stButton > button.correct {
        background-color: #c8f7dc !important;
        border-color: #2ecc71 !important;
        color: #1e8449 !important;
    }
</style>
""", unsafe_allow_html=True)

# --- 2. NGÂN HÀNG CÂU HỎI (Bộ 10 câu - Đã xóa link ảnh) ---
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
        "cau_hoi": "Câu 3. Sông nào ở Hà Nội bị ô nhiễm nặng, mệnh danh là “dòng sông chết”?",
        "dap_an": ["Sông Hồng", "Sông Đuống", "Sông Tô Lịch", "Sông Nhuệ"],
        "dap_an_dung": "Sông Tô Lịch"
    },
    {
        "cau_hoi": "Câu 4. Loài thực vật thủy sinh nào có khả năng hấp thụ kim loại nặng, dùng để xử lý nước hồ?",
        "dap_an": ["Hoa súng", "Bèo tây", "Cây lau sậy", "Rau muống"],
        "dap_an_dung": "Bèo tây"
    },
    {
        "cau_hoi": "Câu 5. Vai trò chính của hệ thống hồ Hà Nội đối với đô thị là gì?",
        "dap_an": ["Nuôi trồng thủy sản", "Điều hòa vi khí hậu, thoát nước", "Giao thông thủy", "Khai thác du lịch tâm linh"],
        "dap_an_dung": "Điều hòa vi khí hậu, thoát nước"
    },
    {
        "cau_hoi": "Câu 6. Yếu tố nào đe dọa đa dạng sinh học ở hồ Hà Nội nhiều nhất hiện nay?",
        "dap_an": ["Thay đổi mực nước", "Xả thải, lấn chiếm", "Đánh bắt tự phát", "Thả hoa đăng"],
        "dap_an_dung": "Xả thải, lấn chiếm"
    },
    {
        "cau_hoi": "Câu 7. Hệ sinh thái sông Hồng đoạn qua Hà Nội khác hồ nội đô ở điểm nào?",
        "dap_an": ["Nước tĩnh", "Nước chảy, phù sa, đa dạng cá", "Không có thực vật thủy sinh", "Độ mặn cao"],
        "dap_an_dung": "Nước chảy, phù sa, đa dạng cá"
    },
    {
        "cau_hoi": "Câu 8. Biện pháp sinh học nào đang cải tạo sông Tô Lịch?",
        "dap_an": ["Thả cá chép", "Chế phẩm vi sinh + bèo, thủy sinh", "Lắp quạt sục khí", "Xây đập ngăn dòng"],
        "dap_an_dung": "Chế phẩm vi sinh + bèo, thủy sinh"
    },
    {
        "cau_hoi": "Câu 9. Loài cá bản địa nào từng phổ biến ở Hồ Tây nhưng nay đã suy giảm mạnh?",
        "dap_an": ["Cá mè", "Cá chép", "Cá rô phi", "Cá trôi"],
        "dap_an_dung": "Cá chép"
    },
    {
        "cau_hoi": "Câu 10. Việc kè bờ hồ bằng bê tông gây tác động tiêu cực gì đến hệ sinh thái?",
        "dap_an": ["Nước sạch hơn", "Mất vùng đệm, giảm nơi trú ẩn", "Tăng oxy hòa tan", "Giúp cây thủy sinh"],
        "dap_an_dung": "Mất vùng đệm, giảm nơi trú ẩn"
    }
]

# --- 3. KHỞI TẠO BỘ NHỚ TRẠNG THÁI (Session State) ---
# Dùng để theo dõi nút nào đã bấm, bấm đúng hay sai
if 'cau_hien_tai' not in st.session_state:
    st.session_state.cau_hien_tai = 0
if 'nut_da_bam' not in st.session_state:
    st.session_state.nut_da_bam = []
if 'da_tra_loi_dung' not in st.session_state:
    st.session_state.da_tra_loi_dung = False

# --- 4. GIAO DIỆN CHÍNH ---
st.markdown("<h1 class='title-text'>🌿 Sinh Thái Ao Hồ Hà Nội</h1>", unsafe_allow_html=True)
st.markdown("---")

total_q = len(danh_sach_cau_hoi)

# Trò chơi kết thúc
if st.session_state.cau_hien_tai >= total_q:
    st.progress(1.0)
    st.balloons()
    st.markdown("<div class='question-box' style='text-align: center;'>", unsafe_allow_html=True)
    st.markdown("<h1 style='color: #2ecc71; font-size: 50px;'>🏆</h1>", unsafe_allow_html=True)
    st.success(f"XUẤT SẮC! BẠN ĐÃ HOÀN THÀNH!")
    st.info(f"Tổng số câu hỏi: **{total_q}** câu")
    st.markdown("</div>", unsafe_allow_html=True)
    
    if st.button("🔄 Chơi lại từ đầu", type="primary", use_container_width=True):
        st.session_state.cau_hien_tai = 0
        st.session_state.nut_da_bam = []
        st.session_state.da_tra_loi_dung = False
        st.rerun()

# Trò chơi đang diễn ra
else:
    cau_hoi_data = danh_sach_cau_hoi[st.session_state.cau_hien_tai]
    dap_an_list = cau_hoi_data["dap_an"]
    dap_an_dung = cau_hoi_data["dap_an_dung"]
    
    # Hiển thị thanh tiến trình
    progress = st.session_state.cau_hien_tai / total_q
    st.progress(progress)
    st.caption(f"Câu {st.session_state.cau_hien_tai + 1} / {total_q}")
    
    # Hiển thị câu hỏi trong hộp màu
    st.markdown(f'<div class="question-box"><h3>{cau_hoi_data["cau_hoi"]}</h3></div>', unsafe_allow_html=True)
    
    # Chia cột cho đáp án
    col1, col2 = st.columns(2)
    
    # Hàm xử lý khi bấm nút
    def run_check(ans, button_name):
        # Lưu lại tên nút đã bấm để đổi màu
        if button_name not in st.session_state.nut_da_bam:
            st.session_state.nut_da_bam.append(button_name)
            
        # Kiểm tra đúng sai
        if ans == dap_an_dung:
            st.session_state.da_tra_loi_dung = True # Đánh dấu đã đúng để chuyển câu
            st.rerun() # Load lại để hiện màu xanh ngay lập tức
        # Nếu sai thì load lại để hiện màu đỏ, vẫn đứng im câu này
        else:
            st.rerun()

    # Tạo nút bấm và đổi màu dựa trên trạng thái
    with col1:
        # NÚT A
        button_id_A = f"btn_{st.session_state.cau_hien_tai}_A"
        class_name_A = ""
        # Nếu đã trả lời đúng rồi thì A hiện màu sai
        if st.session_state.da_tra_loi_dung:
            if button_id_A in st.session_state.nut_da_bam: class_name_A = "incorrect"
        # Khác đúng
        else:
            if button_id_A in st.session_state.nut_da_bam: class_name_A = "incorrect"
            if st.session_state.da_tra_loi_dung and dap_an_list[0] == dap_an_dung: class_name_A = "correct"
            
        # Logic màu nếu sai cho chọn lại
        if button_id_A in st.session_state.nut_da_bam:
             if dap_an_list[0] == dap_an_dung: class_name_A = "correct"
             else: class_name_A = "incorrect"

        if st.button(f"A. {dap_an_list[0]}", key=button_id_A, use_container_width=True, class_name=class_name_A):
            run_check(dap_an_list[0], button_id_A)

        # NÚT C
        button_id_C = f"btn_{st.session_state.cau_hien_tai}_C"
        class_name_C = ""
        if button_id_C in st.session_state.nut_da_bam:
             if dap_an_list[2] == dap_an_dung: class_name_C = "correct"
             else: class_name_C = "incorrect"
             
        if st.button(f"C. {dap_an_list[2]}", key=button_id_C, use_container_width=True, class_name=class_name_C):
            run_check(dap_an_list[2], button_id_C)
            
    with col2:
        # NÚT B
        button_id_B = f"btn_{st.session_state.cau_hien_tai}_B"
        class_name_B = ""
        if button_id_B in st.session_state.nut_da_bam:
             if dap_an_list[1] == dap_an_dung: class_name_B = "correct"
             else: class_name_B = "incorrect"
             
        if st.button(f"B. {dap_an_list[1]}", key=button_id_B, use_container_width=True, class_name=class_name_B):
            run_check(dap_an_list[1], button_id_B)

        # NÚT D
        button_id_D = f"btn_{st.session_state.cau_hien_tai}_D"
        class_name_D = ""
        if button_id_D in st.session_state.nut_da_bam:
             if dap_an_list[3] == dap_an_dung: class_name_D = "correct"
             else: class_name_D = "incorrect"
             
        if st.button(f"D. {dap_an_list[3]}", key=button_id_D, use_container_width=True, class_name=class_name_D):
            run_check(dap_an_list[3], button_id_D)

    # NÚT CHUYỂN CÂU (Chỉ hiện khi đã đúng)
    st.markdown("---")
    if st.session_state.da_tra_loi_dung:
        st.success(f"🎉 CHÍNH XÁC! Đáp án là {dap_an_dung}. Bấm nút bên dưới để chuyển câu.")
        if st.button("Câu tiếp theo ➡️", type="primary", use_container_width=True):
            st.session_state.cau_hien_tai += 1
            st.session_state.nut_da_bam = []
            st.session_state.da_tra_loi_dung = False
            st.rerun()
