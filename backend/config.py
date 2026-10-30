import os
from dotenv import load_dotenv
import json

load_dotenv()

# OpenAI 설정
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = "gpt-4o-mini"  # 비용 절감용 모델

# Firebase 설정
FIREBASE_SERVICE_ACCOUNT_JSON = os.getenv("FIREBASE_SERVICE_ACCOUNT_JSON")

# CORS 설정
ALLOWED_ORIGINS = os.getenv(
    "ALLOWED_ORIGINS",
    "http://localhost:3000,http://localhost:8000"
).split(",")

# API 설정
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")

# Firebase 서비스 계정 키 파싱
def get_firebase_credentials():
    """환경변수에서 Firebase 서비스 계정 키 로드"""
    if not FIREBASE_SERVICE_ACCOUNT_JSON:
        raise ValueError("FIREBASE_SERVICE_ACCOUNT_JSON 환경변수가 설정되지 않았습니다.")
    
    try:
        # JSON 문자열을 딕셔너리로 변환
        credentials = json.loads(FIREBASE_SERVICE_ACCOUNT_JSON)
        return credentials
    except json.JSONDecodeError:
        raise ValueError("FIREBASE_SERVICE_ACCOUNT_JSON이 유효한 JSON이 아닙니다.")