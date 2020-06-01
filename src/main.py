from flask import jsonify
# import interactive_objects
from rooms import room_map

CONTEXT_PATH = '/contexts/_actions_on_google'


def webhook(request):
    try:
        req = request.get_json(force=True)
        print('REQUEST: {}'.format(req))

        result = req.get('queryResult')
        session = req.get('session')

        reply = {'fulfillmentText': """<speak>Oeps. Probeer nogmaals</speak>"""}

        # action
        action = result.get('action')
        if action == 'DefaultWelcomeIntent.name':
            name = result.get('parameters').get('person').get('name')
            reply = respond_to_name(name, session)

        elif action == 'input.welcome':
            reply = {'fulfillmentText': """<speak>
                        <par>
                            <media xml:id="rain" end="question.end+0.5s" fadeOutDur="2s">
                                <audio src="https://actions.google.com/sounds/v1/weather/rain_heavy_loud.ogg" />
                            </media>
                            <media end="question.end+0.2s">
                                <audio src="https://actions.google.com/sounds/v1/weather/rolling_thunder.ogg" />
                            </media>
                            <media xml:id="intro" begin="0.5s">
                                <speak>Welkom bij kasteel Vork!</speak>
                            </media>
                            <media xml:id="thunder" begin="intro.end+0.2s">
                                <audio src="https://actions.google.com/sounds/v1/weather/thunder_crack.ogg" />
                            </media>
                            <media xml:id="question" begin="thunder.end+0.5s">
                                <speak>Wat is jouw naam?</speak>
                            </media>
                        </par>
                    </speak>"""}

        elif action == 'direction_handling':
            session_data_context = list(
                filter(
                      lambda outputContext: outputContext['name'] == '{}{}'
                      .format(session, CONTEXT_PATH),
                      result['outputContexts'])
                    )[0]
            session_data = session_data_context['parameters']['data']
            direction = result.get('parameters').get('direction')
            reply = respond_to_direction(direction, session, session_data)

        print('RESPONSE: {}'.format(reply))
        jsonResponse = jsonify(reply)
        return jsonResponse

    except Exception as exc:
        print('{0}'.format(exc))


def respond_to_direction(direction, session, session_data):
    name = session_data['name']
    current_room_id = session_data['current_room_id']
    next_id = room_map.RoomMap.next_room_id(direction, current_room_id)
    next_room = room_map.RoomMap.room(next_id)

    response = {
                    'fulfillmentText': """ok {}, jij wil naar {}. Veel succes!
                    Je gaat naar {}"""
                    .format(name, direction, next_room.str()),

                    'outputContexts': [
                        {
                            'name': "{}{}".format(session, CONTEXT_PATH),
                            'lifespanCount': 99,
                            'parameters': {
                                'data': {
                                    'name': '{}'.format(name),
                                    'current_room_id': '{}'.format(next_id)
                                }
                            }
                        }
                    ]
                }
    return response


def respond_to_name(name, session):
    response = {
        'fulfillmentText': """<speak>
            <par>
                <media xml:id="rain">
                    <audio src="https://actions.google.com/sounds/v1/weather/rain_heavy_loud.ogg" />
                </media>
                <media>
                    <audio src="https://actions.google.com/sounds/v1/weather/rolling_thunder.ogg" />
                </media>
                <media>
                    <speak><s>Hallo {}, ik ben zeer blij dat je er bent.</s></speak>
                </media>
            </par>
        </speak>"""
        .format(name),

        'outputContexts': [
            {
                'name': "{}{}".format(session, CONTEXT_PATH),
                'lifespanCount': 99,
                'parameters': {
                    'data': {
                                'name': '{}'.format(name),
                                'current_room_id': room_map.RoomMap.BIG_HALLWAY
                            }
                }
            }
        ]
    }

    return response
