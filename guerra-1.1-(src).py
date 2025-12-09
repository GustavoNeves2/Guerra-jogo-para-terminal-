import random
import os
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER

# ------------------------
# Idiomas
# ------------------------
IDIOMAS = {
    "pt": {
        "welcome": "🎮 Bem-vindo ao GUERRA 1.1!",
        "ask_name": "Digite seu nome de guerreiro:",
        "mode_label": "Modo de jogo:",
        "diff_label": "Dificuldade:",
        "mode_opts": ["Clássico (infinito)", "Campanha (fases com objetivos)"],
        "diff_opts": ["Amador", "Veterano", "Experiente"],
        "territories": "🏰 Territórios",
        "soldiers": "👥 Soldados",
        "honor": "⭐ Honra",
        "gold": "💰 Ouro",
        "phase": "📜 Fase da campanha",
        "victory": "⚔ Vitória! Você conquistou um novo território.",
        "defeat": "❌ Derrota! Você perdeu soldados e recursos.",
        "no_soldiers": "❌ Você não tem soldados para atacar!",
        "recruit_ok": "👥 Você recrutou 10 soldados por 10 de ouro.",
        "recruit_fail": "💰 Ouro insuficiente para recrutar.",
        "status": "📊 Status de {nome}: {t} territórios, {s} soldados, {h} honra, {o} ouro.",
        "help": "📖 Comandos: ATACAR, RECRUTAR, STATUS, RANKING, AJUDA, SAIR",
        "bye": "👋 Jogo encerrado. Resultado salvo.",
        "phase_done": "📜 Fase {f} concluída! Avance para a próxima região.",
        "ranking_title": "🏆 Ranking dos Guerreiros:",
        "ranking_none": "📂 Nenhum ranking disponível ainda.",
        "game_over": "💀 GAME OVER 💀\n📜 Fim da campanha. Seu exército foi dizimado...",
        "btn_attack": "ATACAR",
        "btn_recruit": "RECRUTAR",
        "btn_status": "STATUS",
        "btn_ranking": "RANKING",
        "btn_help": "AJUDA",
        "btn_exit": "SAIR",
        "lang_label": "Idioma:",
        "start_btn": "Começar",
        "final_victory": "🏆 CAMPANHA CONCLUÍDA! Você conquistou todas as regiões e se tornou o maior guerreiro!"
    },
    "en": {
        "welcome": "🎮 Welcome to WAR 1.1!",
        "ask_name": "Enter your warrior name:",
        "mode_label": "Game mode:",
        "diff_label": "Difficulty:",
        "mode_opts": ["Classic (endless)", "Campaign (objective-based)"],
        "diff_opts": ["Amateur", "Veteran", "Expert"],
        "territories": "🏰 Territories",
        "soldiers": "👥 Soldiers",
        "honor": "⭐ Honor",
        "gold": "💰 Gold",
        "phase": "📜 Campaign phase",
        "victory": "⚔ Victory! You conquered a new territory.",
        "defeat": "❌ Defeat! You lost soldiers and resources.",
        "no_soldiers": "❌ You have no soldiers to attack!",
        "recruit_ok": "👥 You recruited 10 soldiers for 10 gold.",
        "recruit_fail": "💰 Not enough gold to recruit.",
        "status": "📊 {nome}'s status: {t} territories, {s} soldiers, {h} honor, {o} gold.",
        "help": "📖 Commands: ATTACK, RECRUIT, STATUS, RANKING, HELP, EXIT",
        "bye": "👋 Game closed. Result saved.",
        "phase_done": "📜 Phase {f} completed! Proceed to the next region.",
        "ranking_title": "🏆 Warriors Ranking:",
        "ranking_none": "📂 No ranking available yet.",
        "game_over": "💀 GAME OVER 💀\n📜 End of campaign. Your army was wiped out...",
        "btn_attack": "ATTACK",
        "btn_recruit": "RECRUIT",
        "btn_status": "STATUS",
        "btn_ranking": "RANKING",
        "btn_help": "HELP",
        "btn_exit": "EXIT",
        "lang_label": "Language:",
        "start_btn": "Start",
        "final_victory": "🏆 CAMPAIGN COMPLETED! You conquered all regions and became the greatest warrior!"
    },
    "es": {
        "welcome": "🎮 ¡Bienvenido a GUERRA 1.1!",
        "ask_name": "Escribe tu nombre de guerrero:",
        "mode_label": "Modo de juego:",
        "diff_label": "Dificultad:",
        "mode_opts": ["Clásico (infinito)", "Campaña (por objetivos)"],
        "diff_opts": ["Amateur", "Veterano", "Experto"],
        "territories": "🏰 Territorios",
        "soldiers": "👥 Soldados",
        "honor": "⭐ Honor",
        "gold": "💰 Oro",
        "phase": "📜 Fase de la campaña",
        "victory": "⚔ ¡Victoria! Conquistaste un nuevo territorio.",
        "defeat": "❌ ¡Derrota! Perdiste soldados y recursos.",
        "no_soldiers": "❌ ¡No tienes soldados para atacar!",
        "recruit_ok": "👥 Reclutaste 10 soldados por 10 de oro.",
        "recruit_fail": "💰 Oro insuficiente para reclutar.",
        "status": "📊 Estado de {nome}: {t} territorios, {s} soldados, {h} honor, {o} oro.",
        "help": "📖 Comandos: ATACAR, RECLUTAR, ESTADO, CLASIFICACIÓN, AYUDA, SALIR",
        "bye": "👋 Juego cerrado. Resultado guardado.",
        "phase_done": "📜 ¡Fase {f} completada! Avanza a la siguiente región.",
        "ranking_title": "🏆 Clasificación de Guerreros:",
        "ranking_none": "📂 Aún no hay clasificación disponible.",
        "game_over": "💀 GAME OVER 💀\n📜 Fin de campaña. Tu ejército fue aniquilado...",
        "btn_attack": "ATACAR",
        "btn_recruit": "RECLUTAR",
        "btn_status": "ESTADO",
        "btn_ranking": "CLASIFICACIÓN",
        "btn_help": "AYUDA",
        "btn_exit": "SALIR",
        "lang_label": "Idioma:",
        "start_btn": "Comenzar",
        "final_victory": "🏆 ¡CAMPAÑA COMPLETADA! Conquistaste todas las regiones y te convertiste en el mayor guerrero!"
    },
    "fr": {
        "welcome": "🎮 Bienvenue à GUERRE 1.1!",
        "ask_name": "Entrez votre nom de guerrier:",
        "mode_label": "Mode de jeu:",
        "diff_label": "Difficulté:",
        "mode_opts": ["Classique (infini)", "Campagne (à objectifs)"],
        "diff_opts": ["Amateur", "Vétéran", "Expérimenté"],
        "territories": "🏰 Territoires",
        "soldiers": "👥 Soldats",
        "honor": "⭐ Honneur",
        "gold": "💰 Or",
        "phase": "📜 Phase de campagne",
        "victory": "⚔ Victoire ! Vous avez conquis un nouveau territoire.",
        "defeat": "❌ Défaite ! Vous avez perdu des soldats et des ressources.",
        "no_soldiers": "❌ Vous n'avez pas de soldats pour attaquer !",
        "recruit_ok": "👥 Vous avez recruté 10 soldats pour 10 d'or.",
        "recruit_fail": "💰 Or insuffisant pour recruter.",
        "status": "📊 Statut de {nome} : {t} territoires, {s} soldats, {h} honneur, {o} or.",
        "help": "📖 Commandes : ATTAQUER, RECRUTER, STATUT, CLASSEMENT, AIDE, QUITTER",
        "bye": "👋 Jeu fermé. Résultat enregistré.",
        "phase_done": "📜 Phase {f} terminée ! Passez à la région suivante.",
        "ranking_title": "🏆 Classement des Guerriers :",
        "ranking_none": "📂 Aucun classement disponible pour le moment.",
        "game_over": "💀 GAME OVER 💀\n📜 Fin de campagne. Votre armée a été décimée...",
        "btn_attack": "ATTAQUER",
        "btn_recruit": "RECRUTER",
        "btn_status": "STATUT",
        "btn_ranking": "CLASSEMENT",
        "btn_help": "AIDE",
        "btn_exit": "QUITTER",
        "lang_label": "Langue:",
        "start_btn": "Démarrer",
        "final_victory": "🏆 CAMPAGNE TERMINÉE ! Vous avez conquis toutes les régions et êtes devenu le plus grand guerrier !"
    }
}
# ------------------------
# Ranking
# ------------------------
def salvar_ranking(rank_path, nome, territorios, honra, ouro):
    try:
        os.makedirs(os.path.dirname(rank_path), exist_ok=True)
        with open(rank_path, "a", encoding="utf-8") as f:
            f.write(f"{nome};{territorios};{honra};{ouro}\n")
    except Exception:
        # Evita quebrar o jogo caso não consiga escrever (permissão/armazenamento)
        pass

def ler_ranking(rank_path):
    try:
        with open(rank_path, "r", encoding="utf-8") as f:
            linhas = [linha.strip().split(";") for linha in f if ";" in linha]
            # Ordena por número de territórios (maior primeiro)
            linhas.sort(key=lambda x: int(x[1]), reverse=True)
            return linhas
    except Exception:
        return []
# ------------------------
# App principal
# ------------------------
class GuerraApp(toga.App):
    def startup(self):
        # Estado inicial de setup
        self.lang = "pt"
        self.textos = IDIOMAS[self.lang]
        self.nome = ""
        self.modo = "classico"     # "classico" ou "campanha"
        self.dificuldade = "facil" # "facil", "medio", "dificil"

        # Estado de jogo
        self.territorios = 3
        self.soldados = 50
        self.honra = 100
        self.ouro = 50
        self.fase = 1

        # Caminho seguro para ranking
        self.rank_path = os.path.join(self.paths.data, "ranking.txt")

        # Janela principal
        self.main_window = toga.MainWindow(title="GUERRA 1.1")
        self.main_window.content = self._build_setup_view()
        self.main_window.show()

    # ---------- Views ----------
    def _build_setup_view(self):
        box = toga.Box(style=Pack(direction=COLUMN, padding=16, alignment=CENTER, width=600))
        title = toga.Label(self.textos["welcome"], style=Pack(padding_bottom=10))

        self.lang_select = toga.Selection(items=["Português", "English", "Español", "Français"], style=Pack(padding_bottom=8))
        self.lang_select.value = "Português"

        self.name_input = toga.TextInput(placeholder="Ex.: Gusta", style=Pack(padding_bottom=8))

        self.mode_select = toga.Selection(items=self.textos["mode_opts"], style=Pack(padding_bottom=8))
        self.mode_select.value = self.textos["mode_opts"][0]

        self.diff_select = toga.Selection(items=self.textos["diff_opts"], style=Pack(padding_bottom=16))
        self.diff_select.value = self.textos["diff_opts"][0]

        start_btn = toga.Button(self.textos["start_btn"], style=Pack(padding=10), on_press=self._start_game)

        box.add(title)
        box.add(toga.Label(self.textos["lang_label"])); box.add(self.lang_select)
        box.add(toga.Label(self.textos["ask_name"])); box.add(self.name_input)
        box.add(toga.Label(self.textos["mode_label"])); box.add(self.mode_select)
        box.add(toga.Label(self.textos["diff_label"])); box.add(self.diff_select)
        box.add(start_btn)
        return box

    def _build_game_view(self):
        wrapper = toga.Box(style=Pack(direction=COLUMN, padding=12))
        self.status_label = toga.Label(self._status_text(), style=Pack(padding=6))

        buttons = toga.Box(style=Pack(direction=ROW, padding=6))
        buttons.add(toga.Button(self.textos["btn_attack"], on_press=self._cmd_atacar, style=Pack(padding=4)))
        buttons.add(toga.Button(self.textos["btn_recruit"], on_press=self._cmd_recrutar, style=Pack(padding=4)))
        buttons.add(toga.Button(self.textos["btn_status"], on_press=self._cmd_status, style=Pack(padding=4)))
        buttons.add(toga.Button(self.textos["btn_ranking"], on_press=self._cmd_ranking, style=Pack(padding=4)))
        buttons.add(toga.Button(self.textos["btn_help"], on_press=self._cmd_ajuda, style=Pack(padding=4)))
        buttons.add(toga.Button(self.textos["btn_exit"], on_press=self._cmd_sair, style=Pack(padding=4)))

        wrapper.add(self.status_label)
        wrapper.add(buttons)
        return wrapper

    # ---------- Helpers ----------
    def _status_text(self):
        base = [
            f"{self.textos['territories']}: {self.territorios}",
            f"{self.textos['soldiers']}: {self.soldados}",
            f"{self.textos['honor']}: {self.honra}",
            f"{self.textos['gold']}: {self.ouro}",
        ]
        if self.modo == "campanha":
            base.append(f"{self.textos['phase']}: {self.fase}")
        return " | ".join(base)

    def _update_status(self, msg=""):
        txt = msg + ("\n" if msg else "") + self._status_text()
        self.status_label.text = txt
    # ---------- Fluxo de setup ----------
    def _start_game(self, widget):
        lang_map = {"Português": "pt", "English": "en", "Español": "es", "Français": "fr"}
        self.lang = lang_map.get(self.lang_select.value, "pt")
        self.textos = IDIOMAS[self.lang]

        self.nome = (self.name_input.value or "").strip() or "Guerreiro"

        mv = self.mode_select.value
        if mv in ["Clássico (infinito)", "Classic (endless)", "Clásico (infinito)", "Classique (infini)"]:
            self.modo = "classico"
            self.fase = None
        else:
            self.modo = "campanha"
            self.fase = 1

        dv = self.diff_select.value
        if dv in ["Amador", "Amateur"]:
            self.dificuldade = "facil"
        elif dv in ["Veterano", "Veteran", "Vétéran"]:
            self.dificuldade = "medio"
        else:
            self.dificuldade = "dificil"

        self.territorios = 3
        self.soldados = 50
        self.honra = 100
        self.ouro = 50

        self.main_window.content = self._build_game_view()
        self._update_status(self.textos["welcome"])

    # ---------- Lógica do jogo ----------
    def _chance_vitoria(self):
        base = 0.5
        if self.dificuldade == "facil":
            base += 0.15
        elif self.dificuldade == "dificil":
            base -= 0.15
        return random.random() < base

    def _cmd_atacar(self, widget):
        MAX_FASES = 10

        if self.soldados <= 0:
            self._update_status(self.textos["no_soldiers"])
            return

        if self._chance_vitoria():
            self.territorios += 1
            self.honra += random.randint(10, 20)
            self.ouro += random.randint(10, 20)
            mensagem = self.textos["victory"]
        else:
            self.soldados -= random.randint(5, 15)
            self.honra -= random.randint(10, 20)
            self.ouro += random.randint(5, 15)
            mensagem = self.textos["defeat"]

        evento = random.choice([
            "Tempestade destruiu suprimentos!",
            "Você saqueou um vilarejo!",
            "Uma peste atingiu seu exército!",
            "Traição interna!",
            "Reforços chegaram!",
        ])
        mensagem += f"\n⚡ Evento: {evento}"

        if self.modo == "campanha" and self.territorios % 5 == 0:
            fase_atual = self.fase
            if self.fase < MAX_FASES:
                self.fase += 1
                mensagem += f"\n{self.textos['phase_done'].format(f=fase_atual)}"
            else:
                mensagem += f"\n{self.textos['final_victory']}"
                salvar_ranking(self.rank_path, self.nome, self.territorios, self.honra, self.ouro)
                self.main_window.info_dialog("Vitória Final", self.textos["final_victory"])
                self.exit()

        if self.soldados <= 0:
            mensagem += f"\n{self.textos['game_over']}"
            salvar_ranking(self.rank_path, self.nome, self.territorios, self.honra, self.ouro)

        self._update_status(mensagem)

    def _cmd_recrutar(self, widget):
        if self.ouro >= 10:
            self.soldados += 10
            self.ouro -= 10
            self._update_status(self.textos["recruit_ok"])
        else:
            self._update_status(self.textos["recruit_fail"])

    def _cmd_status(self, widget):
        msg = self.textos["status"].format(
            nome=self.nome, t=self.territorios, s=self.soldados, h=self.honra, o=self.ouro
        )
        self._update_status(msg)

    def _cmd_ranking(self, widget):
        linhas = ler_ranking(self.rank_path)
        if not linhas:
            self._update_status(self.textos["ranking_none"])
            return
        header = self.textos["ranking_title"]
        body = "\n".join(
            [f"- {nome}: {territorios} T, {honra} H, {ouro} $" for (nome, territorios, honra, ouro) in linhas[:10]]
        )
        self._update_status(f"{header}\n{body}")

    def _cmd_ajuda(self, widget):
        self._update_status(self.textos["help"])

    def _cmd_sair(self, widget):
        salvar_ranking(self.rank_path, self.nome, self.territorios, self.honra, self.ouro)
        self.main_window.info_dialog("Saída", self.textos["bye"])
        self.exit()

# ---------- Main ----------
def main():
    return GuerraApp("GUERRA 1.1", "com.gustavo.guerra")

