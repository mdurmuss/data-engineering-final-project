#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Mustafa Durmuş [mustafa-durmuss@outlook.com]

import json
import weathercom
from joblib import load
import numpy as np
import datetime


SPEED_CLASS = {'0': 'Low Speed',
               '1': 'Average Speed',
               '2': 'High Speed'
               }


class MLModel:
    def __init__(self, date):
        self.date = date
        self.month = int(self.date.split("-")[1])
        self.day = int(self.date.split("-")[2])
        self.is_weekend = self.is_the_day_weekend()
        self.is_holiday = self.is_the_day_holiday()
        self.is_school_holiday = 1  # cause of covid19

        self.will_be_returned = {'day': date,
                                 'is_holiday': self.is_holiday,
                                 'speedClass': {'Low Speed': (8.5, 30.0),
                                                'Average Speed': (30.5, 49.5),
                                                'High Speed': (50.0, 75.5)
                                                },
                                 'result': []
                                 }

        # tarih = bugün,yarın veya diğer gün mü?
        # bunu kontrol edelim. Ona göre saatlik veya günlük veri çekilecek.
        self.day_diff = self.find_day_difference()
        if self.day_diff <= 2:
            self.query_type = 'hourly-data'
        else:
            self.query_type = 'ten-days-data'

    def find_day_difference(self):
        now = datetime.datetime.today()
        d1 = datetime.datetime.strptime(self.date, "%Y-%m-%d")

        return abs((now - d1).days)

    def predict(self):
        model = load('model.joblib')

        self.rain_json = json.loads(weathercom.getCityWeatherDetails(city="besiktas",
                                                                     queryType=self.query_type))

        # hour ve isRainy dinamik.
        for hour, is_rainy in self.find_rain():

            ex = np.array([[self.month, self.day, hour,
                            self.is_holiday, self.is_weekend,
                            self.is_school_holiday, is_rainy]])
            label = model.predict(ex)[0]
            self.will_be_returned['result'].append({'hour': hour,
                                                    'rain': is_rainy,
                                                    'speed': SPEED_CLASS[str(label)]})

        return self.will_be_returned

    def find_rain(self):
        if self.query_type == 'hourly-data':
            for idx, d in enumerate(self.rain_json['vt1hourlyForecast']['processTime']):
                hour = d.split("T")[1].split(":")[0]
                if d.find(self.date) != -1:
                    phrase = self.rain_json['vt1hourlyForecast']['phrase'][idx]
                    if phrase.find('Rain') != -1 or phrase.find('Showers') != -1:
                        is_rainy = 1
                    else:
                        is_rainy = 0
                    yield int(hour), is_rainy
        elif self.query_type == 'ten-days-data':
            day_is_rainy = self.rain_json['vt1dailyForecast']['day']['phrase'][self.day_diff]
            night_is_rainy = self.rain_json['vt1dailyForecast']['night']['phrase'][self.day_diff]

            for hour in range(0, 24):
                is_rainy = 0
                if hour in range(6, 21):  # gündüz saatleri
                    if day_is_rainy.find('Rain') != -1 or day_is_rainy.find('Showers') != -1:
                        is_rainy = 1
                else:
                    if night_is_rainy.find('Rain') != -1 or night_is_rainy.find('Showers') != -1:
                        is_rainy = 1
                yield hour, is_rainy

    def is_the_day_weekend(self,):
        day = datetime.datetime.strptime(self.date, '%Y-%m-%d').weekday()
        if day in [5, 6]:
            return 1
        return 0

    def is_the_day_holiday(self):
        national_holidays = ["2021-01-01", "2021-04-23", "2021-05-01",
                             "2021-05-12", "2021-05-13", "2021-05-14",
                             "2021-05-15", "2021-05-19", "2021-07-15",
                             "2021-07-19", "2021-07-20", "2021-07-21",
                             "2021-07-22", "2021-07-23", "2021-08-30",
                             "2021-10-28", "2021-10-29", "2021-12-31"
                             ]
        for d in national_holidays:
            if d == self.date:
                return 1
        return 0


def main():
    input_date = '2021-05-23'

    my_model = MLModel(date=input_date)
    result = my_model.predict()
    print(json.loads(json.dumps(result)))


if __name__ == '__main__':
    main()
