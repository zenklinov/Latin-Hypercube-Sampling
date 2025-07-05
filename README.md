# Latin-Hypercube-Sampling

This project is a simple implementation of the **Latin Hypercube Sampling (LHS)** method using Python. Its primary purpose is to demonstrate how LHS can be used to efficiently estimate expected values from random distributions or stochastic processes by ensuring better coverage of the input space compared to traditional random sampling.

Use Cases: Engineering design simulations, uncertainty quantification.

## 🚀 Live Web App (Streamlit)

A live version of this project is available as a web app powered by **Streamlit**. Try it out here:

🔗 [Try the App on Streamlit](https://latin-hypercube-sampling-ssraf3txq8zvpwyskjbzub.streamlit.app/)

---

## 🧾 Repository Contents

- `lhs.py`: Main Python script containing the LHS sampling logic.
- `requirements.txt`: Lists the dependencies required to run the application.
- `README.md`: This documentation file.

---

## ▶️ How to Run Locally

1. Clone this repository:

```bash
git clone https://github.com/zenklinov/Latin-Hypercube-Sampling.git
cd Latin-Hypercube-Sampling
```

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv env
source env/bin/activate        # On Linux/macOS
env\Scripts\activate.bat       # On Windows
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:
```bash
streamlit run lhs.py
```
