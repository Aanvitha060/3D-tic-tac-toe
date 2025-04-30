from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

# Initialize the 4x4x4 board
board = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)]

def check_winner():
    lines = []
    for x in range(4):
        for y in range(4):
            lines.append([board[x][y][z] for z in range(4)])
    for x in range(4):
        for z in range(4):
            lines.append([board[x][y][z] for y in range(4)])
    for y in range(4):
        for z in range(4):
            lines.append([board[x][y][z] for x in range(4)])
    for z in range(4):
        lines.append([board[i][i][z] for i in range(4)])
        lines.append([board[i][3 - i][z] for i in range(4)])
    for y in range(4):
        lines.append([board[i][y][i] for i in range(4)])
        lines.append([board[i][y][3 - i] for i in range(4)])
    for x in range(4):
        lines.append([board[x][i][i] for i in range(4)])
        lines.append([board[x][i][3 - i] for i in range(4)])
    lines.append([board[i][i][i] for i in range(4)])
    lines.append([board[i][i][3 - i] for i in range(4)])
    lines.append([board[i][3 - i][i] for i in range(4)])
    lines.append([board[3 - i][i][i] for i in range(4)])
    for line in lines:
        if all(cell == 1 for cell in line):
            return 1
        if all(cell == 2 for cell in line):
            return 2
    return 0

def minimax(board_state, depth, maximizing_player, alpha, beta):
    winner = check_winner()
    if winner == 1:
        return -10
    if winner == 2:
        return 10
    if depth == 0 or all(board_state[x][y][z] != 0 for x in range(4) for y in range(4) for z in range(4)):
        return 0
    if maximizing_player:
        max_eval = -float('inf')
        for x in range(4):
            for y in range(4):
                for z in range(4):
                    if board_state[x][y][z] == 0:
                        board_state[x][y][z] = 2
                        eval = minimax(board_state, depth - 1, False, alpha, beta)
                        board_state[x][y][z] = 0
                        max_eval = max(max_eval, eval)
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            return max_eval
        return max_eval
    else:
        min_eval = float('inf')
        for x in range(4):
            for y in range(4):
                for z in range(4):
                    if board_state[x][y][z] == 0:
                        board_state[x][y][z] = 1
                        eval = minimax(board_state, depth - 1, True, alpha, beta)
                        board_state[x][y][z] = 0
                        min_eval = min(min_eval, eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            return min_eval
        return min_eval

def find_best_move(difficulty):
    best_score = -float('inf')
    best_move = None
    depth_limit = {1: 1, 2: 2, 3: 3}.get(difficulty, 2)
    for x in range(4):
        for y in range(4):
            for z in range(4):
                if board[x][y][z] == 0:
                    board[x][y][z] = 2
                    score = minimax(board, depth_limit, False, -float('inf'), float('inf'))
                    board[x][y][z] = 0
                    if score > best_score:
                        best_score = score
                        best_move = (x, y, z)
    return best_move

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move():
    global board
    data = request.get_json()
    x, y, z, player = data['x'], data['y'], data['z'], data['player']
    difficulty = data.get('difficulty', 2)

    if board[x][y][z] != 0:
        return jsonify({'error': 'Invalid move'}), 400

    board[x][y][z] = player
    winner = check_winner()
    if winner:
        board = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)]
        return jsonify({'winner': winner})

    if all(board[x][y][z] != 0 for x in range(4) for y in range(4) for z in range(4)):
        board = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)]
        return jsonify({'winner': 0})  # Draw

    ai_move = find_best_move(difficulty)
    if ai_move:
        board[ai_move[0]][ai_move[1]][ai_move[2]] = 2

    winner = check_winner()
    if winner:
        board = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)]
    return jsonify({'ai_move': ai_move, 'winner': winner})

if __name__ == '__main__':
    app.run(debug=True)
