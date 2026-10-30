# 🤖 AI 비서 앱 - IT 학습 시간 분석 및 대화형 AI

> FastAPI + Firebase + OpenAI GPT를 활용한 학습 시간 분석 및 AI 채팅 애플리케이션

## 📋 프로젝트 개요

### 목표
- **IT 학습 시간 데이터** (2026-07-01 ~ 2026-09-30, 66개 포인트)를 시각화 및 분석
- **OpenAI GPT**와 대화하며 학습 데이터에 대한 인사이트 획득
- **Function Calling** (보너스)을 통해 AI가 자동으로 데이터 조회 및 분석

### 주요 기능

#### 필수 기능
1. **데이터 관리**
   - 학습 시간 데이터 CRUD (생성, 조회, 수정, 삭제)
   - Firestore에 저장

2. **AI 채팅**
   - OpenAI GPT와 대화
   - 학습 데이터 컨텍스트 자동 주입
   - 대화 기록 저장/조회

3. **데이터 분석**
   - 총 학습 시간, 평균, 최대/최소값
   - 추세 분석 (상승/하락/유지)
   - 자동 요약 생성

#### 보너스 기능
- **Function Calling**: AI가 자동으로 데이터 조회 함수 호출
  - `get_data_summary()` - 데이터 요약
  - `get_study_statistics()` - 통계 정보
  - `get_recent_trend()` - 추세 분석


## 🚀 빠른 시작

### 1단계: 저장소 클론
```bash
git clone https://github.com/your-username/ai-secretary.git
cd ai-secretary

cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
