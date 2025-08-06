import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import base64
from io import BytesIO
import os

# macOS 한글 폰트 경로
KOR_FONT_PATH = '/System/Library/Fonts/AppleGothic.ttf'

# 파일 경로
file_path = '[Bonibello] Seller Survey🫶 - 시트1 (1).csv'
df = pd.read_csv(file_path, header=2)

# 결과 HTML
html = """
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>Bonibello Seller Survey 전체 리포트</title>
  <style>
    body { font-family: 'Noto Sans KR', sans-serif; background: #f8f9fa; margin: 0; padding: 0; }
    .container { max-width: 900px; margin: 40px auto; background: #fff; border-radius: 16px; box-shadow: 0 2px 16px rgba(0,0,0,0.07); padding: 32px; }
    h1 { text-align: center; color: #4e79a7; }
    .question-block { margin-bottom: 48px; padding: 24px; border-radius: 12px; background: #f8f9fa; box-shadow: 0 2px 8px rgba(0,0,0,0.04); }
    .question-block h2 { font-size: 1.1rem; margin-bottom: 8px; }
    .insight { font-weight: bold; margin-bottom: 16px; color: #4e79a7; }
    .text-answers ul { margin: 0; padding-left: 20px; }
    .text-answers li { margin-bottom: 6px; color: #333; }
    .chart-img { width: 100%; max-width: 500px; margin: 0 auto 24px auto; display: block; }
    .wordcloud-img { width: 100%; max-width: 500px; margin: 0 auto 24px auto; display: block; }
  </style>
</head>
<body>
  <div class="container">
    <h1>Bonibello Seller Survey 전체 리포트</h1>
"""

# 분석 시작 (메타데이터 3개 컬럼 제외)
for col in df.columns[3:]:
    col_data = df[col].dropna().astype(str)
    html += f'<div class="question-block">\n'
    html += f'<h2>{col}</h2>\n'
    # 복수선택형(쉼표 포함) 자동 감지
    if col_data.str.contains(',').any() and col_data.nunique() > 10:
        all_choices = col_data.str.split(',').explode().str.strip()
        value_counts = all_choices.value_counts()
        top = value_counts.idxmax()
        top_pct = value_counts.max() / value_counts.sum() * 100
        insight = f"가장 많은 응답: '{top}' ({top_pct:.1f}%)"
        html += f'<div class="insight">{insight}</div>\n'
        # Bar 차트
        plt.figure(figsize=(6,3))
        value_counts.head(10).plot(kind='bar', color='#4e79a7')
        plt.title('')
        plt.tight_layout()
        plt.xticks(fontname='AppleGothic')
        buf = BytesIO()
        plt.savefig(buf, format='png')
        plt.close()
        img_str = base64.b64encode(buf.getvalue()).decode()
        html += f'<img class="chart-img" src="data:image/png;base64,{img_str}"/>'
    elif col_data.nunique() < 10 and col_data.str.isnumeric().all():
        # 평가형(1~5점 등)
        value_counts = col_data.value_counts().sort_index()
        avg = col_data.astype(float).mean()
        insight = f"평균 점수: {avg:.2f}점 (5점 만점)"
        html += f'<div class="insight">{insight}</div>\n'
        # Bar 차트
        plt.figure(figsize=(6,3))
        value_counts.plot(kind='bar', color='#4e79a7')
        plt.title('')
        plt.tight_layout()
        plt.xticks(fontname='AppleGothic')
        buf = BytesIO()
        plt.savefig(buf, format='png')
        plt.close()
        img_str = base64.b64encode(buf.getvalue()).decode()
        html += f'<img class="chart-img" src="data:image/png;base64,{img_str}"/>'
    elif col_data.nunique() < 20:
        # 객관식
        value_counts = col_data.value_counts()
        top = value_counts.idxmax()
        top_pct = value_counts.max() / value_counts.sum() * 100
        insight = f"가장 많은 응답: '{top}' ({top_pct:.1f}%)"
        html += f'<div class="insight">{insight}</div>\n'
        # Pie 차트
        plt.figure(figsize=(5,5))
        value_counts.plot(kind='pie', autopct='%1.1f%%', colors=['#4e79a7','#f28e2b','#e15759','#76b7b2','#59a14f','#edc949','#af7aa1','#ff9da7','#9c755f','#bab0ab'])
        plt.ylabel('')
        plt.tight_layout()
        plt.xticks(fontname='AppleGothic')
        buf = BytesIO()
        plt.savefig(buf, format='png')
        plt.close()
        img_str = base64.b64encode(buf.getvalue()).decode()
        html += f'<img class="chart-img" src="data:image/png;base64,{img_str}"/>'
    else:
        # 주관식/서술형
        insight = f"주요 의견 예시:"
        html += f'<div class="insight">{insight}</div>\n'
        # 워드클라우드
        text = ' '.join(col_data)
        if text.strip():
            try:
                wc = WordCloud(font_path=KOR_FONT_PATH, width=500, height=300, background_color='white').generate(text)
                buf = BytesIO()
                wc.to_image().save(buf, format='PNG')
                img_str = base64.b64encode(buf.getvalue()).decode()
                html += f'<img class="wordcloud-img" src="data:image/png;base64,{img_str}"/>'
            except Exception as e:
                html += f'<div style="color:red">워드클라우드 생성 오류: {e}</div>'
        # 대표 의견 5개
        html += '<div class="text-answers"><ul>'
        for txt in col_data.head(5):
            html += f'<li>{txt}</li>'
        html += '</ul></div>\n'
    html += '</div>\n'

html += """
  </div>
</body>
</html>
"""

with open('bonibello_survey_report_full.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("bonibello_survey_report_full.html 생성 완료!") 