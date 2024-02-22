import os
import sys
from subprocess import call

def create_virtual_environment(venv_path):
    try:
        # Create a virtual environment
        call([sys.executable, '-m', 'venv', venv_path])
        print(f"Virtual environment created at {venv_path}")
    except Exception as e:
        print(f"Error creating virtual environment: {e}")

def activate_virtual_environment(venv_path,app_path):
    # Activate the virtual environment
    try:
        if sys.platform == 'win32':
            #activate_script = os.path.join(venv_path, 'Scripts', 'activate')
            #activate_command = f"{activate_script}"
            #call(activate_command, shell=True)
            #print(f"Activated virtual environment at {venv_path}")

            pip_command = os.path.join(venv_path, 'Scripts', 'pip')

            print(f"Installing requirements using {pip_command}")
    
            path_req= str(os.path.join(app_path, 'requi.txt'))
            print(path_req)

            call(f"{pip_command} install -r {path_req}", shell=True)

            print("Requirements installed. Running the application... 1. Clasificador 2. Organizador")
            option=int(input())
            if(option==1):
                combine = os.path.join(venv_path, 'Scripts', 'python') + " clasificador.py"
                call(combine, shell=True)
            else:
                combine = os.path.join(venv_path, 'Scripts', 'python') + " organizador.py"
                call(combine, shell=True)
        else:
            activate_script = os.path.join(venv_path, 'bin', 'activate')
            activate_command = f"source {activate_script}"

            call(activate_command, shell=True)
            print(f"Activated virtual environment at {venv_path}")
            install_requirements(venv_path)
    except Exception as e:
        print(f"Error activating virtual environment: {e}")


if __name__ == "__main__":
    # Set the desired path for the virtual environment
    venv_path = os.path.join(os.getcwd(), 'my_venv')
    app_path = os.getcwd()
    print(app_path)
    print(venv_path)

    # Create, activate, and install requirements for the virtual environment
    create_virtual_environment(venv_path)
    activate_virtual_environment(venv_path,app_path)
    
