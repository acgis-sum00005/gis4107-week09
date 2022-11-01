#-------------------------------------------------------------------------------
# Name:        world_pop_explorer.py
#
# Purpose:     Provide some functions to analyze the data in
#              world_pop_by_country.py
#
# Author:      David Viljoen
#
# Created:     24/11/2017
# Last update: 31/10/2022
#-------------------------------------------------------------------------------

from world_pop_by_country import data as country_pop

# Key = country name and
# Value = population as a number (i.e. not text containing commas)
#
country_to_pop = dict()

countries = [country.split("\t") for country in country_pop.split("\n")[1:]]

def get_country_count():
    """Return the number of countries in country_pop.
    NOTE:  Assume data (country_pop) will always have a header"""
    return len(countries)


def conv_num_with_commas(number_text):
    """Convert a number with commas (str) to a number.
       e.g. '1,000' would be converted to 1000"""
    return int(number_text.replace(',', ''))


def get_top_five_countries():
    """Return a list of names of the top five countries in terms of population"""
    top_five = sorted(country_to_pop.items(), key=lambda x: x[1], reverse=True)[:5]
    return [country[0] for country in top_five]

def set_country_to_pop():
    """Sets the global country_to_pop dictionary where key is country name
         and value is a tuple containing two elements:
            1. A numeric version of the comma separated number in the
               Pop 01Jul2017 column
            2. The % decrease as a number
    """
    for country in countries:
        population = conv_num_with_commas(country[5])
        if country[6][0] == '+':
            change = country[6][1:][:-1]
        else:
            change = country[6][:-1]
        change = float(change)
        country_to_pop[country[1]] = (population, change)

set_country_to_pop()
print(get_top_five_countries())

def get_population(country_name):
    """Given the name of the country, return the population as of 01Jul2017
       from country_to_pop.  If the country_to_pop is
       empty (i.e. no keys or values), then run set_country_to_pop
       to initialize it."""


def get_continents():
    """Return the list of continents"""
    continents_all = [country[2] for country in countries]
    continents = []
    for i in continents_all:
        if i not in continents:
            continents.append(i)
    continents.sort()
    return continents

# print(get_continents())


def get_continent_populations():
    """Returns a dict where the key is the name of the continent and
       the value is the total population of all countries on that continent"""
    africa_total = 0
    asia_total = 0
    americas_total = 0
    europe_total = 0
    oceania_total = 0
    for country in countries:
        continent = country[2]
        population = conv_num_with_commas(country[5])
        if continent == 'Africa':
            africa_total += population
        elif continent == 'Americas':
            americas_total += population
        elif continent == 'Asia':
            asia_total += population
        elif continent == 'Europe':
            europe_total += population
        elif continent == 'Oceania':
            oceania_total += population
    populations = {
        'Africa': africa_total,
        'Asia': asia_total,
        'Americas': americas_total,
        'Europe': europe_total,
        'Oceania': oceania_total,
    }
    return populations
