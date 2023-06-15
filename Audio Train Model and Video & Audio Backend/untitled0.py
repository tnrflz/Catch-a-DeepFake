
import subprocess
import torch
def run_another_script(script_path, arguments):
    command = ['python', script_path] + arguments
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)  # Betiğin çıktısını ekrana yazdır



print (torch.cuda.is_available() )
# Örnek kullanım
script_path = 'train.py'
arguments = ['--feature_classname', 'lfcc', '--model_classname', 'ShallowCNN', '--restore' ,  '--eval_only']
run_another_script(script_path, arguments)