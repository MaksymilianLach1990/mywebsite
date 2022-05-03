import meteomatics.api as api
import datetime as dt
import pandas as pd

username = 'username'
password = 'password'
coordinates = [(52.520551,13.461804)] # Neris Les Bains France
model = 'mix'
startdate = dt.datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
enddate = startdate + dt.timedelta(days=2)
interval = dt.timedelta(hours=0.5)
parameters = ['t_2m:C', 'wind_speed_10m:kmh', 'wind_dir_10m:d', 'msl_pressure:Pa', 'precip_1h:mm', 'precip_24h:mm', 'uv:idx', 'sunrise:sql', 'sunset:sql']

wether = api.query_time_series(coordinates, startdate, enddate, interval, parameters, username, password, model=model)
limits = api.query_user_limits(username, password)
interval_time = []
time = startdate
for _ in wether['t_2m:C']:
    interval_time.append(f'{time}')
    time = time + dt.timedelta(hours=0.5)
# print(wether)
wether.insert(0, 'time', interval_time)
# print(wether)

numbers = wether.to_numpy()


# print(interval_time)

if __name__ == '__main__':

    print("Hello Wether")
