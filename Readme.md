
# Dietary Remix - Your DIet Buddy 🥑💪

## Overview

Dietary Remix is a web application that leverages AI to transform recipes based on different dietary requirements. It allows users to input recipes and convert them to various diets such as vegan, keto, gluten-free. The application uses MindsDB with Google's Gemini Pro model to perform intelligent recipe transformations while maintaining the essence and flavor profile of the original recipe.

[![Quira Vote](https://img.shields.io/badge/Quira-View%20Repo-blue)](https://quira.sh/repo/FaycalZM-dietary-remix-828689730?utm_source=copy&utm_share_context=rdp)


## Table of Contents 📑

- [Features](#features)
- [Technology Stack](#technology_stack)
- [YouTube Demonstration](#youtube-demonstration)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Support](#support)

## Features 🌟

- Add new recipes to a local database
- Transform recipes to different diets:
  - Vegan
  - Keto
  - Gluten-free
- User-friendly web interface for recipe input and transformation
- Display of both original and transformed recipes
- Real-time recipe transformation using AI


## Technology Stack
- **Backend**: Python with Flask framework
- **Database**: SQLite for local storage
- **AI Integration**: MindsDB with Google Gemini Pro Model
- **Frontend**: HTML, CSS, JavaScript (jQuery)
- **API**: RESTful API endpoints for recipe management and transformation

## YouTube Demonstration

[Watch the video](https://www.youtube.com/watch?v=kuW1enQS0do)


## Requirements
- Python 3.7 or higher
- MindsDB SDK
- SQLite3
  
## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/FaycalZM/dietary-remix
    cd dietary-remix
    ```

2. **Create virtual env & activate it & Install required packages**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. **Set up MindsDB**:
    - Follow the [MindsDB installation guide](https://docs.mindsdb.com/install) to install and run MindsDB locally.
    - Note the server address and port (default is `http://127.0.0.1:47334`).
    - make .env file add your Google Gemini api key 
```bash
    API_KEY='YOUR_KEY'
```
4. **Create and populate the SQLite database**:
    ```bash
    python data.py
    ```

## Usage
1. **Run the Flask server**:
    ```bash
    flask --app main run --debug
    ```

2. **Add a recipe** by providing the recipe name and recipe text in the 'add recipe' form:
    
3. **Transform a recipe** by providing the recipe name, recipe text and selecting the desired diet in the 'transform recipe' form, and visualize the transformed recipe.

4. **Visit http://localhost:5000/get_recipes** to get all the recipes in the local database.

    
## Support 💬

If you like this project, please support it by upvoting on Quira and starring the GitHub repository!

[![Quira Repo](https://img.shields.io/badge/Quira-View%20Repo-blue)](https://quira.sh/repo/FaycalZM-dietary-remix-828689730?utm_source=copy&utm_share_context=rdp)

Thank you for your support!
