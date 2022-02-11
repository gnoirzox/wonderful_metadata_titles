SAMPLE_TITLES = [
    "{time_period} in {location}",
    "A trip in {location}",
    "A trip to {location}",
    "A rainy trip to {location}",
    "A sunny trip to {location}",
    "A wonderful trip to {location}",
    "A magical trip to {location}",
    "{location} during {time_period}",
    "{time_period} in {location}",
]


def generate_titles(meaningful_locations: list, meaningful_period: list) -> list:
    all_titles = []

    for location in meaningful_locations:
        for title in SAMPLE_TITLES:
            generated_title = title.replace("{location}", location[0])\
                    .replace("{time_period}", meaningful_period)

            all_titles.append(generated_title.title())

    return all_titles
