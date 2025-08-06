import pandas as pd
import re

# Load fetching DB
fetching = pd.read_csv('Bonibello Pricing/fetching_products_unique_nokids_with_korean.csv')

def clean_product_name(name):
    name = re.sub(r'\b(SS|FW|F/W|S/S|FW\d{2}|SS\d{2}|\d{2}FW|\d{2}SS|컬렉션|라인|에디션|한정판|정품|새상품|미사용|\d{4}|\d{2})\b', '', str(name), flags=re.IGNORECASE)
    name = re.sub(r'\(.*?\)', '', name)
    name = re.sub(r'\[.*?\]', '', name)
    name = re.sub(r'[^\w\s가-힣a-zA-Z0-9]', '', name)
    name = re.sub(r'\s+', ' ', name)
    return name.strip()

def similar(a, b):
    from difflib import SequenceMatcher
    return SequenceMatcher(None, str(a).lower(), str(b).lower()).ratio()

fetching['상품명_clean'] = fetching['상품명'].apply(clean_product_name)
fetching['할인후가격'] = fetching['할인후가격'].replace(',', '', regex=True).astype(float)

# CATEGORY_SYNONYMS for '상의' group, including '폴로셔츠'
synonyms = ['상의', '티셔츠', '셔츠', '블라우스', '니트', '스웨터', '맨투맨', '후드', '폴로셔츠']

# 브랜드 매핑: 몽클레어, 몽클레어 앙팡, moncler, moncler enfant
brand_variants = ['몽클레어', '몽클레어 앙팡', 'moncler', 'moncler enfant']
brand_variants_lower = [b.replace(' ', '').lower() for b in brand_variants]

# 타겟 정보
brand = '몽클레어'
category = '폴로셔츠'
target_name = f'{brand} {category}'

# 유사도 계산
fetching['brand_sim'] = fetching.apply(lambda row: max(similar(str(row['브랜드']), brand), similar(str(row['브랜드(국문)']), brand)), axis=1)

# 필터: 브랜드 유사도 0.7 이상 & 카테고리 그룹 키워드 포함 & 가격 있음
candidates = fetching[
    (fetching['brand_sim'] >= 0.7) &
    (fetching['상품명_clean'].str.replace(' ', '').str.lower().apply(lambda x: any(s in x for s in synonyms))) &
    (fetching['할인후가격'].notna() & (fetching['할인후가격'] > 0))
].copy()

print('--- Fetching DB (상품명 유사도 조건 제거) ---')
print(candidates[['상품명','브랜드','브랜드(국문)','할인후가격','brand_sim']].to_string(index=False))
if len(candidates) > 0:
    print(f'\n평균: {round(candidates["할인후가격"].mean()/1000)*1000}')
else:
    print('\n매칭 결과 없음')

# --- MNKL DB에서 713,000 산출 데이터 확인 ---
mnkl = pd.read_csv('Bonibello Pricing/mnkl_products_processed_v3.csv')
mnkl['name_clean'] = mnkl['name'].apply(clean_product_name)
mnkl_synonyms = synonyms
mnkl_matches = mnkl[
    (mnkl['brand'].str.replace(' ', '').str.lower() == '몽클레어'.replace(' ', '').lower()) &
    (mnkl['name_clean'].str.replace(' ', '').str.lower().apply(lambda x: any(s in x for s in mnkl_synonyms)))
]
mnkl_matches = mnkl_matches[mnkl_matches['consumer_price'].notna() & (mnkl_matches['consumer_price'] > 0)]
print('--- MNKL DB (MSRP 산출 근거) ---')
print(mnkl_matches[['name','brand','category','size','consumer_price']].to_string(index=False))
if len(mnkl_matches) > 0:
    print('\n평균:', round(mnkl_matches['consumer_price'].mean()/1000)*1000)
else:
    print('\n매칭 결과 없음')

# --- 쁘띠바또 집업베스트 분석 ---
fetching = pd.read_csv('Bonibello Pricing/fetching_products_unique_nokids_with_korean.csv')
fetching['상품명_clean'] = fetching['상품명'].apply(clean_product_name)
fetching['할인후가격'] = fetching['할인후가격'].replace(',', '', regex=True).astype(float)

synonyms = ['상의', '티셔츠', '셔츠', '블라우스', '니트', '스웨터', '맨투맨', '후드', '베스트', '집업베스트']
brand = '쁘띠바또'
fetching['brand_sim'] = fetching.apply(lambda row: max(similar(str(row['브랜드']), brand), similar(str(row['브랜드(국문)']), brand)), axis=1)

candidates = fetching[
    (fetching['brand_sim'] >= 0.7) &
    (fetching['상품명_clean'].str.replace(' ', '').str.lower().apply(lambda x: any(s in x for s in synonyms))) &
    (fetching['할인후가격'].notna() & (fetching['할인후가격'] > 0))
].copy()

print('--- Fetching DB (쁘띠바또 집업베스트) ---')
print(candidates[['상품명','브랜드','브랜드(국문)','할인후가격','brand_sim']].to_string(index=False))
if len(candidates) > 0:
    print(f'\n평균: {round(candidates["할인후가격"].mean()/1000)*1000}')
else:
    print('\n매칭 결과 없음') 