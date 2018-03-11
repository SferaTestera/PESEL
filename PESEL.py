#!/usr/bin/env python
from random import randint


def get_year():
    
    while True:
        year = input("Prosze podac roku urodzenia: ")
        if year < 1800 or year > 2299:
            print "Prosze podac date z zakresu 1800 do 2299"
        else:
            return year

def get_month():

    while True:
        month = input("Prosze podac miesiac urodzenia: ")       
        if month < 1 or month > 12:
            print "Prosze podac date z zakresu 1 do 12"
        else:
            return month

def get_day():

    while True:
        day = input("Prosze podac dzien urodzenia :")
        if day < 1 or day > 31:
            print "Prosze podac date z zakresu 1 do 31"
        else:
            return day
  
def year_number(year):
    return str(year)[2:4]

def month_number(year, month):

    if 1800 <= year <= 1899:
        month = month + 80
        return '{0:02}'.format(month)

    if 1900 <= year <= 1999:
        month = month
        return '{0:02}'.format(month)

    if 2000 <= year <= 2299:
        number_from_1_to_2 = month + 20
        return number_from_1_to_2

    if 2100 <= year <= 2199:
        number_from_1_to_2 = month + 40
        return number_from_1_to_2

    if 2200 <= year <= 2899:
        number_from_1_to_2 = month + 60
        return number_from_1_to_2

def day_number(day):
    return day

def serial_number():
    return randint(0, 999)

def gender_number():
    return randint(0, 9)

def check_digit():


year = get_year()
month = get_month()
day = get_day()

year_number = year_number(year)
month_number = month_number(year, month)
day_number = day_number(day)
serial_number = serial_number()
gender_number = gender_number()

print year_number
print month_number
print day
print serial_number
print gender_number



print("Rok: " + str(year) + " Miesiac: " + str(month) + " Dzien: " + str(day))

print ("Numer PESEl: " + str(year_number) + str(month_number) + str(day_number) + str(serial_number))
