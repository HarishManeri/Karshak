import streamlit as st

# Set page configuration
st.set_page_config(page_title="Karshak | Farm to Fork", page_icon="🌾", layout="centered")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Our Story", "Menu", "Contact Us"])

# Home Page
if page == "Home":
    st.title("🌾 Welcome to Karshak!")
    st.image("https://source.unsplash.com/1600x600/?farm,organic-food", use_column_width=True)
    st.subheader("From Farm to Fork")
    st.write("""
        At **Karshak**, we believe in fresh, sustainable, and locally sourced ingredients. 
        Our mission is to bring you closer to nature, one delicious meal at a time.
    """)
    st.success("Now open in your neighborhood!")

# Our Story Page
elif page == "Our Story":
    st.title("🌱 Our Story")
    st.write("""
        Karshak started with a vision to support local farmers and bring farm-fresh ingredients to your plate.
        We collaborate directly with farms to ensure high-quality produce without middlemen.
        
        Every dish we serve tells a story of the soil it came from.
    """)
    st.image("https://source.unsplash.com/800x400/?farmers,organic", use_column_width=True)

# Menu Page
elif page == "Menu":
    st.title("🍽️ Our Menu")
    menu_items = {
        "Farm Fresh Salad": "Lettuce, cherry tomatoes, cucumber, feta, and olives.",
        "Herbed Grilled Chicken": "Free-range chicken with rosemary and garlic.",
        "Rustic Veggie Pizza": "Fresh tomatoes, bell peppers, mushrooms, and cheese on a thin crust.",
        "Seasonal Smoothie": "A refreshing blend of local fruits and herbs."
    }
    for item, desc in menu_items.items():
        st.subheader(item)
        st.write(desc)

# Contact Page
elif page == "Contact Us":
    st.title("📞 Contact Us")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit = st.form_submit_button("Send")

        if submit:
            st.success(f"Thank you {name}, we’ll get back to you at {email} soon!")

    st.write("📍 Location: Tirupati")
    st.write("📱 Phone: +91-9346028588")
