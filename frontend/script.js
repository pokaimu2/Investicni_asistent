// Zatím jen lokální logika v prohlížeči.
// V dalších blocích tady nahradíme "fake" odpověď
// voláním backendu (FastAPI) přes fetch.

document.addEventListener("DOMContentLoaded", () => {
  const questionInput = document.getElementById("question");
  const tickersInput = document.getElementById("tickers");
  const outputDiv = document.getElementById("output");
  const analyzeButton = document.getElementById("analyzeButton");

  analyzeButton.addEventListener("click", () => {
    const question = questionInput.value.trim();
    const tickers = tickersInput.value.trim();

    if (!question) {
      outputDiv.textContent = "Nejdřív napiš nějaký dotaz.";
      return;
    }

    // Zatím jen jednoduchá simulace odpovědi:
    const now = new Date().toLocaleString("cs-CZ");
    const info = [
      `Čas dotazu: ${now}`,
      "",
      "Zadal jsi:",
      `Dotaz: ${question}`,
      tickers ? `Tickery: ${tickers}` : "Tickery: (nevyplněno)",
      "",
      "Další krok: v dalším bloku připojíme backend, který sem vrátí reálnou analýzu."
    ].join("\n");

    outputDiv.textContent = info;
  });
});