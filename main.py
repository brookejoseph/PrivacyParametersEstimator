import streamlit as st

def determine_privacy_params(data_amount):
    epsilon_min, epsilon_max = 0.1, 1.0
    delta_min, delta_max = 1e-6, 1e-5
    sensitivity_min, sensitivity_max = 1.0, 2.0

    data_min, data_max = 100, 10000


    epsilon = epsilon_min + (epsilon_max - epsilon_min) * (data_amount - data_min) / (data_max - data_min)
    epsilon = max(min(epsilon, epsilon_max), epsilon_min) 

    delta = delta_min + (delta_max - delta_min) * (data_amount - data_min) / (data_max - data_min)
    delta = max(min(delta, delta_max), delta_min) 


    sensitivity = sensitivity_min + (sensitivity_max - sensitivity_min) * (data_amount - data_min) / (data_max - data_min)
    sensitivity = max(min(sensitivity, sensitivity_max), sensitivity_min)  

    return {
        "epsilon": epsilon,
        "delta": delta,
        "sensitivity": sensitivity
    }

st.title("Privacy Parameters Estimator")

st.sidebar.header("Input Parameters")
data_amount = st.sidebar.slider("Amount of Data", 100, 10000, 5000)

st.sidebar.markdown("""
Adjust the slider to set the amount of data. The app will calculate and display the privacy parameters accordingly.
""")


privacy_params = determine_privacy_params(data_amount)


st.subheader("Privacy Parameters")
st.write(f"**Epsilon (Privacy Budget):** {privacy_params['epsilon']:.3f}")
st.write(f"**Delta (Failure Probability):** {privacy_params['delta']:.7f}")
st.write(f"**Sensitivity:** {privacy_params['sensitivity']:.3f}")

# Visualization
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.bar(['Epsilon', 'Delta (1e-6)', 'Sensitivity'], 
       [privacy_params['epsilon'], privacy_params['delta'] * 1e6, privacy_params['sensitivity']], 
       color=['violet', 'pink', 'magenta'])

ax.set_ylabel('Value')
ax.set_title('Privacy Parameters')

st.pyplot(fig)
