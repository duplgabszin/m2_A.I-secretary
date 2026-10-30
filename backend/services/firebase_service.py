import firebase_admin
from firebase_admin import credentials, firestore
from config import get_firebase_credentials
from datetime import datetime
from typing import List, Dict, Optional

# Firebase 초기화
try:
    creds = credentials.Certificate(get_firebase_credentials())
    firebase_admin.initialize_app(creds)
except ValueError as e:
    print(f"⚠️ Firebase 초기화 실패: {e}")
    print("환경변수 FIREBASE_SERVICE_ACCOUNT_JSON을 확인하세요.")

db = firestore.client()

class FirebaseService:
    """Firestore 데이터베이스 작업"""
    
    # ============ DATA CRUD ============
    
    @staticmethod
    def add_data(date: str, value: int, memo: str = "") -> Dict:
        """새 데이터 추가"""
        try:
            doc_ref = db.collection("data").document()
            data = {
                "date": date,
                "value": value,
                "memo": memo,
                "created_at": datetime.now(),
                "updated_at": datetime.now()
            }
            doc_ref.set(data)
            return {
                "id": doc_ref.id,
                "status": "success",
                "message": "데이터가 추가되었습니다.",
                **data
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    @staticmethod
    def get_all_data() -> List[Dict]:
        """모든 데이터 조회"""
        try:
            docs = db.collection("data").order_by("date").stream()
            data_list = []
            for doc in docs:
                data_dict = doc.to_dict()
                data_dict["id"] = doc.id
                data_list.append(data_dict)
            return data_list
        except Exception as e:
            print(f"데이터 조회 오류: {e}")
            return []
    
    @staticmethod
    def update_data(doc_id: str, date: str = None, value: int = None, memo: str = None) -> Dict:
        """데이터