# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

import random

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    # Inicializar las variables y patrones
    counter_move = {"R": "P", "P": "S", "S": "R"}

    # Estrategia de predicción basada en patrones
    def predict_move(history, length=3):
        if len(history) < length:
            return random.choice(["R", "P", "S"])
        
        patterns = {}
        for i in range(len(history) - length):
            pattern = tuple(history[i:i + length])
            next_move = history[i + length]
            if pattern not in patterns:
                patterns[pattern] = [0, 0, 0]
            patterns[pattern][{"R": 0, "P": 1, "S": 2}[next_move]] += 1
        
        last_pattern = tuple(history[-length:])
        if last_pattern in patterns:
            prediction = max(range(3), key=lambda x: patterns[last_pattern][x])
            return ["R", "P", "S"][prediction]
        else:
            return random.choice(["R", "P", "S"])
    
    # Elegir la longitud del patrón basado en el historial
    if len(opponent_history) > 3:
        prediction = predict_move(opponent_history, length=3)
    elif len(opponent_history) > 2:
        prediction = predict_move(opponent_history, length=2)
    else:
        prediction = random.choice(["R", "P", "S"])

    return counter_move[prediction]



