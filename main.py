from processor.cleaner import clean_data
from processor.analyzer import analyze_data
from output.report_generator import generate_report
from utils.file_handler import load_csv, save_csv

INPUT_FILE = "data/raw/input.csv"
OUTPUT_FILE = "data/processed/cleaned.csv"

def run_pipeline():
    print("Loading data...")
    df = load_csv(INPUT_FILE)

    print("Cleaning data...")
    cleaned_df = clean_data(df)

    print("Saving cleaned data...")
    save_csv(cleaned_df, OUTPUT_FILE)

    print("Analyzing data...")
    summary = analyze_data(cleaned_df)

    print("Generating report...")
    generate_report(summary)

    print("Pipeline completed successfully.")

if __name__ == "__main__":
    run_pipeline()
