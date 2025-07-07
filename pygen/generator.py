import json
import os
import datetime

def generate_code(config_path, output_dir='generated'):
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    output_path = os.path.join(output_dir, f'generated_code_{timestamp}.py')
    with open(config_path, 'r') as f:
        config = json.load(f)
    with open(output_path, 'w') as f:
        f.write('# This file is generated from config.json\n')
        f.write('def generated_function():\n')
        for key, value in config.items():
            f.write(f'    print("{key}: {value}")\n')
    return output_path
