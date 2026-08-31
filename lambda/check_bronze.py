import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info(f"Received event: {json.dumps(event)}")
    # Step Functions 및 Bronze 데이터 존재 여부 검사용 기본 핸들러
    return {
        "data_exists": False,
        "source_path": "",
        "silver_base_path": "",
        "reject_base_path": "",
        "year": "2026",
        "month": "08",
        "day": "31",
        "hour": "00",
        "gold_prefix": "",
        "gold_partition_query": "",
        "gold_insert_query": ""
    }
