# 🩺 First Aid Virtual Assistant

A lightweight, interactive first aid assistant built using **CrewAI**, **Streamlit**, and **Gemini 2 Flash**. It delivers instant, AI-driven first aid guidance based on user-described symptoms, along with essential health resources.

---

## 🚀 Features

- 🤖 **AI-driven symptom analysis** using CrewAI agents
- ⚖️ **Severity classification** (1–10) + physical/mental evaluation
- 🧰 **First aid guidance** for physical and mental health in simple steps
- 🧠 **Condensed outputs**: 5–6 actionable, formatted points
- 📚 **Extra pages**:
  - Basic First Aid Guide  
  - Emergency Instructions  
  - Personal Info (User Notes)

---

## 🧠 Tech Stack

- `Streamlit` – UI and session management  
- `CrewAI` – Multi-agent orchestration  
- `Gemini 2 Flash` – Fast LLM for concise reasoning  
- `Python` – Backend logic  
- `dotenv` – Environment management  

---

## 📸 Screenshots

![Homepage Screenshot](ss/Screenshot%202025-04-24%20103916.png)  
*Interactive homepage with real-time symptom chat*

![Backend CREW](ss/Screenshot%202025-04-24%20104014.png.png)  
*Backend crew running*

---


---

## 🧪 How It Works

1. The user describes their symptoms in a chat-style input.
2. Five CrewAI agents are activated in sequence:
   - **First Aid Guide:** Analyzes symptoms and identifies possible conditions.
   - **Symptom Severity Evaluator:** Rates the severity on a scale of 1–10 and classifies it as physical or mental.
   - **Physical Health Assistant:** Offers 3–5 first aid steps for physical issues.
   - **Mental Health Support Assistant:** Provides emotional support and coping tips.
   - **Output Condenser:** Formats all results into 5–6 clear, actionable points.
3. Results are presented in a structured format using numbered items with emojis and bold headings.

**Example Output Format:**

```md
**🚨 1. Seek Help:** Call emergency services if symptoms escalate.
**🧊 2. Cold Compress:** Apply ice for 10–15 minutes to reduce swelling.
**💊 3. Medication:** Take over-the-counter pain relief if safe.
**🛏️ 4. Rest:** Minimize movement and rest the affected area.
**🧘 5. Breathe Deeply:** Practice slow breathing to stay calm.
