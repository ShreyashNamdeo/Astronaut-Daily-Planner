import gradio as gr, pandas as pd, json, numpy as np
from ortools.sat.python import cp_model
from stable_baselines3 import PPO

def make_schedule(tasks_file, crew_state):
    with open(tasks_file) as f: tasks=json.load(f)
    m=cp_model.CpModel();h=16;starts={}
    for i,t in enumerate(tasks):
        s=m.NewIntVar(0,h-t["duration"],f"s{i}")
        m.NewIntervalVar(s,t["duration"],s+t["duration"],f"i{i}")
        starts[i]=s
    m.Add(starts[1]+tasks[1]["duration"]<=starts[4])
    sol=cp_model.CpSolver();sol.Solve(m)
    sch=[(t["task"],sol.Value(starts[i])) for i,t in enumerate(tasks)]
    return sorted(sch,key=lambda x:x[1])

rl_model=PPO.load("ppo_astronaut_planner.zip")

def baseline_planner(sleep,stress,co2):
    cs={"sleep":sleep,"stress":stress,"co2":co2}
    return pd.DataFrame(make_schedule("tasks.json",cs),columns=["Task","Start"])

def rl_planner(sleep,stress,co2):
    obs=np.array([sleep,stress,co2],dtype=np.float32)
    a,_=rl_model.predict(obs)
    return pd.DataFrame([["RL Decision",{0:"Keep",1:"Swap",2:"Nap"}[a]]],columns=["Task","Adjustment"])

with gr.Blocks() as demo:
    gr.Markdown("# 👩‍🚀 Astronaut Daily Planner")
    with gr.Row():
        sleep=gr.Slider(4,9,7,0.1,label="Sleep")
        stress=gr.Slider(0,1,0.3,0.05,label="Stress")
        co2=gr.Slider(1000,3000,1700,50,label="CO₂")
    with gr.Tab("Baseline"): o1=gr.Dataframe();b1=gr.Button("Run")
    with gr.Tab("RL"): o2=gr.Dataframe();b2=gr.Button("Run")
    b1.click(baseline_planner,[sleep,stress,co2],o1)
    b2.click(rl_planner,[sleep,stress,co2],o2)

demo.launch()
