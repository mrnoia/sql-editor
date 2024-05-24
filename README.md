# SQL Editor

A simple SQL editor built using Flask and Tabulator.

## Installation

### Prerequisites

- Python 3.11+
- `pip` (Python package installer)

### Steps

1. **Clone the repository**:

    ```sh
    git clone https://github.com/your-username/sql-editor.git
    cd sql-editor
    ```

2. **Create and activate a virtual environment**:

    ```sh
    python3 -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Initialize the database**:

    ```sh
    python init_db.py
    ```

5. **Run the Flask application**:

    ```sh
    flask run
    ```

6. **Open your web browser** and go to `http://127.0.0.1:5000`.

## Usage

- Enter your SQL query in the text area and click "Execute" or press "Enter" to run the query.
- The results will be displayed in a table below the query input area.

## Files

- `app.py`: The main Flask application file.
- `init_db.py`: Script to initialize the SQLite database with sample data.
- `templates/index.html`: The HTML template for the SQL editor.
- `requirements.txt`: List of Python dependencies.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Project Setup

### 1. Create a GitHub Repository

- Go to [GitHub](https://github.com) and log in to your account.
- Click the `+` icon in the top right corner and select "New repository".
- Name your repository (e.g., `sql-editor`).
- Optionally, add a description.
- Choose the repository visibility (public or private).
- Click "Create repository".

### 2. Initialize Git in Your Project Directory

Open your terminal and navigate to your project directory. Then run the following commands to initialize Git, add your files, and commit them:

```sh
git init
git add .
git commit -m "Initial commit"
