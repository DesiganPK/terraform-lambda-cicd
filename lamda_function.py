def lambda_handler(event, context):
    name = event.get("queryStringParameters", {}).get("name", "World")
    return {
        "statusCode": 200,
        "body": f"Hello, {name}! (deployed with Terraform CI/CD)"
    }
