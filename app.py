import pickle
import streamlit as st
# new changes
# loading in the model to predict on the data
pickle_in = open('Model_best.pkl', 'rb')
classifier = pickle.load(pickle_in)


def welcome():
    return 'welcome all'


# defining the function which will make the prediction using
# the data which the user inputs
def prediction(A1_Score,A2_Score,A3_Score,A4_Score,A5_Score,A6_Score,A7_Score,A8_Score,A9_Score,A10_Score,age,gender,jaundice,familyPDD, used_app_before,ME,SA,A,B,H,O,P,T,WE,NewZ,SL,UAE,UK,USA,AFG,AUS,CANADA,FRA,INDIA,JOR,NET,OTH,HealthCarePro,caregiver,others,parent,relative,self):
    prediction = classifier.predict(
        [[A1_Score,A2_Score,A3_Score,A4_Score,A5_Score,A6_Score,A7_Score,A8_Score,A9_Score,A10_Score,age,gender,jaundice,familyPDD, used_app_before,ME,SA,A,B,H,O,P,T,WE,NewZ,SL,UAE,UK,USA,AFG,AUS,CANADA,FRA,INDIA,JOR,NET,OTH,HealthCarePro,caregiver,others,parent,relative,self]])
    print(prediction)
    return prediction


# this is the main function in which we define our webpage
def main():
    # giving the webpage a title
    st.title("Detection of Autism Spectrum Disorder using ML")
    # the following lines create text boxes in which the user can enter
    # the data required to make the prediction
    html_temp = """
        <div style ="background-color:white;padding:8px">
        <h1 style ="color:black;text-align:center;">Screening Scores </h1>
        </div>
        """
    st.markdown(html_temp, unsafe_allow_html=True)
    A1_Score = st.text_input("Inappropriate laughing and giggling",0)
    A2_Score = st.text_input("No sensitivity of pain",0)
    A3_Score = st.text_input("Not able to make eye contact properly",0)
    A4_Score = st.text_input("No proper response to sound ",0)
    A5_Score = st.text_input("May not have a wish for cuddling",0)
    A6_Score = st.text_input("Not able to express their gestures",0)
    A7_Score = st.text_input("No interaction with others",0)
    A8_Score = st.text_input("Inappropriate objects attachment",0)
    A9_Score = st.text_input("Want to live alone",0)
    A10_Score = st.text_input("Using echo words",0)

    html_temp = """
                <div style ="background-color:white;padding:8px">
                <h1 style ="color:black;text-align:center;">General Info. </h1>
                </div>
                """
    st.markdown(html_temp, unsafe_allow_html=True)
    age = st.text_input("age", "Type Here")
    gender = st.text_input("gender","Type 1-Male & 0-Female")
    jaundice = st.text_input("Are u born with Jaundice",0)
    familyPDD = st.text_input("Family member is suffering from PDD",0)
    used_app_before = st.text_input("Used_app_before",0)
    html_temp = """
            <div style ="background-color:white;padding:8px">
            <h1 style ="color:black;text-align:center;">Ethnicity </h1>
            </div>
            """
    st.markdown(html_temp, unsafe_allow_html=True)
    ME = st.text_input("Middle Eastern",0)
    SA = st.text_input("South Asian",0)
    A = st.text_input("Asian",0)
    B = st.text_input("Black",0)
    H = st.text_input("Hispanic",0)
    O = st.text_input("Others",0)
    P = st.text_input("Pasifika",0)
    T = st.text_input("Turkish",0)
    WE = st.text_input("White European",0)
    html_temp = """
            <div style ="background-color:white;padding:8px">
            <h1 style ="color:black;text-align:center;">Country </h1>
            </div>
            """
    st.markdown(html_temp, unsafe_allow_html=True)

    NewZ = st.text_input("New Zealand",0)
    SL = st.text_input("Sri Lanka",0)
    UAE = st.text_input("United Arab Emirates",0)
    UK = st.text_input("United Knigdom",0)
    USA = st.text_input("United States Of America",0)
    AFG = st.text_input("Afghanistan",0)
    AUS = st.text_input("Australia",0)
    CANADA = st.text_input("Canada",0)
    FRA = st.text_input("France",0)
    INDIA = st.text_input("India",0)
    JOR = st.text_input("Jordan",0)
    NET = st.text_input("Netherlands",0)
    OTH = st.text_input("Other",0)

    html_temp = """
                <div style ="background-color:white;padding:8px">
                <h1 style ="color:black;text-align:center;">Supervised By </h1>
                </div>
                """
    st.markdown(html_temp, unsafe_allow_html=True)

    HealthCarePro = st.text_input("Health Care Professional",0)
    caregiver = st.text_input("Caregiver",0)
    others = st.text_input("Other Person",0)
    parent = st.text_input("Parent",0)
    relative = st.text_input("Relative",0)
    self = st.text_input("Self",0)

    result = ""

    # the below line ensures that when the button called 'Predict' is clicked,
    # the prediction function defined above is called to make the prediction
    # and store it in the variable result
    if st.button("Predict"):
        result = prediction(A1_Score,A2_Score,A3_Score,A4_Score,A5_Score,A6_Score,A7_Score,A8_Score,A9_Score,A10_Score,age,gender,jaundice,familyPDD, used_app_before,ME,SA,A,B,H,O,P,T,WE,NewZ,SL,UAE,UK,USA,AFG,AUS,CANADA,FRA,INDIA,JOR,NET,OTH,HealthCarePro,caregiver,others,parent,relative,self)
    st.success('The output is {}'.format(result))


if __name__ == '__main__':
    main()