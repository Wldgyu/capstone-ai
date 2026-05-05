# capstone-ai
캡스톤 ai파트

1. 간단한 설명
공공데이터 API를 통해 정확한 영양 성분을 추출하며, 나아가 사용자 맞춤형 음식 효능 및 활용 방법을 제안하는 AI 에이전트입니다.

2. 주요 기능 (Features)
개발하신 코드의 핵심 로직을 섹션으로 나누어 설명하세요.

Intelligent Image Analysis: Gemini 2.5 Flash를 활용한 식재료/음식 자동 분류 (Keyword, Group, Subgroup 추출).

Hybrid Data Pipeline: 공공데이터 API(식품의약품안전처)와 LLM의 지식을 결합한 하이브리드 영양 정보 검색 시스템.

Data Refinement: API 검색 결과가 부정확할 경우, LLM이 스스로 데이터를 검토하고 보정(Self-correction)하여 정제된 JSON 출력.

3. 데이터 파이프라인 구조 (Architecture)
텍스트로 흐름을 명시하면 전문가적인 느낌을 줍니다.

Input: 음식 이미지 혹은 텍스트 입력.

Step 1 (Gemini): 이미지 분석 및 검색 키워드 정제.

Step 2 (API): 공공데이터 API 연동 및 후보군 추출 (Score-based Matching).

Step 3 (Refinement): LLM을 통한 최종 데이터 검증 및 JSON 생성.

제마나이 apikey 받아오고 그다음 공공데이터 apikey 를 txt 파일에 넣습니다
ex)
GEMINI_API_KEY= apikey넣기
FOOD_NUTRITION_API_KEY= apikey넣기

넣은 txt 파일을 코랩 드라이브에 넣고 실행 하면 됩니다. 오류 발생시 apikey.txt 파일 경로 를 제대로 넣었는지 확인
