import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. .envファイルを読み込む
load_dotenv()

# 2. 環境変数からAPIキーを取得する
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("APIキーが見つかりません。.envファイルを確認してください。")

# 3. Geminiの設定
genai.configure(api_key=api_key)

# 4. 実行テスト
model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("Pythonの.envファイルとは何ですか？一言で答えて。")
print(response.text)