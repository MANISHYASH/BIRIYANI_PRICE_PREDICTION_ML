import streamlit as st
import modelbit

def predict_biryani_price(chicken_price, rice_price, vegetable_price, spices_price, chef_experience):
    # Prepare the input data
    data = [chicken_price, rice_price, spices_price, vegetable_price, chef_experience]
    try:
        # Get inference from the modelbit API
        response = modelbit.get_inference(
            region="ap-south-1",
            workspace="manishyashwant",
            deployment="predict_biryani_price",
            data=data
        )
        # Extract the predicted price
        predicted_price = response.get('data', {}).get('Biryani_Price', None)
        return predicted_price
    except Exception as e:
        st.error(f"Error: {e}")
        return None

# Streamlit app
st.title('Biryani Price Predictor')

# Input fields
chicken_price = st.text_input('Chicken Price')
rice_price = st.text_input('Rice Price')
vegetable_price = st.text_input('Vegetable Price')
spices_price = st.text_input('Spices Price')
chef_experience = st.text_input('Chef Experience')

# Convert inputs to appropriate data types
try:
    chicken_price = float(chicken_price)
    rice_price = float(rice_price)
    vegetable_price = float(vegetable_price)
    spices_price = float(spices_price)
    chef_experience = float(chef_experience)
except ValueError:
    st.error("Please enter valid numbers.")
    st.stop()

# Predict button
if st.button('Predict'):
    price = predict_biryani_price(chicken_price, rice_price, vegetable_price, spices_price, chef_experience)
    if price is not None:
        st.write(f'Predicted Biryani Price: ₹{price:.2f}')
    else:
        st.write("Could not retrieve prediction.")
