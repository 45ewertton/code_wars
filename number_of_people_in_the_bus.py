def number(bus_stops):
    people_number = 0
    for going_up, going_down in bus_stops:
        people_number += going_up - going_down

    return people_number