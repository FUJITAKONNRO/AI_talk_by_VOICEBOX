import requests

text = "こんにちは、これはテスト音声です。"
speaker = 1  # ずんだもん(ノーマル)

# ① audio_query を取得
query = requests.post(
    "http://127.0.0.1:50021/audio_query",
    params={"text": text, "speaker": speaker}
)

# ② synthesis（Content-Type を必ず指定）
synthesis = requests.post(
    "http://127.0.0.1:50021/synthesis",
    params={"speaker": speaker},
    data=query.text,  # ← json() ではなく text で渡す
    headers={"Content-Type": "application/json"}
)

# ③ 出力
with open("test.wav", "wb") as f:
    f.write(synthesis.content)
print(query.status_code)
print(query.text[:200])
print("OK: test.wav を出力しました")
