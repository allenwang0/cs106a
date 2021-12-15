#!/usr/bin/env python3

"""
Stanford CS106A flights Project
"""

import sys


def parse_flights(text):
    """
    Given text with lines of flight data,
    returns flights dict.
    More Doctests TBD
    >>> parse_flights('sfo,1,2\\nsfo,3,4\\n')
    {'sfo': [(1, 2), (3, 4)]}
    >>> parse_flights('iah,5,3\\nhou,4,6\\nsjc,7,3\\nhou,3,2\\n')
    {'iah': [(5, 3)], 'hou': [(3, 2), (4, 6)], 'sjc': [(7, 3)]}
    >>> parse_flights('lax,1,1\\nlax,68,21321\\npdx,123,5678\\nmke,765,432\\nmdw,234,21\\nmke,2,1\\nlga,2,654765467\\n')
    {'lax': [(1, 1), (68, 21321)], 'pdx': [(123, 5678)], 'mke': [(2, 1), (765, 432)], 'mdw': [(234, 21)], 'lga': [(2, 654765467)]}
    """
    flights_dict = {}
    flights_split = text.splitlines()
    for flight in flights_split:
        flights_list = flight.split(',')
        city = flights_list[0]
        time = flights_list[1]
        pax = flights_list[2]
        pair = (int(time), int(pax))
        if city not in flights_dict:
            flights_dict[city] = []
        pair_list = flights_dict[city]
        pair_list.append(pair)
        flights_dict[city] = sorted(pair_list)
    return flights_dict


def read_sched(filename):
    """
    (provided)
    Returns flights dict parsed from file.
    """
    with open(filename, 'r') as f:
        text = f.read()
    return parse_flights(text)


def main():
    # (provided)
    args = sys.argv[1:]
    flights = read_sched(args[0])
    print(flights)


if __name__ == '__main__':
    main()
