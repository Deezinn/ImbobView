# 🏡 ImbobView

The **README** file is the main document that introduces and explains a project.  
It typically includes the project’s purpose, features, and instructions on how to get started using it.

**ImbobView** is an interactive platform built with [Plotly Dash](https://dash.plotly.com/) that provides dynamic visualizations of **real estate prices across Brazil**. The goal is to simplify real estate market analysis through an intuitive, accessible, and data-rich dashboard.

## 📊 Technologies Used

- [Python 3.10+](https://www.python.org/)
- [Plotly Dash](https://dash.plotly.com/)
- [Pandas](https://pandas.pydata.org/)
- [Docker](https://www.docker.com/)

## 📌 Features

- Interactive visualization of property prices by state and city  
- Filters for property type, price range, and time period  
- Map showing geographic distribution of properties  
- Line, bar, and scatter plots  
- Responsive and accessible via web browser  
- Data tables with up-to-date information  

## 📷 Dashboard Preview

![Preview](src/app/assets/img/print_atual.png)

## 🛠️ How to Run Locally

The **Installation Guide** shows users how to install and run the project on their own computer.  
It explains all the steps and tools needed to get the dashboard up and running.

1. Clone the repository:
   ```bash
   git clone https://github.com/seu-usuario/imbobview.git
   cd imbobview
   ```

2. (Optional but recommended) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

Alternatively, you can run the application using **Docker**:

1. Build the Docker image:
   ```bash
   docker build -t imbobview .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 8050:8050 imbobview
   ```
## 🔌 API Reference

The **API Reference** is a detailed list of all functions or endpoints provided by a software.  
It explains what each one does and how to use them.

ImbobView extracts and visualizes data from **SINAPI (National System of Costs Survey and Indexes of Civil Construction)**, a public dataset maintained by the Brazilian Institute of Geography and Statistics ([IBGE](https://www.ibge.gov.br/)).

- **Source**: SINAPI provides monthly updates on construction material prices and labor costs across different Brazilian states and cities.
- **Usage**: The application uses this dataset to generate dynamic visualizations of real estate-related price trends, allowing users to filter and explore the information geographically and temporally.

Currently, data is extracted from public CSV files or APIs when available, and processed using Python scripts. This allows ImbobView to offer relevant insights into housing and construction costs across Brazil.

> Note: Future updates may include direct integration with IBGE’s API for automatic data refresh.

---


Once running, open your browser and go to: [http://localhost:8050](http://localhost:8050)

---
