# GIDA: Global Income Distribution Analytics

## 🌐 Live Demo
**[👉 https://onkarvyawahare04.pythonanywhere.com/](https://onkarvyawahare04.pythonanywhere.com/)**

**GIDA (Global Income Distribution Analytics)** is a sophisticated intelligence platform designed to decode the complexities of wealth distribution and economic disparity. By leveraging authoritative data from global financial institutions, GIDA transforms raw indicators into high-impact visual narratives. The platform empowers researchers, policy-makers, and analysts to explore the intricate relationships between economic growth and societal prosperity across the globe.

---

## ✨ Key Features

### 1. High-Performance Native Dashboard
- **Comprehensive Visualizations**: 9+ custom charts built with **Chart.js**, including heatmaps, scatter plots, and trend lines.
- **Interactive Global Map**: A **Leaflet.js** implementation featuring continent-specific data analysis and immersive popups.
- **Dynamic Slicing**: Real-time filters for regions, years, and economic metrics.

### 2. Advanced Administrator Control Panel
- **Real-Time Analytics**: Monitor platform health, user registration trends, and feedback trends.
- **Dynamic Visitor Tracking**: Select specific dates to view visitor traffic and platform engagement.
- **User Management**: Administrative tools to manage account access and platform security.

### 3. Integrated Feedback & Rating System
- **Star Rating Feedback**: Users can leave qualitative feedback and quantitative star ratings on all pages.
- **Embedded Dashboard Feedback**: A simplified feedback loop integrated directly into the analytics interface.

### 4. Comprehensive "About" Repository
- **Strategic Documentation**: Detailed sections on project objectives, problem statements, and data methodology.

### 5. Automated Reporting
- **Excel Export**: Instant generation of downloadable data reports in `.xlsx` format for offline analysis.

---

## 🛠 Tools & Technology Roles

### Software & Platforms
| Tool | Utilization |
| :--- | :--- |
| **Microsoft Power BI** | Used for initial data modeling, prototype visualization, and defining analytical KPIs. |
| **Microsoft Excel** | Primary tool for historical data storage, dataset cleaning, and final report generation. |
| **SQLite / SQLAlchemy** | Provides a robust relational database layer for user data, analytics, and feedback. |
| **Beekeeper Studio** | Visual database browser (like Prisma Studio) used to inspect and manage the SQLite database live. |
| **Visual Studio Code** | The primary integrated development environment (IDE) for the platform's codebase. |

### Programming Languages
| Language | Implementation Role |
| :--- | :--- |
| **Python** | **Backend Intelligence**: Powering server-side logic (Flask), data analysis (Pandas), and report generation. |
| **HTML5** | **Semantic Structure**: Defining the architecture of all platform templates and user interfaces. |
| **CSS3** | **Visual Design**: Implementing premium glassmorphism, responsive grids, and sophisticated animations. |
| **JavaScript** | **Client-Side Interactivity**: Powering real-time charts, interactive maps, and dynamic UI transitions. |
| **SQL** | **Data Management**: Relational queries managed through SQLite and SQLAlchemy ORM. |
| **Jinja2** | **Template Infrastructure**: Enabling dynamic content injection and modular frontend components. |
| **Markdown** | **Documentation**: Crafting comprehensive technical guides and project repositories. |

---

## 🏗 Technology Stack
- **Web Framework**: Flask (Python 3.x)
- **Security & Auth**: Flask-Login, Werkzeug (PBKDF2 Password Hashing)
- **Database Layer**: SQLite with SQLAlchemy ORM
- **Frontend Core**: HTML5, CSS3, JavaScript (ES6+), Jinja2
- **UI Frameworks**: Bootstrap 5, Bootstrap Icons
- **Visual Intelligence**: Chart.js (Analytics), Leaflet.js (Geospatial Mapping)
- **Animations**: AOS (Animate On Scroll)
- **Data Engineering**: Pandas, NumPy
- **Reporting Engine**: OpenPyXL (Excel Generation)
- **Deployment**: PythonAnywhere
- **Database Tools**: Beekeeper Studio (Live SQLite Browser)

---

## 📂 Project Structure

```text
├── backend/
│   ├── app.py                      # Core Backend Logic & API Endpoints
│   └── requirements.txt            # System Dependencies
├── frontend/
│   ├── static/
│   │   ├── css/
│   │   │   └── dashboard_native.css # Premium Glassmorphism Theme
│   │   └── js/
│   │       └── dashboard_logic.js   # Chart.js & Map Visual Implementations
│   └── templates/
│       ├── base.html               # Master Layout & Professional Navbar
│       ├── home.html               # High-Impact Landing Page
│       ├── about.html              # Project Methodology & Objectives
│       ├── dashboard.html          # Core Analytics Interface
│       ├── admin.html              # Administrator Intelligence Dashboard
│       ├── feedback.html           # User Insight & Rating Gateway
│       └── login.html              # Security Gateway
├── dataset/
│   └── Global Income Distribution Dataset.xlsx  # Global Dataset Repository
├── instance/
│   └── database.db                 # Relational Database (Users, Visits, Feedback)
├── scripts/                        # Utility & Data Processing Scripts
├── docs/                           # Documentation & Reports
└── api/
    └── index.py                    # Deployment Entry Point
```

---

## ⚙️ Installation & Setup

### 1. Prerequisites
- Python 3.8+ installed.
- Modern web browser (Chrome, Firefox, or Edge recommended).

### 2. Setup Procedure
1. **Clone Repository**:
   ```bash
   git clone https://github.com/onkarvyawahare04-jpg/Global_Income_Distribution.git
   cd Global_Income_Distribution
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Initialize Application**:
   ```bash
   python backend/app.py
   ```
4. **Access Platform**:
   Navigate to `http://127.0.0.1:5000` in your browser.

---

## 📑 Data Sources
GIDA utilizes verified socio-economic indicators from authoritative global institutions:
- **World Bank Open Data**
- **International Monetary Fund (IMF)**
- **United Nations Development Programme (UNDP)**
