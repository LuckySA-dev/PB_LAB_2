import streamlit as st

# 1. กำหนดค่าคงที่สำหรับอัตราค่าใช้จ่าย
CAR_RATE = 4    # รถยนต์ใช้น้ำมัน กิโลเมตรละ 4 บาท
EV_RATE = 1     # รถไฟฟ้า กิโลเมตรละ 1 บาท

# 2. ฟังก์ชันหลักของแอป Streamlit
def main():
    st.title("โปรแกรมคำนวณค่าใช้จ่ายการเดินทาง")

    # รับค่าระยะทางจากผู้ใช้
    distance = st.number_input("กรุณากรอกระยะทางที่ต้องการเดินทาง (กิโลเมตร)", min_value=0.0, step=0.1)

    # เลือกยานพาหนะ
    vehicle = st.radio("เลือกยานพาหนะที่ใช้:", ("รถยนต์ใช้น้ำมัน", "รถไฟฟ้า"))

    # คำนวณค่าใช้จ่าย
    if vehicle == "รถยนต์ใช้น้ำมัน":
        rate = CAR_RATE
        vehicle_name = "รถยนต์ใช้น้ำมัน"
    else:
        rate = EV_RATE
        vehicle_name = "รถไฟฟ้า"

    # คำนวณค่าใช้จ่ายรวม
    total_cost = distance * rate

    # แสดงผลลัพธ์
    if distance > 0:
        st.write(f"### สรุปผลการคำนวณค่าใช้จ่าย")
        st.write(f"  ระยะทางรวมที่เดินทาง: {distance:.2f} กิโลเมตร")
        st.write(f"  ยานพาหนะที่ใช้: {vehicle_name}")
        st.write(f"  อัตราค่าใช้จ่าย: {rate:.2f} บาท/กม.")
        st.write(f"  **ค่าใช้จ่ายรวม: {total_cost:.2f} บาท**")

if __name__ == "__main__":
    main()
