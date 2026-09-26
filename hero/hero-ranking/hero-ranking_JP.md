# ヒーロー序列 — 誰が一番強く殴り、誰が一番長く耐えるか (Last Light)

## 1. この一覧の読み方

- **ダメージ = スキル倍率 × そのヒーローの ATK。** ここで並べているのは記録された倍率であって、最終的なダメージではない — 弱いヒーローの 670 % スキルは、強いヒーローの 512 % スキルに負ける。
- **星効果は足し込んでいない。** ゲームは階段（+30/70/120/185/270 %）として表示するだけで、段が前の値を置き換えるのか上に積むのかを書いていない。基礎値で並べるほうが順序として誠実であり、ヒーローごとの階段はヒーローデータベースにある。
- **Hero タブは未所持のヒーローでも ATK · HP · DEF · Soldier Capacity を表示する。** 本当のステータス序列はそこから作る。いまのところそう記録できているのは1体だけ: Rosa の Lv. 150 / 5★ — ATK 44.0K · HP 388.0K · DEF 5.2K · 兵士433 · CP 788,715。
- **被ダメ軽減は数字より適用範囲を読む。** 全ダメージ／物理のみ／エネルギーのみ／モンスターのみは別物であり、「モンスターのみ」はアリーナでは無価値。

## 2. 最も大きなダメージ — 単発

| ヒーロー | スキル | 基礎 | 備考 |
|----------|--------|------|------|
| Clara | Vital Drain (CS) | 670 % | 物理、**ランダム**対象 — 狙えない |
| Rosa | Killshot Lock (CS) | 614 % | エネルギー、単体 + 後列へ飛び散る |
| Ella | Forest Ambush | 512 % | エネルギー、単体 |
| Irena | Bounty Kill (CS) | 476 % | 物理。対象が倒れると**50 % で再発動** |
| Jessica | Sawblade Storm | 415 % | エネルギー、単体 |
| Viper | Decisive Raid | 388 % | 物理、単体 |
| Bella | Full Swing (CS) | 360 % | 物理 + ★2からスタン率 |
| Admira | Blade of Judgment | 330 % | 物理、単体 |
| Grace | Stealth Assassination | 323 % | エネルギー、**後列を優先**、スタン率 |

## 3. 最も大きなダメージ — 1回の発動あたり（多段・範囲）

| ヒーロー | スキル | 1回あたり | 散り方 |
|----------|--------|-----------|--------|
| Rosa | Twin-Gun Dance (CS) | 3 × 396 % = 1,188 % | ランダムな敵（★4から5回） |
| Ella | Phantom Volley (CS) | 8 × 117 % = 936 % | ランダム（星で12回、続いて16回） |
| Sagitta | Arrow Spray (CS) | 3 × 194 % = 582 % | ランダム3体 |
| Clara | Frontline Support | 2 × 273 % = 546 % | ランダム2体 |
| Noctina | Phantom Mirage (CS) | 2 × 142 % = 284 % | ランダム2体 |
| Leora | Bullet Storm (CS) | 4 × 63 % = 252 % | ランダム（星で6回、続いて8回） |
| Jessica | Chainsaw Carnival (CS) | 243 % | **敵全体** |
| Scarlett | Fireline Combo (CS) | 5 × 48 % = 240 % | ランダム（星で7回、続いて9回） |
| Victor | Cleanup Command (CS) | 2 × 108 % = 216 % | 2体（星で3体） |
| Eileen | Frontline Strafe (CS) | 177 % | **敵の1列まるごと** + その ATK −6 % |
| Admira | Governing Edge (CS) | 72 % | **敵全体** + その魔法DMG −12 % |

## 4. 最も耐える — 被ダメ軽減

| ヒーロー | スキル | 軽減 | 適用範囲 |
|----------|--------|------|----------|
| Admira | Fearless Heart | −28 % | エネルギーDMG、自身、常時（星ごとに −4 %） |
| Viper | Iron Grip | −26 % | 物理、前列、1ターン（星: 2ターン、味方全体） |
| Eileen | Wavebreaker | −25.5 % | **モンスターのみ**、常時（星ごとに −4 %） |
| Cassidy | Gunfire Verdict | −24 % | **モンスターのみ**、1ターン（星ごとに −4 %）· 加えて自身のDEF +70 % |
| Strike | Steady Steps | −21.5 % | **モンスターのみ**、常時（星ごとに −4 %） |
| Marcus | Fortification | −21 % | **全ダメージ**、自身（星ごとに −3 %）· 加えて前列DEF +35 % |
| Valkyra | Momentum | −21 % | **全ダメージ**、自身（星ごとに −3 %）· 加えて敵2体を挑発 |
| Gracie · Noelle | Calm Breakthrough · Killing Instinct | −16.3 % | **モンスターのみ**、常時（星ごとに −4 %） |
| Viper | Nightfall's Shelter | −15.6 % | **全ダメージ**、前列、常時（星ごとに −2 %） |

→ 対人で持ちこたえるのは **Admira・Viper・Marcus・Valkyra** だけ。ほかはすべてモンスター被ダメを下げるもので、アリーナでは何もしない。

## 5. バフとデバフ

| ヒーロー | スキル | 効果 | 詳細 |
|----------|--------|------|------|
| Cassidy | Border Hold | 自身のDEF +70 % | 星ごとに +10 % — 単体バフとして最大 |
| Marcus | Undying Creed | 前列DEF +35 %、1ターン | 星: 味方全体、2ターン |
| Strike | Declaration of Invincibility | 前列DEF +23.5 %、1ターン | 重複不可（4★: 2ターン） |
| Loki | Frenzied Beat | 味方全体 ATK +11.5 %、1ターン | 星: +2 % 刻み、クリティカル +10 %、2ターン |
| Clara | Vital Drain | モンスターの被ダメ +12 %、2ターン | 加えてモンスター撃破の食料・鉄・ゴールド +52 % |
| Admira | Governing Edge | 敵の魔法DMG −12 %、2ターン | 敵全体 |
| Valkyra | Speedy Charge | 敵の ATK −11.5 %、2ターン | 2体を挑発（星で最大4体） |
| Valkyrie | Suppressive Fire | 対象のDEF −10 %、1ターン | ★2から（4★: −15 %） |
| Gracie | Duel Moment | 後列の味方 +10.2 % 対モンスターDMG | 1ターン（4★: 2ターン） |

## 6. クリティカルと常時の自己バフ

| ヒーロー | スキル | 効果 | 星ごと |
|----------|--------|------|--------|
| Rosa | Deadly Hunt | クリティカル +30 % | +3 % — 最も高いクリティカルパッシブ |
| Grace | Path of Vengeance | 自身の ATK +30 % | +4 % |
| Ella | Jungle Rage | 自身のエネルギーDMG +28 % | +3 % |
| Jessica | Crit Frenzy | クリティカル +26 % | +3 % |
| Bella | Ignited Courage | 対モンスターDMG +20.6 % | +4 % |
| Sonic | Lightning Speed | 自身のエネルギーDMG +20 % | +3 % |
| Sagitta | Hunter Instinct | クリティカル +20 % | +3 % |
| Clara | Battlefield Angel | 対モンスターDMG +16.4 % | +2 % · 加えて戦利品ボーナス |
| Scarlett | Burning Resolve | 対モンスターDMG +16.3 % | +4 % |
| Leora | Reserve Magazine | 自身の ATK +15.4 % | +3 % |
| Noctina · Valkyrie | Nightfall · Tactical Guidance | 自身の ATK +15.2 % | +3 % |
| Irena | Absolute Order | 後列の Guardians +13 % 対モンスターDMG | +2 % |

## 7. 育成順序への意味

- **単発の最大値を持つのはサポート。** Clara の Vital Drain は 670 % で殴るが、対象はランダム。**狙える**最大の一撃は Rosa の Killshot Lock の 614 % で、後列へ飛び散るのはこれだけ。
- **ボス1体が相手なら、ランダム対象スキルは単体スキルになる。** これが序列をひっくり返す。World Boss では Rosa の1発動あたり 1,188 %（★4で攻撃上限が5になれば 1,980 %）と Ella の 936 % がすべて同じ体に入り、どの単発よりはるかに上に来る。
- **範囲攻撃は敵が複数いるときだけ得になる:** Frenzied Boss・Storm Rescue・アリーナでは Jessica と Admira。ボス1体が相手なら、敵全体スキルは小さな単発にすぎない。
- **クリティカルはその上のすべてを掛け算する。** Rosa（+30 %）と Jessica（+26 %）がクリティカルの核であり、平坦なATKパッシブのヒーローより星を注ぐ価値がある。
- **2つの一覧、2つの用途。** 被ダメ軽減と対モンスターDMGは World Boss・ラリー・レーダー用の一式、単発とクリティカルはアリーナ用の一式 — ヒーローデータベースの S と S+ の分かれ方と同じ。

## 8. チェックリスト

- [ ] 倍率の序列を信じる前に、自分の ATK を Hero タブで確認した
- [ ] ボス戦 → 多段ヒーロー（Rosa・Ella・Sagitta）を編成し、単体ニュカーにしていない
- [ ] 敵が複数 → 範囲（Jessica・Admira・Eileen）を編成した
- [ ] アリーナ防衛 → 被ダメ軽減として数えるのは Admira・Viper・Marcus・Valkyra だけ
- [ ] モンスター系イベント → S+ のアリーナ一式ではなく、モンスターボーナス持ちを編成した
- [ ] 星はまずクリティカルのキャリーへ、そのあと平坦なATKパッシブへ
