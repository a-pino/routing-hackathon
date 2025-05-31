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
cd martian-hackathon
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

# My Edits (Proposed Project Structure) 
Now I am talking about this subfolder


martian-hackathon/          # Root directory for all hackathon work

├── .env                    # Environment variables

├── .venv/                  # Virtual environment 

├── martian-sdk-python/     # Cloned SDK repository

└── **project/**              # Your hackathon project directory



