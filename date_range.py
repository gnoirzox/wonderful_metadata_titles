from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class TimePeriod:
    def __init__(self, datetimes: list):
        self._assess_period_length(datetimes)
        self.period_length = self._define_period_length()

    def _assess_period_length(self, datetime_strings: list): 
        timestamps = []

        for datetime_string in datetime_strings:
            try:
                datetime_object = datetime.strptime(
                    datetime_string, "%Y-%m-%d %H:%M:%S")
            except ValueError as e:
                datetime_object = datetime.strptime(
                    datetime_string, "%Y-%m-%dT%H:%M:%SZ")
                    
            timestamp = datetime.timestamp(datetime_object)

            if timestamp > 0:
                timestamps.append(timestamp)

        timestamps.sort()

        self.time_delta = datetime.fromtimestamp(timestamps[-1]) \
                - datetime.fromtimestamp(timestamps[0])
        self.first_datetime = datetime.fromtimestamp(timestamps[0])
        self.last_datetime = datetime.fromtimestamp(timestamps[-1])

    def _define_period_length(self) -> str:
        days_delta = self.time_delta.days
        period_string = ""

        if days_delta ==1:
            period_string = "a day"
        elif days_delta == 2 and self._is_weekend():
            period_string = "a weekend"
        elif days_delta == 2 and not self._is_weekend():
            period_string = "two days"
        elif 3 <= days_delta <= 6:
            period_string = "a few days"
        elif 7 <= days_delta <= 10:
            period_string = "a week"
        elif 11 <= days_delta <= 19:
            period_string = "two weeks"
        elif 20 <= days_delta <= 30:
            period_string = self.get_period_month()
        elif 80  <= days_delta <= 90:
            period_string = "a quarter"
        elif 150  <= days_delta <= 190:
            period_string = "a semester"
        elif 300  <= days_delta <= 400:
            period_string = "a year"

        return period_string

    def _is_weekend(self) -> bool:
        is_weekend = False
        days_delta = self.time_delta.days
        first_day = selffirst_datetime.strftime('%A')
        second_day = self.last_datetime.strftime('%A')

        if days_delta == 2 and \
                (first_day == "Saturday" and second_day == "Sunday"):
            is_weekend = True

        return is_weekend

    def get_period_month(self) -> str:
        months = []

        if slef.period_length == "month":
            month = self.first_datetime.strftime("%B")

        return month
