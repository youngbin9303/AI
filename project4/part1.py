import random
import math
import numpy as np
import matplotlib.pyplot as plt
paddle_height = 0.2
state = {
    'ball_x': 0.5,
    'ball_y': 0.5,
    'velocity_x': 0.03,
    'velocity_y': 0.01,
    'paddle_y': 0.5 - paddle_height/2,
}
actions = (0, 0.04, -0.04)
q_table = {}

def get_action(ball_x, ball_y, velocity_x, velocity_y, paddle_y):
    return random.randint(0,2)

def get_discrete(state):
    ball_x = int(round(state['ball_x']*12))
    ball_y = int(round(state['ball_y']*12))
    velocity_x = int(round(abs(state['velocity_x'])/state['velocity_x']))
    velocity_y = int(round(abs(state['velocity_y'])/state['velocity_y']))
    if state['velocity_y'] < 0.015:
        velocity_y = 0
    paddle_y = int(round(12*state['paddle_y'] / 0.8))
    if state['paddle_y'] == 0.8:
        paddle_y = 11
    discrete = (ball_x, ball_y, velocity_x, velocity_y, paddle_y)
    return discrete


hits2 = []
idx2= []
i = 0
while i < 200:
    end = False
    hit = 0
    while end == False:
        #last_discrete = get_discrete(state)

        a = get_action(state['ball_x'], state['ball_y'], state['velocity_x'], state['velocity_y'], state['paddle_y'])

        state['paddle_y'] += actions[a]
        if state['paddle_y'] < 0:
            state['paddle_y'] = 0
        if state['paddle_y'] + 0.2 >= 1:
            state['paddle_y'] = 0.8
        state['ball_x'] += state['velocity_x']
        state['ball_y'] += state['velocity_y']

        if state['ball_y'] < 0:
            state['ball_y'] = -state['ball_y']
            state['velocity_y'] = -state['velocity_y']
        elif state['ball_y'] > 1:
            state['ball_y'] = 2 - state['ball_y']
            state['velocity_y'] = -state['velocity_y']
        elif state['ball_x'] < 0:
            state['ball_x'] = -state['ball_x']
            state['velocity_x'] = -state['velocity_x']

        elif state['ball_x'] >= 1 and (state['ball_y'] > state['paddle_y']+paddle_height or state['ball_y'] < state['paddle_y']):
            end = True

        elif state['ball_x'] < 1:
            reward = 0
        else:
            #reward = 1
            hit += 1
            state['ball_x'] = 2 - state['ball_x']
            state['velocity_x'] = -state['velocity_x'] + random.uniform(-0.015,0.015)
            state['velocity_y'] = -state['velocity_y'] + random.uniform(-0.03,0.03)
            while abs(state['velocity_x']) <= 0.03 or abs(state['velocity_x']) >= 1:
                state['velocity_x'] = -state['velocity_x'] + random.uniform(-0.015,0.015)
            while abs(state['velocity_y']) >= 1:
                state['velocity_y'] = -state['velocity_y'] + random.uniform(-0.015,0.015)
        
    state = {
        'ball_x': 0.5,
        'ball_y': 0.5,
        'velocity_x': 0.03,
        'velocity_y': 0.01,
        'paddle_y': 0.5 - paddle_height/2,
    }
    hits2.append(hit)
    idx2.append(i)
    i+= 1

print(hits2)
print('testing avg = ', np.average(np.array(hits2)))