import simpleaudio as sa
import request_Gemini as rGem
import request_VOICEVOX as rVOICE

# Gemini からテキストを取得
prompt = "Please list three completely random, unrelated words in Japanese. Please output only the words, separated by spaces, without any descriptions or greetings."
text = rGem.words(prompt)
speaker = 1  # ずんだもん(ノーマル)

# 音声ファイルをリストの要素ごとに生成して保存

for i, word in enumerate(text):
    wav_data = rVOICE.voice(word, speaker)
    filename = f"test_{i}.wav"
    with open(filename, "wb") as f:
        f.write(wav_data)
    print(f"OK: {filename} を出力しました")

# 音声ファイルをすべて３秒ずつ再生
for i in range(len(text)):
    filename = f"test_{i}.wav"
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
    print(f"再生中: {filename}")
    sa.sleep(3)  # 3秒待機

print("再生が終了しました")
