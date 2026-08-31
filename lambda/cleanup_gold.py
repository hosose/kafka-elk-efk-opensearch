import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info(f"Received event: {json.dumps(event)}")
    gold_prefix = event.get("gold_prefix", "")
    logger.info(f"Cleaning up gold prefix: {gold_prefix}")
    return {
        "statusCode": 200,
        "message": "Cleanup completed",
        "gold_prefix": gold_prefix
    }
