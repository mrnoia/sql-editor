<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SQL Editor Project Documentation</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <h1>SQL Editor</h1>
        <p>A simple SQL editor built using Flask and Tabulator.</p>

        <h2>Installation</h2>
        
        <h3>Prerequisites</h3>
        <ul>
            <li>Python 3.11+</li>
            <li><code>pip</code> (Python package installer)</li>
        </ul>
        
        <h3>Steps</h3>
        <ol>
            <li>
                <strong>Clone the repository:</strong>
                <pre><code>git clone https://github.com/your-username/sql-editor.git
cd sql-editor</code></pre>
            </li>
            <li>
                <strong>Create and activate a virtual environment:</strong>
                <pre><code>python3 -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`</code></pre>
            </li>
            <li>
                <strong>Install the dependencies:</strong>
                <pre><code>pip install -r requirements.txt</code></pre>
            </li>
            <li>
                <strong>Initialize the database:</strong>
                <pre><code>python init_db.py</code></pre>
            </li>
            <li>
                <strong>Run the Flask application:</strong>
                <pre><code>flask run</code></pre>
            </li>
            <li>
                <strong>Open your web browser</strong> and go to <a href="http://127.0.0.1:5000">http://127.0.0.1:5000</a>.
            </li>
        </ol>

        <h2>Usage</h2>
        <ul>
            <li>Enter your SQL query in the text area and click "Execute" or press "Enter" to run the query.</li>
            <li>The results will be displayed in a table below the query input area.</li>
        </ul>

        <h2>Files</h2>
        <ul>
            <li><code>app.py</code>: The main Flask application file.</li>
            <li><code>init_db.py</code>: Script to initialize the SQLite database with sample data.</li>
            <li><code>templates/index.html</code>: The HTML template for the SQL editor.</li>
            <li><code>requirements.txt</code>: List of Python dependencies.</li>
        </ul>

        <h2>License</h2>
        <p>This project is licensed under the MIT License - see the <code>LICENSE</code> file for details.</p>

        <h2>Project Setup</h2>

        <h3>1. Create a GitHub Repository</h3>
        <ul>
            <li>Go to <a href="https://github.com">GitHub</a> and log in to your account.</li>
            <li>Click the <code>+</code> icon in the top right corner and select "New repository".</li>
            <li>Name your repository (e.g., <code>sql-editor</code>).</li>
            <li>Optionally, add a description.</li>
            <li>Choose the repository visibility (public or private).</li>
            <li>Click "Create repository".</li>
        </ul>

        <h3>2. Initialize Git in Your Project Directory</h3>
        <p>Open your terminal and navigate to your project directory. Then run the following commands to initialize Git, add your files, and commit them:</p>
        <pre><code>git init
git add .
git commit -m "Initial commit"</code></pre>

        <h3>3. Add Remote Repository and Push</h3>
        <p>Run the following commands to add your GitHub repository as a remote and push your files:</p>
        <pre><code>git remote add origin https://github.com/your-username/sql-editor.git
git branch -M main
git push -u origin main</code></pre>
        <p>Replace <code>your-username</code> with your GitHub username and <code>sql-editor</code> with your repository name.</p>

        <h3>4. Add the README File and Push Changes</h3>
        <p>Run the following commands to add the README file to your repository and push the changes:</p>
        <pre><code>git add README.md
git commit -m "Add README file"
git push</code></pre>

        <p>Now your project is saved on GitHub with a README file that explains how to install and run the SQL editor on another machine.</p>

        <h2>Final Project Structure</h2>
        <p>Your project directory should look like this:</p>
        <pre><code>sql-editor/
├── venv/
├── app.py
├── init_db.py
├── templates/
│   └── index.html
├── requirements.txt
└── README.md</code></pre>

        <h3>Example <code>requirements.txt</code> File</h3>
        <p>Make sure you have a <code>requirements.txt</code> file in your project directory. Here is an example of what it might include:</p>
        <pre><code>Flask==2.1.1
Flask-SQLAlchemy==2.5.1</code></pre>

        <p>Now, you can follow the steps in the README file to set up the project, and others can do the same by following the detailed instructions.</p>
    </div>
</body>
</html>
