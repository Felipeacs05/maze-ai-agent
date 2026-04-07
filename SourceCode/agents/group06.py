import heapq
from move import Move

class Group06:
    #Medir o labirinto
    def __init__(self, maze, prize_positions, agent_position, opponent_position, max_turns):
        self.rows = len(maze)
        self.cols = len(maze[0])

    #Heurística: Distância de Manhattan
    def get_manhattan_dist(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


    def a_star(self, current_maze, start, goal):
        #Se ja ta em cima do prêmio, não precisa se mover
        if start == goal:
            return 0, Move.STAY

        # frontier: (f, g, current_pos, first_move_index)
        # Uso de índice do movimento para evitar erro de comparação de Enums
        
        # Mapemento de movimentos e seus deltas correspondentes
        moves_list = [Move.UP, Move.DOWN, Move.LEFT, Move.RIGHT]
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        frontier = []
        for i, move in enumerate(moves_list):
            dr, dc = deltas[i]
            r, c = start[0] + dr, start[1] + dc
            if 0 <= r < self.rows and 0 <= c < self.cols and current_maze[r][c] != '#':
                g = 1
                h = self.get_manhattan_dist((r, c), goal)
                heapq.heappush(frontier, (g + h, g, (r, c), i))

        visited = {start}
        
        while frontier:
            f, g, current, move_idx = heapq.heappop(frontier)

            if current == goal:
                return g, moves_list[move_idx]

            if current in visited:
                continue
            visited.add(current)

            for dr, dc in deltas:
                nr, nc = current[0] + dr, current[1] + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols and current_maze[nr][nc] != '#' and (nr, nc) not in visited:
                    new_g = g + 1
                    h = self.get_manhattan_dist((nr, nc), goal)
                    heapq.heappush(frontier, (new_g + h, new_g, (nr, nc), move_idx))

        return float('inf'), Move.STAY

    def next_move(self, maze, prize_positions, agent_position, opponent_position):
        if not prize_positions:
            return Move.STAY

        max_utility = -float('inf')
        best_move = Move.STAY

        # Ordenar prêmios por valor para processar os melhores primeiro
        sorted_prizes = sorted(prize_positions.items(), key=lambda x: x[1], reverse=True)

        for pos, value in sorted_prizes:
            my_dist, move_to_prize = self.a_star(maze, agent_position, pos)
            
            if my_dist == float('inf'):
                continue

            opp_dist = self.get_manhattan_dist(opponent_position, pos)
            
            # Utilidade melhorada
            utility = value / (my_dist + 0.1)
            
            # Se o oponente estiver mais perto de um prêmio muito valioso, ainda tentamos se estivermos perto
            if opp_dist < my_dist:
                utility *= 0.1 

            if utility > max_utility:
                max_utility = utility
                best_move = move_to_prize

        # Caso de segurança: se a utilidade falhou mas há prêmios, tenta ir ao mais próximoo
        if best_move == Move.STAY and prize_positions:
            closest_prize = min(prize_positions.keys(), key=lambda p: self.get_manhattan_dist(agent_position, p))
            _, best_move = self.a_star(maze, agent_position, closest_prize)

        return best_move