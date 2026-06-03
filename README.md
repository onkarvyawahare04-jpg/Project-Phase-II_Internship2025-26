# Global Income Distribution Analytics Dashboard (GIDA)

## Overview
A comprehensive, web-based interactive analytics platform designed to provide insights into global income distribution. Built with Flask, this dashboard allows users to seamlessly visualize and analyze crucial economic metrics such as GDP per capita, Gini Index, and unemployment rates across various countries and continents.

## Key Features
- **Interactive Data Dashboard:** Engaging visualizations for key economic indicators using dynamic charts and graphs.
- **Country Comparison:** Side-by-side data comparison between different countries across various years.
- **AI Chatbot Integration:** An embedded, intelligent assistant to help users navigate the platform and query data.
- **Robust User Authentication:** Secure login and registration system with clearly defined User and Administrator roles.
- **Admin Control Center:** A comprehensive management panel for monitoring site traffic, managing users (including ban capabilities), and reviewing/responding to user feedback.
- **Dual Theme Support:** Modern Dark Premium UI design with an intuitive Light mode toggle for optimal accessibility.
- **Data Export:** One-click functionality to download the core dataset for external analysis.

## Technology Stack
- **Backend:** Python, Flask, Flask-SQLAlchemy (ORM), Flask-Login (Authentication), Pandas (Data Processing), Werkzeug (Security)
- **Frontend:** HTML5, CSS3, Vanilla JavaScript, Chart.js (Data Visualization)
- **Database:** SQLite (default local database)

## Project Structure
```text
📦 Global Income Distribution Project
├── 📂 backend/                  # Server-side logic
│   ├── app.py                   # Main Flask application and API routing
│   ├── chatbot.py               # Chatbot logic and NLP processing
│   └── requirements.txt         # Backend-specific dependencies
│
├── 📂 frontend/                 # Client-side presentation
│   ├── 📂 static/               # CSS styles, JS logic, and image assets
│   └── 📂 templates/            # HTML templates for rendering views
│
├── 📂 dataset/                  # Source data files (e.g., Global Income Excel dataset)
├── 📂 docs/                     # Project documentation and specifications
├── 📂 instance/                 # Instance-specific files (automatically generated SQLite DB)
├── 📂 scripts/                  # Auxiliary utility scripts
└── 📄 requirements.txt          # Main project dependencies
```

## Setup and Installation

### Prerequisites
- Python 3.8+ installed on your system.

### Installation Steps

1. **Navigate to the project directory**
   Ensure you are in the root directory of the project in your terminal.

2. **Create a Virtual Environment (Recommended)**
   ```bash
   python -m venv venv
   ```
   Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**
   Run the following command to install all required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   Launch the Flask development server by executing:
   ```bash
   python backend/app.py
   ```
   The application will initialize the database, create default tables, and start. You can access it by opening `http://127.0.0.1:5000` in your web browser.

## Default Credentials
For administrative access, a default account is generated upon the first run:
- **Email:** `admin@gida.com`
- **Password:** `admin123`

## Usage Roles
- **Standard Users:** Can register an account, log in, explore the analytics dashboard, interact with the AI chatbot, and submit feedback to the admin.
- **Administrators:** Can access a dedicated portal to view system growth metrics, manage the user base, analyze daily site visits, and reply to user feedback.
