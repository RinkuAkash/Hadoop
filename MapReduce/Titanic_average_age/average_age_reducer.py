#!/usr/bin/env python3

import sys

# Reducer code to calculate average age of died people in titanic tragedy

female_count = 0
female_age = 0
male_count = 0
male_age = 0


for line in sys.stdin:
    line = line.strip()
    gender, age = line.split(',')
    if gender == 'male':
        male_count += 1
        male_age += float(age)
    if gender == 'female':
        female_count += 1
        female_age += float(age)

print("Female average age: %d" % (female_age//female_count))
print("Male average age: %d" % (male_age//male_count))
