from processor.cleaner import clean_data
from processor.analyzer import analyze_data
from output.report_generator import generate_report
from utils.file_handler import load_csv, save_csv
from utils.email_sender import send_email
import os

INPUT_FILE = "data/raw/input.csv"
OUTPUT_FILE = "data/processed/cleaned.csv"


def run_pipeline():
    try:
        print("🔹 Loading data...")
        df = load_csv(INPUT_FILE)

        if df.empty:
            raise ValueError("Input CSV is empty.")

        print("🔹 Cleaning data...")
        cleaned_df = clean_data(df)

        # Ensure output directory exists
        os.makedirs("data/processed", exist_ok=True)

        print("🔹 Saving cleaned data...")
        save_csv(cleaned_df, OUTPUT_FILE)

        print("🔹 Analyzing data...")
        summary = analyze_data(cleaned_df)

        print("🔹 Generating report...")
        report_path = generate_report(summary)

        print("🔹 Sending email...")
        email_status = send_email(report_path)

        if not email_status:
            print("⚠️ Email failed, but pipeline completed.")

        print("✅ Pipeline completed successfully.")

    except FileNotFoundError:
        print(f"❌ Error: Input file not found at '{INPUT_FILE}'")

    except ValueError as ve:
        print(f"⚠️ Data Error: {ve}")

    except Exception as e:
        print(f"🔥 Unexpected Error: {e}")


if __name__ == "__main__":
    run_pipeline()
