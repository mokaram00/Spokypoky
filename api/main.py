from http import HTTPStatus

def handler(request):
    print("hi world")  # هذا سيظهر في سجلات Vercel
    return {
        "statusCode": HTTPStatus.OK,
        "body": "Hello from /api/main"
    }
