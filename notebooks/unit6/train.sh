# --- PART A: TRAINING ---
# Change the --env path based on your OS (.exe for Win, .app for Mac)
mlagents-learn ./config/poca/SoccerTwos.yaml \
  --env=./training-envs-executables/SoccerTwos \
  --run-id="SoccerTwos_v1" \
  --no-graphics

# --- PART B: AUTHENTICATION ---
# When you run this, it will ask for your Hugging Face Write Token
huggingface-cli login

# --- PART C: PUSH TO HUB ---
# Replace placeholders with your HF username and chosen repo name
mlagents-push-to-hf \
  --run-id="SoccerTwos_v1" \
  --local-dir="./results/SoccerTwos_v1" \
  --repo-id="PinchuPanda/SoccerTwos" \
  --commit-message="Initial trained soccer model"

  # --- PART D: RECORDING A VIDEO ---
# 1. We run the model in inference mode (no training)
# 2. We remove --no-graphics so we can see the window
# 3. Use your favorite screen recorder (OBS, Windows Game Bar Win+G, or Mac QuickTime)

mlagents-learn ./config/poca/SoccerTwos.yaml \
  --env=./training-envs-executables/SoccerTwos \
  --run-id="SoccerTwos_v1" \
  --resume \
  --inference