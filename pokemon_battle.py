import pygame
import random
import sys
import io
import os
import urllib.request
import contextlib
from collections import deque

with contextlib.redirect_stdout(open(os.devnull, "w")):
    from MovesClass import (
        pokemonNameList, pokemonHPList, pokemonAttackList,
        pokemonDefenseList, pokemonTypeList, movesClassList,
    )

pygame.init()

# --- Constants ---
SW, SH   = 800, 600
FIELD_H  = 360
PANEL_Y  = 360
FPS      = 60
LEVEL    = 30

C_SKY       = (100, 160, 220)
C_GRASS     = (120, 180,  80)
C_PLATFORM  = (100, 160,  60)
C_PANEL     = (240, 230, 200)
C_INFO_BG   = (255, 255, 255)
C_BORDER    = ( 50,  50,  50)
C_TEXT      = ( 20,  20,  20)
C_HP_GREEN  = (  0, 200,   0)
C_HP_YELLOW = (220, 180,   0)
C_HP_RED    = (220,  30,  30)
C_HP_BG     = (100, 100, 100)
C_BTN       = (220, 220, 220)
C_BTN_HOVER = (180, 210, 255)

TYPE_COLORS = {
    "Fire":     (240,  80,  30),
    "Water":    ( 50, 130, 250),
    "Grass":    ( 60, 190,  60),
    "Electric": (255, 215,   0),
    "Psychic":  (240,  60, 160),
    "Normal":   (168, 168, 120),
    "Fighting": (190,  80,  30),
    "Poison":   (160,  60, 200),
    "Ground":   (210, 180,  90),
    "Ice":      (150, 220, 255),
    "Dragon":   ( 80,  60, 230),
    "Ghost":    (112,  85, 155),
    "Rock":     (180, 160,  60),
    "Bug":      (166, 185,  26),
    "Flying":   (105, 145, 240),
    "Fairy":    (238, 153, 172),
}

OPP_INFO = pygame.Rect(15,  15, 240, 76)
PLR_INFO = pygame.Rect(495, 255, 290, 76)

OPP_SPRITE_RECT = pygame.Rect(150,  55, 130, 130)
PLR_SPRITE_RECT = pygame.Rect(440, 145, 160, 160)

# FIGHT spans the full top row; POKeMON and RUN share the bottom row
MAIN_BTNS = [
    pygame.Rect(415, 375, 365, 100),   # 0 FIGHT  (full-width top)
    pygame.Rect(415, 485, 170, 100),   # 1 POKeMON
    pygame.Rect(600, 485, 170, 100),   # 2 RUN
]
MAIN_LABELS = ["FIGHT", "POKeMON", "RUN"]


# --- Sprite loading ---

def _fetch_image(url, timeout=6):
    try:
        with urllib.request.urlopen(url.strip(), timeout=timeout) as r:
            data = r.read()
        return pygame.image.load(io.BytesIO(data)).convert_alpha()
    except Exception:
        return None


def load_sprites(pokedex_number):
    base  = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon"
    front = _fetch_image(f"{base}/{pokedex_number}.png")
    back  = _fetch_image(f"{base}/back/{pokedex_number}.png")
    return front, back


def fallback_sphere(rect, color):
    surf = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
    cx, cy, r = rect.width // 2, rect.height // 2, min(rect.width, rect.height) // 2 - 4
    pygame.draw.circle(surf, color, (cx, cy), r)
    hi = tuple(min(255, c + 90) for c in color)
    pygame.draw.circle(surf, hi, (cx - r // 3, cy - r // 3), r // 4)
    rim = tuple(max(0, c - 60) for c in color)
    pygame.draw.circle(surf, rim, (cx, cy), r, 3)
    return surf


# --- Pokemon setup ---

def scaled_hp(base_hp, level=LEVEL):
    return int(((2 * base_hp * level) / 100) + level + 10)


def pick_moves(count=4):
    damaging = [m for m in movesClassList if m.getPower() > 0 and m.getPP() >= 5]
    chosen = random.sample(damaging, min(count, len(damaging)))
    return [{
        "name":     m.getName(),
        "power":    int(m.getPower()),
        "accuracy": int(m.getAccuracy()) if m.getAccuracy() > 0 else 100,
        "pp":       m.getPP(),
        "type":     m.getmoveType(),
        "class":    m.getDamageType(),
    } for m in chosen]


def pick_party(n=6):
    indices = random.sample(range(151), n)
    return [
        {
            "idx":     i,
            "name":    pokemonNameList[i],
            "hp":      scaled_hp(pokemonHPList[i]),
            "attack":  pokemonAttackList[i],
            "defense": pokemonDefenseList[i],
            "type":    pokemonTypeList[i],
            "color":   TYPE_COLORS.get(pokemonTypeList[i], (168, 168, 120)),
            "moves":   pick_moves(),
        }
        for i in indices
    ]


# --- Data classes ---

class BattleMove:
    def __init__(self, d):
        self.name         = d["name"]
        self.power        = d["power"]
        self.accuracy     = d["accuracy"]
        self.max_pp       = d["pp"]
        self.current_pp   = d["pp"]
        self.move_type    = d["type"]
        self.damage_class = d["class"]

    def use(self):
        if self.current_pp <= 0:
            return False
        self.current_pp -= 1
        return True


class Pokemon:
    def __init__(self, name, hp, attack, defense, moves):
        self.name       = name
        self.level      = LEVEL
        self.max_hp     = hp
        self.current_hp = hp
        self.attack     = attack
        self.defense    = defense
        self.moves      = [BattleMove(m) for m in moves]

    @property
    def hp_pct(self):
        return self.current_hp / self.max_hp

    def is_fainted(self):
        return self.current_hp <= 0

    def take_damage(self, amount):
        self.current_hp = max(0, self.current_hp - amount)


# --- Battle logic ---

def calc_damage(attacker, move, defender):
    if move.power <= 0:
        return 0
    lf  = (2 * attacker.level / 5) + 2
    dmg = int((lf * move.power * attacker.attack / max(1, defender.defense)) / 50) + 2
    return max(1, int(dmg * random.uniform(0.85, 1.0)))


def resolve(attacker, move, defender):
    msgs = []
    if not move.use():
        return 0, [f"{attacker.name} has no PP left!"]
    msgs.append(f"{attacker.name} used {move.name}!")
    if random.randint(1, 100) > move.accuracy:
        msgs.append("But it missed!")
        return 0, msgs
    dmg = calc_damage(attacker, move, defender)
    defender.take_damage(dmg)
    msgs.append(f"{defender.name} took {dmg} damage!")
    if defender.is_fainted():
        msgs.append(f"{defender.name} fainted!")
    return dmg, msgs


# --- Drawing helpers ---

def draw_hp_bar(surf, x, y, w, h, pct):
    pygame.draw.rect(surf, C_HP_BG, (x, y, w, h))
    fill  = int(w * max(0.0, pct))
    color = C_HP_GREEN if pct > 0.5 else (C_HP_YELLOW if pct > 0.25 else C_HP_RED)
    if fill > 0:
        pygame.draw.rect(surf, color, (x, y, fill, h))
    pygame.draw.rect(surf, C_BORDER, (x, y, w, h), 1)


def draw_info_box(surf, poke, rect, label, f_med, f_sm):
    pygame.draw.rect(surf, C_INFO_BG, rect, border_radius=6)
    pygame.draw.rect(surf, C_BORDER,  rect, 2, border_radius=6)
    surf.blit(f_med.render(f"{label}: {poke.name}", True, C_TEXT), (rect.x + 8, rect.y + 6))
    lv = f_sm.render(f"Lv{poke.level}", True, C_TEXT)
    surf.blit(lv, (rect.right - lv.get_width() - 8, rect.y + 6))
    surf.blit(f_sm.render("HP", True, C_TEXT), (rect.x + 8, rect.y + 34))
    draw_hp_bar(surf, rect.x + 30, rect.y + 37, rect.width - 38, 12, poke.hp_pct)
    hp_txt = f_sm.render(f"{poke.current_hp}/{poke.max_hp}", True, C_TEXT)
    surf.blit(hp_txt, (rect.right - hp_txt.get_width() - 8, rect.y + 52))


def draw_btn(surf, rect, label, hovered, f_lg):
    pygame.draw.rect(surf, C_BTN_HOVER if hovered else C_BTN, rect, border_radius=8)
    pygame.draw.rect(surf, C_BORDER, rect, 2, border_radius=8)
    t = f_lg.render(label, True, C_TEXT)
    surf.blit(t, t.get_rect(center=rect.center))


def draw_move_btn(surf, rect, move, hovered, f_med, f_sm):
    pygame.draw.rect(surf, C_BTN_HOVER if hovered else C_BTN, rect, border_radius=8)
    pygame.draw.rect(surf, C_BORDER, rect, 2, border_radius=8)
    surf.blit(f_med.render(move.name, True, C_TEXT), (rect.x + 10, rect.y + 10))
    tc    = TYPE_COLORS.get(move.move_type, (168, 168, 120))
    badge = pygame.Rect(rect.x + 10, rect.y + 42, 72, 18)
    pygame.draw.rect(surf, tc, badge, border_radius=4)
    tl = f_sm.render(move.move_type.upper(), True, (255, 255, 255))
    surf.blit(tl, tl.get_rect(center=badge.center))
    surf.blit(f_sm.render(f"PP {move.current_pp}/{move.max_pp}", True, (80, 80, 80)),
              (rect.x + 10, rect.y + 68))


# --- Main battle controller ---

class Battle:
    MENU          = "MENU"
    MOVES         = "MOVES"
    ANIM          = "ANIM"
    END           = "END"
    HANDOFF       = "HANDOFF"
    PARTY         = "PARTY"
    FORCED_SWITCH = "FORCED_SWITCH"

    def __init__(self):
        self.screen = pygame.display.set_mode((SW, SH))
        pygame.display.set_caption("Pokemon Battle")
        self.clock  = pygame.time.Clock()
        self.f_lg   = pygame.font.SysFont("monospace", 20, bold=True)
        self.f_med  = pygame.font.SysFont("monospace", 17)
        self.f_sm   = pygame.font.SysFont("monospace", 13)

        self._show_loading("Generating parties...")

        p1_data = pick_party(6)
        p2_data = pick_party(6)

        self.p1_party   = [Pokemon(d["name"], d["hp"], d["attack"], d["defense"], d["moves"]) for d in p1_data]
        self.p2_party   = [Pokemon(d["name"], d["hp"], d["attack"], d["defense"], d["moves"]) for d in p2_data]
        self.p1_indices = [d["idx"] for d in p1_data]
        self.p2_indices = [d["idx"] for d in p2_data]
        self.p1_colors  = [d["color"] for d in p1_data]
        self.p2_colors  = [d["color"] for d in p2_data]
        self.p1_active  = 0
        self.p2_active  = 0

        self.sprites    = {}   # {pokedex_idx: (front_surf, back_surf)} lazy cache

        self._show_loading("Loading sprites...")
        self._ensure_sprite(self.p1_indices[0])
        self._ensure_sprite(self.p2_indices[0])

        self.current    = 1    # whose turn: 1 or 2
        self.state      = self.HANDOFF
        self.messages   = deque(maxlen=4)
        self.anim_timer = 0
        self.hover      = -1
        self.end_msg    = ""

    # ---- party / player helpers ----

    def _party_for(self, player):
        return self.p1_party if player == 1 else self.p2_party

    def _active_for(self, player):
        return self.p1_active if player == 1 else self.p2_active

    def _set_active_for(self, player, idx):
        if player == 1:
            self.p1_active = idx
        else:
            self.p2_active = idx

    def _indices_for(self, player):
        return self.p1_indices if player == 1 else self.p2_indices

    def _colors_for(self, player):
        return self.p1_colors if player == 1 else self.p2_colors

    def _other(self):
        return 2 if self.current == 1 else 1

    def _attacker(self):
        return self._party_for(self.current)[self._active_for(self.current)]

    def _defender(self):
        opp = self._other()
        return self._party_for(opp)[self._active_for(opp)]

    def _swap_current(self):
        self.current = self._other()

    def _set_end(self, msg):
        self.end_msg = msg
        self.state   = self.END

    # ---- sprite helpers ----

    def _ensure_sprite(self, pokedex_idx):
        if pokedex_idx not in self.sprites:
            self.sprites[pokedex_idx] = load_sprites(pokedex_idx + 1)

    def _get_scaled_sprite(self, pokedex_idx, color, rect, back=False):
        self._ensure_sprite(pokedex_idx)
        front, bk = self.sprites[pokedex_idx]
        raw = (bk or front) if back else (front or bk)
        if raw is None:
            raw = fallback_sphere(rect, color)
        return pygame.transform.scale(raw, (rect.width, rect.height))

    def _show_loading(self, msg="Loading..."):
        self.screen.fill((30, 30, 30))
        txt = self.f_lg.render(msg, True, (220, 220, 220))
        self.screen.blit(txt, txt.get_rect(center=(SW // 2, SH // 2)))
        pygame.display.flip()

    # ---- event handling ----

    def _events(self):
        mx, my = pygame.mouse.get_pos()
        self.hover = next((i for i, r in enumerate(MAIN_BTNS) if r.collidepoint(mx, my)), -1)

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                pygame.quit(); sys.exit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                self._handle_click(ev, mx, my)

    def _handle_click(self, ev, mx, my):
        if self.state == self.HANDOFF:
            self.state = self.MENU

        elif self.state == self.MENU:
            if self.hover == 0:               # FIGHT
                self.state = self.MOVES
            elif self.hover == 1:             # POKeMON
                self.state = self.PARTY
            elif self.hover == 2:             # RUN
                winner = self._other()
                self._set_end(f"P{self.current} fled!  Player {winner} wins!")

        elif self.state == self.MOVES:
            if ev.button == 3:
                self.state = self.MENU
            elif self.hover >= 0:
                self._do_attack(self.hover)

        elif self.state == self.ANIM:
            self._advance()

        elif self.state in (self.PARTY, self.FORCED_SWITCH):
            if ev.button == 3 and self.state == self.PARTY:
                self.state = self.MENU
                return
            self._handle_party_click(mx, my)

        elif self.state == self.END:
            pygame.quit(); sys.exit()

    def _handle_party_click(self, mx, my):
        party          = self._party_for(self.current)
        indices        = self._indices_for(self.current)
        current_active = self._active_for(self.current)
        slots          = self._party_slot_rects()

        for i, slot_rect in enumerate(slots):
            if not slot_rect.collidepoint(mx, my):
                continue
            if party[i].is_fainted():
                continue
            if self.state == self.PARTY and i == current_active:
                continue   # already out
            self._show_loading("Loading sprite...")
            self._ensure_sprite(indices[i])
            self._set_active_for(self.current, i)
            if self.state == self.PARTY:
                self.messages.append(f"P{self.current} switched to {party[i].name}!")
            else:
                self.messages.append(f"P{self.current} sent out {party[i].name}!")
            self._swap_current()
            self.state = self.HANDOFF
            break

    # ---- update ----

    def _update(self, dt):
        if self.state == self.ANIM:
            self.anim_timer -= dt
            if self.anim_timer <= 0:
                self._advance()

    # ---- battle actions ----

    def _do_attack(self, move_idx):
        attacker = self._attacker()
        defender = self._defender()
        _, msgs  = resolve(attacker, attacker.moves[move_idx], defender)
        for m in msgs:
            self.messages.append(m)
        self.anim_timer = 1800
        self.state      = self.ANIM

    def _advance(self):
        opp            = self._other()
        defender_party = self._party_for(opp)
        if self._defender().is_fainted():
            if any(not p.is_fainted() for p in defender_party):
                self.current = opp   # defender picks a replacement
                self.state   = self.FORCED_SWITCH
            else:
                self._set_end(f"Player {self.current} wins!")
        else:
            self._swap_current()
            self.state = self.HANDOFF

    # ---- drawing ----

    def _party_slot_rects(self):
        slot_w, slot_h = 340, 72
        gap     = 12
        start_x = (SW - (slot_w * 2 + gap)) // 2
        start_y = 120
        rects   = []
        for row in range(3):
            for col in range(2):
                x = start_x + col * (slot_w + gap)
                y = start_y + row * (slot_h + gap)
                rects.append(pygame.Rect(x, y, slot_w, slot_h))
        return rects

    def _draw_field(self):
        self.screen.fill(C_SKY)
        pygame.draw.rect(self.screen, C_GRASS, (0, FIELD_H // 2, SW, FIELD_H // 2))

        opp          = self._other()
        def_ai       = self._active_for(opp)
        def_poke_idx = self._indices_for(opp)[def_ai]
        def_color    = self._colors_for(opp)[def_ai]
        att_ai       = self._active_for(self.current)
        att_poke_idx = self._indices_for(self.current)[att_ai]
        att_color    = self._colors_for(self.current)[att_ai]

        pygame.draw.ellipse(self.screen, C_PLATFORM,
                            (OPP_SPRITE_RECT.x - 10, OPP_SPRITE_RECT.bottom - 14,
                             OPP_SPRITE_RECT.width + 20, 22))
        pygame.draw.ellipse(self.screen, C_PLATFORM,
                            (PLR_SPRITE_RECT.x - 10, PLR_SPRITE_RECT.bottom - 18,
                             PLR_SPRITE_RECT.width + 20, 28))

        opp_img = self._get_scaled_sprite(def_poke_idx, def_color, OPP_SPRITE_RECT, back=False)
        plr_img = self._get_scaled_sprite(att_poke_idx, att_color, PLR_SPRITE_RECT, back=True)
        self.screen.blit(opp_img, OPP_SPRITE_RECT.topleft)
        self.screen.blit(plr_img, PLR_SPRITE_RECT.topleft)

        draw_info_box(self.screen, self._defender(), OPP_INFO,
                      f"P{opp}", self.f_med, self.f_sm)
        draw_info_box(self.screen, self._attacker(), PLR_INFO,
                      f"P{self.current}", self.f_med, self.f_sm)

    def _draw_panel(self):
        pygame.draw.rect(self.screen, C_PANEL, (0, PANEL_Y, SW, SH - PANEL_Y))
        pygame.draw.line(self.screen, (80, 80, 80), (0, PANEL_Y), (SW, PANEL_Y), 2)
        pygame.draw.line(self.screen, (80, 80, 80), (400, PANEL_Y), (400, SH), 2)
        for i, line in enumerate(self.messages):
            self.screen.blit(
                self.f_med.render(f"> {line}", True, C_TEXT),
                (14, PANEL_Y + 18 + i * 44),
            )

    def _draw_handoff(self):
        overlay = pygame.Surface((SW, SH), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 200))
        self.screen.blit(overlay, (0, 0))
        title = self.f_lg.render(f"Player {self.current}'s Turn", True, (255, 255, 100))
        sub   = self.f_med.render("Click anywhere to begin", True, (200, 200, 200))
        self.screen.blit(title, title.get_rect(center=(SW // 2, SH // 2 - 24)))
        self.screen.blit(sub,   sub.get_rect(center=(SW // 2, SH // 2 + 16)))

    def _draw_party_screen(self):
        forced         = self.state == self.FORCED_SWITCH
        party          = self._party_for(self.current)
        indices        = self._indices_for(self.current)
        colors         = self._colors_for(self.current)
        current_active = self._active_for(self.current)

        overlay = pygame.Surface((SW, SH), pygame.SRCALPHA)
        overlay.fill((20, 20, 40, 230))
        self.screen.blit(overlay, (0, 0))

        title_txt = (f"Player {self.current} — Send out a Pokemon!"
                     if forced else f"Player {self.current} — Choose a Pokemon")
        title = self.f_lg.render(title_txt, True, (255, 255, 100))
        self.screen.blit(title, title.get_rect(center=(SW // 2, 70)))

        if not forced:
            hint = self.f_sm.render("Right-click to cancel", True, (160, 160, 160))
            self.screen.blit(hint, hint.get_rect(center=(SW // 2, 100)))

        mx, my = pygame.mouse.get_pos()
        slots  = self._party_slot_rects()

        for i, slot_rect in enumerate(slots):
            poke      = party[i]
            fainted   = poke.is_fainted()
            is_active = (i == current_active) and not forced

            hovered = (slot_rect.collidepoint(mx, my)
                       and not fainted and not is_active)
            bg = (160, 160, 160) if fainted else (
                (180, 210, 255) if hovered else
                (200, 230, 200) if is_active else (240, 240, 240)
            )
            pygame.draw.rect(self.screen, bg, slot_rect, border_radius=8)
            pygame.draw.rect(self.screen, C_BORDER, slot_rect, 2, border_radius=8)

            tx = slot_rect.x + 10
            ty = slot_rect.y + 8
            name_color = (100, 100, 100) if fainted else C_TEXT
            self.screen.blit(self.f_med.render(poke.name, True, name_color), (tx, ty))

            if is_active:
                lbl = self.f_sm.render("(active)", True, (50, 130, 50))
                self.screen.blit(lbl, (slot_rect.right - lbl.get_width() - 10, ty + 2))

            if fainted:
                self.screen.blit(self.f_sm.render("FAINTED", True, (180, 60, 60)),
                                 (tx, ty + 30))
            else:
                tc    = colors[i]
                badge = pygame.Rect(tx, ty + 30, 70, 16)
                pygame.draw.rect(self.screen, tc, badge, border_radius=3)
                tl = self.f_sm.render(pokemonTypeList[indices[i]].upper(), True, (255, 255, 255))
                self.screen.blit(tl, tl.get_rect(center=badge.center))

                bar_x = tx + 80
                bar_w = slot_rect.width - 160
                draw_hp_bar(self.screen, bar_x, ty + 32, bar_w, 12, poke.hp_pct)
                hp_txt = self.f_sm.render(f"{poke.current_hp}/{poke.max_hp}", True, C_TEXT)
                self.screen.blit(hp_txt,
                                 (slot_rect.right - hp_txt.get_width() - 10, ty + 30))

    def _draw(self):
        if self.state == self.HANDOFF:
            self.screen.fill((30, 30, 30))
            self._draw_handoff()
            pygame.display.flip()
            return

        if self.state in (self.PARTY, self.FORCED_SWITCH):
            self.screen.fill((20, 20, 40))
            self._draw_party_screen()
            pygame.display.flip()
            return

        self._draw_field()
        self._draw_panel()

        if self.state == self.MENU:
            for i, (r, lbl) in enumerate(zip(MAIN_BTNS, MAIN_LABELS)):
                draw_btn(self.screen, r, lbl, self.hover == i, self.f_lg)

        elif self.state == self.MOVES:
            for i, (r, mv) in enumerate(zip(MAIN_BTNS, self._attacker().moves)):
                draw_move_btn(self.screen, r, mv, self.hover == i, self.f_med, self.f_sm)
            hint = self.f_sm.render("Right-click to go back", True, (110, 110, 110))
            self.screen.blit(hint, (403, SH - 18))

        elif self.state == self.ANIM:
            dim = pygame.Surface((400, SH - PANEL_Y), pygame.SRCALPHA)
            dim.fill((200, 190, 170, 180))
            self.screen.blit(dim, (400, PANEL_Y))
            w = self.f_sm.render("Click to continue...", True, (80, 80, 80))
            self.screen.blit(w, (500, SH - 22))

        elif self.state == self.END:
            overlay = pygame.Surface((SW, SH), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 150))
            self.screen.blit(overlay, (0, 0))
            end = self.f_lg.render(self.end_msg, True, (255, 255, 255))
            sub = self.f_sm.render("Click anywhere to exit", True, (200, 200, 200))
            self.screen.blit(end, end.get_rect(center=(SW // 2, SH // 2 - 18)))
            self.screen.blit(sub, sub.get_rect(center=(SW // 2, SH // 2 + 18)))

        pygame.display.flip()

    def run(self):
        while True:
            dt = self.clock.tick(FPS)
            self._events()
            self._update(dt)
            self._draw()


if __name__ == "__main__":
    Battle().run()
