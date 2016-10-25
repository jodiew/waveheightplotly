"""
    Converts wave data csv file from NBDC into python dictionary.
"""
import csv
import requests

# wave data is currently only for neah bay buoy
CSV_URL = "http://sdf.ndbc.noaa.gov/sos/server.php?request=GetObservation&service=SOS&version=1.0.0&offering=urn:ioos:station:wmo:46087&observedproperty=Waves&responseformat=text/csv&eventtime=2016-10-01T00:00Z/2016-10-31T00:00Z"

def get_wave_dic():
    """ Returns list of dictionaries, one for every row in csv"""
    wave_list = []

    with requests.Session() as s:
        download = s.get(CSV_URL)

        decoded_content = download.content.decode('utf-8')

        wave_list = [row for row in csv.DictReader(decoded_content.splitlines(), skipinitialspace=True, delimiter=',')]

    return wave_list
