from typing import List, Dict
from datetime import datetime
import statistics

class DataAnalyzer:
    """시계열 데이터 분석"""
    
    @staticmethod
    def analyze_data(data_list: List[Dict]) -> Dict:
        """데이터 분석 및 요약 생성"""
        
        if not data_list:
            return {
                "period": "데이터 없음",
                "count": 0,
                "metrics": {
                    "total": 0,
                    "average": 0,
                    "max": 0,
                    "min": 0
                },
                "trend": "분석 불가"
            }
        
        # 값 추출
        values = [item["value"] for item in data_list]
        dates = [item["date"] for item in data_list]
        
        # 기본 통계
        total = sum(values)
        average = round(total / len(values), 2)
        max_val = max(values)
        min_val = min(values)
        
        # 기간
        start_date = dates[0]
        end_date = dates[-1]
        period = f"{start_date} ~ {end_date}"
        
        # 추세 분석 (최근 vs 초기)
        mid_point = len(values) // 2
        first_half_avg = statistics.mean(values[:mid_point])
        second_half_avg = statistics.mean(values[mid_point:])
        
        if second_half_avg > first_half_avg:
            trend_direction = "상승"
            trend_percent = round(
                ((second_half_avg - first_half_avg) / first_half_avg) * 100, 1
            )
        elif second_half_avg < first_half_avg:
            trend_direction = "하락"
            trend_percent = round(
                ((first_half_avg - second_half_avg) / first_half_avg) * 100, 1
            )
        else:
            trend_direction = "유지"
            trend_percent = 0
        
        trend = f"{trend_direction} (월평균 {trend_percent:+.1f}%)"
        
        return {
            "period": period,
            "count": len(values),
            "metrics": {
                "total": total,
                "average": average,
                "max": max_val,
                "min": min_val
            },
            "trend": trend,
            "raw_data": {
                "first_half_avg": round(first_half_avg, 2),
                "second_half_avg": round(second_half_avg, 2)
            }
        }
    
    @staticmethod
    def get_summary_text(analysis: Dict) -> str:
        """분석 결과를 텍스트로 변환"""
        return f"""
[사용자 학습 데이터 요약]
- 데이터 기간: {analysis['period']}
- 총 학습 기록: {analysis['count']}일
- 총 학습 시간: {analysis['metrics']['total']}분
- 평균 학습 시간: {analysis['metrics']['average']}분/일
- 최대 학습 시간: {analysis['metrics']['max']}분
- 최소 학습 시간: {analysis['metrics']['min']}분
- 최근 추세: {analysis['trend']}
"""