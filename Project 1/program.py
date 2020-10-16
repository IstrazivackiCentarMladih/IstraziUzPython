'''
    File name: program.py
    Author: Istrazivacki centar mladih
    Date created: 16.10.2020
    Date last modified: 16.10.2020
    Python Version: 2.7
    Description:
        Program obtains weather data from yr.no API by using https://api.met.no/weatherapi/locationforecast/2.0/documentation#/.
        When running the program one must follow yr.no terms of service https://hjelp.yr.no/hc/en-us/articles/360001946134-Data-access-and-terms-of-service
'''

import requests
import pandas as pd
import matplotlib.pyplot as plt

def obtain_weather_data(lat, lon, altitude=None):
    forecast_json = get_complete_forecast_json(lat, lon, altitude)
    df_forecast = transform_weather_data_to_dataframe(forecast_json)
    return df_forecast

def get_complete_forecast_json(lat, lon, altitude=None):
    uri = f"https://api.met.no/weatherapi/locationforecast/2.0/complete?lat={lat}&lon={lon}"
    if altitude:
        uri = uri + f"&altitude={altitude}"
    return requests.get(uri).json()

def transform_weather_data_to_dataframe(forecast_json):
    ts = forecast_json['properties']['timeseries']
    data_dict = {'time':[]}

    data_columns = [
        "air_pressure_at_sea_level", "air_temperature",
        "cloud_area_fraction","cloud_area_fraction_high","cloud_area_fraction_low","cloud_area_fraction_medium",
        "dew_point_temperature","fog_area_fraction","relative_humidity","ultraviolet_index_clear_sky",
        "wind_from_direction", "wind_speed"]

    for column in data_columns:
        data_dict[column] = []
    
    for t in ts:
        data_dict['time'].append(t['time'])
        details = t['data']['instant']['details']
        for column in data_columns:
            curr_value = details[column] if column in details else None
            data_dict[column].append(curr_value)
    df= pd.DataFrame(data_dict)
    df['time'] = df['time'].apply(pd.to_datetime)
    return df

def plot_temperature_forecast(weather_forecast):
    weather_forecast.plot('time', 'air_temperature')
    plt.xlabel('Time')
    plt.ylabel('Air temperature')
    plt.title('Air temperature forecast')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    weather_forecast = obtain_weather_data(lat=53.270050, lon=-6.204731)
    weather_forecast.to_csv('weather_data.csv')
    plot_temperature_forecast(weather_forecast)

