import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="sum")
def sum_numbers(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing request to add two numbers.')

    try:
        a = int(req.params.get('a'))
        b = int(req.params.get('b'))
        result = a + b
        return func.HttpResponse(f"Result: {result}", status_code=200)
    except (TypeError, ValueError):
        return func.HttpResponse(
            "Usage: /api/sum?a=1&b=2 — Make sure both a and b are integers.",
            status_code=400
        )
