from typing import Any, Dict, List


def get_mock_prices(tickers: str | None) -> List[Dict[str, Any]]:
    if not tickers:
        return []

    items = []
    for t in [x.strip().upper() for x in tickers.split(",") if x.strip()]:
        items.append(
            {
                "ticker": t,
                "mock_price": 100.0,  # TODO: nahradit reálnými daty z FMP
                "mock_pe": 20.0,
                "mock_comment": "Mock data – sem přijdou skutečná finanční data.",
            }
        )
    return items


def get_mock_news(tickers: str | None) -> List[Dict[str, Any]]:
    if not tickers:
        return []

    return [
        {
            "ticker": "AAPL",
            "headline": "Mock: Apple reports stable earnings",
            "summary": "Toto je testovací news, později nahradit voláním news API.",
        }
    ]


def get_mock_weather_for_commodities() -> Dict[str, Any]:
    # Jen placeholder – později volání weather API.
    return {
        "region": "Global",
        "comment": "Mock weather data – zde může být informace o počasí pro zemědělské komodity.",
    }