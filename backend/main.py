from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json

import data_providers
import openai_client


class AnalyzeRequest(BaseModel):
    question: str
    tickers: str | None = None


class AnalyzeResponse(BaseModel):
    analysis_text: str


# >>> TADY DEFINUJEME app – MUSÍ být před @app.get/@app.post <<<
app = FastAPI(title="Investicni asistent API")

# CORS – pro vývoj povolíme všechno
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {"status": "ok"}



@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(request: AnalyzeRequest):
    prices = data_providers.get_mock_prices(request.tickers)
    news = data_providers.get_mock_news(request.tickers)
    weather = data_providers.get_mock_weather_for_commodities()

    context_data = {
        "question": request.question,
        "tickers": request.tickers,
        "prices": prices,
        "news": news,
        "weather": weather,
    }

    try:
        analysis_text = openai_client.generate_investment_analysis(
            question=request.question,
            context_data=context_data,
        )
    except Exception as e:
        # pro vývoj – ať místo „Internal Server Error“ vidíš konkrétní problém
        raise HTTPException(
            status_code=500,
            detail=f"Chyba při volání OpenAI: {e}",
        )

    return AnalyzeResponse(analysis_text=analysis_text)