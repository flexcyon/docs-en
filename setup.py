#!/usr/bin/env python
import argparse
import os
import subprocess
import sys
import shutil
import logging
import time
from glob import glob

# --- Add watchdog import and its dependencies ---
try:
    from watchdog.observers import Observer
    # Import specific event types for better filtering
    from watchdog.events import FileSystemEventHandler, FileModifiedEvent, FileCreatedEvent, FileDeletedEvent
except ImportError:
    pass

# --- 1. Basic Logging Setup ---
# Configure basic logging for the script
# Setting level to DEBUG can help see debounced events
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- 2. Helper Functions for Virtual Environment Paths ---
def _get_venv_paths(venv_path):
    # ... (unchanged) ...
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
    # ... (unchanged) ...
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
            
            # --- IMPORTANT: Explicitly install watchdog for the file watching feature ---
            logger.info("Installing 'watchdog' for Markdown file watching...")
            subprocess.run([venv_uv_path, "pip", "install", "watchdog"], check=True,
                           stdout=sys.stdout, stderr=sys.stderr)
            
            logger.info(f"Python dependencies and 'watchdog' installed successfully into '{venv_path}' using 'uv'.")
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to install Python dependencies or 'watchdog' using 'uv'. Command: {' '.join(e.cmd)} Error: {e}")
            sys.exit(1)
        except FileNotFoundError:
            logger.error(f"Error: uv executable not found at '{venv_uv_path}'. 'uv' might not have installed correctly.")
            sys.exit(1)
        except Exception as e:
            logger.error(f"An unexpected error occurred while installing Python dependencies with 'uv': {e}")
            sys.exit(1)
    else:
        logger.warning(f"Requirements file '{requirements_file}' not found. Skipping dependency installation.")
        # We still need to install watchdog even if no requirements.txt, if serve is to be run
        logger.info("Installing 'watchdog' for Markdown file watching...")
        try:
            subprocess.run([venv_uv_path, "pip", "install", "watchdog"], check=True,
                           stdout=sys.stdout, stderr=sys.stderr)
            logger.info("'watchdog' installed successfully.")
        except Exception as e:
            logger.error(f"Failed to install 'watchdog': {e}")
            sys.exit(1)

    logger.info("Virtual environment setup complete.")

# --- 4. Core Function: Run MkDocs Serve ---
def _run_mkdocs_serve(venv_path):
    # ... (unchanged) ...
    """
    Runs 'mkdocs serve' using the Python interpreter from the specified venv.
    Returns the subprocess Popen object.
    """
    _, _, _, venv_mkdocs_path = _get_venv_paths(venv_path)

    if not os.path.exists(venv_mkdocs_path):
        logger.error(f"mkdocs executable not found at '{venv_mkdocs_path}'. "
                     "Please ensure mkdocs is listed in your requirements.txt and setup is run.")
        sys.exit(1)

    try:
        logger.info(f"Executing: {venv_mkdocs_path} serve")
        # Start mkdocs serve as a child process, do not wait for it to finish
        process = subprocess.Popen([venv_mkdocs_path, "serve"], stdout=sys.stdout, stderr=sys.stderr)
        return process
    except Exception as e:
        logger.error(f"An error occurred while running mkdocs serve: {e}")
        sys.exit(1)

# --- 5. New Core Function: File Watcher Handler (UPDATED FOR SPECIFIC EVENTS) ---
class MarkdownChangeHandler(FileSystemEventHandler):
    """
    Custom handler to detect Markdown file changes, debounce events,
    and signal a single restart, filtering for specific file modification events.
    """
    def __init__(self, debounce_time=0.5):
        super().__init__()
        self.restart_required = False
        self.debounce_time = debounce_time
        # Stores the time of the last recorded event that triggered a restart
        self._last_trigger_time = 0
        
        # Define the specific event types we care about
        self.relevant_events = (FileModifiedEvent, FileCreatedEvent, FileDeletedEvent)

    def on_any_event(self, event):
        # 1. Check if the event is for a file and is one of the relevant types
        if event.is_directory or not isinstance(event, self.relevant_events):
            return

        # 2. Check if the file is a Markdown file
        if not event.src_path.endswith('.md'):
            return

        # 3. Apply Debouncing Logic
        current_time = time.time()
        
        # Check if enough time has passed since the last actual restart was requested
        if (current_time - self._last_trigger_time) > self.debounce_time:
            # This is a new, isolated change event
            logger.info(f"\n📝 Markdown {type(event).__name__.replace('File', '')} Detected: {event.src_path}")
            self.restart_required = True
            self._last_trigger_time = current_time # Record the time of the new trigger
        else:
            # Ignore rapid-fire events from a single save action
            # Use logger.debug if you want to see how many events are being ignored
            pass 

# --- 6. New Core Function: Watch and Serve Loop ---
def _watch_and_serve(venv_path):
    # ... (unchanged, as the change was only in the handler logic) ...
    """
    Runs mkdocs serve and starts a file system watcher on **/*.md files.
    If a Markdown change is detected, it restarts the mkdocs serve process.
    """
    # 1. Start the initial mkdocs serve process
    mkdocs_process = _run_mkdocs_serve(venv_path)

    # 2. Setup the Watchdog Observer
    # The debouncing logic is now inside the handler class.
    event_handler = MarkdownChangeHandler(debounce_time=1.0) # Wait 1.0 second after a change before acting
    
    observer = Observer()
    
    # Watch the current working directory recursively
    observer.schedule(event_handler, path=os.getcwd(), recursive=True)
    observer.start()
    
    logger.info(f"Watching for changes in **/*.md files in {os.getcwd()} (Will restart server on change)...")
    logger.info("Press Ctrl+C to stop both the watcher and mkdocs serve.")

    try:
        while True:
            # Check for Markdown change signal
            if event_handler.restart_required:
                logger.warning("Restarting mkdocs serve due to debounced Markdown file change...")
                
                # Terminate the current mkdocs process
                if mkdocs_process.poll() is None: # Check if it's still running
                    # Use SIGTERM (default terminate)
                    mkdocs_process.terminate()
                    try:
                        mkdocs_process.wait(timeout=5) # Wait for it to properly shut down
                    except subprocess.TimeoutExpired:
                        logger.error("MkDocs process did not terminate gracefully. Forcing kill.")
                        mkdocs_process.kill()
                        
                # Restart the mkdocs process
                mkdocs_process = _run_mkdocs_serve(venv_path)
                
                # Reset the restart flag
                event_handler.restart_required = False

            # Wait for a short period before checking the flag again
            time.sleep(1) # This sleep interval controls the loop checking speed.

    except KeyboardInterrupt:
        logger.info("\nCaught KeyboardInterrupt. Stopping services.")
    finally:
        # 3. Cleanup: Stop the observer and the mkdocs process
        observer.stop()
        observer.join()
        if mkdocs_process.poll() is None:
            mkdocs_process.terminate()
            mkdocs_process.wait(timeout=5)
        logger.info("Watcher and mkdocs serve stopped.")


# --- 7. Main Script Logic ---
def main():
    # ... (unchanged) ...
    parser = argparse.ArgumentParser(
        description="Manages project setup and serves documentation using MkDocs."
    )
    parser.add_argument(
        "--setup",
        action="store_true",
        help="Create/recreate .venv and install dependencies from requirements.txt."
    )
    # The --serve flag description is updated to reflect the new watch feature
    parser.add_argument(
        "--serve",
        action="store_true",
        help="Checks if .venv exists, then runs 'mkdocs serve' with Markdown file watching and automatic restart."
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
            # Check if watchdog is installed before proceeding to watch
            try:
                import watchdog.observers
                # Ensure the specific event classes are available
                from watchdog.events import FileModifiedEvent 
            except ImportError:
                logger.error("The 'watchdog' package is required for --serve but not found in the venv. Please run --setup.")
                sys.exit(1)
                
            logger.info(f"Virtual environment '{args.venv_name}' found. Skipping setup.")

        # Call the watch and serve function
        _watch_and_serve(venv_path)
        logger.info("MkDocs watch and serve process finished.")


if __name__ == "__main__":
    main()
