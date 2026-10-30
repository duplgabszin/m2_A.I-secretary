```markdown
# 🔧 환경 설정 가이드

이 문서는 **AI 비서 앱**을 로컬에서 실행하기 위한 단계별 설정 가이드입니다.

---

## 📋 사전 요구사항

### 필수 설치
- **Python 3.9+** (Windows/macOS/Linux)
- **Git** (버전 관리)
- **Node.js 18+** (선택사항, 프론트엔드 빌드 도구용)

### 필수 계정
- **Google 계정** (Firebase)
- **OpenAI 계정** (API 키)
- **GitHub 계정** (저장소 관리)
- **Render 계정** (백엔드 배포)
- **Vercel 계정** (프론트엔드 배포)

---

## 🔑 Step 1: Firebase 프로젝트 생성

### 1-1. Firebase 콘솔 접속
URL: https://console.firebase.google.com
→ Google 계정으로 로그인

code
📋 복사

### 1-2. 새 프로젝트 생성
1. "프로젝트 추가" 클릭
2. 프로젝트 이름: `ai-secretary`
3. "계속" → "프로젝트 만들기"
4. 완료 대기 (1-2분)

### 1-3. Firestore Database 생성
1. 왼쪽 메뉴 → "빌드" → "Firestore Database"
2. "데이터베이스 만들기" 클릭
3. 보안 규칙: **개발 모드** 선택 (테스트용)
4. 위치: **asia-northeast1** (서울) 선택
5. "데이터베이스 만들기" 클릭

### 1-4. 서비스 계정 키 생성
1. 왼쪽 메뉴 → "프로젝트 설정" (톱니바퀴)
2. "서비스 계정" 탭
3. "새 개인 키 생성" 클릭
4. JSON 파일 다운로드
5. 파일명: `firebase-key.json`
6. **안전한 폴더에 저장** (GitHub에 절대 올리지 말 것!)

### 1-5. 프로젝트 ID 확인
- 프로젝트 설정에서 "프로젝트 ID" 복사
- 예: `ai-secretary-12345`

---

## 🔑 Step 2: OpenAI API 키 발급

### 2-1. OpenAI 플랫폼 접속
URL: https://platform.openai.com
→ 계정 생성 또는 로그인