import sys
import subprocess
import os
import shutil

def main():
    print("=== Module 4 Lab Setup ===")
    
    # 1. Check Python version
    major, minor = sys.version_info[:2]
    print(f"Current Python: {major}.{minor}")
    
    python_cmd = sys.executable
    
    # If Python is too new (e.g., 3.14) or too old, try to find a better one
    if minor >= 14 or minor < 8:
        print("Warning: Your default Python version might be incompatible with some libraries.")
        print("Attempting to find a compatible Python version (3.8 - 3.12)...")
        
        # Try common names
        candidates = ["python3.12", "python3.11", "python3.10", "python3.9", "python3.8", "/usr/bin/python3"]
        found = False
        for cmd in candidates:
            try:
                ver_output = subprocess.check_output([cmd, "--version"], stderr=subprocess.STDOUT).decode()
                # Parse version like "Python 3.9.6"
                ver_parts = ver_output.strip().split()[-1].split('.')
                v_major, v_minor = int(ver_parts[0]), int(ver_parts[1])
                
                if v_major == 3 and 8 <= v_minor <= 12:
                    print(f"Found compatible Python: {cmd} ({ver_output.strip()})")
                    python_cmd = cmd
                    found = True
                    break
            except (FileNotFoundError, subprocess.CalledProcessError):
                continue
        
        if not found:
            print("Error: Could not find a compatible Python version (3.8-3.12).")
            print("Please install Python 3.9 or 3.10 from python.org.")
            return

    # 2. Create Virtual Environment
    venv_dir = ".venv_lab"
    print(f"\nCreating virtual environment in '{venv_dir}' using {python_cmd}...")
    try:
        subprocess.check_call([python_cmd, "-m", "venv", venv_dir])
    except subprocess.CalledProcessError:
        print("Failed to create virtual environment.")
        return

    # 3. Install Dependencies
    pip_cmd = os.path.join(venv_dir, "bin", "pip")
    if sys.platform == "win32":
        pip_cmd = os.path.join(venv_dir, "Scripts", "pip.exe")

    print("\nInstalling dependencies...")
    try:
        # Use requirements.pip instead of .txt to avoid gitignore issues
        subprocess.check_call([pip_cmd, "install", "-r", "requirements.pip"])
    except subprocess.CalledProcessError:
        print("Failed to install dependencies.")
        return

    # 4. Success Message
    print("\n=== Setup Complete! ===")
    print("To start the lab:")
    
    if sys.platform == "win32":
        print(f"1. {os.path.join(venv_dir, 'Scripts', 'activate')}")
    else:
        print(f"1. source {os.path.join(venv_dir, 'bin', 'activate')}")
        
    print("2. jupyter notebook module4_experiment.ipynb")

if __name__ == "__main__":
    main()
