import hug
import json
import datetime
from operator import itemgetter
from hug.middleware import CORSMiddleware

# Avoid CORS
api = hug.API(__name__)
api.http.add_middleware(CORSMiddleware(api))


# Return all down services
@hug.get('/currently_down_services')
def currently_down_services():
    with open('outages.json') as json_file:
        my_dict = json.load(json_file)

    down_services = []
    for key in my_dict:
        date_time_obj = datetime.datetime.strptime(key['startTime'], '%Y-%m-%d %H:%M:%S')
        minutes_added = datetime.timedelta(minutes=int(key['duration']))
        end_time = date_time_obj + minutes_added
        if end_time >= datetime.datetime.now() >= date_time_obj:
            end_time = end_time.strftime('%Y-%m-%d %H:%M:%S')
            outage_details = {"service_id": key['service_id'],
                              "duration": key['duration'],
                              "startTime": key['startTime'],
                              "endTime": end_time}
            down_services.append(outage_details)
    return down_services


# Return recently down services (which were down from 'hour' to current time)
@hug.get('/recently_down_services', examples='hours=3')
def recently_down_services(hours: hug.types.number):
    with open('outages.json') as json_file:
        my_dict = json.load(json_file)

    online_services = []
    for key in my_dict:
        date_time_obj = datetime.datetime.strptime(key["startTime"], '%Y-%m-%d %H:%M:%S')
        minutes_added = datetime.timedelta(minutes=int(key["duration"]))
        end_time = date_time_obj + minutes_added
        if datetime.datetime.now() > end_time > datetime.datetime.now() - datetime.timedelta(hours=hours):
            end_time = end_time.strftime('%Y-%m-%d %H:%M:%S')
            outage_details = {"service_id": key['service_id'],
                              "duration": key['duration'],
                              "startTime": key['startTime'],
                              "endTime": end_time}
            online_services.append(outage_details)
    return online_services


# Add new outage to json (Takes service_id, duration and start time)
@hug.post('/add_new_outage', examples='service_id=1&duration=2&startTime=2020-07-02 09:01:31')
def add_new_outage_for_service(body):
    service_id = int(body["service_id"])
    duration = int(body["duration"])
    startTime = body["startTime"]
    startTime = startTime.replace("T", " ")
    startTime = startTime + ":00"

    with open('outages.json') as json_file:
        my_dict = json.load(json_file)

    updated_json_file = []
    data_to_add = {"service_id": service_id, "duration": duration, "startTime": startTime}
    for key in my_dict:
        updated_json_file.append(key)
    updated_json_file.append(data_to_add)
    with open('outages.json', 'w') as write_data:
        json.dump(updated_json_file, write_data)
    return data_to_add


# Return all flapping scenarios from two hour timeframe
@hug.get('/flapping_scenarios')
def detect():
    with open('outages.json') as json_file:
        json_object = json.load(json_file)
    return detect_flapping_scenarios(json_object)


def detect_flapping_scenarios(json_object):
    detected_flapping_scenarios = []
    timeframe = 2
    json_object = sorted(json_object, key=itemgetter('service_id', 'startTime'))
    for key in range(0, len(json_object)):
        date_time_obj = datetime.datetime.strptime(json_object[key]['startTime'], '%Y-%m-%d %H:%M:%S')
        hours_added = datetime.timedelta(hours=timeframe)
        timeframe_end_time = date_time_obj + hours_added
        end_time = ""
        previous_end_time = date_time_obj
        sum_of_outages = 0
        amount_of_outages = 0
        for innerKey in range(key, len(json_object)):
            if int(json_object[innerKey]['service_id']) == int(json_object[key]['service_id']):
                start_time = datetime.datetime.strptime(json_object[innerKey]['startTime'],
                                                        '%Y-%m-%d %H:%M:%S')
                if start_time < timeframe_end_time:
                    end_time = start_time + datetime.timedelta(minutes=int(json_object[innerKey]['duration']))
                    if end_time > timeframe_end_time:
                        matched_minutes = (
                                                      timeframe_end_time.hour * 60 + timeframe_end_time.minute + timeframe_end_time.second / 60) \
                                          - (start_time.hour * 60 + start_time.minute + start_time.second / 60)
                        end_time = timeframe_end_time
                        sum_of_outages += int(matched_minutes)
                        amount_of_outages += 1
                    else:
                        if previous_end_time > end_time:
                            amount_of_outages += 1
                        elif previous_end_time > start_time:
                            matched_minutes = (end_time.hour * 60 + end_time.minute + end_time.second / 60) \
                                              - (
                                                          previous_end_time.hour * 60 + previous_end_time.minute + previous_end_time.second / 60)
                            if matched_minutes > 0:
                                sum_of_outages += int(matched_minutes)
                            amount_of_outages += 1
                        else:
                            sum_of_outages += int(json_object[innerKey]['duration'])
                            amount_of_outages += 1
                        if previous_end_time < end_time:
                            previous_end_time = end_time
                else:
                    break
            else:
                break
        if sum_of_outages >= 15:
            end_time = end_time.strftime('%Y-%m-%d %H:%M:%S')
            data_to_add = {"service_id": json_object[key]['service_id'],
                           "duration": json_object[key]['duration'],
                           "startTime": json_object[key]['startTime'],
                           "endTime": end_time,
                           "amountOfOutages": amount_of_outages,
                           "sumOfOutages": sum_of_outages}
            detected_flapping_scenarios.append(data_to_add)
    return detected_flapping_scenarios
