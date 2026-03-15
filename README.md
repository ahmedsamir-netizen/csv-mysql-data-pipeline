# CSV to MySQL Data Pipeline

## Overview
This project demonstrates a complete ETL (Extract, Transform, Load) pipeline using Python and MySQL.
It reads raw sales data from CSV, cleans and transforms it, and loads it into a MySQL database.

## Technologies Used
- Python
- Pandas
- MySQL
- python-dotenv

## Pipeline Steps
1. **Extract**: Read raw CSV dataset
2. **Transform**: Clean column names, handle missing values, convert data types
3. **Load**: Insert cleaned data into MySQL table

## Project Structure
```
csv-mysql-data-pipeline/
├── data/                   # Raw and cleaned CSV files
├── src/                    # Python scripts
│   ├── clean_data.py       # Data cleaning and transformation
│   ├── db_connection.py    # DB connection handler
│   ├── load_data.py        # Load cleaned data to MySQL
│   └── read_data.py        # Preview / check data
├── .env                    # Environment variables for DB credentials
├── .gitignore
├── requirements.txt        # Python dependencies
├── schema.sql              # SQL table schema
└── README.md
```

## How to Run
1. Install dependencies:
```bash
pip install -r requirements.txt
```
2. Create MySQL database and table using `schema.sql`
3. Add DB credentials in `.env`
4. Run cleaning script:
```bash
python clean_data.py
```
5. Run loading script:
```bash
python load_data.py
```
6. Optional: Preview first 10 rows:
```bash
python read_data.py
```

## Notes
- Handles day/month/year date format
- Drops invalid/missing rows automatically
- Prints any row insertion errors without stopping the process
- Fully modular ETL pipeline with clean separation of steps

