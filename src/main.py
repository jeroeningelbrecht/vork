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

        reply = {'fulfillmentText': """<speak>Oeps.
                                        Probeer nogmaals</speak>"""}

        # action
        action = result.get('action')
        if action == 'DefaultWelcomeIntent.name':
            name = result.get('parameters').get('person').get('name')
            reply = respond_to_name(name, session)

        elif action == 'input.welcome':
            reply = {'fulfillmentText': """<speak>
                        <par>
                            <media xml:id="rain" end="question.end+0.5s"
                                                                fadeOutDur="2s">
<audio
src="https://actions.google.com/sounds/v1/weather/rain_heavy_loud.ogg"
/>
                            </media>
                            <media end="question.end+0.2s">
<audio
src="https://actions.google.com/sounds/v1/weather/rolling_thunder.ogg"
/>
                            </media>
                            <media xml:id="intro" begin="0.5s">
                                <speak>Welkom bij kasteel Vork!</speak>
                            </media>
                            <media xml:id="thunder" begin="intro.end+0.2s">
<audio
src="https://actions.google.com/sounds/v1/weather/thunder_crack.ogg"
/>
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
                    'fulfillmentText': """
                    <speak> <par>
                        <media xml:id="move_to_room" end="describe_the_room.end">
                            <audio src="https://actions.google.com/sounds/v1/foley/walking_fast_on_dirt.ogg" />
                        </media>
                        <media xml:id="describe_the_room">
                            <speak>
                              <p><s>ok {}</s></p>
                              <p><s>Je betreedt {}</s></p>
                            </speak>
                        <media>
                    </par> </speak>
                    """
                    .format(name, next_room.str()),

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
                <media xml:id="rain" end="door.begin+5s" fadeOutDur="3s">
                    <audio src="https://actions.google.com/sounds/v1/weather/rain_heavy_loud.ogg"/>
                </media>
                <media xml:id="thunder">
                    <audio src="https://actions.google.com/sounds/v1/weather/rolling_thunder.ogg"/>
                </media>
                <media xml:id="voice">
                    <speak>
                        <p><s>Hallo {} <break time="750ms" /> ik ben zeer blij dat je er bent.</s></p>
                        <p><s>Ik ben prins Hans en ik heb hier in het
                                kasteel geleefd.</s></p>
                        <p><s>Moment, ik laat je binnen.</s></p>
                    </speak>
                </media>
                <media xml:id="door" begin="voice.end+0.5s">
                    <audio src="https://actions.google.com/sounds/v1/household/creaky_oven_door_open.ogg" clipEnd="7s"/>
                </media>
                <media xml:id="water running" begin="door.begin+0.5s" >
                    <audio src="https://actions.google.com/sounds/v1/water/water_leak.ogg" />
                </media>
                <media xml:id="explanation" begin="door.end+0.5s">
                    <speak>
                        <p><s>Alles ging goed hier in het kasteel totdat het drakenkristal gestolen werd!</s></p>
                        <p><s>Nu huizen er vreemde en soms gevaarlijke wezens in het kasteel en is het hier niet meer veilig voor ons</s></p>
                        <p><s>Het kristal bevindt zich ergens in het kasteel maar we weten niet waar</s></p>
                        <p><s>Nu staan we {}</s></p>
                        <p><s>Je kan je voortbewegen naar voor <break time="750ms" />
                                achter <break time="750ms" />
                                links en rechts</s></p>
                        <p><s>Zeg maar eens: ik wil naar voor om naar de volgende kamer te gaan</s></p>
                    </speak>
                </media>
            </par>
        </speak>"""
        .format(name, room_map.RoomMap.room(room_map.RoomMap.DARK_ALLEY_1).str()),

        'outputContexts': [
            {
                'name': "{}{}".format(session, CONTEXT_PATH),
                'lifespanCount': 99,
                'parameters': {
                    'data': {
                                'name': '{}'.format(name),
                                'current_room_id': room_map.RoomMap.DARK_ALLEY_1
                            }
                }
            }
        ]
    }

    return response
