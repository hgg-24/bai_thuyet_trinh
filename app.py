import streamlit as st
import time

# --- 1. CẤU HÌNH TRANG VÀ GIAO DIỆN (UI/CSS) ---
st.set_page_config(page_title="Đấu Trường Sinh Thái Hà Nội", page_icon="🌿", layout="centered")

# --- CSS NÂNG CAO: ĐẸP, HIỆN ĐẠI, CHỐNG LAG, MÀU NÚT ---
st.markdown("""
<style>
    /* Ẩn các menu mặc định của Streamlit để web nhẹ và giống App thật hơn */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Background pattern nhẹ nhàng chuẩn sinh thái */
    .stApp {
        background-color: #f7fff7;
        background-image: radial-gradient(#d3eee0 0.8px, transparent 0.8px);
        background-size: 15px 15px;
    }

    /* Tiêu đề chính đẹp hơn */
    .title-text {
        text-align: center;
        color: #1a6d3f;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-weight: 800;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.1);
        padding-bottom: 25px;
    }

    /* Khung câu hỏi bo góc, đổ bóng, viền xanh lá mượt */
    .question-box {
        background: white;
        padding: 30px;
        border-radius: 20px;
        border-left: 10px solid #2ecc71;
        box-shadow: 0 10px 25px rgba(0,0,0,0.06);
        margin-bottom: 30px;
        margin-top: 10px;
        color: #2c3e50;
    }
    
    .question-box h3 {
        font-weight: 700;
        line-height: 1.4;
    }

    /* TÙY CHỈNH NÚT BẤM (NÚT CHỌN ĐÁP ÁN A B C D) */
    div.stButton > button {
        border-radius: 15px;
        min-height: 85px;
        height: auto;
        font-size: 18px;
        font-weight: 600;
        color: #34495e;
        background-color: white;
        border: 2px solid #e2e8f0;
        transition: all 0.2s ease-in-out;
        white-space: normal;
        word-wrap: break-word;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    }
    
    /* Hiệu ứng nảy và đổi màu khi di chuột vào nút thường */
    div.stButton > button:hover {
        border-color: #2ecc71;
        color: #2ecc71;
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(46, 204, 113, 0.1);
    }
    
    /* MÀU XANH KHI CHỌN ĐÚNG */
    div.stButton > button.correct {
        background-color: #c8f7dc !important;
        border-color: #2ecc71 !important;
        color: #1e8449 !important;
        box-shadow: 0 4px 10px rgba(46, 204, 113, 0.2);
    }
    
    /* MÀU ĐỎ KHI CHỌN SAI */
    div.stButton > button.incorrect {
        background-color: #ffcccc !important;
        border-color: #ff4d4d !important;
        color: #b30000 !important;
        box-shadow: 0 4px 10px rgba(255, 77, 77, 0.2);
    }
</style>
""", unsafe_allow_html=True)

# --- 2. NGÂN HÀNG CÂU HỎI CHUẨN (Bộ 10 câu Ao Hồ Hà Nội) ---
danh_sach_cau_hoi = [
    {
        "cau_hoi": "Câu 1. Hồ nào ở Hà Nội có nguồn gốc là đoạn sông Hồng cũ còn sót lại?",
        "dap_an": ["Hồ Gươm", "Hồ Tây", "Hồ Trúc Bạch", "Hồ Thiền Quang"],
        "dap_an_dung": "Hồ Tây" # 1B
    },
    {
        "cau_hoi": "Câu 2. Hiện tượng “nở hoa nước” ở hồ Hà Nội chủ yếu do loại sinh vật nào gây ra?",
        "dap_an": ["Bèo tây", "Tảo lam", "Rong đuôi chó", "Sen"],
        "dap_an_dung": "Tảo lam" # 2B
    },
    {
        "cau_hoi": "Câu 3. Sông nào ở Hà Nội bị ô nhiễm nặng, mệnh danh là “dòng sông chết”?",
        "dap_an": ["Sông Hồng", "Sông Đuống", "Sông Tô Lịch", "Sông Nhuệ"],
        "dap_an_dung": "Sông Tô Lịch" # 3C
    },
    {
        "cau_hoi": "Câu 4. Loài thực vật thủy sinh nào hấp thụ kim loại nặng, dùng để xử lý nước hồ?",
        "dap_an": ["Hoa súng", "Bèo tây", "Cây lau sậy", "Rau muống"],
        "dap_an_dung": "Bèo tây" # 4B
    },
    {
        "cau_hoi": "Câu 5. Vai trò chính của hệ thống hồ Hà Nội đối với đô thị là gì?",
        "dap_an": ["Nuôi trồng thủy sản", "Điều hòa vi khí hậu, thoát nước", "Giao thông thủy", "Khai thác du lịch"],
        "dap_an_dung": "Điều hòa vi khí hậu, thoát nước" # 5B (rút gọn text)
    },
    {
        "cau_hoi": "Câu 6. Yếu tố nào đe dọa đa dạng sinh học ở hồ Hà Nội nhiều nhất hiện nay?",
        "dap_an": ["Thay đổi mực nước", "Xả thải sinh hoạt, lấn chiếm", "Đánh bắt tự phát", "Thả hoa đăng"],
        "dap_an_dung": "Xả thải sinh hoạt, lấn chiếm" # 6B
    },
    {
        "cau_hoi": "Câu 7. Hệ sinh thái sông Hồng đoạn qua Hà Nội khác hồ nội đô ở điểm nào?",
        "dap_an": ["Nước tĩnh", "Nước chảy, phù sa nhiều, đa dạng cá sông hơn", "Không có thực vật thủy sinh", "Độ mặn cao"],
        "dap_an_dung": "Nước chảy, phù sa nhiều, đa dạng cá sông hơn" # 7B
    },
    {
        "cau_hoi": "Câu 8. Biện pháp sinh học nào đang cải tạo sông Tô Lịch?",
        "dap_an": ["Thả cá chép", "Dùng chế phẩm vi sinh + bèo, thủy sinh lọc nước", "Lắp quạt sục khí", "Xây đập ngăn dòng"],
        "dap_an_dung": "Dùng chế phẩm vi sinh + bèo, thủy sinh lọc nước" # 8B (rút gọn text)
    },
    {
        "cau_hoi": "Câu 9. Loài cá bản địa từng rất phổ biến ở Hồ Tây nhưng nay đã suy giảm mạnh?",
        "dap_an": ["Cá mè", "Cá chép", "Cá rô phi", "Cá trôi"],
        "dap_an_dung": "Cá chép" # 9B
    },
    {
        "cau_hoi": "Câu 10. Việc kè bờ hồ bằng bê tông gây tác động tiêu cực gì đến hệ sinh thái?",
        "dap_an": ["Làm nước hồ sạch hơn", "Mất vùng đệm ven bờ, giảm sinh vật trú ẩn", "Tăng oxy hòa tan", "Gi giúp cây thủy sinh"],
        "dap_an_dung": "Mất vùng đệm ven bờ, giảm sinh vật trú ẩn" # 10B (rút gọn text)
    }
]

# --- 3. KHỞI TẠO BỘ NHỚ TRẠNG THÁI (Session State) ---
# Cơ chế cực kỳ quan trọng để đổi màu nút và giữ câu hỏi
if 'cau_hien_tai' not in st.session_state:
    st.session_state.cau_hien_tai = 0
# Theo dõi các nút sai đã bị bấm để báo đỏ
if 'nut_da_bam_sai' not in st.session_state:
    st.session_state.nut_da_bam_sai = []
# Đánh dấu khi đã trả lời đúng để hiện nút "Tiếp theo"
if 'da_tra_loi_dung' not in st.session_state:
    st.session_state.da_tra_loi_dung = False

# --- 4. GIAO DIỆN CHÍNH ---
st.markdown("<h1 class='title-text'>🌿 Khám Phá Ao Hồ Hà Nội</h1>", unsafe_allow_html=True)
st.markdown("---")

total_q = len(danh_sach_cau_hoi)

# Nếu trò chơi kết thúc (Hết 10 câu)
if st.session_state.cau_hien_tai >= total_q:
    st.progress(1.0)
    st.balloons()
    st.markdown("<div class='question-box' style='text-align: center; padding: 50px;'>", unsafe_allow_html=True)
    st.markdown("<h1 style='color: #2ecc71; font-size: 80px;'>🏆</h1>", unsafe_allow_html=True)
    st.markdown("<h2>XUẤT SẮC! BẠN ĐÃ HOÀN THÀNH BÀI TRẮC NGHIỆM!</h2>", unsafe_allow_html=True)
    st.markdown(f"<h4>Bạn đã giải mã hết bộ **{total_q}** câu hỏi về sinh thái Hà Nội.</h4>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Nút chơi lại từ đầu
    if st.button("🔄 Chơi lại từ đầu", type="primary", use_container_width=True):
        st.session_state.cau_hien_tai = 0
        st.session_state.nut_da_bam_sai = []
        st.session_state.da_tra_loi_dung = False
        st.rerun()

# Nếu đang trong quá trình chơi
else:
    cau_hoi_data = danh_sach_cau_hoi[st.session_state.cau_hien_tai]
    dap_an_dung = cau_hoi_data["dap_an_dung"]
    
    # --- CHẨN ĐOÁN LỖI DỮ LIỆU (ANTI-CRASH) ---
    # Code sẽ tự kiểm tra xem câu hỏi này có trường 'dap_an' hợp lệ không
    has_error = False
    if "dap_an" not in cau_hoi_data or cau_hoi_data["dap_an"] is None or not isinstance(cau_hoi_data["dap_an"], list):
        print(f"--- [ERROR LOG] CẢNH BÁO DỮ LIỆU ---")
        print(f"Câu số {st.session_state.cau_hien_tai + 1} bị sai dữ liệu 'dap_an'!")
        print(f"Dữ liệu câu hỏi: {cau_hoi_data}")
        has_error = True
        
    if has_error:
        st.markdown(f'<div class="question-box"><h3>{cau_hoi_data["cau_hoi"]}</h3></div>', unsafe_allow_html=True)
        st.error(f"❌ Lỗi dữ liệu! Câu hỏi số {st.session_state.cau_hien_tai + 1} chưa được điền danh sách đáp án hợp lệ hoặc kiểu dữ liệu sai.")
        st.caption("Hãy kiểm tra file `app.py` trên GitHub ở câu hỏi này.")
        
        # Cho phép người thuyết trình bỏ qua câu bị lỗi để không đứng app
        col1, col2 = st.columns([3, 1])
        with col1:
            st.warning("Vui lòng sửa dữ liệu trên GitHub.")
        with col2:
            if st.button("Bỏ qua câu này ⏩", type="secondary", use_container_width=True):
                st.session_state.cau_hien_tai += 1
                st.session_state.nut_da_bam_sai = []
                st.session_state.da_tra_loi_dung = False
                st.rerun()
    # --- KẾT THÚC CHẨN ĐOÁN LỖI DỮ LIỆU ---
    
    # Tiếp tục chơi nếu dữ liệu chuẩn
    else:
        dap_an_list = cau_hoi_data["dap_an"]

        # Thanh tiến trình (Progress bar)
        progress = st.session_state.cau_hien_tai / total_q
        st.progress(progress)
        st.caption(f"Đang giải câu hỏi {st.session_state.cau_hien_tai + 1} trên {total_q}")
        
        # Hiển thị câu hỏi trong hộp màu bo góc
        st.markdown(f'<div class="question-box"><h3>{cau_hoi_data["cau_hoi"]}</h3></div>', unsafe_allow_html=True)
        
        # Chia 2 cột cho 4 đáp án A B C D cho đẹp
        col1, col2 = st.columns(2)
        
        # Hàm xử lý logic khi bấm bất kỳ nút nào
        def run_check(ans, button_name):
            # Nếu đáp án ĐÚNG
            if ans == dap_an_dung:
                st.session_state.da_tra_loi_dung = True # Đánh dấu đã tìm được câu đúng để hiện nút "Tiếp theo"
                # Khi đúng thì xóa hết lịch sử các nút đã bấm sai trước đó cho sạch
                st.session_state.nut_da_bam_sai = []
                st.rerun() # Tự động load lại để cập nhật giao diện
            # Nếu đáp án SAI
            else:
                # Nếu đã đúng rồi mà vẫn bấm nút sai thì không làm gì
                if st.session_state.da_tra_loi_dung: return
                # Lưu tên nút đã bấm sai vào bộ nhớ
                if button_name not in st.session_state.nut_da_bam_sai:
                    st.session_state.nut_da_bam_sai.append(button_name)
                # Load lại để hiện màu Đỏ và cho người chơi bấm nút khác (VẪN ĐỨNG IM CÂU NÀY)
                st.rerun()

        # Tạo nút bấm và xác định màu dựa trên session state
        with col1:
            # --- NÚT A ---
            button_id_A = f"btn_{st.session_state.cau_hien_tai}_A"
            class_name_A = ""
            # Nếu đã đúng rồi, thì nút A chỉ hiện màu xanh nếu bản thân nó là đáp án đúng
            if st.session_state.da_tra_loi_dung:
                if dap_an_list[0] == dap_an_dung: class_name_A = "correct"
            # Nếu chưa trả lời đúng, thì hiện đỏ nếu nó nằm trong danh sách nút sai đã bấm
            else:
                if button_id_A in st.session_state.nut_da_bam_sai: class_name_A = "incorrect"
                
            # Nút A thực sự (Standard Standard st.button)
            if st.button(f"A. {dap_an_list[0]}", key=button_id_A, use_container_width=True, class_name=class_name_A):
                run_check(dap_an_list[0], button_id_A)

            # --- NÚT C ---
            button_id_C = f"btn_{st.session_state.cau_hien_tai}_C"
            class_name_C = ""
            if st.session_state.da_tra_loi_dung:
                if dap_an_list[2] == dap_an_dung: class_name_C = "correct"
            else:
                if button_id_C in st.session_state.nut_da_bam_sai: class_name_C = "incorrect"
                
            if st.button(f"C. {dap_an_list[2]}", key=button_id_C, use_container_width=True, class_name=class_name_C):
                run_check(dap_an_list[2], button_id_C)
                
        with col2:
            # --- NÚT B ---
            button_id_B = f"btn_{st.session_state.cau_hien_tai}_B"
            class_name_B = ""
            if st.session_state.da_tra_loi_dung:
                if dap_an_list[1] == dap_an_dung: class_name_B = "correct"
            else:
                if button_id_B in st.session_state.nut_da_bam_sai: class_name_B = "incorrect"
                
            if st.button(f"B. {dap_an_list[1]}", key=button_id_B, use_container_width=True, class_name=class_name_B):
                run_check(dap_an_list[1], button_id_B)

            # --- NÚT D ---
            button_id_D = f"btn_{st.session_state.cau_hien_tai}_D"
            class_name_D = ""
            if st.session_state.da_tra_loi_dung:
                if dap_an_list[3] == dap_an_dung: class_name_D = "correct"
            else:
                if button_id_D in st.session_state.nut_da_bam_sai: class_name_D = "incorrect"
                
            if st.button(f"D. {dap_an_list[3]}", key=button_id_D, use_container_width=True, class_name=class_name_D):
                run_check(dap_an_list[3], button_id_D)

        # --- NÚT CHUYỂN CÂU (CHỈ HIỆN KHI ĐÃ ĐÚNG) ---
        st.markdown("---")
        if st.session_state.da_tra_loi_dung:
            st.success(f"🎉 CHÍNH XÁC! Đáp án chính xác là: **{dap_an_dung}**.")
            st.caption("Bấm nút 'Câu tiếp theo' bên dưới để chuyển sang câu trắc nghiệm tiếp theo.")
            
            # Nút chuyển câu "Câu tiếp theo"
            if st.button("Câu tiếp theo ➡️", type="primary", use_container_width=True):
                # Tăng số thứ tự câu hỏi
                st.session_state.cau_hien_tai += 1
                # Xóa hết lịch sử bấm sai của câu vừa rồi cho sạch
                st.session_state.nut_da_bam_sai = []
                # Đánh dấu là câu hỏi mới chưa trả lời
                st.session_state.da_tra_loi_dung = False
                st.rerun() # Load sang câu tiếp theo
