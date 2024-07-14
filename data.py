import sqlite3

# Database connection
SQLITE_DB_PATH = 'recipes.db'

# Sample recipes
recipes = [
    {
        "name": "Classic Spaghetti Bolognese",
        "text": "Ingredients: 500g ground beef, 1 onion (diced), 2 garlic cloves (minced), 2 carrots (diced), 2 celery stalks (diced), 400g canned tomatoes, 2 tbsp tomato paste, 1 tsp dried oregano, 1 tsp dried basil, Salt and pepper to taste, 400g spaghetti. Instructions: 1. Brown beef in a large pan. 2. Add onion, garlic, carrots, and celery; cook until softened. 3. Add tomatoes, paste, and herbs. Simmer for 30 minutes. 4. Cook spaghetti according to package instructions. 5. Serve sauce over spaghetti."
    },
    {
        "name": "Chicken Stir-Fry",
        "text": "Ingredients: 2 chicken breasts (sliced), 1 bell pepper (sliced), 1 carrot (julienned), 1 cup broccoli florets, 2 tbsp soy sauce, 1 tbsp oyster sauce, 1 tsp sesame oil, 2 cloves garlic (minced), 1 tbsp ginger (grated), 2 tbsp vegetable oil. Instructions: 1. Heat oil in a wok. 2. Stir-fry chicken until cooked. Remove from wok. 3. Stir-fry vegetables for 2-3 minutes. 4. Add garlic and ginger, cook for 30 seconds. 5. Return chicken to wok. Add sauces and sesame oil. 6. Stir-fry for another minute. Serve hot with rice."
    },
    {
        "name": "Vegetarian Lentil Soup",
        "text": "Ingredients: 1 cup red lentils, 1 onion (chopped), 2 carrots (diced), 2 celery stalks (diced), 2 cloves garlic (minced), 1 can diced tomatoes, 6 cups vegetable broth, 1 tsp cumin, 1 tsp paprika, Salt and pepper to taste, 2 tbsp olive oil, Juice of 1 lemon. Instructions: 1. Heat oil in a large pot. Sauté onion, carrots, celery, and garlic until softened. 2. Add lentils, tomatoes, broth, and spices. Bring to a boil. 3. Reduce heat and simmer for 25-30 minutes until lentils are tender. 4. Stir in lemon juice before serving."
    },
    {
        "name": "Chocolate Chip Cookies",
        "text": "Ingredients: 2 1/4 cups all-purpose flour, 1 tsp baking soda, 1 tsp salt, 1 cup unsalted butter (softened), 3/4 cup granulated sugar, 3/4 cup brown sugar, 2 large eggs, 2 tsp vanilla extract, 2 cups chocolate chips. Instructions: 1. Preheat oven to 375°F (190°C). 2. Mix flour, baking soda, and salt in a bowl. 3. In another bowl, cream butter and sugars. Beat in eggs and vanilla. 4. Gradually stir in flour mixture. Fold in chocolate chips. 5. Drop spoonfuls onto baking sheets. 6. Bake for 9-11 minutes until golden brown. Cool on wire racks."
    },
    {
        "name": "Grilled Salmon with Lemon-Dill Sauce",
        "text": "Ingredients: 4 salmon fillets, 2 tbsp olive oil, Salt and pepper to taste, 1/4 cup plain Greek yogurt, 2 tbsp fresh dill (chopped), 1 tbsp lemon juice, 1 tsp lemon zest. Instructions: 1. Brush salmon with olive oil, season with salt and pepper. 2. Grill salmon for 4-5 minutes per side until cooked through. 3. For the sauce, mix yogurt, dill, lemon juice, and zest in a bowl. 4. Serve grilled salmon with a dollop of lemon-dill sauce on top."
    }
]


def connect_db():
    try:
        conn = sqlite3.connect(SQLITE_DB_PATH)
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")


def init_db():
    conn = sqlite3.connect(SQLITE_DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recipes (
            recipe_id INTEGER PRIMARY KEY AUTOINCREMENT,
            recipe_name TEXT NOT NULL,
            recipe_text TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_recipes():
    conn = sqlite3.connect(SQLITE_DB_PATH)
    cursor = conn.cursor()
    for recipe in recipes:
        cursor.execute("INSERT INTO recipes (recipe_name, recipe_text) VALUES (?, ?)",
                       (recipe['name'], recipe['text']))
    conn.commit()
    conn.close()

def main():
    print("Initializing database...")
    init_db()
    print("Inserting recipes...")
    insert_recipes()
    print("Database populated successfully!")

if __name__ == "__main__":
    main()