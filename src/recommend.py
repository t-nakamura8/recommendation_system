from utils import load_data, preprocess_data
from train_model import train_model, get_recommendations
import sys

# コマンドライン引数から学生IDを取得
if len(sys.argv) < 2:
    print("学生IDを指定してください。")
    sys.exit(1)

student_id = int(sys.argv[1])

# データの読み込み
students = preprocess_data(load_data('/app/data/students.csv'))
jobs = preprocess_data(load_data('/app/data/jobs.csv'))

# モデルのトレーニング
tfidf_matrix_students, tfidf_matrix_jobs, tfidf = train_model(students, jobs)

# 推薦の取得
recommendations = get_recommendations(
    student_id, students, jobs, tfidf_matrix_students, tfidf_matrix_jobs)

# 推薦結果の表示
print(f"Recommendations for student {student_id}:")
print(recommendations[['職種', '仕事内容', '会社情報', '必要経験', '必要言語']])
