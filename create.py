import os
import sys
from datetime import datetime

def create_folders_and_files(year=None, day=None):
    # Get the current year if not provided
    if year is None:
        year = datetime.now().year

    # Ensure the year is an integer
    year = int(year)

    # Define the base directory name
    base_dir = f"{year}-python"

    # Create the base directory if it does not exist
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    # Determine the day folder
    if day is None:
        # Find the last day folder in the base directory
        existing_days = [
            int(folder.split('-')[1]) for folder in os.listdir(base_dir)
            if folder.startswith("day-") and folder.split('-')[1].isdigit()
        ]
        day = max(existing_days, default=0) + 1
    
    day = int(day)

    # Define the day folder name
    day_folder = os.path.join(base_dir, f"day-{day}")

    # Create the day folder if it does not exist
    if not os.path.exists(day_folder):
        os.makedirs(day_folder)

    # Create the solution.py file
    solution_file = os.path.join(day_folder, "solution.py")
    if not os.path.exists(solution_file):
        with open(solution_file, "w") as f:
            f.write("""from aocd import get_data, submit

use_example = False
submit_ans = False and not use_example

if use_example:
    with open('example.txt') as f:
        inputs = f.read().splitlines()
else:
    inputs = get_data(year={}, day={}).splitlines()



ans_a = ans_b = 0



if submit_ans:
    submit(ans_a, part='a', year={}, day={})
    submit(ans_b, part='b', year={}, day={})
""".format(year, day, year, day, year, day))

    # Create the example.txt file
    example_file = os.path.join(day_folder, "example.txt")
    if not os.path.exists(example_file):
        with open(example_file, "w") as f:
            f.write("")

if __name__ == "__main__":
    # Parse command-line arguments
    args = sys.argv[1:]

    # Get year and day from arguments if provided
    year = int(args[0]) if len(args) > 0 else None
    day = int(args[1]) if len(args) > 1 else None

    # Create the folders and files
    create_folders_and_files(year, day)
