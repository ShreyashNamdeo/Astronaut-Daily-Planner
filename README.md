# 🚀 Astronaut Daily Planner

**AI/ML-Powered Daily Activity Planner for Astronauts**  
This project generates optimized daily schedules for astronauts, predicts fatigue, and adapts tasks dynamically using AI and Reinforcement Learning. It simulates astronaut health and environmental factors like sleep, stress, and CO₂ levels.

---

## **Features**

### Core Features
- **Baseline Scheduler:** Generates task schedules using OR-Tools based on task priorities, durations, and crew state.
- **RL Adaptation:** Uses PPO (Reinforcement Learning) and a custom AstroEnv to adapt schedules dynamically (swap tasks, insert naps) based on astronaut fatigue and environment.
- **Interactive UI:** Sliders for Sleep, Stress, CO₂ with real-time table updates.
- **Environment-Aware:** Accounts for CO₂ and stress to optimize daily tasks.
- **Synthetic Dataset:** Generates realistic astronaut logs for sleep, heart rate, stress, and CO₂.

### Unique Aspects
- AI-driven adaptive scheduling not currently used in real-life astronaut missions.
- Predictive fatigue modeling for proactive schedule adjustments.
- Integrated end-to-end pipeline: Simulation → Optimization → RL → Web UI.

---

## **Installation**

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Astronaut-Daily-Planner.git
cd Astronaut-Daily-Planner
