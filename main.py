import pandas as pd
import os
import sys
from pathlib import Path

# Default path returned by kagglehub (change this if your cache is elsewhere)
DEFAULT_KAGGLE_PATH = r"C:\Users\asant\.cache\kagglehub\datasets\karkavelrajaj\amazon-sales-dataset\versions\1"


def find_first_csv(directory: Path):
	"""Return the first .csv Path in directory (non-recursive), or the first found recursively.
	Returns None when no CSV is found.
	"""
	if not directory.exists():
		return None
	# Non-recursive first
	for p in directory.iterdir():
		if p.is_file() and p.suffix.lower() == ".csv":
			return p
	# Recursive fallback
	csvs = list(directory.rglob("*.csv"))
	return csvs[0] if csvs else None


def main():
	# Try the default kagglehub cache path first
	default_path = Path(DEFAULT_KAGGLE_PATH)
	csv_path = find_first_csv(default_path)

	if csv_path:
		print(f"Using CSV found at: {csv_path}")
	else:
		# Try project folder as a friendly fallback
		project_root = Path(__file__).parent
		csv_path = find_first_csv(project_root)
		if csv_path:
			print(f"Default path not found. Using CSV found in project: {csv_path}")
		else:
			print(f"Could not find dataset at default path: {default_path}")
			print(f"Also did not find any .csv files under the project folder: {project_root}")
			print("Please download the dataset, place the CSV in the project folder, or update the DEFAULT_KAGGLE_PATH variable in this script to point to the folder that contains the CSV.")
			# Exit cleanly instead of raising an unhelpful traceback
			sys.exit(1)

	# Load into pandas with a friendly error message on failure
	try:
		df = pd.read_csv(csv_path)
	except Exception as exc:
		print(f"Error reading CSV file {csv_path}: {exc}")
		sys.exit(1)

	print(df.shape)
	print(df.head())


if __name__ == "__main__":
	main()
