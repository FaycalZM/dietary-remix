from flask import Flask, request, jsonify, render_template
from data import *
from recipe_transformer import *

app = Flask(__name__)

engine = get_gemini_engine()
model = get_gemini_model(gemini_engine=engine)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/transform_recipe', methods=['POST'])
def transform_recipe():
    recipe_name = request.form.get('recipe_name')
    original_recipe_text = request.form.get('recipe_text')
    diet = request.form.get('diet')

    
    recipe_text = original_recipe_text[:]

    input_recipe = f"recipe name: {recipe_name}, diet: {diet}, " + recipe_text

    prediction = model.predict({
        'original_recipe' : input_recipe
    })
    
    transformed_recipe = prediction.at[0,'transformed_recipe']
    
    return jsonify({
        "recipe_name": recipe_name,
        "original_recipe": original_recipe_text,
        "transformed_recipe": transformed_recipe,
        "diet": diet
    })

@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    recipe_name = request.form.get('recipe_name')
    recipe_text = request.form.get('recipe_text')

    if not recipe_name or not recipe_text:
        return jsonify({"error": "Both recipe name and text are required"}), 400

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO recipes (recipe_name, recipe_text) VALUES (?, ?)", (recipe_name, recipe_text))
    recipe_id = cursor.lastrowid
    conn.commit()
    conn.close()

    return jsonify({"message": "Recipe added successfully", "recipe_id": recipe_id}), 201

@app.route('/get_recipes', methods=['GET'])
def get_recipes():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT recipe_id, recipe_name FROM recipes")
    recipes = cursor.fetchall()
    conn.close()

    return jsonify([{"id": id, "name": name} for id, name in recipes])

if __name__ == '__main__':
    app.run(debug=True)