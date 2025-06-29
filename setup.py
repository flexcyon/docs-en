#!/usr/bin/env python3
# This shebang line ensures the script is executable directly on Linux/macOS systems.

import os
import subprocess
import sys
import shutil
import logging
import logging.handlers # For RotatingFileHandler
import platform # For platform.system()
import argparse

# --- Standalone Utility Functions ---

def rel2abspath(path):
    """Converts a relative path to an absolute path based on the script's directory."""
    return os.path.abspath(os.path.join(os.path.dirname(__file__), path))

def get_log_dir():
    """Returns a suitable directory for logging. Creates it if it doesn't exist."""
    # A generic, user-specific log directory for this setup script
    log_dir = os.path.join(os.path.expanduser("~"), ".local", "share", "python_setup_logs")
    os.makedirs(log_dir, exist_ok=True)
    return log_dir

def setup_logging():
    """Sets up logging for the script."""
    log_dir = get_log_dir()
    log_file = os.path.join(log_dir, "setup.log")

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG) # Set a base level for the logger

    # Ensure handlers are not duplicated if setup_logging is called multiple times
    if not logger.handlers:
        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO) # Info level for console
        console_formatter = logging.Formatter('%(levelname)s: %(message)s')
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

        # File handler
        file_handler = logging.handlers.RotatingFileHandler(
            log_file, maxBytes=5*1024*1024, backupCount=5
        )
        file_handler.setLevel(logging.DEBUG) # Debug level for file
        file_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
        )
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

    return logger

# --- End of Standalone Utility Functions ---


# Initialize logging
logger = setup_logging()

def find_python_executable(version=None):
    """
    Finds a suitable Python executable, prioritizing a specific version if given.
    Returns the path to the executable or raises an error if not found.
    """
    candidates = []
    if version:
        # Prioritize exact version, e.g., "python3.12"
        candidates.append(f"python{version}")
        candidates.append(f"python{version.split('.')[0]}") # e.g., python3
    
    # Fallback to general Python 3 and then just 'python'
    candidates.extend(["python3", "python"])

    for candidate in candidates:
        try:
            # Use shutil.which to find the executable in PATH
            python_path = shutil.which(candidate)
            if python_path:
                # Verify it's a working Python executable
                # Use --version to avoid full interpreter startup for speed
                result = subprocess.run([python_path, "--version"], capture_output=True, text=True, check=False)
                if result.returncode == 0 and "Python" in result.stdout:
                    logger.debug(f"Found Python executable: {python_path} ({result.stdout.strip()})")
                    return python_path
        except Exception:
            # Ignore errors if the command fails (e.g., not found)
            pass
    
    logger.error(f"Could not find a suitable Python executable (tried {', '.join(candidates)}).")
    sys.exit(1)


def get_venv_executables(venv_path: str):
    """
    Determines and returns the paths to the Python interpreter and pip executable
    within the specified virtual environment, based on the operating system.
    Returns a tuple: (venv_python_path, venv_pip_path, venv_activate_cmd).
    """
    if sys.platform == "win32":
        venv_python_path = os.path.join(venv_path, "Scripts", "python.exe")
        venv_pip_path = os.path.join(venv_path, "Scripts", "pip.exe")
        venv_activate_cmd = f"call {os.path.join(venv_path, 'Scripts', 'activate.bat')}"
    else: # Linux, macOS, and other Unix-like systems
        venv_python_path = os.path.join(venv_path, "bin", "python") # Common symlink in venv
        venv_pip_path = os.path.join(venv_path, "bin", "pip")
        # For activate command, need full path
        venv_activate_cmd = f"source {os.path.join(venv_path, 'bin', 'activate')}"

    return venv_python_path, venv_pip_path, venv_activate_cmd


def create_and_install_venv(venv_name=".venv", requirements_file="requirements.txt"):
    """
    Creates a .venv virtual environment, installs dependencies from requirements.txt,
    and provides instructions for manual activation.
    This function is designed to be cross-platform (Windows, Linux, macOS).
    """
    logger.info("Starting local Python virtual environment setup...")

    # Define the path for the virtual environment
    venv_path = rel2abspath(venv_name)

    # Find the Python 3.12 executable (or fallback) to create the venv
    python_to_use = find_python_executable(version="3.12")
    logger.info(f"Using Python interpreter '{python_to_use}' to create virtual environment.")

    # Step 1: Remove existing virtual environment if it exists for a clean setup
    if os.path.exists(venv_path):
        logger.info(f"Removing existing virtual environment at: {venv_path}")
        try:
            shutil.rmtree(venv_path)
            logger.info("Existing virtual environment removed successfully.")
        except OSError as e:
            logger.error(
                f"Error removing virtual environment '{venv_path}': {e}", exc_info=True
            )
            sys.exit(1)

    # Step 2: Create a new Python virtual environment
    logger.info(f"Creating new virtual environment at: {venv_path}")
    try:
        subprocess.run(
            [python_to_use, "-m", "venv", venv_path],
            check=True,
            stdout=sys.stdout, # Direct output of venv creation to console
            stderr=sys.stderr, # Direct errors of venv creation to console
        )
        logger.info("Virtual environment created successfully.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to create virtual environment: {e}", exc_info=True)
        sys.exit(1)
    
    # Get venv executable paths after creation
    venv_python_path, venv_pip_path, venv_activate_cmd = get_venv_executables(venv_path)

    # Step 3: Install Python dependencies from requirements.txt into the new venv
    requirements_file = rel2abspath(requirements_file)
    if os.path.exists(requirements_file):
        logger.info(f"Installing Python dependencies from '{requirements_file}' into '{venv_path}'...")
        # Prepare pip command with increased timeout
        pip_command = [
            venv_pip_path,
            "install",
            "--default-timeout=600", # Increase timeout to 600 seconds (10 minutes)
            "-r",
            requirements_file
        ]
        
        # Ensure the venv_pip_path is valid before running
        if not os.path.exists(venv_pip_path):
            # Fallback check for pip executable name inside venv
            if sys.platform != "win32":
                # Try 'pip3' if 'pip' not found in venv's bin
                venv_pip_path_fallback = os.path.join(venv_path, "bin", "pip3")
                if os.path.exists(venv_pip_path_fallback):
                    venv_pip_path = venv_pip_path_fallback
                    pip_command[0] = venv_pip_path # Update the command list with fallback path
                else:
                    logger.error(f"Neither '{venv_pip_path}' nor '{venv_pip_path_fallback}' found after venv creation.")
                    sys.exit(1)
            else:
                logger.error(f"Pip executable not found at '{venv_pip_path}' after venv creation.")
                sys.exit(1)
        
        try:
            subprocess.run(
                pip_command,
                check=True,
                stdout=sys.stdout, # Direct output of pip install to console
                stderr=sys.stderr, # Direct errors of pip install to console
            )
            logger.info("Dependencies from requirements.txt installed successfully.")
        except subprocess.CalledProcessError as e:
            logger.error(
                f"Failed to install dependencies from requirements.txt: {e}",
                exc_info=True,
            )
            sys.exit(1)
        except FileNotFoundError:
            logger.error(f"Pip executable not found at '{venv_pip_path}'. "
                         "This indicates an issue with virtual environment creation or Python setup.", exc_info=True)
            sys.exit(1)
        except Exception as e:
            logger.error(f"An unexpected error occurred during pip install: {e}", exc_info=True)
            sys.exit(1)
    else:
        logger.warning(
            f"'{requirements_file}' not found. Skipping standard Python dependency installation."
        )

    logger.info("Local virtual environment setup complete.")
    logger.info(f"\nTo manually activate the virtual environment for your session, run:")
    logger.info(f"  {activate_command}")
    logger.info(f"Then you can run your application using 'python {rel2abspath('your_app_name.py')}' or similar.")


def update_script_shebang(script_path: str, venv_python_path: str):
    """
    Updates the shebang line of a specific application script
    to point to the Python executable within the created virtual environment.
    Makes the script executable on Unix-like systems.
    """
    absolute_script_path = rel2abspath(script_path)
    
    if not os.path.exists(absolute_script_path):
        logger.error(f"Script not found at '{absolute_script_path}'. Cannot update shebang.")
        return

    # Ensure venv_python_path is a full absolute path to the interpreter within the venv
    shebang_line = f"#!{venv_python_path}\n"

    try:
        with open(absolute_script_path, 'r+', encoding='utf-8') as f:
            content = f.read()
            f.seek(0)
            
            # Check if shebang exists and is correct
            if content.startswith("#!"):
                first_line = content.splitlines()[0]
                if first_line == shebang_line.strip():
                    logger.info(f"Shebang in '{script_path}' already correct.")
                else:
                    # Replace existing shebang
                    lines = content.splitlines()
                    lines[0] = shebang_line.strip()
                    f.truncate(0) # Clear file
                    f.write('\n'.join(lines) + '\n') # Rewrite with new shebang
                    logger.info(f"Updated shebang in '{script_path}' to use venv Python.")
            else:
                # Add new shebang
                f.write(shebang_line + content)
                logger.info(f"Added shebang to '{script_path}' to use venv Python.")
        
        # Make executable on Unix-like systems
        if sys.platform != "win32":
            # Add executable bits if not already set
            os.chmod(absolute_script_path, os.stat(absolute_script_path).st_mode | 0o111) 
            logger.info(f"Made '{absolute_script_path}' executable.")

    except Exception as e:
        logger.error(f"Failed to update shebang for '{script_path}': {e}", exc_info=True)


# This function remains, but it's not called directly by setup.py anymore.
# It's here for reference/if translate.py needs to call it.
def run_libretranslate_models_init(venv_python_path: str):
    """
    Runs the libretranslate command to load/update language models.
    Assumes libretranslate is installed in the venv.
    """
    logger.info("Initializing/updating libretranslate language models (es, en, zh) via setup.py...")
    
    libretranslate_cmd_path = os.path.join(os.path.dirname(venv_python_path), "libretranslate")
    
    if sys.platform == "win32":
        if os.path.exists(f"{libretranslate_cmd_path}.exe"):
            libretranslate_cmd_path = f"{libretranslate_cmd_path}.exe"
        elif os.path.exists(f"{libretranslate_cmd_path}.cmd"):
            libretranslate_cmd_path = f"{libretranslate_cmd_path}.cmd"
        else:
            libretranslate_cmd_path = None

    cmd = []
    if libretranslate_cmd_path and os.path.exists(libretranslate_cmd_path):
        cmd = [libretranslate_cmd_path, "--load-only", "es,en,zh", "--update-models"]
    else:
        logger.warning("Could not find direct libretranslate executable in venv. Attempting to run as python module.")
        cmd = [venv_python_path, "-m", "libretranslate", "--load-only", "es,en,zh", "--update-models"]

    if not cmd:
        logger.error("Failed to construct libretranslate command for model initialization.")
        sys.exit(1)

    try:
        subprocess.run(
            cmd,
            check=True,
            stdout=sys.stdout,
            stderr=sys.stderr,
        )
        logger.info("Libretranslate models loaded/updated successfully by setup.py.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to load/update libretranslate models: {e}", exc_info=True)
        logger.error(f"Command failed: {' '.join(e.cmd)}")
        sys.exit(1)
    except FileNotFoundError:
        logger.error("Libretranslate command not found. Ensure it's installed via requirements.txt.")
        sys.exit(1)
    except Exception as e:
        logger.error(f"An unexpected error occurred during libretranslate init by setup.py: {e}", exc_info=True)
        sys.exit(1)


def run_translate_script(venv_python_path: str):
    """
    Executes the translate.py script using the venv's Python interpreter.
    """
    translate_script_path = rel2abspath("translate.py")

    if not os.path.exists(translate_script_path):
        logger.error(f"Translate script not found at '{translate_script_path}'. Cannot run.")
        sys.exit(1)
    
    logger.info(f"Attempting to run translation script: {translate_script_path}")
    try:
        subprocess.run(
            [venv_python_path, translate_script_path],
            check=True,
            stdout=sys.stdout,
            stderr=sys.stderr,
        )
        logger.info("Translation script completed successfully.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Translation script failed with error: {e}", exc_info=True)
        logger.error(f"Command failed: {' '.join(e.cmd)}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"An unexpected error occurred while running translate.py: {e}", exc_info=True)
        sys.exit(1)


def main():
    """Main function to orchestrate environment setup and translation workflow."""
    parser = argparse.ArgumentParser(description="Setup and run utilities for the project.")
    parser.add_argument(
        "--setup-local",
        action="store_true",
        help="Create/recreate .venv and install dependencies from requirements.txt."
    )
    parser.add_argument(
        "--run-translate",
        action="store_true",
        help="Run the translation workflow: setup .venv (if needed), update translate.py shebang, and run translate.py (which handles libretranslate models)."
    )
    parser.add_argument(
        "--check-translate",
        action="store_true",
        help="Check the translation setup: ensure .venv exists, update translate.py shebang, and run translate.py (without explicit libretranslate model init by setup.py)."
    )
    args = parser.parse_args()

    # Define common venv path
    venv_path = rel2abspath(".venv")

    # If no flags are provided, default to --setup-local
    if not any([args.setup_local, args.run_translate, args.check_translate]):
        logger.info("No specific action requested. Defaulting to --setup-local.")
        args.setup_local = True # Set flag to trigger default action


    if args.setup_local:
        logger.info("Initiating local setup process...")
        create_and_install_venv()
        logger.info("Local setup process completed.")
    
    if args.run_translate:
        logger.info("Initiating full translation workflow...")
        # Ensure venv is set up first if it's not already
        if not os.path.exists(venv_path):
            logger.warning("Virtual environment not found for translation. Running initial setup...")
            create_and_install_venv()
        else:
            logger.info("Virtual environment already exists. Skipping recreation for --run-translate.")
        
        # Get venv executables after ensuring venv exists
        venv_python_path, _, _ = get_venv_executables(venv_path)
        logger.info(f"Using virtual environment Python at: {venv_python_path}")

        # LibreTranslate model initialization is now handled *within* translate.py
        # setup.py's responsibility is just to launch translate.py correctly.

        # Update translate.py shebang and run it
        translate_script_name = "translate.py"
        logger.info(f"Proceeding to update shebang and run '{translate_script_name}'...")
        update_script_shebang(translate_script_name, venv_python_path)
        run_translate_script(venv_python_path) 
        logger.info(f"Translation script '{translate_script_name}' execution finished.")

    if args.check_translate:
        logger.info("Initiating translation check workflow...")
        # For a check, we assume the venv should already exist.
        if not os.path.exists(venv_path):
            logger.error(f"Virtual environment not found at '{venv_path}'. "
                         "Please run 'python3 setup.py --setup-local' first.")
            sys.exit(1)
        
        # Get venv executables
        venv_python_path, _, _ = get_venv_executables(venv_path)
        logger.info(f"Using virtual environment Python at: {venv_python_path}")

        # Update translate.py shebang and run it
        translate_script_name = "translate.py"
        logger.info(f"Proceeding to update shebang and run '{translate_script_name}' for check...")
        update_script_shebang(translate_script_name, venv_python_path)
        run_translate_script(venv_python_path)
        logger.info(f"Translation script '{translate_script_name}' check finished.")

    logger.info("Script execution finished.")


if __name__ == "__main__":
    # For demonstration, create dummy files if they don't exist
    if not os.path.exists("requirements.txt"):
        with open("requirements.txt", "w") as f:
            f.write("libretranslate\n") # Ensure libretranslate is in requirements
            f.write("requests\n")
            f.write("python-dotenv\n")
            f.write("Pillow\n")
        logger.info("Created a dummy requirements.txt for demonstration purposes.")

    if not os.path.exists("translate.py"):
        with open("translate.py", "w") as f:
            # translate.py now handles libretranslate model initialization itself
            f.write("#!/usr/bin/env python\n") # Placeholder shebang, will be updated by setup.py
            f.write("import sys\n")
            f.write("import os\n")
            f.write("import subprocess\n") # Needed for calling libretranslate
            f.write("import logging\n")
            f.write("import requests\n") # Needed for health check
            f.write("import time\n")   # Needed for sleep in health check
            f.write("\n")
            f.write("logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')\n")
            f.write("logger = logging.getLogger(__name__)\n")
            f.write("\n")
            f.write("def start_libretranslate_internal(target_language):\n")
            f.write("    \"\"\"Start LibreTranslate server using the CLI if not already running, only loading en and the target language.\"\"\"\n")
            f.write("    api_url = \"http://localhost:5000/translate\"\n")
            f.write("    \n")
            f.write("    # Check if server is already running\n")
            f.write("    try:\n")
            f.write("        requests.get(f\"{api_url.replace('/translate', '/health')}\", timeout=2)\n")
            f.write("        logger.info(\"translate.py: LibreTranslate server is already running.\")\n")
            f.write("        return None # Return None if already running, no new process to manage\n")
            f.write("    except requests.exceptions.ConnectionError:\n")
            f.write("        logger.info(\"translate.py: LibreTranslate server not detected, attempting to start...\")\n")
            f.write("    except Exception as e:\n")
            f.write("        logger.warning(f\"translate.py: Unexpected error during health check: {e}\")\n")
            f.write("\n")
            f.write("    logger.info(f\"translate.py: [START] Starting LibreTranslate server using CLI (only en and {target_language})...\")\n")
            f.write("    \n")
            f.write("    # Determine libretranslate executable path from within the venv\n")
            f.write("    venv_bin_dir = os.path.dirname(sys.executable)\n")
            f.write("    libretranslate_cmd_path = os.path.join(venv_bin_dir, \"libretranslate\")\n")
            f.write("\n")
            f.write("    cmd_list = []\n")
            f.write("    if sys.platform == \"win32\":\n")
            f.write("        if os.path.exists(f\"{libretranslate_cmd_path}.exe\"):\n")
            f.write("            libretranslate_cmd_path = f\"{libretranslate_cmd_path}.exe\"\n")
            f.write("        elif os.path.exists(f\"{libretranslate_cmd_path}.cmd\"):\n")
            f.write("            libretranslate_cmd_path = f\"{libretranslate_cmd_path}.cmd\"\n")
            f.write("        else:\n")
            f.write("            libretranslate_cmd_path = None\n")
            f.write("\n")
            f.write("    if libretranslate_cmd_path and os.path.exists(libretranslate_cmd_path):\n")
            f.write("        cmd_list = [libretranslate_cmd_path, \"--host\", \"127.0.0.1\", \"--port\", \"5000\", \"--load-only\", f\"en,{target_language}\"]\n")
            f.write("    else:\n")
            f.write("        logger.warning(\"translate.py: Could not find direct libretranslate executable. Attempting to run as python module.\")\n")
            f.write("        cmd_list = [sys.executable, \"-m\", \"libretranslate\", \"--host\", \"127.0.0.1\", \"--port\", \"5000\", \"--load-only\", f\"en,{target_language}\"]\n")
            f.write("\n")
            f.write("    if not cmd_list:\n")
            f.write("        logger.error(\"translate.py: Failed to construct libretranslate command.\")\n")
            f.write("        return None\n")
            f.write("\n")
            f.write("    try:\n")
            f.write("        process = subprocess.Popen(\n")
            f.write("            cmd_list,\n")
            f.write("            stdout=subprocess.DEVNULL, # Suppress stdout\n")
            f.write("            stderr=subprocess.DEVNULL, # Suppress stderr\n")
            f.write("            # preexec_fn=os.setsid, # For Unix-like: makes process independent of parent shell\n")
            f.write("        )\n")
            f.write("        # Wait for server to start\n")
            f.write("        for _ in range(30): # Wait up to 30 seconds\n")
            f.write("            try:\n")
            f.write("                requests.get(f\"{api_url.replace('/translate', '/health')}\", timeout=2)\n")
            f.write("                logger.info(\"translate.py: [START] LibreTranslate server started successfully.\")\n")
            f.write("                return process # Return the process object so it can be terminated later\n")
            f.write("            except requests.exceptions.ConnectionError:\n")
            f.write("                time.sleep(1)\n")
            f.write("        \n")
            f.write("        logger.error(\"translate.py: Failed to start LibreTranslate server within timeout.\")\n")
            f.write("        if process.poll() is None: # If process is still running, try to terminate it\n")
            f.write("            process.terminate()\n")
            f.write("        return None\n")
            f.write("    except FileNotFoundError:\n")
            f.write("        logger.error(\"translate.py: Libretranslate executable/module not found. Ensure it's installed.\")\n")
            f.write("        return None\n")
            f.write("    except Exception as e:\n")
            f.write("        logger.error(f\"translate.py: Error attempting to start LibreTranslate: {e}\")\n")
            f.write("        return None\n")
            f.write("\n")
            f.write("if __name__ == \"__main__\":\n")
            f.write("    logger.info(\"--------------------------------------------------\")\n")
            f.write("    logger.info(f\"Hello from translate.py! Running with Python: {sys.executable}\")\n")
            f.write("    logger.info(f\"Current working directory: {os.getcwd()}\")\n")
            f.write("\n")
            f.write("    # Placeholder for actual translation logic.\n")
            f.write("    # This script would typically accept arguments for target language, input/output paths.\n")
            f.write("    # For demonstration, we'll hardcode 'zh' as a target language and initiate LibreTranslate.\n")
            f.write("    target_lang_for_init = \"zh\" # Or get from argparse if translate.py has its own parser\n")
            f.write("\n")
            f.write("    lt_process = None\n")
            f.write("    try:\n")
            f.write("        lt_process = start_libretranslate_internal(target_lang_for_init)\n")
            f.write("        if lt_process is not None or requests.get(\"http://localhost:5000/health\", timeout=2).status_code == 200:\n")
            f.write("            logger.info(\"translate.py: LibreTranslate models are ready. Proceeding with actual translation logic.\")\n")
            f.write("            # Your actual translation logic goes here\n")
            f.write("            logger.info(\"translate.py: This is where your core translation logic would execute.\")\n")
            f.write("            # Example: Call translation service, process text, update cache, etc.\n")
            f.write("            \n")
            f.write("            # Dummy calls to translation functions to ensure they are runnable\n")
            f.write("            # Note: These would need an actual LibreTranslate server to be running and available\n")
            f.write("            # on localhost:5000\n")
            f.write("            # from translate_lib import translate_text, batch_translate_text, run_translation, save_cache, load_cache, load_edit_cache # Assuming these are in a separate lib\n")
            f.write("            # For this dummy, we'll just print.\n")
            f.write("            dummy_text = \"Hello world!\"\n")
            f.write("            logger.info(f\"translate.py: Simulating translation of: '{dummy_text}'\")\n")
            f.write("            # You would call your translation functions here, e.g.:\n")
            f.write("            # translated_dummy_text = translate_text(dummy_text, target_lang=\"zh\", edit_cache={}, api_url=\"http://localhost:5000/translate\")\n")
            f.write("            # logger.info(f\"translate.py: Translated (dummy): {translated_dummy_text}\")\n")
            f.write("\n")
            f.write("        else:\n")
            f.write("            logger.error(\"translate.py: Failed to initialize LibreTranslate models. Aborting translation.\")\n")
            f.write("    except requests.exceptions.ConnectionError:\n")
            f.write("        logger.error(\"translate.py: Could not connect to LibreTranslate after trying to start it. Is it installed and able to run?\")\n")
            f.write("    except Exception as e:\n")
            f.write("        logger.error(f\"translate.py: An unexpected error occurred in main translation logic: {e}\")\n")
            f.write("        \n")
            f.write("    finally:\n")
            f.write("        if lt_process:\n")
            f.write("            logger.info(\"translate.py: Terminating LibreTranslate server process.\")\n")
            f.write("            lt_process.terminate()\n")
            f.write("            lt_process.wait(timeout=5) # Give it a moment to terminate\n")
            f.write("            if lt_process.poll() is None:\n")
            f.write("                logger.warning(\"translate.py: LibreTranslate process did not terminate gracefully, killing.\")\n")
            f.write("                lt_process.kill()\n")
            f.write("            logger.info(\"translate.py: LibreTranslate server terminated.\")\n")
            f.write("    logger.info(\"--------------------------------------------------\")\n")
        logger.info("Created a dummy translate.py for demonstration purposes.")

    main()
