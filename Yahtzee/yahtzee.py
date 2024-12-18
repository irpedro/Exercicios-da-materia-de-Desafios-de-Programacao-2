# Pedro Gabriel Ruiz - 13875571
# Matheus Silva Lopes da Costa - 12674680
# Mateus Caetano da Silva - 12543989

from collections import Counter

# Funções para calcular as pontuações em cada categoria
def score_upper(dice, number):
    return dice.count(number) * number

def score_three_of_a_kind(dice):
    counts = Counter(dice)
    for value, count in counts.items():
        if count >= 3:
            return sum(dice)
    return 0

def score_four_of_a_kind(dice):
    counts = Counter(dice)
    for value, count in counts.items():
        if count >= 4:
            return sum(dice)
    return 0

def score_full_house(dice):
    counts = Counter(dice)
    if sorted(counts.values()) == [2, 3]:
        if max(set(dice), key=dice.count) == 6:
            return 0
        return 40
    return 0

def score_small_straight(dice):
    unique_dice = sorted(set(dice))
    straights = [{1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6}]
    for straight in straights:
        if straight.issubset(unique_dice):
            return 25
    return 0

def score_large_straight(dice):
    unique_dice = sorted(set(dice))
    if unique_dice == [1, 2, 3, 4, 5] or unique_dice == [2, 3, 4, 5, 6]:
        return 35
    return 0

def score_yahtzee(dice):
    if len(set(dice)) == 1:
        return 50
    return 0

def score_chance(dice):
    
    if max(set(dice), key=dice.count) == 1:
        return 0
    return sum(dice)

# Função que calcula a pontuação para todas as categorias
def calculate_scores(dice):
    scores = {}
    # Upper section (1 to 6)
    for i in range(1, 7):
        scores[f"Upper {i}"] = score_upper(dice, i)
    
    # Lower section
    scores["Yahtzee"] = score_yahtzee(dice)
    scores["Full House"] = score_full_house(dice)
    scores["Large Straight"] = score_large_straight(dice)
    scores["Three of a Kind"] = score_three_of_a_kind(dice)
    scores["Four of a Kind"] = score_four_of_a_kind(dice)
    scores["Small Straight"] = score_small_straight(dice)
    scores["Chance"] = score_chance(dice)
    
    return scores

# Função que simula o jogo completo com a regra do bônus
def play_yahtzee():
    used_categories = set()  # Conjunto de categorias já usadas
    total_score = 0
    upper_section_score = 0
    category_scores = {
        "Ones": 0,
        "Twos": 0,
        "Threes": 0,
        "Fours": 0,
        "Fives": 0,
        "Sixes": 0,
        "Chance": 0,
        "Three of a Kind": 0,
        "Four of a Kind": 0,
        "Yahtzee": 0,
        "Short Straight": 0,
        "Long Straight": 0,
        "Full House": 0
    }
    
    # Mapeamento das categorias para a ordem desejada
    category_mapping = {
        "Upper 1": "Ones",
        "Upper 2": "Twos",
        "Upper 3": "Threes",
        "Upper 4": "Fours",
        "Upper 5": "Fives",
        "Upper 6": "Sixes",
        "Chance": "Chance",
        "Three of a Kind": "Three of a Kind",
        "Four of a Kind": "Four of a Kind",
        "Yahtzee": "Yahtzee",
        "Small Straight": "Short Straight",
        "Large Straight": "Long Straight",
        "Full House": "Full House"
    }

    for round_number in range(13):  # 13 rodadas no jogo
        # Lê os dados da entrada do usuário
        dice_roll = list(map(int, input().split()))
        
        # Garantir que são exatamente 5 números e que estão no intervalo de 1 a 6
        if len(dice_roll) != 5 or any(d < 1 or d > 6 for d in dice_roll):
            print("Entrada inválida! Por favor insira 5 números entre 1 e 6.")
            return
        
        available_scores = calculate_scores(dice_roll)
        available_scores = {k: v for k, v in available_scores.items() if k not in used_categories}
        
        # Escolher a melhor pontuação disponível
        best_category = max(available_scores, key=available_scores.get)
        best_score = available_scores[best_category]
        
        # Marcar a categoria como usada
        used_categories.add(best_category)
        total_score += best_score
        
        # Atualizar a pontuação na categoria correspondente
        mapped_category = category_mapping[best_category]
        category_scores[mapped_category] = best_score
        
        # Se for uma categoria da parte superior (Upper Section: 1 a 6), acumular pontuação
        if "Upper" in best_category:
            upper_section_score += best_score
    
    # Gambiarra para lidar com a categoria "Chance" (se não foi escolhida, soma-se todos os dados)
    if category_scores['Chance'] == 0:
        score = 1+2+3+4+5
        total_score += score
        mapped_category = category_mapping["Chance"]
        category_scores[mapped_category] = score

    # Verificar se o jogador ganhou o bônus (63 ou mais na seção superior)
    bonus = 35 if upper_section_score >= 63 else 0
    total_score += bonus
    
    # Adicionar o total à lista de categorias
    category_scores["Total"] = total_score
    
    # Gerar a saída na ordem especificada
    output = [
        category_scores['Ones'], category_scores['Twos'], category_scores['Threes'], category_scores['Fours'], 
        category_scores['Fives'], category_scores['Sixes'], category_scores['Chance'], 
        category_scores['Three of a Kind'], category_scores['Four of a Kind'], category_scores['Yahtzee'], 
        category_scores['Short Straight'], category_scores['Long Straight'], category_scores['Full House'], 
        bonus, category_scores['Total']
    ]
    
    # Exibir o resultado final
    print(" ".join(map(str, output)))

for i in range(2):
    # Executa o jogo, lendo entrada diretamente do usuário
    play_yahtzee()
