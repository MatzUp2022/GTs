# Clasificación de héroes — quién pega más fuerte, quién aguanta más (Last Light)

## 1. Cómo leer estas listas

- **Daño = multiplicador de la habilidad × ATQ del héroe.** Aquí se clasifican los multiplicadores documentados, no el daño final: una habilidad del 670 % en un héroe débil pierde contra una del 512 % en uno fuerte.
- **Los efectos de estrella no están sumados.** El juego los muestra como una escalera (+30/70/120/185/270 %) sin decir si un escalón sustituye al anterior o se acumula. Ordenar por valores base mantiene el orden honesto; la escalera de cada héroe está en la base de datos de héroes.
- **La pestaña Hero muestra ATQ · PS · DEF · capacidad de soldados incluso para héroes no obtenidos.** De ahí sale una clasificación real de estadísticas. Hasta ahora hay exactamente un héroe documentado así: Rosa en Lv. 150 / 5★ — ATQ 44,0K · PS 388,0K · DEF 5,2K · 433 soldados · CP 788.715.
- **En la reducción de daño cuenta el alcance, no la cifra.** Todo el daño / solo físico / solo energía / solo monstruos son cuatro cosas distintas, y «solo monstruos» no vale nada en la arena.

## 2. Reparte más daño — golpe único

| Héroe | Habilidad | Base | Nota |
|-------|-----------|------|------|
| Clara | Vital Drain (CS) | 670 % | físico, objetivo **aleatorio**: no dirigible |
| Rosa | Killshot Lock (CS) | 614 % | energía, objetivo único + salpicadura a la línea trasera |
| Ella | Forest Ambush | 512 % | energía, objetivo único |
| Irena | Bounty Kill (CS) | 476 % | físico; **se lanza de nuevo al 50 %** si el objetivo muere |
| Jessica | Sawblade Storm | 415 % | energía, objetivo único |
| Viper | Decisive Raid | 388 % | físico, objetivo único |
| Bella | Full Swing (CS) | 360 % | físico + probabilidad de aturdir desde ★2 |
| Admira | Blade of Judgment | 330 % | físico, objetivo único |
| Grace | Stealth Assassination | 323 % | energía, **prioriza la línea trasera**, aturdimiento |

## 3. Reparte más daño — por lanzamiento (múltiple y en área)

| Héroe | Habilidad | Por lanzamiento | Reparto |
|-------|-----------|-----------------|---------|
| Rosa | Twin-Gun Dance (CS) | 3 × 396 % = 1.188 % | enemigos aleatorios (5 ataques desde ★4) |
| Ella | Phantom Volley (CS) | 8 × 117 % = 936 % | aleatorio (12 y luego 16 ataques por estrellas) |
| Sagitta | Arrow Spray (CS) | 3 × 194 % = 582 % | 3 objetivos aleatorios |
| Clara | Frontline Support | 2 × 273 % = 546 % | 2 objetivos aleatorios |
| Noctina | Phantom Mirage (CS) | 2 × 142 % = 284 % | 2 objetivos aleatorios |
| Leora | Bullet Storm (CS) | 4 × 63 % = 252 % | aleatorio (6 y luego 8 ataques por estrellas) |
| Jessica | Chainsaw Carnival (CS) | 243 % | **todos los enemigos** |
| Scarlett | Fireline Combo (CS) | 5 × 48 % = 240 % | aleatorio (7 y luego 9 ataques por estrellas) |
| Victor | Cleanup Command (CS) | 2 × 108 % = 216 % | 2 objetivos (3 por estrellas) |
| Eileen | Frontline Strafe (CS) | 177 % | **una línea enemiga entera** + su ATQ −6 % |
| Admira | Governing Edge (CS) | 72 % | **todos los enemigos** + su daño mágico −12 % |

## 4. Aguanta más daño — reducción

| Héroe | Habilidad | Reducción | Alcance |
|-------|-----------|-----------|---------|
| Admira | Fearless Heart | −28 % | daño de energía, propia, permanente (−4 %/estrella) |
| Viper | Iron Grip | −26 % | físico, primera línea, 1 turno (estrellas: 2 turnos, todos los aliados) |
| Eileen | Wavebreaker | −25,5 % | **solo monstruos**, permanente (−4 %/estrella) |
| Cassidy | Gunfire Verdict | −24 % | **solo monstruos**, 1 turno (−4 %/estrella) · además DEF propia +70 % |
| Strike | Steady Steps | −21,5 % | **solo monstruos**, permanente (−4 %/estrella) |
| Marcus | Fortification | −21 % | **todo el daño**, propia (−3 %/estrella) · además DEF de primera línea +35 % |
| Valkyra | Momentum | −21 % | **todo el daño**, propia (−3 %/estrella) · además provocación a 2 enemigos |
| Gracie · Noelle | Calm Breakthrough · Killing Instinct | −16,3 % | **solo monstruos**, permanente (−4 %/estrella) |
| Viper | Nightfall's Shelter | −15,6 % | **todo el daño**, primera línea, permanente (−2 %/estrella) |

→ Solo **Admira, Viper, Marcus y Valkyra** aguantan contra jugadores. Todo lo demás de esta lista reduce daño de monstruos y no hace nada en la arena.

## 5. Bonificaciones y penalizaciones

| Héroe | Habilidad | Efecto | Detalle |
|-------|-----------|--------|---------|
| Cassidy | Border Hold | DEF propia +70 % | +10 %/estrella: la mayor bonificación individual |
| Marcus | Undying Creed | DEF de primera línea +35 %, 1 turno | estrellas: todos los aliados, 2 turnos |
| Strike | Declaration of Invincibility | DEF de primera línea +23,5 %, 1 turno | no acumulable (4★: 2 turnos) |
| Loki | Frenzied Beat | todos los aliados ATQ +11,5 %, 1 turno | estrellas: escalones de +2 %, crítico +10 %, 2 turnos |
| Clara | Vital Drain | los monstruos reciben +12 % de daño, 2 turnos | además +52 % de pan/hierro/oro de monstruos |
| Admira | Governing Edge | daño mágico enemigo −12 %, 2 turnos | todos los enemigos |
| Valkyra | Speedy Charge | ATQ enemigo −11,5 %, 2 turnos | provocación a 2 objetivos (hasta 4 por estrellas) |
| Valkyrie | Suppressive Fire | DEF del objetivo −10 %, 1 turno | desde ★2 (4★: −15 %) |
| Gracie | Duel Moment | aliados de la línea trasera +10,2 % de daño a monstruos | 1 turno (4★: 2 turnos) |

## 6. Crítico y bonificaciones propias permanentes

| Héroe | Habilidad | Efecto | Por estrella |
|-------|-----------|--------|--------------|
| Rosa | Deadly Hunt | crítico +30 % | +3 %: la pasiva de crítico más alta |
| Grace | Path of Vengeance | ATQ propio +30 % | +4 % |
| Ella | Jungle Rage | daño de energía propio +28 % | +3 % |
| Jessica | Crit Frenzy | crítico +26 % | +3 % |
| Bella | Ignited Courage | daño a monstruos +20,6 % | +4 % |
| Sonic | Lightning Speed | daño de energía propio +20 % | +3 % |
| Sagitta | Hunter Instinct | crítico +20 % | +3 % |
| Clara | Battlefield Angel | daño a monstruos +16,4 % | +2 % · además el bono de botín |
| Scarlett | Burning Resolve | daño a monstruos +16,3 % | +4 % |
| Leora | Reserve Magazine | ATQ propio +15,4 % | +3 % |
| Noctina · Valkyrie | Nightfall · Tactical Guidance | ATQ propio +15,2 % | +3 % |
| Irena | Absolute Order | Guardians de la línea trasera +13 % de daño a monstruos | +2 % |

## 7. Qué significa para tu orden de desarrollo

- **La cifra individual más alta pertenece a un Support.** El Vital Drain de Clara pega al 670 %, pero elige objetivo al azar. El golpe **dirigible** más alto es el Killshot Lock de Rosa con 614 %, y es el único que salpica a la línea trasera.
- **Contra un solo jefe, las habilidades de objetivo aleatorio se vuelven de objetivo único.** Eso da la vuelta a la clasificación: en el World Boss, los 1.188 % por lanzamiento de Rosa (1.980 % en cuanto ★4 sube el límite de ataques a 5) y los 936 % de Ella caen todos sobre el mismo cuerpo, muy por delante de cualquier golpe único.
- **El área solo paga con varios enemigos:** Jessica y Admira para Frenzied Boss, Storm Rescue y las arenas; contra un solo jefe, sus habilidades a todos los enemigos son apenas un golpe pequeño.
- **El crítico multiplica todo lo anterior.** Rosa (+30 %) y Jessica (+26 %) son el núcleo de crítico; las estrellas en ellas valen más que en un héroe con pasiva plana de ATQ.
- **Dos listas, dos propósitos.** La reducción de daño y el daño a monstruos son el kit de World Boss, rallys y radar; el golpe único y el crítico, el kit de arena — la misma división que S frente a S+ en la base de datos de héroes.

## 8. Lista de comprobación

- [ ] Valores de ATQ leídos en la pestaña Hero antes de fiarse de una clasificación de multiplicadores
- [ ] Combate de jefe → héroe de golpes múltiples alineado (Rosa, Ella, Sagitta), no un nuker de objetivo único
- [ ] Varios enemigos → área alineada (Jessica, Admira, Eileen)
- [ ] Defensa de arena → como reducción solo cuentan Admira, Viper, Marcus, Valkyra
- [ ] Eventos de monstruos → alineados los héroes con bono contra monstruos, no los kits de arena S+
- [ ] Estrellas primero en las portadoras de crítico, después en las pasivas planas de ATQ
