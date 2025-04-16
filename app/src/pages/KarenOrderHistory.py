import streamlit as st

st.title("Order History")

# Mock order data
orders = [
    {
        "order_id": 1,
        "pickup_time": "2025-04-10 10:00",
        "location": "Lawrence Laundry",
        "total_cost": 25.14,
        "treatment": "Detergent: Gentle, Temperature: Cold"
    },
    {
        "order_id": 2,
        "pickup_time": "2025-04-05 14:00",
        "location": "Suds and Duds",
        "total_cost": 29.99,
        "treatment": "Detergent: Regular, Temperature: Warm"
    }
]

# Optional refresh button
if st.button("Refresh Orders"):
    st.write("Orders refreshed!")

# Display orders
for order in orders:
    with st.expander(f"Order on {order['pickup_time']} at {order['location']}"):
        st.write(f"Total Cost: ${order['total_cost']:.2f}")
        st.write(f"Treatment: {order['treatment']}")