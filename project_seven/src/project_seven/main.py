#!/usr/bin/env python

import sys
import warnings
from datetime import datetime

from project_seven.crew import ProjectSeven

# Ignore syntax warnings from pysbd
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew with a topic and file.
    """
    inputs = {
        "file_path": "/Users/sabarinath404/--study-projects-allianz/Agentic ai projects/project_seven/src/project_seven/EVpaper.pdf",
        "topic": "electric vehicles",
        "current_year": str(datetime.now().year)
    }

    try:
        ProjectSeven().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"❌ Error running the crew: {e}")


def train():
    """
    Train the crew with n_iterations and output filename.
    Usage: python main.py train <n_iterations> <filename>
    """
    if len(sys.argv) < 4:
        raise ValueError("Usage: python main.py train <n_iterations> <filename>")

    n_iterations = int(sys.argv[2])
    filename = sys.argv[3]

    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }

    try:
        ProjectSeven().crew().train(n_iterations=n_iterations, filename=filename, inputs=inputs)
    except Exception as e:
        raise Exception(f"❌ Error training the crew: {e}")


def replay():
    """
    Replay from a specific task.
    Usage: python main.py replay <task_id>
    """
    if len(sys.argv) < 3:
        raise ValueError("Usage: python main.py replay <task_id>")

    task_id = sys.argv[2]

    try:
        ProjectSeven().crew().replay(task_id=task_id)
    except Exception as e:
        raise Exception(f"❌ Error replaying the crew: {e}")


def test():
    """
    Test the crew execution.
    Usage: python main.py test <n_iterations> <eval_llm>
    """
    if len(sys.argv) < 4:
        raise ValueError("Usage: python main.py test <n_iterations> <eval_llm>")

    n_iterations = int(sys.argv[2])
    eval_llm = sys.argv[3]

    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }

    try:
        ProjectSeven().crew().test(n_iterations=n_iterations, eval_llm=eval_llm, inputs=inputs)
    except Exception as e:
        raise Exception(f"❌ Error testing the crew: {e}")


if __name__ == "__main__":
    """
    Command-line entry point.
    Usage:
      python main.py run
      python main.py train <n_iterations> <filename>
      python main.py replay <task_id>
      python main.py test <n_iterations> <eval_llm>
    """
    if len(sys.argv) < 2:
        print("Usage: python main.py [run|train|replay|test]")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "run":
        run()
    elif command == "train":
        train()
    elif command == "replay":
        replay()
    elif command == "test":
        test()
    else:
        print(f"Unknown command: {command}")
