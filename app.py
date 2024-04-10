from flask import Flask, render_template, request

app = Flask(__name__)

def convert_units(weight, weight_unit, height, height_unit):
    # Convert to kilograms if weight is in pounds
    if weight_unit == 'lbs':
        weight = weight * 0.453592
    # Convert to meters if height is in inches
    if height_unit == 'in':
        height = height * 0.0254
    return weight, height

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def recommend_yoga_and_nutrition(bmi):
    if bmi < 18.5:
        return "Surya Namaskar, Vrikshasana", "Increase intake of proteins and healthy fats, and consume more calories."
    elif bmi < 25:
        return "Tadasana, Trikonasana", "Maintain a balanced diet with a good mix of fruits, vegetables, whole grains, and lean proteins."
    elif bmi < 30:
        return "Bhujangasana, Dhanurasana", "Focus on a diet rich in fiber, reduce sugar intake, and increase physical activity."
    else:
        return "Balasana, Savasana", "Adopt a low-calorie diet, increase water intake, and consult a nutritionist for a personalized plan."

# Route for handling the index and results
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Collect data from form
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        weight_unit = request.form.get('weight_unit')
        height_unit = request.form.get('height_unit')

        # Convert units and calculate BMI
        weight, height = convert_units(weight, weight_unit, height, height_unit)
        bmi = calculate_bmi(weight, height)

        # Get recommendations
        yoga, nutrition = recommend_yoga_and_nutrition(bmi)

        # Render the results template with the BMI value and recommendations
        return render_template('results.html', bmi=round(bmi, 2), yoga=yoga, nutrition=nutrition)

    # Render the index page if method is GET
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

