# Setup

## Environment variables

In order to run this script, we rely on the Google Maps Geocoding API to be able to do reverse-geocoding. So, to be able to access to the Google Maps API, we rely on these 2 environment variables: 
- `GOOGLE_MAPS_API_KEY=<your api key>`
- `GOOGLE_MAPS_GEOCODING_API_URL="https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&key={GOOGLE_MAPS_API_KEY}"`

Please, retrieve your Google Maps api key in order to be able to access it. Please ensure that the access to the Geocoding api is enabled for your api key.

## Dependencies

Also, we rely on the `requests` library to make HTTP calls. In order to install it, please setup a virtual environment with `virtualenv` and then run `pip install -r rquirements.txt` to install the listed dependency in `requirements.txt`.

# Areas of improvements

These are the tasks to do in order to improve the project to a production level state: 

* Convert it into a REST api endpoint with either Flask or FastAPI.
* Use asynchronous calls with async/await and `aiorequests` library.
* Add unit tests.
* Add metrics/alerting on external dependency such as the Google Maps API.
* Add caching on API calls
