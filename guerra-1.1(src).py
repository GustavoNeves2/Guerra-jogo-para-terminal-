import random

# --- Utilidades de entrada ---
def norm(s):
    return (s or "").strip().lower()

def escolher(opcoes, prompt, aliases=None):
    """
    opcoes: dict chave -> valor
    aliases: dict alias -> chave
    Retorna o valor escolhido, validando até acertar.
    """
    while True:
        escolha = norm(input(prompt))
        if not escolha:
            print("➡ Digite uma opção válida.")
            continue
        if escolha in opcoes:
            return opcoes[escolha]
        if aliases and escolha in aliases and aliases[escolha] in opcoes:
            return opcoes[aliases[escolha]]
        print("❌ Opção inválida. Tente novamente.")

# --- Idiomas e prompts ---
IDIOMAS = {
    "pt": {
        "welcome": "🎮 Bem-vindo ao GUERRA 1.1!",
        "ask_name": "Digite seu nome de guerreiro: ",
        "mode_prompt": "Escolha o modo de jogo:\n1 - Clássico (infinito)\n2 - Campanha (fases com objetivos)\n>> ",
        "diff_prompt": "🎚 Escolha a dificuldade:\n1 - Amador\n2 - Veterano\n3 - Experiente\n>> ",
        "stats_header": "=========================",
        "territories": "🏰 Territórios",
        "soldiers": "👥 Soldados",
        "honor": "⭐ Honra",
        "gold": "💰 Ouro",
        "phase": "📜 Fase da campanha",
        "cmd_prompt": "Digite um comando (1-ATACAR, 2-RECRUTAR, 3-STATUS, 4-RANKING, 5-AJUDA, 6-SAIR): ",
        "victory": "⚔ Vitória! Você conquistou um novo território.",
        "defeat": "❌ Derrota! Você perdeu soldados e recursos.",
        "no_soldiers": "❌ Você não tem soldados para atacar!",
        "recruit_ok": "👥 Você recrutou 10 soldados por 10 de ouro.",
        "recruit_fail": "💰 Ouro insuficiente para recrutar.",
        "status": "📊 Status de {nome}: {t} territórios, {s} soldados, {h} honra, {o} ouro.",
        "help": "📖 Comandos: 1-ATACAR, 2-RECRUTAR, 3-STATUS, 4-RANKING, 5-AJUDA, 6-SAIR",
        "bye": "👋 Jogo encerrado. Resultado salvo.",
        "phase_done": "📜 Fase {f} concluída! Avance para a próxima região.",
        "ranking_title": "🏆 Ranking dos Guerreiros:",
        "ranking_none": "📂 Nenhum ranking disponível ainda.",
        "game_over": "💀 GAME OVER 💀\n📜 Fim da campanha. Seu exército foi dizimado...",
    },
    "en": {
        "welcome": "🎮 Welcome to WAR 1.1!",
        "ask_name": "Enter your warrior name: ",
        "mode_prompt": "Choose the game mode:\n1 - Classic (endless)\n2 - Campaign (objective-based)\n>> ",
        "diff_prompt": "🎚 Choose difficulty:\n1 - Amateur\n2 - Veteran\n3 - Expert\n>> ",
        "stats_header": "=========================",
        "territories": "🏰 Territories",
        "soldiers": "👥 Soldiers",
        "honor": "⭐ Honor",
        "gold": "💰 Gold",
        "phase": "📜 Campaign phase",
        "cmd_prompt": "Enter a command (1-ATTACK, 2-RECRUIT, 3-STATUS, 4-RANKING, 5-HELP, 6-EXIT): ",
        "victory": "⚔ Victory! You conquered a new territory.",
        "defeat": "❌ Defeat! You lost soldiers and resources.",
        "no_soldiers": "❌ You have no soldiers to attack!",
        "recruit_ok": "👥 You recruited 10 soldiers for 10 gold.",
        "recruit_fail": "💰 Not enough gold to recruit.",
        "status": "📊 {nome}'s status: {t} territories, {s} soldiers, {h} honor, {o} gold.",
        "help": "📖 Commands: 1-ATTACK, 2-RECRUIT, 3-STATUS, 4-RANKING, 5-HELP, 6-EXIT",
        "bye": "👋 Game closed. Result saved.",
        "phase_done": "📜 Phase {f} completed! Proceed to the next region.",
        "ranking_title": "🏆 Warriors Ranking:",
        "ranking_none": "📂 No ranking available yet.",
        "game_over": "💀 GAME OVER 💀\n📜 End of campaign. Your army was wiped out...",
    },
    "es": {
        "welcome": "🎮 ¡Bienvenido a GUERRA 1.1!",
        "ask_name": "Escribe tu nombre de guerrero: ",
        "mode_prompt": "Elige el modo de juego:\n1 - Clásico (infinito)\n2 - Campaña (por objetivos)\n>> ",
        "diff_prompt": "🎚 Elige la dificultad:\n1 - Amateur\n2 - Veterano\n3 - Experto\n>> ",
        "stats_header": "=========================",
        "territories": "🏰 Territorios",
        "soldiers": "👥 Soldados",
        "honor": "⭐ Honor",
        "gold": "💰 Oro",
        "phase": "📜 Fase de la campaña",
        "cmd_prompt": "Escribe un comando (1-ATACAR, 2-RECLUTAR, 3-ESTADO, 4-CLASIFICACIÓN, 5-AYUDA, 6-SALIR): ",
        "victory": "⚔ ¡Victoria! Conquistaste un nuevo territorio.",
        "defeat": "❌ ¡Derrota! Perdiste soldados y recursos.",
        "no_soldiers": "❌ ¡No tienes soldados para atacar!",
        "recruit_ok": "👥 Reclutaste 10 soldados por 10 de oro.",
        "recruit_fail": "💰 Oro insuficiente para reclutar.",
        "status": "📊 Estado de {nome}: {t} territorios, {s} soldados, {h} honor, {o} oro.",
        "help": "📖 Comandos: 1-ATACAR, 2-RECLUTAR, 3-ESTADO, 4-CLASIFICACIÓN, 5-AYUDA, 6-SALIR",
        "bye": "👋 Juego cerrado. Resultado guardado.",
        "phase_done": "📜 ¡Fase {f} completada! Avanza a la siguiente región.",
        "ranking_title": "🏆 Clasificación de Guerreros:",
        "ranking_none": "📂 Aún no hay clasificación disponible.",
        "game_over": "💀 GAME OVER 💀\n📜 Fin de campaña. Tu ejército fue aniquilado...",
    },
    "fr": {
        "welcome": "🎮 Bienvenue à GUERRE 1.1!",
        "ask_name": "Entrez votre nom de guerrier: ",
        "mode_prompt": "Choisissez le mode de jeu:\n1 - Classique (infini)\n2 - Campagne (à objectifs)\n>> ",
        "diff_prompt": "🎚 Choisissez la difficulté:\n1 - Amateur\n2 - Vétéran\n3 - Expérimenté\n>> ",
        "stats_header": "=========================",
        "territories": "🏰 Territoires",
        "soldiers": "👥 Soldats",
        "honor": "⭐ Honneur",
        "gold": "💰 Or",
        "phase": "📜 Phase de campagne",
        "cmd_prompt": "Entrez une commande (1-ATTAQUER, 2-RECRUTER, 3-STATUT, 4-CLASSEMENT, 5-AIDE, 6-QUITTER): ",
        "victory": "⚔ Victoire ! Vous avez conquis un nouveau territoire.",
        "defeat": "❌ Défaite ! Vous avez perdu des soldats et des ressources.",
        "no_soldiers": "❌ Vous n'avez pas de soldats pour attaquer !",
        "recruit_ok": "👥 Vous avez recruté 10 soldats pour 10 d'or.",
        "recruit_fail": "💰 Or insuffisant pour recruter.",
        "status": "📊 Statut de {nome} : {t} territoires, {s} soldats, {h} honneur, {o} or.",
        "help": "📖 Commandes : 1-ATTAQUER, 2-RECRUTER, 3-STATUT, 4-CLASSEMENT, 5-AIDE, 6-QUITTER",
        "bye": "👋 Jeu fermé. Résultat enregistré.",
        "phase_done": "📜 Phase {f} terminée ! Passez à la région suivante.",
        "ranking_title": "🏆 Classement des Guerriers :",
        "ranking_none": "📂 Aucun classement disponible pour le moment.",
        "game_over": "💀 GAME OVER 💀\n📜 Fin de campagne. Votre armée a été décimée...",
    },
}

def salvar_ranking(nome, territorios, honra, ouro):
    with open("ranking.txt", "a", encoding="utf-8") as f:
        f.write(f"{nome};{territorios};{honra};{ouro}\n")

def mostrar_ranking(textos):
    try:
        with open("ranking.txt", "r", encoding="utf-8") as f:
            print("\n" + textos["ranking_title"])
            linhas = [linha.strip().split(";") for linha in f]
            linhas.sort(key=lambda x: int(x[1]), reverse=True)  # por territórios
            for nome, territorios, honra, ouro in linhas:
                print(f"- {nome}: {territorios} {textos['territories'].split()[1].lower()}, {honra} {textos['honor'].split()[1].lower()}, {ouro} {textos['gold'].split()[1].lower()}")
    except FileNotFoundError:
        print(textos["ranking_none"])

def jogo():
    print("🌍 🌍 Escolha o idioma:\n1 - Português\n2 - English\n3 - Español\n4 - Français")
    lang_choice = escolher(
        {"1": "pt", "2": "en", "3": "es", "4": "fr", "português": "pt", "portugues": "pt", "pt": "pt",
         "english": "en", "en": "en", "español": "es", "espanol": "es", "es": "es", "français": "fr", "francais": "fr", "fr": "fr"},
        ">> ",
    )
    textos = IDIOMAS[lang_choice]

    print(textos["welcome"])
    nome = input(textos["ask_name"])

    modo = escolher(
        {"1": "classico", "2": "campanha", "clássico": "classico", "classico": "classico", "classic": "classico",
         "campanha": "campanha", "campaign": "campanha"},
        textos["mode_prompt"]
    )

    dificuldade = escolher(
        {"1": "facil", "2": "medio", "3": "dificil",
         "amador": "facil", "veterano": "medio", "experiente": "dificil",
         "amateur": "facil", "veteran": "medio", "expert": "dificil"},
        textos["diff_prompt"]
    )

    # Estado inicial
    territorios, soldados, honra, ouro = 3, 50, 100, 50
    fase = 1 if modo == "campanha" else None

    # Mapa de comandos com números e palavras
    comandos = {
        "1": "atacar", "atacar": "atacar", "attack": "atacar", "attaquer": "atacar", "atacar ": "atacar",
        "2": "recrutar", "recrutar": "recrutar", "recruit": "recrutar", "reclutar": "recrutar",
        "3": "status", "status": "status", "estado": "status", "statut": "status",
        "4": "ranking", "ranking": "ranking", "classement": "ranking", "clasificación": "ranking",
        "5": "ajuda", "ajuda": "ajuda", "help": "ajuda", "ayuda": "ajuda", "aide": "ajuda",
        "6": "sair", "sair": "sair", "exit": "sair", "salir": "sair", "quitter": "sair",
    }

    while True:
        print("\n" + textos["stats_header"])
        print(f"{textos['territories']}: {territorios}")
        print(f"{textos['soldiers']}: {soldados}")
        print(f"{textos['honor']}: {honra}")
        print(f"{textos['gold']}: {ouro}")
        if fase:
            print(f"{textos['phase']}: {fase}")
        print(textos["stats_header"])

        cmd_raw = norm(input(textos["cmd_prompt"]))
        comando = comandos.get(cmd_raw)
        if not comando:
            print("Comando inválido.")
            continue

        if comando == "atacar":
            if soldados <= 0:
                print(textos["no_soldiers"])
            else:
                if random.choice([True, False]):
                    print(textos["victory"])
                    territorios += 1
                    honra += random.randint(10, 20)
                    ouro += random.randint(10, 20)
                else:
                    print(textos["defeat"])
                    soldados -= random.randint(5, 15)
                    honra -= random.randint(10, 20)
                    ouro += random.randint(5, 15)

                evento = random.choice([
                    "Tempestade destruiu suprimentos!",
                    "Você saqueou um vilarejo!",
                    "Uma peste atingiu seu exército!",
                    "Traição interna!",
                    "Reforços chegaram!"
                ])
                print(f"⚡ Evento: {evento}")

                if fase and territorios % 5 == 0:
                    print(textos["phase_done"].format(f=fase))
                    fase += 1

        elif comando == "recrutar":
            if ouro >= 10:
                soldados += 10
                ouro -= 10
                print(textos["recruit_ok"])
            else:
                print(textos["recruit_fail"])

        elif comando == "status":
            print(textos["status"].format(nome=nome, t=territorios, s=soldados, h=honra, o=ouro))

        elif comando == "ranking":
            mostrar_ranking(textos)

        elif comando == "ajuda":
            print(textos["help"])

        elif comando == "sair":
            print(textos["bye"])
            salvar_ranking(nome, territorios, honra, ouro)
            break

        # Game Over
        if soldados <= 0:
            print("\n" + textos["game_over"])
            print(f"{textos['territories']}: {territorios}")
            print(f"{textos['honor']}: {honra}")
            print(f"{textos['gold']}: {ouro}")
            salvar_ranking(nome, territorios, honra, ouro)
            break

if __name__ == "__main__":
    jogo()
