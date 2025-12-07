import random
import sys

# Status inicial
territorios = 3
soldados = 120
honra = 250
nivel = "Soldado"

# Ranking inicial
ranking = [
    {"nome": "Imperador das Sombras", "territorios": 12, "honra": 950},
    {"nome": "General de Ferro", "territorios": 8, "honra": 600},
    {"nome": "Senhora das Lâminas", "territorios": 5, "honra": 420},
    {"nome": "Capitão Errante", "territorios": 2, "honra": 150},
]

eventos = [
    "Um inimigo tentou invadir seus territórios!",
    "Espiões foram capturados e revelaram segredos.",
    "Refugiados se juntaram ao seu exército.",
    "Uma peste atingiu parte das tropas.",
    "Aliados enviaram reforços inesperados.",
    "Traidores sabotaram seus suprimentos."
]

def atualizar_nivel():
    global nivel, honra
    if honra < 200:
        nivel = "Soldado"
    elif honra < 400:
        nivel = "Capitão"
    elif honra < 700:
        nivel = "General"
    else:
        nivel = "Imperador"

def verificar_game_over():
    global soldados, territorios
    if soldados <= 0:
        print("\n💀 GAME OVER: Seu exército foi destruído!")
        sys.exit()
    if territorios <= 0:
        print("\n💀 GAME OVER: Você perdeu todos os territórios!")
        sys.exit()

def evento_aleatorio():
    evento = random.choice(eventos)
    print(f"\n⚠️ Evento: {evento}")
    global soldados, honra, territorios
    if "inimigo" in evento:
        if random.choice([True, False]):
            print("🛡️ Você defendeu com sucesso!")
            honra += 30
        else:
            print("❌ Você perdeu um território!")
            territorios -= 1
            honra -= 40
    elif "refugiados" in evento or "reforços" in evento:
        novos = random.randint(10, 40)
        soldados += novos
        print(f"👥 {novos} novos soldados se juntaram ao seu exército!")
    elif "peste" in evento or "sabotaram" in evento:
        perda = random.randint(10, 30)
        soldados -= perda
        honra -= 20
        print(f"💀 Você perdeu {perda} soldados.")
    elif "espiões" in evento:
        honra += 25
        print("🔎 Informações valiosas obtidas! Honra aumentada.")
    atualizar_nivel()
    verificar_game_over()
    atualizar_ranking()

def atacar():
    global territorios, honra
    resultado = random.choice(["vitória", "derrota"])
    if resultado == "vitória":
        territorios += 1
        honra += 50
        print("⚔️ Vitória! Você conquistou um novo território.")
    else:
        honra -= 20
        print("❌ Derrota! Seu exército recuou.")
    atualizar_nivel()
    verificar_game_over()
    evento_aleatorio()

def defender():
    global honra
    honra += 30
    print("🛡️ Defesa bem-sucedida! Você manteve seus territórios.")
    atualizar_nivel()
    verificar_game_over()
    evento_aleatorio()

def recrutar():
    global soldados
    novos = random.randint(10, 30)
    soldados += novos
    print(f"👥 Você recrutou {novos} novos soldados.")
    atualizar_nivel()
    verificar_game_over()
    evento_aleatorio()

def status():
    print("\n🎮 GUERRA!")
    print(f"🏰 Territórios: {territorios}")
    print(f"👥 Soldados: {soldados}")
    print(f"⭐ Honra: {honra}")
    print(f"📈 Nível: {nivel}")

def atualizar_ranking():
    global ranking, territorios, honra
    # Atualiza inimigos aleatoriamente
    for inimigo in ranking:
        inimigo["honra"] += random.randint(-30, 50)
        inimigo["territorios"] += random.choice([-1, 0, 1])
        if inimigo["honra"] < 0:
            inimigo["honra"] = 0
        if inimigo["territorios"] < 0:
            inimigo["territorios"] = 0
    # Adiciona o jogador ao ranking
    jogador = {"nome": "Você", "territorios": territorios, "honra": honra}
    todos = ranking + [jogador]
    # Ordena por honra
    todos = sorted(todos, key=lambda x: x["honra"], reverse=True)
    ranking = [r for r in todos if r["nome"] != "Você"]
    posicao = [i for i, r in enumerate(todos, 1) if r["nome"] == "Você"][0]
    print(f"\n📊 Sua posição no ranking: {posicao}º lugar")

def mostrar_ranking():
    atualizar_ranking()
    print("\n📊 RANKING GLOBAL")
    jogador = {"nome": "Você", "territorios": territorios, "honra": honra}
    todos = ranking + [jogador]
    todos = sorted(todos, key=lambda x: x["honra"], reverse=True)
    for i, r in enumerate(todos, 1):
        print(f"{i}º - {r['nome']} | Territórios: {r['territorios']} | Honra: {r['honra']}")

# Loop principal
print("🎮 Bem-vindo ao GUERRA! (1.0)")
while True:
    comando = input("\nDigite ATACAR, DEFENDER, RECRUTAR, STATUS ou RANKING: ").upper()
    if comando == "ATACAR":
        atacar()
    elif comando == "DEFENDER":
        defender()
    elif comando == "RECRUTAR":
        recrutar()
    elif comando == "STATUS":
        status()
    elif comando == "RANKING":
        mostrar_ranking()
    else:
        print("Comando inválido.")
