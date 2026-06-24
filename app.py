import streamlit as st
st.image("logo.jpg.jfif")

st.set_page_config(page_title="Tính Khoản Vay", page_icon="💰")

st.title("💰 Công Cụ Tính Khoản Vay")

# Nhập dữ liệu
so_tien_vay = st.number_input(
    "Nhập số tiền vay (VNĐ)",
    min_value=0,
    value=200000000,
    step=1000000
)

so_thang_vay = st.number_input(
    "Nhập số tháng vay",
    min_value=1,
    value=12,
    step=1
)

lai_suat_nam = st.number_input(
    "Nhập lãi suất năm (%/năm)",
    min_value=0.0,
    value=9,3 ,
    step=0.1
)

if st.button("Tính toán"):
    # Tính toán
    goc_thang = so_tien_vay / so_thang_vay

    lai_thang = so_tien_vay * (lai_suat_nam / 100) / 12

    tong_thang = goc_thang + lai_thang

    tong_thanh_toan = tong_thang * so_thang_vay

    tong_lai = tong_thanh_toan - so_tien_vay

    # Hiển thị kết quả
    st.subheader("===== KẾT QUẢ =====")

    st.success(
        f"Số tiền gốc phải trả mỗi tháng: {goc_thang:,.0f} VNĐ"
    )

    st.success(
        f"Số tiền lãi phải trả mỗi tháng: {lai_thang:,.0f} VNĐ"
    )

    st.success(
        f"Tổng số tiền phải trả mỗi tháng: {tong_thang:,.0f} VNĐ"
    )

    st.info(
        f"Tổng số tiền phải trả sau {so_thang_vay} tháng: {tong_thanh_toan:,.0f} VNĐ"
    )

    st.info(
        f"Tổng tiền lãi phải trả: {tong_lai:,.0f} VNĐ"
    )
    )
