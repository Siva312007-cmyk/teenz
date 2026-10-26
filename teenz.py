
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Financial Identity Oracle",
    page_icon="💳",
    layout="centered"
)

st.title("💳 Financial Identity Oracle")
st.subheader("Team Teenz")
st.write("By Sivasruthi SR and Haniska A")

st.info(
    "This prototype helps informal workers build an "
    "alternative financial profile using everyday financial signals."
)

st.header("1. User Consent")

consent = st.checkbox(
    "I consent to using my entered information for this demo."
)

st.header("2. Enter Financial Information")

work_type = st.selectbox(
    "Occupation",
    [
        "Street Vendor",
        "Small Shop Owner",
        "Farmer",
        "Tea-Shop Owner",
        "Other Informal Worker"
    ]
)

months = st.number_input(
    "Months working in this occupation",
    min_value=0,
    max_value=600,
    value=12
)

bill_payments = st.slider(
    "Bills paid on time (%)",
    min_value=0,
    max_value=100,
    value=75
)

recharge = st.selectbox(
    "Mobile recharge pattern",
    ["Regular", "Sometimes irregular", "Often irregular"]
)

income = st.selectbox(
    "Income pattern",
    ["Mostly consistent", "Seasonal or variable", "Highly unpredictable"]
)

savings = st.selectbox(
    "Savings behaviour",
    ["Regular savings", "Occasional savings", "No savings recorded"]
)

verified = st.selectbox(
    "Financial evidence verification",
    ["Not verified", "Partially verified", "Fully verified"]
)

if st.button("Calculate Trust Score", type="primary"):

    if not consent:
        st.error("Please provide consent before calculating the score.")

    else:
        # Illustrative demo weights only
        work_score = min(months / 24, 1) * 20
        bill_score = bill_payments * 0.25

        recharge_score = {
            "Regular": 15,
            "Sometimes irregular": 8,
            "Often irregular": 2
        }[recharge]

        income_score = {
            "Mostly consistent": 15,
            "Seasonal or variable": 10,
            "Highly unpredictable": 5
        }[income]

        savings_score = {
            "Regular savings": 15,
            "Occasional savings": 9,
            "No savings recorded": 4
        }[savings]

        verification_score = {
            "Not verified": 0,
            "Partially verified": 5,
            "Fully verified": 10
        }[verified]

        score = round(
            work_score
            + bill_score
            + recharge_score
            + income_score
            + savings_score
            + verification_score
        )

        score = min(score, 100)

        st.header("3. Financial Profile Result")

        st.metric("Illustrative Trust Score", f"{score}/100")

        st.write("Occupation:", work_type)

        st.progress(score / 100)

        breakdown = pd.DataFrame({
            "Financial Factor": [
                "Work continuity",
                "On-time bill payments",
                "Mobile recharge pattern",
                "Income pattern",
                "Savings behaviour",
                "Evidence verification"
            ],
            "Points": [
                round(work_score, 1),
                round(bill_score, 1),
                recharge_score,
                income_score,
                savings_score,
                verification_score
            ]
        })

        st.subheader("Score Breakdown")
        st.dataframe(breakdown, use_container_width=True)

        st.subheader("4. Next Steps")
        st.write("• Verify financial records with user permission.")
        st.write("• Allow users to correct inaccurate information.")
        st.write("• Explain the score factors transparently.")
        st.write("• Obtain human review before any real-world assessment.")

        st.warning(
            "This is an educational prototype with illustrative scoring "
            "weights. It is not a validated credit score and does not "
            "guarantee loan approval. Do not use it for real lending decisions."
        )
