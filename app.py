import streamlit as st

def main():
    st.title("Enhanced Health Test Checker")
    st.header("Your Personal Health Assessment Tool")

    # Sidebar for navigation
    st.sidebar.title("Select a Test")
    test_type = st.sidebar.selectbox(
        "Choose the type of health test you want:",
        [
            "Blood Sugar Level",
            "Blood Platelets Check",
            "Blood Pressure",
            "Body Mass Index (BMI)",
            "Cholesterol Level",
            "Hemoglobin Level",
            "White Blood Cell Count",
            "Iron Level",
            "Vitamin D Level",
            "C-Reactive Protein Check"
        ]
    )

    if test_type == "Blood Sugar Level":
        blood_sugar = st.number_input("Enter your blood sugar level (mg/dL):", min_value=0)
        check_blood_sugar(blood_sugar)

    elif test_type == "Blood Platelets Check":
        blood_platelets = st.number_input("Enter your blood platelets count (cells/mcL):", min_value=0)
        check_blood_platelets(blood_platelets)

    elif test_type == "Blood Pressure":
        systolic = st.number_input("Enter your systolic blood pressure (mmHg):", min_value=0)
        diastolic = st.number_input("Enter your diastolic blood pressure (mmHg):", min_value=0)
        check_blood_pressure(systolic, diastolic)

    elif test_type == "Body Mass Index (BMI)":
        weight = st.number_input("Enter your weight (kg):", min_value=0)
        height = st.number_input("Enter your height (m):", min_value=0)
        check_bmi(weight, height)

    elif test_type == "Cholesterol Level":
        total_cholesterol = st.number_input("Enter your total cholesterol level (mg/dL):", min_value=0)
        hdl_cholesterol = st.number_input("Enter your HDL cholesterol level (mg/dL):", min_value=0)
        ldl_cholesterol = st.number_input("Enter your LDL cholesterol level (mg/dL):", min_value=0)
        triglycerides = st.number_input("Enter your triglycerides level (mg/dL):", min_value=0)
        check_cholesterol(total_cholesterol, hdl_cholesterol, ldl_cholesterol, triglycerides)

    elif test_type == "Hemoglobin Level":
        hemoglobin = st.number_input("Enter your hemoglobin level (g/dL):", min_value=0.0)
        check_hemoglobin(hemoglobin)

    elif test_type == "White Blood Cell Count":
        wbc_count = st.number_input("Enter your WBC count (cells/mcL):", min_value=0)
        check_wbc(wbc_count)

    elif test_type == "Iron Level":
        iron_level = st.number_input("Enter your iron level (mcg/dL):", min_value=0)
        check_iron(iron_level)

    elif test_type == "Vitamin D Level":
        vitamin_d = st.number_input("Enter your Vitamin D level (ng/mL):", min_value=0)
        check_vitamin_d(vitamin_d)

    elif test_type == "C-Reactive Protein Check":
        crp_level = st.number_input("Enter your CRP level (mg/L):", min_value=0)
        check_crp(crp_level)

    # Signature
    st.markdown("\nMade by Muhammad Zeeshan Burki")


def check_blood_sugar(level):
    st.subheader("Blood Sugar Level Check:")
    if level < 70:
        st.write("Your blood sugar level is low (Hypoglycemia).")
        st.write("### Potential Issues:")
        st.write("Fatigue, dizziness, irritability, and fainting.")
        st.write("### Suggestions:")
        st.write("Consume fast-acting carbohydrates such as glucose tablets, fruit juice, or candy. If symptoms persist, seek medical attention.")
    elif 70 <= level <= 130:
        st.write("Your blood sugar level is normal.")
        st.write("### Maintenance Tips:")
        st.write("Maintain a balanced diet and regular exercise to keep it stable.")
    elif 130 < level <= 199:
        st.write("Your blood sugar level is high (Prediabetes).")
        st.write("### Potential Issues:")
        st.write("Increased risk of type 2 diabetes, cardiovascular diseases.")
        st.write("### Suggestions:")
        st.write("Consult a healthcare provider for further evaluation and consider lifestyle changes.")
    else:
        st.write("Your blood sugar level is very high (Diabetes).")
        st.write("### Potential Issues:")
        st.write("Nerve damage, kidney damage, cardiovascular diseases, and other serious health conditions.")
        st.write("### Suggestions:")
        st.write("Immediate medical consultation is recommended.")

def check_blood_platelets(count):
    st.subheader("Blood Platelets Check:")
    if count < 150000:
        st.write("Your platelet count is low (Thrombocytopenia).")
        st.write("### Potential Issues:")
        st.write("Excessive bleeding, easy bruising, prolonged bleeding from cuts.")
        st.write("### Suggestions:")
        st.write("Consult a healthcare provider for tests to determine the cause and possible treatments.")
    elif 150000 <= count <= 450000:
        st.write("Your platelet count is normal.")
        st.write("### Maintenance Tips:")
        st.write("Regular health check-ups are recommended to maintain overall health.")
    else:
        st.write("Your platelet count is high (Thrombocytosis).")
        st.write("### Potential Issues:")
        st.write("Risk of blood clots, strokes, and heart attacks.")
        st.write("### Suggestions:")
        st.write("Seek medical evaluation to assess underlying causes and consider lifestyle modifications.")

def check_blood_pressure(systolic, diastolic):
    st.subheader("Blood Pressure Check:")
    if systolic < 90 or diastolic < 60:
        st.write("Your blood pressure is low (Hypotension).")
        st.write("### Potential Issues:")
        st.write("Dizziness, fainting, fatigue, and shock in severe cases.")
        st.write("### Suggestions:")
        st.write("Stay hydrated, consider increasing salt intake, and consult a healthcare provider.")
    elif 90 <= systolic <= 120 and 60 <= diastolic <= 80:
        st.write("Your blood pressure is normal.")
        st.write("### Maintenance Tips:")
        st.write("Maintain a healthy lifestyle with regular exercise and a balanced diet.")
    elif (120 < systolic <= 129) and diastolic < 80:
        st.write("Your blood pressure is elevated.")
        st.write("### Potential Issues:")
        st.write("Increased risk of hypertension.")
        st.write("### Suggestions:")
        st.write("Monitor your blood pressure regularly and consider lifestyle changes.")
    elif systolic >= 130 or diastolic >= 80:
        st.write("Your blood pressure is high (Hypertension).")
        st.write("### Potential Issues:")
        st.write("Increased risk of heart disease, stroke, and kidney problems.")
        st.write("### Suggestions:")
        st.write("Consult a healthcare provider for evaluation and management strategies.")

def check_bmi(weight, height):
    st.subheader("BMI Check:")
    bmi = weight / (height ** 2)
    st.write(f"Your BMI is: {bmi:.2f}")
    if bmi < 18.5:
        st.write("You are underweight.")
        st.write("### Potential Issues:")
        st.write("Nutritional deficiency, weakened immune system.")
        st.write("### Suggestions:")
        st.write("Consult a healthcare provider for dietary advice and consider increasing caloric intake.")
    elif 18.5 <= bmi < 24.9:
        st.write("You have a normal weight.")
        st.write("### Maintenance Tips:")
        st.write("Maintain a healthy lifestyle to keep your BMI in this range.")
    elif 25 <= bmi < 29.9:
        st.write("You are overweight.")
        st.write("### Potential Issues:")
        st.write("Increased risk of heart disease, diabetes, and certain cancers.")
        st.write("### Suggestions:")
        st.write("Engage in regular physical activity and follow a balanced diet.")
    else:
        st.write("You are obese.")
        st.write("### Potential Issues:")
        st.write("High risk of diabetes, heart disease, and joint problems.")
        st.write("### Suggestions:")
        st.write("Seek professional advice for a weight management program.")

def check_cholesterol(total, hdl, ldl, triglycerides):
    st.subheader("Cholesterol Level Check:")
    st.write(f"Total Cholesterol: {total} mg/dL")
    st.write(f"HDL Cholesterol (Good): {hdl} mg/dL")
    st.write(f"LDL Cholesterol (Bad): {ldl} mg/dL")
    st.write(f"Triglycerides: {triglycerides} mg/dL")
    
    if total < 200:
        st.write("Your total cholesterol level is ideal.")
        st.write("### Maintenance Tips:")
        st.write("Continue to maintain a heart-healthy lifestyle.")
    elif 200 <= total <= 239:
        st.write("Your total cholesterol level is borderline high.")
        st.write("### Potential Issues:")
        st.write("Increased risk of heart disease.")
        st.write("### Suggestions:")
        st.write("Adopt a healthier diet and exercise regularly.")
    else:
        st.write("Your total cholesterol level is high.")
        st.write("### Potential Issues:")
        st.write("High risk of heart disease and stroke.")
        st.write("### Suggestions:")
        st.write("Consult a healthcare provider for a management plan.")

    if hdl < 40:
        st.write("Your HDL (Good) cholesterol level is low.")
        st.write("### Suggestions:")
        st.write("Incorporate healthy fats in your diet, such as olive oil and avocados.")
    elif hdl >= 60:
        st.write("Your HDL (Good) cholesterol level is optimal.")
    if ldl >= 160:
        st.write("Your LDL (Bad) cholesterol level is high.")
        st.write("### Suggestions:")
        st.write("Limit saturated fats and trans fats in your diet.")
    
    if triglycerides >= 150:
        st.write("Your triglycerides level is high.")
        st.write("### Suggestions:")
        st.write("Reduce sugar and refined carbohydrates in your diet.")

def check_hemoglobin(level):
    st.subheader("Hemoglobin Level Check:")
    if level < 13.5:
        st.write("Your hemoglobin level is low (Anemia).")
        st.write("### Potential Issues:")
        st.write("Fatigue, weakness, and shortness of breath.")
        st.write("### Suggestions:")
        st.write("Consult a healthcare provider for dietary changes and possible supplementation.")
    elif 13.5 <= level <= 17.5:
        st.write("Your hemoglobin level is normal.")
        st.write("### Maintenance Tips:")
        st.write("Maintain a balanced diet rich in iron.")
    else:
        st.write("Your hemoglobin level is high.")
        st.write("### Potential Issues:")
        st.write("Risk of blood clots and other complications.")
        st.write("### Suggestions:")
        st.write("Consult a healthcare provider for further evaluation.")

def check_wbc(count):
    st.subheader("White Blood Cell Count Check:")
    if count < 4000:
        st.write("Your WBC count is low (Leukopenia).")
        st.write("### Potential Issues:")
        st.write("Increased risk of infections.")
        st.write("### Suggestions:")
        st.write("Consult a healthcare provider for further evaluation.")
    elif 4000 <= count <= 10000:
        st.write("Your WBC count is normal.")
        st.write("### Maintenance Tips:")
        st.write("Stay healthy and monitor for any symptoms.")
    else:
        st.write("Your WBC count is high (Leukocytosis).")
        st.write("### Potential Issues:")
        st.write("May indicate infection, inflammation, or other medical conditions.")
        st.write("### Suggestions:")
        st.write("Seek medical advice for appropriate testing.")

def check_iron(level):
    st.subheader("Iron Level Check:")
    if level < 60:
        st.write("Your iron level is low (Iron Deficiency).")
        st.write("### Potential Issues:")
        st.write("Fatigue, weakness, and anemia.")
        st.write("### Suggestions:")
        st.write("Increase iron-rich foods like red meat, beans, and leafy greens. Consider supplementation.")
    elif 60 <= level <= 170:
        st.write("Your iron level is normal.")
        st.write("### Maintenance Tips:")
        st.write("Maintain a balanced diet with adequate iron intake.")
    else:
        st.write("Your iron level is high.")
        st.write("### Potential Issues:")
        st.write("Risk of organ damage and iron overload.")
        st.write("### Suggestions:")
        st.write("Consult a healthcare provider for further evaluation.")

def check_vitamin_d(level):
    st.subheader("Vitamin D Level Check:")
    if level < 20:
        st.write("Your Vitamin D level is low.")
        st.write("### Potential Issues:")
        st.write("Fatigue, bone pain, and increased risk of chronic diseases.")
        st.write("### Suggestions:")
        st.write("Consider vitamin D supplements and get more sunlight exposure.")
    elif 20 <= level <= 50:
        st.write("Your Vitamin D level is normal.")
        st.write("### Maintenance Tips:")
        st.write("Maintain a balanced diet and safe sun exposure.")
    else:
        st.write("Your Vitamin D level is high.")
        st.write("### Potential Issues:")
        st.write("Nausea, vomiting, weakness, and serious health issues.")
        st.write("### Suggestions:")
        st.write("Consult a healthcare provider for further evaluation.")

def check_crp(level):
    st.subheader("C-Reactive Protein Check:")
    if level < 1:
        st.write("Your CRP level is low.")
        st.write("### Maintenance Tips:")
        st.write("Continue to lead a healthy lifestyle.")
    elif 1 <= level <= 3:
        st.write("Your CRP level is normal.")
        st.write("### Maintenance Tips:")
        st.write("Regular health check-ups are recommended.")
    else:
        st.write("Your CRP level is high.")
        st.write("### Potential Issues:")
        st.write("May indicate inflammation or infection in the body.")
        st.write("### Suggestions:")
        st.write("Consult a healthcare provider for further investigation.")

if __name__ == "__main__":
    main()
