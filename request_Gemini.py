import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# 1. .envファイルを読み込む
load_dotenv()

# 2. クライアントの初期化
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise ValueError("APIキーが見つかりません。.envを確認してください")

client = genai.Client(api_key=api_key)

def words(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=prompt, 
            config=types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(thinking_budget=0) # Disables thinking
            ),
        )
        print(response.text)
        return response.text
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return ""  # エラー時は空文字列を返す
