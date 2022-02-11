import csv
import logging

logger = logging.getLogger(__name__)


def extract_data_from_csv_file(file_content):
    timestamps = []
    locations = []

    with open(file_content, "r",  newline='') as csv_file: 
        try:
            metadata_reader = csv.reader(csv_file)

            for row in list(metadata_reader):
                timestamps.append(row[0])
                locations.append({"latitude": row[1], "longitude": row[2]}) 
        except csv.Error as e:
            logger.error(f"Unexcepted error occured while processing the CSV file {file_content}: {e}")
    
    return timestamps, locations
