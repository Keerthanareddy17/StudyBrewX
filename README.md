# 📚 StudyBrewX: Your Personalized AI-Powered Learning Path Generator

Welcome to **StudyBrewX**, an agent-powered platform that helps learners transform vague learning goals into actionable weekly study plans — complete with curated YouTube videos, blogs, and weekly tasks. Built using **LangChain**, **LangGraph**, and **Streamlit**, it combines the power of language models with structured task planning to offer a personalized, goal-oriented experience.

---

## 🚀 Project Overview

**StudyBrewX** is designed for self-learners who want:
- A **clear path** from start to mastery for any goal (e.g., "Become a Data Analyst in 2 months")
- **Curated multimedia resources** (blogs & videos)
- **Weekly hands-on tasks** to track learning
- A downloadable **Excel-based plan** for offline use

---

## 🧠 Agents Used

StudyBrewX uses a multi-agent system, implemented with **LangGraph + LangChain**, where each agent performs a distinct cognitive function:

| Agent | Purpose |
|-------|---------|
| 🧠 `goal_interpreter_agent` | Converts the user’s high-level goal into structured weekly milestones. |
| 📋 `preference_collector_agent` | Gathers user preferences (e.g., video/blog, duration). |
| 🔍 `source_fetcher_agent` | Fetches relevant resources (YouTube + blogs) for each weekly topic. |
| 🛠️ `path_builder_agent` | Combines resources and weekly goals into a sequential learning plan. |
| 📝 `weekly_task_generator_agent` | Assigns practical tasks (mini-projects, reflections, challenges) for each week. |

---

## 🛠️ Tech Stack & Libraries

| Component | Description |
|----------|-------------|
| 🦜 LangChain | Agent logic, LLM integrations |
| 🧑‍💻 OpenAI/Groq | LLMs for reasoning, summarizing, structuring plans |
| 🌐 SERP API & YouTube API | Fetches top blogs/videos for study topics |
| 📊 Streamlit | Frontend interface for user interaction and downloads |
| 📦 pandas / xlsxwriter | Generates downloadable Excel plans |

---

## 🧠 How It Works

1. **User Input**: Goal + preferred format
2. **Goal Breakdown**: Agent splits goal into weekly learning milestones
3. **Resource Fetching**: Blogs + YouTube videos are fetched using APIs
4. **Task Assignment**: Hands-on or reflective weekly tasks generated
5. **Display**: UI shows weekly breakdown with links + task info
6. **Export**: Option to download the entire plan as Excel

---


## Snapshots of StudyBrewX


<img width="1710" alt="Screenshot 2025-06-07 at 13 37 57" src="https://github.com/user-attachments/assets/1ac59673-3e1b-46ef-b560-082d00c3455b" />


<img width="1710" alt="Screenshot 2025-06-07 at 13 38 28" src="https://github.com/user-attachments/assets/f8ec703b-351c-4473-83d2-9272d6238d8d" />


<img width="1440" alt="Screenshot 2025-06-07 at 13 47 20" src="https://github.com/user-attachments/assets/9f8b918e-ba5b-48e0-965c-450600f2bc58" />

