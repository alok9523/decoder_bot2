import subprocess

def run_code(language, code):
    """
    Executes the given code in the specified language and returns the output.
    Supported languages: Python, JavaScript, Bash, etc.
    """
    try:
        if language.lower() == "python":
            result = subprocess.run(["python3", "-c", code], capture_output=True, text=True, timeout=10)

        elif language.lower() == "javascript":
            result = subprocess.run(["node", "-e", code], capture_output=True, text=True, timeout=10)

        elif language.lower() == "bash":
            result = subprocess.run(["bash", "-c", code], capture_output=True, text=True, timeout=10)

        else:
            return f"Unsupported language: {language}"

        if result.returncode == 0:
            return result.stdout.strip() or "Execution finished with no output."
        else:
            return f"Error:\n{result.stderr.strip()}"

    except subprocess.TimeoutExpired:
        return "Error: Code execution timed out."

    except Exception as e:
        return f"Error: {str(e)}"
