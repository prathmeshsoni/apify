import json
import requests





def main():
    apifyapi = 'apify_api_RPbQ0UZkRYgtO2wSlZf5Qkv28JfEK10WXUEn'

    header = {
        'Authorization': f'Bearer {apifyapi}'
    }
    idd = get_actor(apifyapi, header)

    # idd = create_actor(apifyapi, header)
    # id = build_actor(apifyapi, header, idd[1])
    create_task(apifyapi, idd[1], idd[0])
    # run_actor(apifyapi)


# Gets the list of all actors
def get_actor(apify_api, headers):
    response = requests.get(
        f'https://api.apify.com/v2/acts?token={apify_api}',
        headers=headers
        )
    response_data = json.loads(response.text)
    actId_1 = response_data['data']['items'][-1]['id']
    name_1 = response_data['data']['items'][-1]['name']
    return name_1, actId_1


# run actor
def run_actor(apify_api):
    response = requests.get(
        f'https://api.apify.com/v2/actor-runs?token={apify_api}',
    )
    response_data = json.loads(response.text)
    runId = response_data['data']['items'][0]['id']
    response_ = requests.get(
        f'https://api.apify.com/v2/actor-runs/{runId}?token={apify_api}',
    )
    print(response_.text)
    print("run actor")


# Creates a new actor
def create_actor(apify_api, headers):
    response = requests.post(
        f'https://api.apify.com/v2/acts?token={apify_api}',
        headers=headers
        )
    response_data = json.loads(response.text)
    actId = response_data['data']['id']
    name = response_data['data']['name']
    return actId, name


# Builds an actor.
def build_actor(apify_api, headers, idd):
    response = requests.post(
        f'https://api.apify.com/v2/acts/{idd}/builds?token={apify_api}&version=0.0',
        headers=headers
        )
    response_1 = requests.get(
        f'https://api.apify.com/v2/acts/{idd}/builds?token={apify_api}&version=0.0',
        headers=headers
    )
    response_data = json.loads(response.text)
    actId = response_data['data']['actId']
    # name = response_data['data']['name']
    return actId


# Create a new task with settings specified
def create_task(apify_api, id, name):
    headers = {
        'Authorization': f'Bearer {apify_api}',
        'Content-Type': 'application/json',
    }
    json_data = {
        'actId': f'{id}',
        'name': f'{name}',
        'options': {
            'build': 'latest',
            'timeoutSecs': 300,
            'memoryMbytes': 128,
        },
        'input': {
            'demo': 'world',
        },
    }
    response = requests.post(
        f'https://api.apify.com/v2/actor-tasks?token={apify_api}',
        headers=headers,
        json=json_data
    )
    response_data = json.loads(response.text)
    actorTaskId = response_data['data']['id']
    response_ = requests.post(
        f'https://api.apify.com/v2/actor-tasks/{actorTaskId}/runs?token={apify_api}',
        headers={
            'Authorization': f'Bearer {apify_api}',
        }
    )
    print(response_.text)


# Creates a version of an actor
def create_version(apify_api, actId):
    headers = {
        'Authorization': f'Bearer {apify_api}',
        'Content-Type': 'application/json',
        'Location': f'https://api.apify.com/v2/acts/{actId}/versions/0.0'
    }
    response = requests.get(
        f'https://api.apify.com/v2/acts/{actId}/versions?token={apify_api}',
        headers=headers
    )
    print('')


#
# headers = {
#     'Content-Type': 'application/json',
# }
#
# json_data = {
#     'actId': f'{actId}',
#     'name': f'{name}',
#     'options': {
#         'build': 'latest',
#         'timeoutSecs': 300,
#         'memoryMbytes': 128,
#     },
#     'input': {
#         'hello': 'world',
#     },
# }
#
# response_3 = requests.post(f'https://api.apify.com/v2/actor-tasks?token={apify_api}', headers=headers, json=json_data)
# print(response_3.text)


if __name__ == '__main__':
    main()