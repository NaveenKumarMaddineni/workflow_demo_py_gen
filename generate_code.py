import json
import os
import datetime

# Path to the config file
config_path = 'configs/config.json'
# Directory to save generated Python files
output_dir = 'generated'
os.makedirs(output_dir, exist_ok=True)
# Generate a unique filename with timestamp
timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
output_path = os.path.join(output_dir, f'generated_code_{timestamp}.py')


def main():
    with open(config_path, 'r') as f:
        config = json.load(f)

    # Example: generate a Python file with a function using config values
    with open(output_path, 'w') as f:
        f.write('# This file is generated from config.json\n')
        f.write('def generated_function():\n')
        for key, value in config.items():
            f.write(f'    print("{key}: {value}")\n')


if __name__ == '__main__':
    main()
