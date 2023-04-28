def predict_test_score(study_time, study_content, motivation):
    # 重み付け係数
    w1 = 0.4
    w2 = 0.3
    w3 = 0.3

    # 各変数に対するスコア
    score1 = study_time
    score2 = study_content
    score3 = motivation

    # 重み付けした総合スコアを計算
    total_score = w1 * score1 + w2 * score2 + w3 * score3

    # 総合スコアに対応するテスト点数を返す
    return int(total_score * 100)

a, b, c = map(int, input().split()) # 全て何%目標達成したか
# 少数に変更
a = 0.01 * a
b = 0.01 * b
c = 0.01 * c
print(predict_test_score(a, b, c))