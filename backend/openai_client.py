from typing import Any, Dict

from openai import OpenAI
import config  # pokud máš strukturu jako plain backend folder, použij: import config


client = OpenAI(api_key=config.OPENAI_API_KEY)


SYSTEM_PROMPT = """Jsi investiční analytik. 
Pracuj pouze s daty, která dostaneš v JSONu od backendu (ceny, základní fundamenty, news, počasí/sentiment).
Odpovědi dávej v češtině, strukturovaně, srozumitelně pro chytrého laika.
Nikdy si nevymýšlej konkrétní čísla, která v datech nejsou, maximálně můžeš opatrně odhadnout trend a rizika.
"""


def generate_investment_analysis(question: str, context_data: Dict[str, Any]) -> str:
    """
    question = co se ptal uživatel
    context_data = dict s daty z FMP/news/weather (zatím klidně mock)
    """
    # pro přehlednost si poskládáme "payload" do promptu
    user_content = {
        "question": question,
        "data": context_data,
    }

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": (
                    "Toto jsou vstupní informace ve formátu JSON. "
                    "Nejdřív si je v duchu analyzuj, pak napiš odpověď:\n"
                    f"{user_content}"
                ),
            },
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content or ""