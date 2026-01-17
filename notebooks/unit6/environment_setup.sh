# 1. Create and activate the environment
conda create --name rl python=3.10.12 -y
conda activate rl

# 2. Clone and install ML-Agents
git clone https://github.com/Unity-Technologies/ml-agents
cd ml-agents
pip install -e ./ml-agents-envs
pip install -e ./ml-agents

# 3. For Mac (Apple Silicon) users only:
# conda install -c conda-forge grpcio -y

# 4. Create folder for the executable
mkdir training-envs-executables