# Internationalization (i18n) in This Application

This application demonstrates the use of internationalization (i18n) with Flask and Flask-Babel. It supports multiple languages and allows for dynamic language selection based on user preferences.

## Setup and Running the Application

1. Ensure you have the required dependencies installed:
   ```bash
   pip install Flask Flask-Babel
   ```

2. Set the environment variables for the host and port (optional):
   ```bash
   export API_HOST=0.0.0.0
   export API_PORT=5000
   ```

3. Run the application:
   ```bash
   python i18n/0-app.py
   ```

## Supported Languages

- English (en)
- French (fr)

To add more languages, update the `LANGUAGES` list in the `Config` class in the application files.

## Using Flask-Babel Features

- Use the `@babel.localeselector` decorator to define a function that determines the best match for the user's language preferences.
- Utilize the `gettext` function to mark strings for translation.

This README provides a basic overview of the i18n functionality in this application. For more detailed usage, refer to the Flask-Babel documentation.
