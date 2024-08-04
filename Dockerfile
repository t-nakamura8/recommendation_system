# ベースイメージ
FROM python:3.9

# 作業ディレクトリの設定
WORKDIR /app

# 依存関係のコピーとインストール
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのコピー
COPY . .

# エントリポイントの設定
ENTRYPOINT ["python", "src/recommend.py"]

# デフォルトコマンドの設定（引数がない場合のデフォルト）
CMD ["1"]