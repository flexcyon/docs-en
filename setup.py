#!/usr/bin/env python
import argparse
import os
import subprocess
import sys
import shutil
import logging

# --- 1. Basic Logging Setup ---
# Configure basic logging for the script
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- 2. Helper Functions for Virtual Environment Paths ---
def _get_venv_paths(venv_path):
    """
    Determines the paths to the python, pip, uv, and mkdocs executables
    within the virtual environment, based on the operating system.
    """
    if sys.platform == "win32":
        # On Windows, executables are in 'Scripts'
        venv_bin_path = os.path.join(venv_path, "Scripts")
        venv_python_path = os.path.join(venv_bin_path, "python.exe")
        venv_pip_path = os.path.join(venv_bin_path, "pip.exe")
        venv_uv_path = os.path.join(venv_bin_path, "uv.exe")
        venv_mkdocs_path = os.path.join(venv_bin_path, "mkdocs.exe")
    else:
        # On Linux/macOS, executables are in 'bin'
        venv_bin_path = os.path.join(venv_path, "bin")
        venv_python_path = os.path.join(venv_bin_path, "python")
        venv_pip_path = os.path.join(venv_bin_path, "pip")
        venv_uv_path = os.path.join(venv_bin_path, "uv")
        venv_mkdocs_path = os.path.join(venv_bin_path, "mkdocs")

    return venv_python_path, venv_pip_path, venv_uv_path, venv_mkdocs_path

# --- 3. Core Function: Setup Virtual Environment ---
def _setup_venv(venv_path, requirements_file):
    """
    Creates a .venv virtual environment, installs uv, and then installs
    dependencies from requirements_file using uv.
    """
    logger.info(f"Starting virtual environment setup at: {venv_path}")

    # Remove existing venv for a clean setup
    if os.path.exists(venv_path):
        logger.info(f"Removing existing virtual environment at: {venv_path}")
        try:
            shutil.rmtree(venv_path)
            logger.info("Existing virtual environment removed successfully.")
        except OSError as e:
            logger.error(f"Error removing virtual environment '{venv_path}': {e}")
            sys.exit(1)

    # Create a new virtual environment
    logger.info(f"Creating new virtual environment at: {venv_path}")
    try:
        # Use the system's default Python to create the venv
        subprocess.run([sys.executable, "-m", "venv", venv_path], check=True,
                       stdout=sys.stdout, stderr=sys.stderr)
        logger.info("Virtual environment created successfully.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to create virtual environment: {e}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"An unexpected error occurred during venv creation: {e}")
        sys.exit(1)

    # Get paths to executables within the new venv
    venv_python_path, venv_pip_path, venv_uv_path, _ = _get_venv_paths(venv_path)

    # Ensure pip is up-to-date in the venv (optional but good practice)
    logger.info("Upgrading pip in the virtual environment...")
    try:
        subprocess.run([venv_python_path, "-m", "pip", "install", "--upgrade", "pip"], check=True,
                       stdout=sys.stdout, stderr=sys.stderr)
        logger.info("pip upgraded successfully.")
    except subprocess.CalledProcessError as e:
        logger.warning(f"Failed to upgrade pip: {e}") # Warning, not critical error

    # Install uv using pip within the venv
    logger.info(f"Installing 'uv' into '{venv_path}'...")
    try:
        subprocess.run([venv_pip_path, "install", "uv"], check=True,
                       stdout=sys.stdout, stderr=sys.stderr)
        logger.info("'uv' installed successfully.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to install 'uv'. Command: {' '.join(e.cmd)} Error: {e}")
        sys.exit(1)
    except FileNotFoundError:
        logger.error(f"Error: pip executable not found at '{venv_pip_path}'. Make sure the venv is correctly set up.")
        sys.exit(1)
    except Exception as e:
        logger.error(f"An unexpected error occurred while installing 'uv': {e}")
        sys.exit(1)

    # Install Python dependencies from requirements.txt using uv
    if os.path.exists(requirements_file):
        logger.info(f"Installing Python dependencies from '{requirements_file}' using 'uv'...")
        try:
            subprocess.run([venv_uv_path, "pip", "install", "-r", requirements_file], check=True,
                           stdout=sys.stdout, stderr=sys.stderr)
            logger.info(f"Python dependencies installed successfully into '{venv_path}' using 'uv'.")
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to install Python dependencies using 'uv'. Command: {' '.join(e.cmd)} Error: {e}")
            sys.exit(1)
        except FileNotFoundError:
            logger.error(f"Error: uv executable not found at '{venv_uv_path}'. 'uv' might not have installed correctly.")
            sys.exit(1)
        except Exception as e:
            logger.error(f"An unexpected error occurred while installing Python dependencies with 'uv': {e}")
            sys.exit(1)
    else:
        logger.warning(f"Requirements file '{requirements_file}' not found. Skipping dependency installation.")

    logger.info("Virtual environment setup complete.")

# --- 4. Core Function: Run MkDocs Serve ---
def _run_mkdocs_serve(venv_path):
    """
    Runs 'mkdocs serve' using the Python interpreter from the specified venv.
    """
    logger.info("Attempting to run 'mkdocs serve'...")
    _, _, _, venv_mkdocs_path = _get_venv_paths(venv_path)

    if not os.path.exists(venv_mkdocs_path):
        logger.error(f"mkdocs executable not found at '{venv_mkdocs_path}'. "
                     "Please ensure mkdocs is listed in your requirements.txt and setup is run.")
        sys.exit(1)

    try:
        logger.info(f"Executing: {venv_mkdocs_path} serve")
        # Use subprocess.run with no check=True here if you want it to run indefinitely
        # and allow user to Ctrl+C. If check=True, it will raise an error if mkdocs exits.
        subprocess.run([venv_mkdocs_path, "serve"], stdout=sys.stdout, stderr=sys.stderr)
    except Exception as e:
        logger.error(f"An error occurred while running mkdocs serve: {e}")
        sys.exit(1)

# --- 5. Main Script Logic ---
def main():
    parser = argparse.ArgumentParser(
        description="Manages project setup and serves documentation using MkDocs."
    )
    parser.add_argument(
        "--setup",
        action="store_true",
        help="Create/recreate .venv and install dependencies from requirements.txt."
    )
    parser.add_argument(
        "--serve",
        action="store_true",
        help="Checks if .venv exists, then runs 'mkdocs serve'. If .venv doesn't exist, it performs setup first."
    )
    parser.add_argument(
        "--venv-name",
        default=".venv",
        help="Name of the virtual environment directory (default: .venv)."
    )
    parser.add_argument(
        "--reqs-file",
        default="requirements.txt",
        help="Path to the requirements file (default: requirements.txt)."
    )

    args = parser.parse_args()

    # Define absolute paths
    venv_path = os.path.abspath(args.venv_name)
    requirements_file = os.path.abspath(args.reqs_file)

    # If no flags are provided, show help and exit
    if not any([args.setup, args.serve]):
        parser.print_help()
        sys.exit(0)

    # --- Handle --setup flag ---
    if args.setup:
        _setup_venv(venv_path, requirements_file)
        logger.info("Setup process completed.")

    # --- Handle --serve flag ---
    if args.serve:
        # Check if venv exists. If not, run setup first.
        if not os.path.exists(venv_path):
            logger.warning(f"Virtual environment '{args.venv_name}' not found. Running setup first...")
            _setup_venv(venv_path, requirements_file)
        else:
            logger.info(f"Virtual environment '{args.venv_name}' found. Skipping setup.")

        _run_mkdocs_serve(venv_path)
        logger.info("MkDocs serve process initiated.")

if __name__ == "__main__":
    main()

