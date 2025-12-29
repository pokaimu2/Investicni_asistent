// Základní konfigurace – URL backendu (lokálně)
const API_BASE_URL = "http://127.0.0.1:8000";
// Pokud bys backend spouštěl na jiném portu (např. 8001), uprav na:
// const API_BASE_URL = "http://127.0.0.1:8001";

async function callAnalyze(question, tickers) {
  const payload = {
    question: question,
    tickers: tickers && tickers.trim() !== "" ? tickers.trim() : null,
  };

  const response = await fetch(`${API_BASE_URL}/analyze`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  if (!response.ok) {
    const text = await response.text();
    throw new Error(`Server error ${response.status}: ${text}`);
  }

  return response.json(); // vrátí { analysis_text: "..." }
}

document.addEventListener("DOMContentLoaded", () => {
  const questionInput = document.getElementById("question");
  const tickersInput = document.getElementById("tickers");
  const outputDiv = document.getElementById("output");
  const analyzeButton = document.getElementById("analyzeButton");

  analyzeButton.addEventListener("click", async () => {
    const question = questionInput.value.trim();
    const tickers = tickersInput.value.trim();

    if (!question) {
      outputDiv.textContent = "Nejdřív napiš nějaký dotaz.";
      return;
    }

    // UI: indikace, že se něco děje
    analyzeButton.disabled = true;
    analyzeButton.textContent = "Analyzuji…";
    outputDiv.textContent = "Dotaz odeslán na backend, čekám na odpověď...";

    try {
      const data = await callAnalyze(question, tickers);
      outputDiv.textContent = data.analysis_text || "Backend nevrátil analysis_text.";
    } catch (err) {
      console.error(err);
      outputDiv.textContent =
        "Došlo k chybě při komunikaci s backendem: " + err.message;
    } finally {
      analyzeButton.disabled = false;
      analyzeButton.textContent = "Odeslat dotaz";
    }
  });
});