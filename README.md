# Mechanistic Analysis of Manipulation Vulnerabilities n AI Orchestration

Submission to the [Apart x Martian Router Interpretability Hackathon](https://apartresearch.com/sprints/apart-x-martian-mechanistic-router-interpretability-hackathon-2025-05-30-to-2025-06-01).


# How to get started (Installation) 

## Prerequisites
- Python 3.9 or higher
- Git
- uv - Fast Python package installer and resolver

## Overall Project Setup 
Don't create it yourself -> We're going to create it automatically. 

```
martian-hackathon/          # Root directory for all hackathon work
├── .env                    # Environment variables
├── .venv/                  # Virtual environment (will be created by uv, below)
├── martian-sdk-python/     # Cloned SDK repository
└── project/               # Your hackathon project directory
 ```

## Installation 
0. Before you start, Install an extremely fast Python package and project manager, written in Rust.
 ```
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows (cmd)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
 ```

1. Create and enter the hackathon root directory:
 ```
# On Windows (cmd)
mkdir martian-hackathon
cd martian-hackathon
 ```

2. Clone the SDK repository:
 ```
# On Windows (git cmd)
git clone https://github.com/withmartian/martian-sdk-python.git
 ```

3. Create and activate a virtual environment in the hackathon root directory:
 ```
# On Windows (cmd)
uv venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
 ```

4. Install the SDK in editable mode along with Jupyter:
 ```
# On Windows (cmd)
uv pip install -e martian-sdk-python
uv pip install jupyter
```

5. Create your project directory:
 ```
# On Windows (cmd)
mkdir project
 ```

6. Create a .env file in the hackathon root directory with your Martian credentials. 
 ```
# On Windows (git bash)
cat > .env << EOL
MARTIAN_API_URL=https://withmartian.com/api
MARTIAN_API_KEY=replace-with-our-api-key
EOL
```

#  Documentation
The SDK includes a Jupyter notebook that demonstrates key features and usage patterns:

From your hackathon parent directory, start Jupyter:

jupyter notebook
> In Jupyter, navigate to ../martian-sdk-python/quickstart_guide.ipynb

The quickstart guide will walk you through:

- Setting up the Martian client
- Using the gateway to access various LLM models
- Creating and using judges
- Working with routers
- Training and evaluating models

Docs: 
```
https://withmartian.github.io/martian-sdk-python/
```

Understand Core Martian Concepts:
- **martian.Model:** Represents your LLM-based experts and judges. You'll define their prompts, model IDs, etc.
- **martian.Router:** Represents your routing logic. It can use conditions based on model outputs (judge signals) or be an LLM itself.
- **martian.scan:** The workhorse function to run datasets through your models/routers and collect results.
- **martian.GroundTruth:** To specify the expected/correct outcomes for comparison.
- **Datasets:** Martian scan takes a list of dictionaries as a dataset.




# Inside the Project Structure
Now I am talking about this subfolder


martian-hackathon/          # Root directory for all hackathon work

├── .env                    # Environment variables

├── .venv/                  # Virtual environment 

├── martian-sdk-python/     # Cloned SDK repository

└── **project/**              # Your hackathon project directory



  ### Project Phases


> Brief instructions on how to run each phase in `project/src/`.

  - **Phase 1 (Define EO components):**  
    Run nothing—just make sure `components.py` has correct model/router definitions.
  - **Phase 2 (Baseline):**  
    ```bash
    python src/phase2_baseline/baseline_safety.py
    python src/phase2_baseline/baseline_quality.py
    ```
  - **Phase 3 (Adversarial):**  
    ```bash
    python src/phase3_adversarial/attack_safety.py
    python src/phase3_adversarial/attack_quality.py
    ```
  - **Phase 4 (Analysis):**  
    ```bash
    python src/phase4_analysis/analyze_attacks.py
    python src/phase4_analysis/visualize_results.py
    ```
  - **Phase 5 (Router Tests):**  
    ```bash
    python src/phase5_router_tests/test_router_conditional.py
    python src/phase5_router_tests/test_router_llm.py
    ```
  - **Phase 6 (Defenses):**  
    ```bash
    python src/phase6_defenses/robust_safety.py
    python src/phase6_defenses/robust_quality.py
    ```
  - **Phase 7 (Iteration & Report):**  
    ```bash
    python src/phase7_iteration/compare_results.py
    ```
    Then review or edit `src/phase7_iteration/final_report.md`.

  ## Logs

  Any CSV/JSON outputs from `scan(...).to_df().to_csv(...)` go into `logs/`.  
  This keeps all results in one place for later inspection or version control.


Let's assume you have:
- **Expert_A** and **Expert_B** (LLM-based, performing some task).
- **Judge_Safety:** An LLM-based judge to check for harmful content.
- **Judge_Quality:** An LLM-based judge to score response quality.
- **Main_Router:** Decides which expert to use based on judge signals.
