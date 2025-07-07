import json

# Path to the config file
config_path = 'configs/config.json'
# Path to the generated Python file
output_path = 'generated_code.py'

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
