# Recommendation System

このプロジェクトは、学生の情報に基づいて適切な求人情報を推薦するシステムです。PythonとDockerを使用して実装されており、Docker Composeを使用して環境を簡単に管理・実行できます。

## プロジェクト構成
```recommendation_system/
├── data/
│ ├── students.csv
│ └── jobs.csv
├── src/
│ ├── recommend.py
│ ├── train_model.py
│ └── utils.py
├── .gitignore
├── Dockerfile
├── requirements.txt
└── README.md
```

## 実行方法
```terminal
docker build -t recommendation_system .
docker run --rm recommendation_system 1
```