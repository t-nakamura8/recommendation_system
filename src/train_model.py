from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pandas as pd


def train_model(students, jobs):
    # 特徴量を結合
    students['features'] = students['志望職種'] + ' ' + \
        students['業務関心'] + ' ' + students['言語']
    jobs['features'] = jobs['職種'] + ' ' + jobs['仕事内容'] + ' ' + jobs['必要言語']

    # 学生と求人の特徴量を結合
    combined_features = pd.concat([students['features'], jobs['features']])

    # TF-IDFベクトライザーのセットアップ
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(combined_features)

    # 学生と求人のTF-IDFベクトルを分割
    tfidf_matrix_students = tfidf_matrix[:len(students)]
    tfidf_matrix_jobs = tfidf_matrix[len(students):]

    return tfidf_matrix_students, tfidf_matrix_jobs, tfidf


def get_recommendations(student_id, students, jobs, tfidf_matrix_students, tfidf_matrix_jobs):
    cosine_sim = linear_kernel(
        tfidf_matrix_students[student_id], tfidf_matrix_jobs)
    sim_scores = list(enumerate(cosine_sim[0]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[:10]
    job_indices = [i[0] for i in sim_scores]
    return jobs.iloc[job_indices]
