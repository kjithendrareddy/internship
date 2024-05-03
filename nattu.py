import streamlit as st

class SportsNutritionGuide:
    def __init__(self, weight, height, age, gender, activity_level, sport):
        self.weight = weight  # in kg
        self.height = height  # in cm
        self.age = age  # in years
        self.gender = gender  # 'male' or 'female'
        self.activity_level = activity_level  # 'sedentary', 'lightly active', 'moderately active', 'very active', 'extremely active'
        self.sport = sport

    def calculate_bmi(self):
        # Calculate Body Mass Index (BMI)
        height_meters = self.height / 100
        bmi = self.weight / (height_meters ** 2)
        return bmi

    def calculate_bmr(self):
        # Calculate Basal Metabolic Rate (BMR) using Harris-Benedict equation
        if self.gender == 'male':
            bmr = 88.362 + (13.397 * self.weight) + (4.799 * self.height) - (5.677 * self.age)
        elif self.gender == 'female':
            bmr = 447.593 + (9.247 * self.weight) + (3.098 * self.height) - (4.330 * self.age)
        else:
            raise ValueError("Invalid gender. Please specify 'male' or 'female'.")
        
        if self.activity_level == 'sedentary':
            activity_multiplier = 1.2
        elif self.activity_level == 'lightly active':
            activity_multiplier = 1.375
        elif self.activity_level == 'moderately active':
            activity_multiplier = 1.55
        elif self.activity_level == 'very active':
            activity_multiplier = 1.725
        elif self.activity_level == 'extremely active':
            activity_multiplier = 1.9
        else:
            raise ValueError("Invalid activity level.")
        
        bmr *= activity_multiplier
        return bmr

    def suggest_caloric_intake(self):
        # Suggest daily caloric intake based on activity level and BMR
        bmr = self.calculate_bmr()
        return bmr

    def suggest_nutrition_plan(self):
        # Suggest a basic nutrition plan for a sportsman
        caloric_intake = self.suggest_caloric_intake()
        protein_intake = 2.2 * self.weight  # grams of protein per kg of body weight
        fat_intake = 0.25 * caloric_intake / 9  # 25% of total calories from fat (9 calories per gram of fat)
        carbs_intake = (caloric_intake - (protein_intake * 4) - (fat_intake * 9)) / 4  # remaining calories from carbs (4 calories per gram of carb)
        
        nutrition_plan = {
            'Calories (kcal)': caloric_intake,
            'Protein (g)': protein_intake,
            'Fat (g)': fat_intake,
            'Carbohydrates (g)': carbs_intake
        }
        return nutrition_plan

def main():
    st.title("Sports Nutrition Guide")
    st.markdown('<style>body {background-color: transparent;}</style>', unsafe_allow_html=True)

    weight = st.number_input("Weight (kg)")
    height = st.number_input("Height (cm)")
    age = st.number_input("Age")
    gender = st.radio("Gender", ('Male', 'Female'))
    activity_level = st.selectbox("Activity Level", ('Sedentary', 'Lightly active', 'Moderately active', 'Very active', 'Extremely active'))
    sport = st.selectbox("Select Sport", ('Cricket', 'Kabaddi', 'Badminton', 'Football'))

    if st.button("Calculate"):
        nutrition_guide = SportsNutritionGuide(weight, height, age, gender.lower(), activity_level.lower(), sport)
        bmi = nutrition_guide.calculate_bmi()
        bmr = nutrition_guide.calculate_bmr()
        caloric_intake = nutrition_guide.suggest_caloric_intake()
        nutrition_plan = nutrition_guide.suggest_nutrition_plan()

        st.write(f"BMI: {bmi}")
        st.write(f"BMR: {bmr}")
        st.write("\nSuggested daily caloric intake:", caloric_intake, "kcal")
        st.write("\nSuggested nutrition plan:")
        for nutrient, amount in nutrition_plan.items():
            st.write(f"{nutrient}: {amount}")

page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)
if __name__ == "__main__":
    main()
