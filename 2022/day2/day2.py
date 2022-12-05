import pandas as pd
import numpy as np

# Part 1
inputs = pd.read_csv('input.txt', header=None, delimiter=' ', names=['opponent', 'response'])
response_conditions = [
    inputs['response'].eq('X'),
    inputs['response'].eq('Y'),
    inputs['response'].eq('Z')
]
response_scores = [1, 2, 3]
inputs['base_score'] = np.select(response_conditions, response_scores, default=0)
game_condition = [
    inputs['response'].eq('X') & inputs['opponent'].eq('A'),
    inputs['response'].eq('X') & inputs['opponent'].eq('B'),
    inputs['response'].eq('X') & inputs['opponent'].eq('C'),
    inputs['response'].eq('Y') & inputs['opponent'].eq('A'),
    inputs['response'].eq('Y') & inputs['opponent'].eq('B'),
    inputs['response'].eq('Y') & inputs['opponent'].eq('C'),
    inputs['response'].eq('Z') & inputs['opponent'].eq('A'),
    inputs['response'].eq('Z') & inputs['opponent'].eq('B'),
    inputs['response'].eq('Z') & inputs['opponent'].eq('C'),
]
game_score = [3, 0, 6, 6, 3, 0, 0, 6, 3]
inputs['game_score'] = np.select(game_condition, game_score, default=0)
inputs['total_score'] = inputs['base_score'] + inputs['game_score']
print(inputs['total_score'].sum())

# Part 2
inputs = pd.read_csv('input.txt', header=None, delimiter=' ', names=['opponent', 'results'])
response_conditions = [
    inputs['results'].eq('X'),
    inputs['results'].eq('Y'),
    inputs['results'].eq('Z')
]
response_scores = [0, 3, 6]
inputs['base_score'] = np.select(response_conditions, response_scores, default=0)
game_condition = [
    inputs['results'].eq('X') & inputs['opponent'].eq('A'),
    inputs['results'].eq('X') & inputs['opponent'].eq('B'),
    inputs['results'].eq('X') & inputs['opponent'].eq('C'),
    inputs['results'].eq('Y') & inputs['opponent'].eq('A'),
    inputs['results'].eq('Y') & inputs['opponent'].eq('B'),
    inputs['results'].eq('Y') & inputs['opponent'].eq('C'),
    inputs['results'].eq('Z') & inputs['opponent'].eq('A'),
    inputs['results'].eq('Z') & inputs['opponent'].eq('B'),
    inputs['results'].eq('Z') & inputs['opponent'].eq('C'),
]
game_score = [3, 1, 2, 1, 2, 3, 2, 3, 1]
inputs['game_score'] = np.select(game_condition, game_score, default=0)
inputs['total_score'] = inputs['base_score'] + inputs['game_score']
print(inputs['total_score'].sum())

