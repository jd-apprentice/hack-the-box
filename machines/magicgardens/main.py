from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/api/payments", status_code=200)
def receive_payment(data: dict):

    print(data)

    response = {
        "status": "success",
        "message": "Payment received successfully",
    }

    return response
