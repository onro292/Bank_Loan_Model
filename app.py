import streamlit as st
import pickle
import numpy as np
model = pickle.load(open('model.pkl', 'rb'))


def predict_output(age, income, family, ccavg, education, mortgage, securities, cd, online, credit):
    input = np.array([[age, income, family, ccavg, education,
                       mortgage, securities, cd, online, credit]]).astype(np.float64)
    prediction = model.predict_proba(input)
    # pred ='{0:.{1}f}'.format(prediction[0][0], 2)
    pred = prediction[:, 1]

    return float(pred)

def main():
    html_temp = """
    <div style="background-color:#000000;padding:10px">
    <h2 style="color:white;text-align:center;">Bank Loan Classification </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    age = st.text_input("Age")
    income = st.text_input("Annual Income (E.g) Type 50 for 50,000")
    family = st.text_input("Number of Family Members")
    ccavg = st.text_input("Average credit card spending per month (E.g) Type 1.6 for $1,600")
    education = st.text_input("Education Level 1=Undergrad, 2=Graduate, 3=Advanced")
    mortgage = st.text_input("Value of House Mortgage (E.g) Type 134 for 134,000")
    securities = st.text_input("Securities Account 1=Yes 0=No")
    cd = st.text_input("Certificate of Deposit Account 1=Yes, 0=No")
    online = st.text_input("If they use online banking 1=Yes, 0=No")
    credit = st.text_input("If they have a credit card with the bank 1=Yes, 0=No")

    safe_html = """  
          <div style="background-color:#F4D03F;padding:10px >
           <h2 style="color:white;text-align:center;"> This customer is a good candidate for a loan offer!</h2>
           </div>
        """
    danger_html = """  
          <div style="background-color:#F08080;padding:10px >
           <h2 style="color:black ;text-align:center;"> This customer is not a good candidate!</h2>
           </div>
        """
    if st.button("Predict"):
        output=predict_output(age, income, family, ccavg, education, mortgage, securities, cd, online, credit)
        st.success('The probability this customer is a good candidate{} '.format(output))

        if output > 0.5:
            st.markdown(safe_html,unsafe_allow_html=True)
        else:
            st.markdown(danger_html,unsafe_allow_html=True)

if __name__=='__main__':
    main()