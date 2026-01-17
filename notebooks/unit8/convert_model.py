import gymnasium as gym
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.monitor import Monitor
from stable_baselines3 import PPO
from huggingface_sb3 import load_from_hub, package_to_hub
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.monitor import Monitor

# 1. Define the model details
repo_id = "PinchuPanda/ppo-LunarLander-v3"
filename = "ppo-LunarLander-v3.zip"

# 2. Load the model
checkpoint = load_from_hub(repo_id, filename)
model = PPO.load(checkpoint, print_system_info=True)

# 3. Create the v2 environment with the correct render mode for video recording


def make_env():
    env = gym.make("LunarLander-v2", render_mode="rgb_array")
    env = Monitor(env)  # Still need this for the stats
    return env


# We wrap it in DummyVecEnv because package_to_hub's video recorder needs it
eval_env = DummyVecEnv([make_env])

# 4. Evaluate (evaluate_policy handles VecEnvs automatically)
print("Evaluating model in LunarLander-v2...")
mean_reward, std_reward = evaluate_policy(
    model, eval_env, n_eval_episodes=10, deterministic=True)
print(f"Mean reward in v2: {mean_reward:.2f} +/- {std_reward:.2f}")

# 5. Save locally
model_name = "ppo-LunarLander-v2"
model.save(model_name)

# 6. Upload to Hub
package_to_hub(
    model=model,
    model_name=model_name,
    model_architecture="PPO",
    env_id="LunarLander-v2",
    eval_env=eval_env,  # Now this is a VecEnv with rgb_array mode
    repo_id=f"PinchuPanda/{model_name}",
    commit_message="Converted model from v3 to v2"
)
