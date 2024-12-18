from collections import defaultdict
import re

# Função que processa os resultados do jogo
def parse_game_result(line):
    pattern = r"(.+)#(\d+)@(\d+)#(.+)"
    match = re.match(pattern, line)
    team1 = match.group(1)
    goals1 = int(match.group(2))
    goals2 = int(match.group(3))
    team2 = match.group(4)
    return team1, goals1, goals2, team2

def main():
    input_data = []
    
    #Quantidade de torneios
    n = int(input())
    
    for _ in range(n):
        tournament_name = input()
        input_data.append(tournament_name)
        
        #Quantidade de times
        T = int(input())
        input_data.append(str(T))
        
        #Adiciona os times
        for _ in range(T):
            team_name = input()
            input_data.append(team_name)
        
        #Quantidade de jogos
        G = int(input())
        input_data.append(str(G))
        
        #Adiciona os resultados dos jogos
        for _ in range(G):
            game_result = input()
            input_data.append(game_result)

    idx = 0
    output = []
    
    #Processa os torneios
    for _ in range(n):
        tournament_name = input_data[idx]

        #Adiciona o nome do torneio
        output.append(tournament_name)
        idx += 1
        
        #Adiciona a quantidade de times
        T = int(input_data[idx])
        idx += 1

        #Armazena os dados dos times
        teams = {}
        for _ in range(T):
            team_name = input_data[idx]
            teams[team_name] = {
                "points": 0, "games": 0, "wins": 0, "ties": 0, "losses": 0,
                "goals_scored": 0, "goals_against": 0
            }
            idx += 1

        #Adiciona a quantidade de jogos
        G = int(input_data[idx])
        idx += 1

        #Processa os resultados dos jogos
        for _ in range(G):
            game_line = input_data[idx]
            team1, goals1, goals2, team2 = parse_game_result(game_line)
            idx += 1

            #Atualiza os dados dos times
            teams[team1]["games"] += 1
            teams[team2]["games"] += 1

            teams[team1]["goals_scored"] += goals1
            teams[team1]["goals_against"] += goals2
            teams[team2]["goals_scored"] += goals2
            teams[team2]["goals_against"] += goals1

            #Atualiza os pontos dos times
            if goals1 > goals2:
                teams[team1]["points"] += 3
                teams[team1]["wins"] += 1
                teams[team2]["losses"] += 1
            elif goals2 > goals1:
                teams[team2]["points"] += 3
                teams[team2]["wins"] += 1
                teams[team1]["losses"] += 1
            else:
                teams[team1]["points"] += 1
                teams[team2]["points"] += 1
                teams[team1]["ties"] += 1
                teams[team2]["ties"] += 1

        #Ordena os times
        sorted_teams = sorted(
            teams.items(),
            key=lambda item: (
                -item[1]["points"],
                -item[1]["wins"],
                -(item[1]["goals_scored"] - item[1]["goals_against"]),
                -item[1]["goals_scored"],
                item[1]["games"],
                item[0].lower()
            )
        )

        #Adiciona os times
        for rank, (team_name, stats) in enumerate(sorted_teams, start=1):
            gd = stats["goals_scored"] - stats["goals_against"]
            line = (
                f"{rank}) {team_name} {stats['points']}p, {stats['games']}g "
                f"({stats['wins']}-{stats['ties']}-{stats['losses']}), "
                f"{gd}gd ({stats['goals_scored']}-{stats['goals_against']})"
            )
            output.append(line)
        output.append("")

    print("\n".join(output).strip())

main()
