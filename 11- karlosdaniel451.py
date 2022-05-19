from .hotel import (
    Hotel,
    HotelReservation,
    get_lakewood_instance,
    get_bridgewood_instance,
    get_ridgewood_instance
)

from .day import DayOfWeek


lakewood_hotel = get_lakewood_instance()
bridgewood_hotel = get_bridgewood_instance()
ridgewood_hotel = get_ridgewood_instance()


def main():
    date_sequence_samples: list[str] = []

    date_sequence_samples.append('Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)')
    date_sequence_samples.append('Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)')
    date_sequence_samples.append('Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)')

    for date_sequence in date_sequence_samples:
        print(f'For the date sequence "{date_sequence}" the cheapest hotel is'
              f' {get_cheapest_hotel(date_sequence)}.')

def get_cheapest_hotel(number: str) -> str:   # DO NOT change the function's name
    """
    Get the name of the cheapest Hotel between Lakewood, Bridgewood and
    Ridgewood for a given sequence of dates and considering the type of client
    (Regular or Reward.)
    """
    has_client_loyalty = number.startswith('Rewards')
    days_of_weeks_of_reservations = extract_days_of_week_from_dates(
        dates=number)

    total_price_for_lakewood = 0.0
    total_price_for_bridgewood = 0.0
    total_price_for_ridgewood = 0

    for day in days_of_weeks_of_reservations:
        reservation = HotelReservation(
            day_of_week=day,
            has_client_loyalty=has_client_loyalty
        )

        total_price_for_lakewood += lakewood_hotel.get_price_for_reservation(reservation)
        total_price_for_bridgewood += bridgewood_hotel.get_price_for_reservation(reservation)
        total_price_for_ridgewood += ridgewood_hotel.get_price_for_reservation(reservation)

    if total_price_for_lakewood < total_price_for_bridgewood:
        if total_price_for_lakewood < total_price_for_ridgewood:
            return lakewood_hotel.name
        else:
            return ridgewood_hotel.name
    
    if total_price_for_lakewood == total_price_for_bridgewood:
        if total_price_for_bridgewood < total_price_for_ridgewood:
            return bridgewood_hotel.name
        else:
            return ridgewood_hotel.name

    if total_price_for_bridgewood < total_price_for_ridgewood:
        return bridgewood_hotel.name

    return ridgewood_hotel.name


def extract_days_of_week_from_dates(dates: str) -> list[DayOfWeek]:
    """
    Extract and return the list of days of the week in `dates`
    delimited by parentheses and commas. For instance, if `dates` is
    equals to '(seg),foobar(tues),(thur)', then the returned list would
    be ['seg', 'tues', 'thur'].
    """
    extracted_days_of_week: list[DayOfWeek] = []

    for date in dates.split(','):
        extracted_days_of_week.append(DayOfWeek(date.split('(')[1].split(')')[0].upper()))

    return extracted_days_of_week

if __name__ == '__main__':
    main()
    