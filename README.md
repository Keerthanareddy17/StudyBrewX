# 📚 StudyBrewX: Your Personalized AI-Powered Learning Path Generator

Welcome to **StudyBrewX**, an agent-powered platform that helps learners transform vague learning goals into actionable weekly study plans — complete with curated YouTube videos, blogs, and weekly tasks. Built using **LangChain**, **LangGraph**, and **Streamlit**, it combines the power of language models with structured task planning to offer a personalized, goal-oriented experience.

---

## 🚀 Project Overview

**StudyBrewX** is designed for self-learners who want:
- A **clear path** from start to mastery for any goal (e.g., "Become a Data Analyst in 2 months")
- **Curated multimedia resources** (blogs & videos)
- **Weekly hands-on tasks** to track learning
- A downloadable **Excel-based plan** for offline use

Whether you're diving into Data Science or Prompt Engineering, this tool gives structure to your ambition.

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
| 🔁 LangGraph | Multi-agent workflow orchestration |
| 🧑‍💻 OpenAI/Groq | LLMs for reasoning, summarizing, structuring plans |
| 🌐 SERP API & YouTube API | Fetches top blogs/videos for study topics |
| 📊 Streamlit | Frontend interface for user interaction and downloads |
| 📦 pandas / xlsxwriter | Generates downloadable Excel plans |

---
