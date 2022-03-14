from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def ping():
    """[ping func provides a health check]
    Returns:
        [dict]: [success response for health check]
    """
    return {"response": "Hello from patient service "}