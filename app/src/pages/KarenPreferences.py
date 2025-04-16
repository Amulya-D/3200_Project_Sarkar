import streamlit as st
import requests

st.set_page_config(page_title="Karen's Laundry Preferences", layout="centered")

st.title("👵 Karen's Laundry Preferences")
st.markdown("Welcome, Karen! Let's make sure your delicate clothes are treated with care.")

API_BASE = "http://localhost:3111" 

st.header("🧼 Laundry Treatment Options")

treatment = st.selectbox("How should we handle your laundry?", ["Standard", "Delicate"])
if st.button("Update Treatment to Order #1"):
    response = requests.put(f"{API_BASE}/Orders/1/{treatment.lower()}")
    if response.status_code == 200:
        st.success("Treatment updated successfully!")
    else:
        st.error("Something went wrong updating the treatment.")

st.header("🖼️ View a Clothing Item")

image_url = st.text_input("Enter image URL (e.g. blouse123.png):", "blouse123.png")
if st.button("Fetch Clothing Info"):
    response = requests.get(f"{API_BASE}/Clothing/{image_url}")
    if response.status_code == 200:
        data = response.json()
        st.image(data["image_url"], caption=data["item_name"])
    else:
        st.warning("Clothing not found.")

st.header("💳 Payment Method")

payment = st.radio("Choose a payment method for Order #1:", ["cash", "card"])
if st.button("Update Payment Method"):
    response = requests.put(f"{API_BASE}/OrderDetails", json={
        "order_id": 1,
        "payment_method": payment
    })
    if response.status_code == 200:
        st.success("Payment method updated.")
    else:
        st.error("Could not update payment method.")

st.header("📜 View Past Orders")





st.header("⭐ Read Laundromat Reviews")

laundromat_id = st.number_input("Enter laundromat ID", value=1, step=1)
if st.button("Fetch Reviews"):
    response = requests.get(f"{API_BASE}/CustomerReviews/{laundromat_id}")
    if response.status_code == 200:
        reviews = response.json()
        for r in reviews:
            st.markdown(f"**Rating:** {r['rating']} ⭐")
            st.write(r['comment'])
            st.markdown("---")
    else:
        st.warning("No reviews found.")

if st.button("View Karen's Order History", type="primary", use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'user'
    st.session_state['first_name'] = 'Karen'
    st.switch_page("pages/KarenOrderHistory.py")