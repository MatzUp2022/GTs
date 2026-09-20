# Guide d'équipe — qui pour quoi, et quoi développer d'abord (Last Light)

*Analyse tirée des données de la base de héros. Les points marqués **[hypothèse]** découlent des textes de compétences mais ne sont pas confirmés en jeu.*

## 1. Deux règles qui gouvernent toute composition

**Contre de faction** (bouton info dans l'écran de composition) : chaque faction est blindée contre exactement un attaquant.

| Défenseur | subit 20 % de dégâts en moins de la part de |
|-----------|---------------------------------------------|
| **Guardian** | Berserker |
| **Berserker** | Ranger |
| **Ranger** | Guardian |

→ À l'envers : **ne pas** envoyer de Berserker sur du Guardian, **ni** de Guardian sur du Ranger, **ni** de Ranger sur du Berserker. En PvP (arènes, Region Duel), vérifier les icônes adverses avant d'attaquer.

**Bonus de composition** (par faction, s'applique aux cinq héros) :

| Composition | PV / ATQ / DÉF |
|-------------|----------------|
| 3 identiques | +5 % |
| 3 identiques + 2 d'une autre | +10 % |
| 4 identiques | +15 % |
| **5 identiques (mono-faction)** | **+20 %** |

→ **La mono-faction est la composition la plus forte.** Un héros un peu plus fort d'une autre faction doit d'abord compenser ces 10–20 %. Et le Faction Trial comme le Frenzied Boss trient de toute façon par faction — les +20 % y sont offerts.

## 2. Les quatre schémas

1. **Les compétences multi-coups sont les meilleurs nukes contre les boss.** « X attaques sur des cibles aléatoires » frappent toutes la même cible s'il n'y en a qu'une. *Phantom Volley* d'Ella : 8 × 117 % = **936 %**, et ~1 870 % à 5★ avec 16 coups. À comparer à la plus haute valeur unique du roster : *Bounty Kill* d'Irena à 476 %. **[hypothèse]**
2. **Les bonus contre les monstres sont un axe distinct de la rareté.** Aucun héros S+ n'en a, 9 des 12 héros S oui. En PvE, un héros S avec +20 % de dégâts aux monstres dépasse souvent un S+ sans.
3. **Seul Loki renforce toute l'équipe en offense** (*Frenzied Beat* : ATQ de tous les alliés +11,5 %, plus crit +10 % et 2 tours via les étoiles). Tout le reste n'est que buff personnel.
4. **Clara est la seule à affaiblir les monstres :** *Vital Drain* fait subir au monstre **+12 % de dégâts pendant 2 tours** — pour toute l'équipe.

## 3. Qui brille où

| Événement | Composition clé | Pourquoi |
|-----------|-----------------|----------|
| **World Boss** (solo, 1 cible) | **Ella · Clara** · Bella · Scarlett · Sonic/Jessica | Burst multi-coups + affaiblissement ; aucun tank nécessaire |
| **Frenzied Boss** (3 boss de faction) | Guardian : Ella, Clara, Irena · Ranger : Jessica, Grace, Bella · Berserker : Sagitta, Sonic, Scarlett | Impose trois équipes de faction |
| **Alliance Boss** (rally, 30 min) | comme le World Boss | Cible unique + bonus contre les monstres |
| **Storm Rescue** (vagues) | **Jessica** (243 % à tous) · **Admira** (zone + débuff magique) · Eileen (ligne entière) | Le seul événement où la zone paie vraiment |
| **Peak / 3V3 Arena** (PvP) | **Viper + Marcus** · **Loki** · Ella/Jessica · Grace | Protection avant + le seul buff d'ATQ d'équipe ; Grace vise la ligne arrière |
| **Faction Trial** | trois équipes de faction distinctes | **Chaque héros dans une seule épreuve** — Ranger et Berserker (7 chacun) sont les goulots |
| **Élite radar / chasse** | Clara · Cassidy · Eileen · Gracie · Noelle | Plus de dégâts aux monstres, moins de dégâts subis |

## 4. Combinaisons

- **Le véhicule comme second amplificateur :** *Global Strike* touche 2 cibles et augmente **l'ensemble des dégâts qu'elles subissent de 15 → 25 %** pendant 1 tour (par étoiles, ★4 exige le véhicule niv. 90). Cela agit sur tout, pas seulement sur les monstres — le plus fort amplificateur d'équipe. À déclencher avant la volée d'Ella.
- **Noyau boss :** Clara + Ella — le débuff dure 2 tours, exactement la fenêtre de Phantom Volley. Ajouter Loki pour +11,5 % d'ATQ sur les deux.
- **Front d'arène :** Viper (−26 % physique) + Marcus (+35 % DÉF) — les deux s'étendent à **tous** les alliés via les étoiles, ils se cumulent donc.
- **Couverture par provocation :** Valkyra attire 2 à 4 ennemis **et** baisse leur ATQ de 11,5 % — la ligne arrière (Ella, Grace, Sonic) survit plus longtemps.
- **Anti-magie :** Admira (−12 % de dégâts magiques ennemis, −28 % de dégâts d'énergie subis) contre les carries d'énergie.
- **Astuce Guardian arrière :** *Absolute Order* d'Irena donne **+13 % de dégâts aux monstres aux héros Guardian de la ligne arrière** — placer Ella et Clara derrière quand Irena est là.

## 5. Priorité de développement

**Le niveau de base d'abord.** Si un héros affiche « Base Level needs to be increased! », toute EXP supplémentaire est perdue. Le goulot, c'est la base, pas le héros.

| # | Priorité | Raison |
|---|----------|--------|
| 1 | **Ella** | Meilleur rendement contre les boss ; jusqu'à +270 % par étoile et plus de coups |
| 2 | **Clara** | Seul débuff d'équipe contre les monstres + 52 % de butin — elle se rentabilise |
| 3 | **Loki à 5★** | L'effet d'étoile débloque crit +10 % pour tous et 2 tours |
| 4 | **Un Berserker solide** (Sonic ou Sagitta) | Faction la plus mince ; Faction Trial et Frenzied Boss imposent les trois |
| 5 | **Tous les héros 2★ vers 3★+** | À 2★, plafond de compétence niv. 5 et éveil verrouillé — le progrès le moins cher |
| 6 | **Héros A en remplissage seulement** | 2 compétences, éveil +5 %, étoiles jusqu'à +100 % — pas de médailles |

**Équipement :** arme + casque portent les dégâts aux monstres, armure + gants la réduction (voir le manuel de la forge). Sur les chasseurs de boss, monter d'abord **arme et casque** aux niv. 10/20/30 — cela fait +17 % de dégâts aux monstres.

## 6. Checklist

- [ ] Niveau de base suffisant pour les carries principaux
- [ ] Équipes montées en mono-faction autant que possible (+20 %)
- [ ] Ella, Clara, Loki développés en premier
- [ ] Les trois factions couvertes par un noyau solide
- [ ] Aucun héros laissé sous 3★ (plafond de compétence !)
- [ ] Arme + casque des chasseurs de boss aux niv. 10/20/30
