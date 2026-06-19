---
title: Cap Refrigerator
emoji: 🍅
colorFrom: green
colorTo: yellow
sdk: docker
pinned: false
---

# capstone-ai
캡스톤 ai파트

🥗 Capstone Project: AI 기반 음식 분석 및 맞춤형 추천 시스템
📌 프로젝트 개요

사용자가 음식 이미지 또는 텍스트를 입력하면 AI가 식재료를 분석하고, 공공데이터 API를 기반으로 정확한 영양 정보를 추출합니다.

이후 LangChain 기반 AI Food Agent가 사용자의 취향 정보와 영양 데이터를 종합 분석하여 맞춤형 요리 및 건강 활용법을 추천하는 AI 시스템입니다.

🏗️ System Architecture
Frontend (React)
        │
        ▼
Backend (Java Spring)
- 사용자 인증 및 세션 관리
- 사용자 선호도 저장
- AI 서버와 데이터 통신
        │
        ▼
AI Server (FastAPI)
        │
        ├─ STEP 1. Gemini 2.5 Flash
        │     └─ 음식 이미지/텍스트 분석
        │        - Keyword 추출
        │        - Food Group 분류
        │        - Subgroup 분류
        │
        ├─ STEP 2. Public Nutrition API
        │     └─ 식약처 공공데이터 검색
        │        - Score 기반 후보군 추출
        │        - 원재료 우선 매칭
        │
        ├─ STEP 3. AI Refinement
        │     └─ Gemini Self-Correction
        │        - API 결과 검증
        │        - 부족한 데이터 보정
        │        - 표준 JSON 생성
        │
        ▼
LangChain Food Recommendation Agent
        │
        ├─ 사용자 취향 분석
        ├─ 영양 데이터 기반 판단
        ├─ 요리 3종 추천
        └─ JSON 구조화 응답
🚀 주요 기능 (Features)
1. Intelligent Food Analysis
Gemini 2.5 Flash 기반 음식 인식

이미지 및 텍스트를 분석하여 음식 정보를 구조화합니다.

출력 예시:

[
  {
    "keyword": "시금치",
    "group": "농축수산물",
    "subgroup": "채소류"
  }
]
2. Hybrid Nutrition Data Pipeline

AI와 공공데이터를 결합한 하이브리드 영양 분석 시스템입니다.

데이터 흐름
Food Input
     |
     ▼
Gemini Analysis
     |
     ▼
식약처 공공데이터 API
     |
     ▼
Score-Based Matching
     |
     ▼
Gemini Validation
     |
     ▼
Final Nutrition JSON

특징:

공공데이터 API 기반 실제 영양 정보 활용
Score 알고리즘을 통한 유사 데이터 선별
원재료(생것) 우선 가중치 적용
API 검색 실패 시 Gemini 지식 기반 보정
3. LangChain 기반 맞춤형 Food Agent
입력 데이터
user_id
user_preference (한식, 양식, 일식 등)
food_name
category
nutrition_data
AI Agent 역할

AI Food Consultant Persona를 적용하여:

사용자 음식 취향 분석
영양 성분 고려
건강한 조리 방법 추천
요리 3가지 생성
4. Structured JSON Response

Pydantic + JsonOutputParser를 사용하여 AI 응답을 Java Backend가 바로 처리 가능한 JSON 형태로 변환합니다.

예시:

{
  "recommendations": [
    {
      "dish_name": "시금치 파스타",
      "additional_ingredients": [
        "올리브오일",
        "마늘"
      ],
      "health_benefits": "철분과 식이섬유 섭취에 도움",
      "recipe_tip": "센 불에서 짧게 조리하여 영양 손실 최소화"
    }
  ]
}
📡 API Endpoints
음식 분석 API
POST /analyze

입력:

이미지 파일
음식 텍스트

출력:

정제된 영양 성분 JSON
특정 음식 기반 추천 API
POST /fdmake

입력:

{
    "user_id": "user1",
    "food_name": "시금치",
    "cat": "채소류",
    "user_preference": "양식",
    "nutrition_data": {}
}

출력:

개인 맞춤 요리 추천 3개
냉장고 기반 전체 재료 추천 API
POST /api/recommend

입력:

{
    "user_id": "user1",
    "user_preference": "한식",
    "ingredients": [
        "계란",
        "양파",
        "감자"
    ]
}

출력:

보유 식재료 기반 맞춤 레시피 추천
🔑 Environment Setting

프로젝트 루트에 api_key.txt 생성

GEMINI_API_KEY=YOUR_GEMINI_API_KEY
FOOD_NUTRITION_API_KEY=YOUR_PUBLIC_API_KEY

실행 전 해당 파일 경로가 올바르게 설정되어 있는지 확인합니다.

🛠️ Tech Stack
AI Server
Python
FastAPI
Gemini 2.5 Flash
LangChain
Pydantic

💡 핵심 기술 포인트
Multi-stage AI Pipeline
Gemini → Public API → Gemini Refinement 구조
Hybrid AI + Public Data Architecture
LLM의 추론 능력과 실제 영양 DB 결합
LangChain Agent Personalization
사용자 취향 및 영양 데이터를 기반으로 맞춤 추천
Structured AI Output
Pydantic + JsonOutputParser를 통한 안정적인 백엔드 연동
