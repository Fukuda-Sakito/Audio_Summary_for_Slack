import openai
import requests
import os
from requests.structures import CaseInsensitiveDict
openai.api_key = "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"

# 音声ファイルを読み込み
with open("木曜日（10-02）.txt", "r") as f:
    audio_file = f.read()

# 音声からテキストを生成
response = openai.Completion.create(
    engine="davinci",
    prompt="Transcribe the following audio:\n",
    audio='audio_file.txt',
    max_tokens=2048
)

# テキストをファイルに書き出し
with open("output.txt", "w") as f:
    f.write(response.choices[0].text)
