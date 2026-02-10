# intent-routing-for-agents

A **simple, plug-and-play intent routing template** for agentic AI systems.
Designed to route user queries into the correct workflow using **intent detection + entity extraction**.

This is **not a chatbot** — it’s a reusable **decision layer** for AI agents.

Check out the [blog](https://medium.com/@rishabh.b1910/routing-user-queries-into-agentic-ai-workflows-using-intent-detection-c68711b2d64a) for an easily understandable step-by-step demo!

---

## 🔧 What You Can Change vs What You Shouldn’t

| Component                        | Can Change? | Notes                                          |
| -------------------------------- | ----------- | ---------------------------------------------- |
| `call_llm()`                     | ✅ Yes       | Replace with OpenAI / Ollama / Claude / Gemini |
| Intent names                     | ✅ Yes       | Add or remove intents to match your domain     |
| Entity fields                    | ✅ Yes       | Customize schema (`target`, `timeframe`, etc.) |
| Workflow logic                   | ✅ Yes       | Plug in tools, APIs, DB calls, or other agents |
| Output formatting                | ✅ Yes       | Console output, API response, UI, logs         |
| Core flow (Intent → Workflow)    | ❌ No        | This is the agent’s backbone                   |
| Intent router pattern            | ❌ No        | Keeps decision-making predictable              |
| Separation of intent & execution | ❌ No        | Prevents fragile agent behavior                |

---

## Suggested Next Steps

If you want to level this up:

### 🔌 Plug in a real LLM

Replace `call_llm()` with your preferred provider.

### 🧩 Add more workflows

New intent = new workflow function + routing entry.

### 💾 Add memory or persistence

Store state between turns for long-running conversations.

### 🌐 Expose as an API

Wrap `run_agent()` with **FastAPI** or **Flask**.

---

## 🤝 Open Source Contributions

Contributions are **very welcome** 🎉

Feel free to:

* Improve prompts
* Add examples
* Optimize routing logic
* Add LangGraph / AutoGen variants
* Write tests or documentation

Open an issue or submit a PR — **all ideas are welcome**.

---
