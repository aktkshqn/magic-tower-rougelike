
# -機能-
# common：複数画面で使う共通表示
# menu：タイトルやメニュー
# character：冒険者作成
# exploration：移動や探索
# encounter：敵との遭遇
# combat：戦闘
# skill：スキル
# map：地図
# save：保存と読み込み
# game：開始、終了、勝敗
# -種類-
# prompt：入力を求める
# info：通常案内
# success：成功
# warning：注意
# error：失敗や不正入力
# result：計算結果
# confirm：確認 

MESSAGE_TEMPLATES = {
    # 共通
    "common.prompt.continue": "[Enter]で進む",
    "common.error.invalid_input": "その内容は選べない",

    # タイトルメニュー
    "menu.prompt.select": "番号を入力せよ：",
    "menu.error.invalid_choice": "表示された番号から選んでください。",
    "menu.confirm.selected": "「{option_label}」でよろしいですか？",
    "menu.confirm.yes": "はい",
    "menu.confirm.no": "いいえ",

    # ゲーム進行
    "game.info.start": "新しい冒険を始めます。",
    "game.info.exit": "ゲームを終了します。",
    "game.result.victory": "魔法の塔からの脱出に成功した！",
    "game.result.defeat": "{player_name}の冒険は、ここで終わった……",

    # 冒険者作成
    "character.prompt.name": "目覚めた者の名前は...：",
    "character.error.empty_name": "名前を空にはできません。",
    "character.error.name_too_long": "名前は12文字以内で入力してください。",
    "character.success.to_create": "「{player_name}...」その名前で間違いないか？",
    "character.success.created": "冒険者「{player_name}」が誕生した！",

    # 探索
    "exploration.info.move": "{direction}へ進んだ。",
    "exploration.warning.blocked": "その方向には進めない。",
    "exploration.info.new_area": "新しい場所を発見した。",

    # エンカウント
    "encounter.info.enemy_appeared": "{enemy_name}が現れた！",
    "encounter.info.remaining": "この階の残り敵数：{remaining}",

    # 戦闘
    "combat.prompt.action": "行動を選択してください：",
    "combat.result.damage": "{attacker}は{target}に{damage}のダメージ！",
    "combat.result.heal": "{target}のHPが{amount}回復した。",
    "combat.error.not_enough_mp": "MPが足りない。",
    "combat.result.enemy_defeated": "{enemy_name}を倒した！",

    # スキル
    "skill.prompt.select": "習得するスキルを選んでください：",
    "skill.success.learned": "{skill_name}を習得した！",
    "skill.error.already_learned": "そのスキルは習得済みです。",

    # 地図
    "map.info.inherited": "過去の冒険者が残した地図を受け継いだ。",
    "map.info.updated": "地図に新しい情報が記録された。",

    # 保存
    "save.success.completed": "進行状況を保存しました。",
    "save.error.broken_file": "保存データを読み込めませんでした。",
}

def get_message(message_key, **values):
    if message_key not in MESSAGE_TEMPLATES:
        raise KeyError(
            f"メッセージが登録されていません: {message_key}"
        )

    template = MESSAGE_TEMPLATES[message_key]

    return template.format(**values)
