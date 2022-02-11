import argparse

from file_handling import extract_data_from_csv_file
from date_range import TimePeriod 
from reverse_geocoding import get_most_common_location_details
from generate_titles import generate_titles



def main():
    parser = argparse.ArgumentParser(
            description='Process a metadata CSV file.')
    parser.add_argument(
            "-f", help="the CSV file to retrieve photos metadata from")
    arguments = parser.parse_args()

    datetimes, locations = extract_data_from_csv_file(arguments.f) 
    most_common_locations = get_most_common_location_details(locations)
    time_period = TimePeriod(datetimes)

    generated_titles = generate_titles(
            most_common_locations, time_period.period_length)

    print(f"'suggested titles': {generated_titles}")


if __name__ == "__main__":
    main()
