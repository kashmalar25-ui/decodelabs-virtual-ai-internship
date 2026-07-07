# Rule-Based AI Chatbot

A simple rule-based chatbot built in Python as part of my AI Engineering internship (Project 1). It responds to predefined greetings and questions using dictionary-based intent matching, runs in a continuous loop, and includes a couple of personal touches on top of the core requirements.

## Features
- Continuous input loop (keeps running until an exit command is typed)
- Input sanitization (handles different casing and extra whitespace)
- Dictionary-based knowledge base for fast, clean intent matching (8 intents)
- Explicit if-elif command (`time`) alongside the dictionary lookup
- Remembers the user's name (e.g. "my name is Iraj") and personalizes replies
- Fallback response for unrecognized input
- Clean exit via `bye`, `exit`, or `quit`

## How to run
```bash
python chatbot.py
```

Then chat with it in the terminal. Try:
- `hello`
- `my name is <your name>`
- `time`
- `what can you do`
- `bye` (to exit)

## Self-verification against the project rubric
| Requirement | Status |
|---|---|
| Continuous input loop | Done |
| Input sanitization | Done |
| Knowledge base (5+ intents) | Done (8 intents) |
| If-else decision logic | Done |
| Fallback for unknown input | Done |
| Clean exit command | Done |

## What I learned
This project focuses on control flow and decision-making logic rather than machine learning. Before building systems that learn from data, it's important to understand how to structure deterministic, rule-based decision systems — the same underlying idea used in real-world "guardrails" around LLM applications.

## Next steps
Possible future improvements: expanding the intent dictionary further, adding more nuanced keyword matching, and eventually connecting the rule-based layer to a generative model as a fallback (hybrid architecture).
