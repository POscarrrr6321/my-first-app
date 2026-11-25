import streamlit as st

st.markdown("# :red[คำcalculate your Body Mass Index BMI]")
st.write("กรอกข้อมูลน้ำหนักเเละส่วนสูงของคุณ เพื่อเช็กสุขภาพเบื้องต้น")

weight = st.number_input("enter your weight (kilogram):", min_value=0, value=0)
height = st.number_input("enter your height (centimeter):", mim_value=0, value=0)

if st.button("calculate BMI"):
  height_m = height_cm / 100
  BMI = weight / (height_m ** 2)

  st.write("---")
  st.header(f"your BMI is **{BMI:.2f}**")

  if BMI < 18.5:
    st.warning("!! your BMI is below average, you're underweight")
  elif 18.5 <= BMI < 23.0:
    st.success("your BMI meet the average, you're healthy")
  elif 23.0 <= BMI < 25.0:
    st.success("!! your BMI is above average, you're overweight")
  else:
    st.error("!! you're at risk of obesity, time to take care of your health")

st.divider()
st.write("นาย พงศ์เพียร ห่างสูงเนิน ม. 4/5 เลขที่ 22")
