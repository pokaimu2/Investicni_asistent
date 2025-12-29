from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Investicni asistent API")


class AnalyzeRequest(BaseModel):
    question: str
    tickers: str | None = None


class AnalyzeResponse(BaseModel):
    analysis_text: str


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(request: AnalyzeRequest):
    """
    Zatím jen dummy logika:
    vrátíme zpátky dotaz a tickery.
    Později sem připojíme OpenAI + finanční API.
    """
    base_text = [
        "Toto je zatím testovací odpověď backendu.",
        f"Dotaz: {request.question}",
        f"Tickery: {request.tickers or '(nevyplněno)'}",
        "",
        "V další fázi zde backend:",
        "- stáhne data z finančních API,",
        "- doplní news a počasí,",
        "- zavolá OpenAI a vrátí skutečnou analýzu."
    ]
    return AnalyzeResponse(analysis_text="\n".join(base_text))