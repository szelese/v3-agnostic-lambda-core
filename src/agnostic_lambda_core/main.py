import os
import json
import logging
from .core import process_data

#  Standard AWS Lambda logger configuration
logger = logging.getLogger()
logger.setLevel(logging.INFO) # INFO level for production!!!, can be set to DEBUG for more verbose output during development

def handler(event, context):
    version=os.environ.get("VERSION", "dev-manual")  
    logger.info(f"Incoming event: {json.dumps(event)}")

    security_headers = {
        "Content-Type": "application/json",
        "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
        "X-Content-Type-Options": "nosniff",
        "Cache-Control": "no-cache, no-store, must-revalidate, proxy-revalidate",
        "Pragma": "no-cache",
        "Expires": "0"
    }

    path = event.get("rawPath", "/")
    if path != "/":
        return {
            "statusCode": 404,
            "headers": security_headers,
            "body": json.dumps({
                "error": "Not Found",
                "path": path,
                "version": version
            })
        }

    try:
        # 1. Intelleigent data load (Adapter logic)
        if "body" in event:
            if isinstance(event["body"], str):
                payload = json.loads(event["body"])
            else:
                payload = event["body"]
        else:
            payload = event

        # 2. Core logic call
        result = process_data(payload)

        # 3. Success response
        return {
            "statusCode": 200,
            "headers": security_headers,
            "body": json.dumps({
                "version": version,
                "status": "success",
                "message": "Request processed successfully.",
                "result": result
            })
        }
    # 4. Error handling
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON received: {str(e)}")
        return {
            "statusCode": 400,
            "headers": security_headers,
            "body": json.dumps({
                "error": "Invalid JSON input",
                "details": "The provided input is not valid JSON.",
                "version": version
            })
        }
    except Exception as e:
        logger.error(f"Unexpected system error: {str(e)}")
        return {
            "statusCode": 500,
            "headers": security_headers,
            "body": json.dumps({
                "error": "Internal Server Error",
                "details": "An unexpected error occurred. Please try again later. Check a CloudWatch logs for more details.",
                "version": version
            })
        }