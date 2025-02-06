import yaml

def create_config(bot_id, bot_token, *commands):
  config = {
    "bot_id": bot_id,
    "bot_token": bot_token,
    "commands": []
  }

  for description, function in commands:
    config["commands"].append({
      "description": description,
      "function": function
    })

  return yaml.dump(config, indent=2, allow_unicode=True)