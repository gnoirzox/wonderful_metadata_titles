from collections import Counter
import itertools
import json
import logging
import os

from typing import Optional

import requests

logger = logging.getLogger(__name__)


class Location:
    def __init__(self, latitude: float, longitude: float):
        if self._validate_coordinates(latitude, longitude):
            self.latitude = format(float(latitude), ".2f")
            self.longitude = format(float(longitude), ".2f")
            self.api_query_url = self._build_reverse_geocoding_api_url()
        else:
            logger.error(
                f"The given coordinates (latitude: {self.latitude}; "\
                        "longitude: {self.longitude}) are not valid.")

    def _validate_coordinates(self, latitude: float, longitude: float) -> bool:
        valid_latitude = False
        valid_longitude = False

        if -90 <= float(latitude) <= 90:
            valid_latitude = True
        if -180 <= float(longitude) <= 180:
            valid_longitude = True

        return valid_latitude and valid_longitude

    def _build_reverse_geocoding_api_url(self) -> Optional[str]:
        base_url = os.getenv("GOOGLE_MAPS_GEOCODING_API_URL")
        api_key = os.getenv("GOOGLE_MAPS_API_KEY")

        if (base_url or api_key) is None:
            logger.error(
                "Please check whether the environment variables GOOGLE_MAPS_GEOCODING_API_URL"\
                " and GOOGLE_MAPS_API_KEY are setup correctly into your environment.")
            return 

        new_url = base_url.replace("{latitude}", self.latitude)\
            .replace("{longitude}", self.longitude)\
            .replace("{GOOGLE_MAPS_API_KEY}", api_key)

        return new_url

    def get_location_details(self) -> Optional[object]:
        if self.latitude == 0.00 and self.longitude == 0.00:
            logger.error(
                f"The given coordinates (latitude: {self.latitude}; "\
                        "longitude: {self.longitude}) "\
                        "are not expected to be on the Null Island point.")
            return

        try:
            response = requests.get(self.api_query_url)
            if response.status_code == 200:
                return response.json()
            else:
                logger.error(f"We got an unexpected response while trying"\
                        f" to reach reverse geocoding api: {response.status_code}")
        except Exception as e:
            logger.error(
                f"Handled an exception while trying to reach reverse geocoding api: {e}")


def extract_meaningful_location_data(location_data: object):
    results = location_data.get("results")
    administrative_types = {
            "locality", "administrative_area_level_1", "country"}
    meaningful_locations = []

    for address_components in results:
        for address_component in address_components.get("address_components"):
            if address_components.get("types")[0] in administrative_types:
                meaningful_locations.append(address_component.get("long_name"))

    return meaningful_locations


def get_most_common_location_details(locations: list) -> list:
    all_location_details = []

    for location in locations: 
        location_object = Location(
            location.get("latitude"),
            location.get("longitude")
        )
        location_details = location_object.get_location_details()

        meaningful_location_details = extract_meaningful_location_data(
                location_details)
        all_location_details.extend(meaningful_location_details)

    all_location_details_counter =  Counter(all_location_details)

    return list(itertools.islice(all_location_details_counter.items(), 3))
