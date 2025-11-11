# Hami MiniMarket Management Suite

A comprehensive Python project suite developed during my 4-week intensive internship with **HamiSkills**. This collection of applications simulates a full business workflow for a small market, from inventory management and sales processing to data analysis and visualization.

I am profoundly grateful to the HamiSkills team for providing me and my fellow interns with this incredible learning opportunity. The structured curriculum and practical projects were instrumental in strengthening my Python programming and software development skills.

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Acknowledgements](#acknowledgements)
- [Technologies Used](#technologies-used)
- [Project Structure & Weekly Progression](#project-structure--weekly-progression)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Features in Detail](#features-in-detail)
- [Repository Structure](#repository-structure)
- [Professional Links](#professional-links)

## 🚀 Project Overview

The **Hami MiniMarket Management Suite** is a four-phase project that builds upon a core idea, demonstrating progressive skill development in Python programming.

- **Week 1:** Core logic with a Command-Line Interface (CLI) Inventory System.
- **Week 2:** Enhanced functionality with a CLI Order Management System.
- **Week 3:** Improved user experience with a GUI Desktop Application.
- **Week 4:** Data-driven decision-making with a Sales Analytics Dashboard.

## 🙏 Acknowledgements

I would like to extend my sincere gratitude to **HamiSkills** for this invaluable internship experience. Thank you for designing a program that not only taught us technical skills but also emphasized professional growth through project building and presentation.

This opportunity has been a significant milestone in my journey as a developer, and I appreciate the chance to have learned and built alongside other talented interns.

## 💻 Technologies Used

*   **Language:** Python 3
*   **Libraries & Frameworks:**
    *   `tkinter` (for GUI)
    *   `pandas` (for data manipulation)
    *   `matplotlib` or `plotly` (for data visualization)
    *   `csv`, `json` (for file handling)
    *   `datetime` (for timestamps)
*   **Tools:** Git, GitHub, Command Line/Terminal

## 📈 Project Structure & Weekly Progression

### **Week 1: CLI Product Inventory System**
*   **Objective:** Build a foundational command-line program to manage market inventory.
*   **Key Features:**
    *   Add, view, and update product details (name, category, price, quantity).
    *   Calculate the total value of all inventory.
    *   Input validation for robust data entry.
*   **Skills Demonstrated:** Python basics, data structures (lists/dictionaries), functions, file I/O.

### **Week 2: CLI Order Management System**
*   **Objective:** Extend the Week 1 project to handle customer orders and transactions.
*   **Key Features:**
    *   Load inventory from a file.
    *   Interactive shopping cart.
    *   Calculate subtotal, tax, and final total.
    *   Generate and save itemized receipts as text files.
*   **Skills Demonstrated:** Modular programming, error handling with try/except, advanced file operations.

### **Week 3: GUI Inventory & Order Tracker**
*   **Objective:** Transform the CLI application into an intuitive desktop application.
*   **Key Features:**
    *   Graphical User Interface built with Tkinter.
    *   Real-time cart management and order confirmation.
    *   Automatic inventory updates and sales reporting to CSV.
    *   Low-stock alerts.
*   **Skills Demonstrated:** Object-Oriented Programming (OOP) with Python Classes, event-driven programming, GUI development.

### **Week 4: Sales Dashboard & Analytics (Capstone)**
*   **Objective:** Create a data analytics tool to derive insights from sales history.
*   **Key Features:**
    *   Load and combine multiple sales data files.
    *   Calculate key metrics: Total Revenue, Number of Orders, Average Order Value.
    *   Identify top-selling and low-stock products.
    *   Generate visualizations: Daily Sales Trends and Product Popularity charts.
*   **Skills Demonstrated:** Data analysis with Pandas, data visualization with Matplotlib/Plotly, producing actionable business insights.

## ⚙️ Installation & Setup

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/hami-minimarket-suite.git
    cd hami-minimarket-suite
    ```

2.  **Install Required Dependencies:**
    It is recommended to use a virtual environment. Then, install the packages:
    ```bash
    pip install pandas matplotlib
    ```
    *Note: Tkinter is usually included with standard Python installations.*

## 🏃‍♂️ Usage

Each weekly project is contained within its own folder. Navigate to the respective directory and run the main Python file.

*   **For Week 1 & 2 (CLI programs):**
    ```bash
    cd week_1_inventory
    python main.py
    ```

*   **For Week 3 (GUI application):**
    ```bash
    cd week_3_gui
    python gui.py
    ```

*   **For Week 4 (Analytics Dashboard):**
    ```bash
    cd week_4_analytics
    python main.py
    ```
    *Generated charts will be saved in the `charts/` folder.*

## ✨ Features in Detail

| Module | Core Function | Key Achievement |
| :--- | :--- | :--- |
| **Inventory Management** | Add, View, Update Stock | Foundational data integrity and CRUD operations. |
| **Order Processing** | Cart, Checkout, Receipts | Simulated real-world customer transactions. |
| **GUI Application** | Visual Interface, Alerts | Enhanced usability and user experience (UX). |
| **Data Analytics** | Metrics, Trends, Visualization | Transformed raw data into business intelligence. |

## 📁 Repository Structure
