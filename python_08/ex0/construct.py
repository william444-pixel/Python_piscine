import os
import sys
import site


def check_context():
    actual_executable = sys.executable
    is_venv = os.environ.get('VIRTUAL_ENV')

    if is_venv:
        env_name = os.path.basename(is_venv)
        pathe_site = site.getsitepackages()[0]
        print("MATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {actual_executable}")
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {is_venv}")
        print("\nSUCCESS: You're in an isolated environment!"
              "\nSafe to install packages without affecting"
              "\nthe global system")
        print(f"Package installation path:\n{pathe_site}")
    else:
        print("MATRIX STATUS: You're still plugged in")
        print(f"\nCurrent Python: {actual_executable}")
        print("Virtual Environment: None detected")
        print("\nWARNING: You're in the global environment!\
The machines can see everything you install.")
        print("\nTo enter the construct, run:\npython -m venv matrix_env\
 source matrix_env/bin/activate # On Unix\
\nmatrix_env\\Scripts\\activate # On Windows")


if __name__ == "__main__":
    check_context()
