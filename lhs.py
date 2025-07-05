import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import qmc
import plotly.express as px

# --- App Configuration ---
st.set_page_config(
    page_title="LHS Data Generator",
    page_icon="🎲",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Helper Functions ---

def generate_lhs_data(dimensions, samples):
    """
    Generates a Latin Hypercube Sampling dataset.

    Args:
        dimensions (int): The number of variables (dimensions).
        samples (int): The number of samples to generate.

    Returns:
        pandas.DataFrame: A DataFrame containing the generated LHS data.
    """
    sampler = qmc.LatinHypercube(d=dimensions)
    sample_points = sampler.random(n=samples)
    return pd.DataFrame(sample_points, columns=[f'Variable {i+1}' for i in range(dimensions)])

def convert_df_to_csv(df):
    """Converts a DataFrame to a CSV string for downloading."""
    return df.to_csv(index=False).encode('utf-8')


# --- Main Application UI ---

st.title("🎲 Latin Hypercube Sampling (LHS) Data Generator")

st.markdown("""
Welcome to the Latin Hypercube Sampling (LHS) Data Generator! This tool helps you create structured random samples from a multidimensional distribution.
LHS is a statistical method for generating a near-random sample of parameter values from a multidimensional distribution. It is often used in computer experiments and Monte Carlo simulations.
""")

# --- Sidebar for User Inputs ---
with st.sidebar:
    st.header("⚙️ Parameters")
    
    st.markdown("### 1. Define Dimensions & Samples")
    num_dimensions = st.number_input("Enter the number of dimensions (variables):", min_value=2, max_value=100, value=2, step=1,
                                     help="This is the number of independent variables in your dataset.")
    
    num_samples = st.number_input("Enter the number of samples:", min_value=1, max_value=10000, value=100, step=10,
                                  help="This is the number of data points you want to generate.")

    generate_button = st.button("🚀 Generate Data", type="primary", use_container_width=True)


# --- Main Content Area ---

if generate_button:
    st.header("📊 Generated Data & Visualization")
    
    try:
        # Generate the data
        with st.spinner('Generating your LHS dataset...'):
            lhs_df = generate_lhs_data(num_dimensions, num_samples)

        # Display the data in a table
        st.subheader("Generated Dataset")
        st.dataframe(lhs_df, height=300)

        # Provide download functionality
        csv_data = convert_df_to_csv(lhs_df)
        st.download_button(
            label="📥 Download Data as CSV",
            data=csv_data,
            file_name=f'lhs_data_{num_dimensions}d_{num_samples}s.csv',
            mime='text/csv',
            use_container_width=True
        )

        # Visualize the data
        st.subheader("Data Visualization")
        if num_dimensions == 2:
            st.markdown("A 2D scatter plot of the first two variables.")
            fig = px.scatter(lhs_df, x='Variable 1', y='Variable 2',
                             title='2D Scatter Plot of LHS Samples',
                             labels={'Variable 1': 'Variable 1', 'Variable 2': 'Variable 2'})
            fig.update_layout(
                xaxis_title="Variable 1",
                yaxis_title="Variable 2",
                showlegend=False,
                margin=dict(l=20, r=20, t=40, b=20)
            )
            fig.update_traces(marker=dict(size=8, opacity=0.7))
            st.plotly_chart(fig, use_container_width=True)
            
            # Also show histograms to demonstrate the stratification
            col1, col2 = st.columns(2)
            with col1:
                fig_hist1 = px.histogram(lhs_df, x='Variable 1', nbins=num_samples, title='Histogram of Variable 1')
                st.plotly_chart(fig_hist1, use_container_width=True)
            with col2:
                fig_hist2 = px.histogram(lhs_df, x='Variable 2', nbins=num_samples, title='Histogram of Variable 2')
                st.plotly_chart(fig_hist2, use_container_width=True)

        elif num_dimensions > 2:
            st.markdown(f"A 3D scatter plot of the first three variables (out of {num_dimensions}).")
            fig = px.scatter_3d(lhs_df, x='Variable 1', y='Variable 2', z='Variable 3',
                                title='3D Scatter Plot of LHS Samples',
                                labels={'Variable 1': 'Var 1', 'Variable 2': 'Var 2', 'Variable 3': 'Var 3'})
            fig.update_layout(margin=dict(l=0, r=0, b=0, t=40))
            fig.update_traces(marker=dict(size=5, opacity=0.7))
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Visualization is available for 2 or more dimensions.")

    except Exception as e:
        st.error(f"An error occurred: {e}")

else:
    st.info("Please set your parameters in the sidebar and click 'Generate Data'.")

# --- Footer ---
st.markdown("---")
st.markdown("Created with ❤️ using [Streamlit](https://streamlit.io) and [SciPy](https://scipy.org/).")
