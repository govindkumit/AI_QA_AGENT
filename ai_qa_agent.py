from agents.explorer import Explorer
from agents.planner import Planner
from agents.executor import Executor
from agents.analyzer import Analyzer


def main():

    print("=" * 60)
    print("AI QA AGENT")
    print("=" * 60)

    explorer = Explorer()
    explorer.explore()

    planner = Planner()
    planner.generate_test_cases()

    executor = Executor()
    executor.execute()

    analyzer = Analyzer()
    analyzer.analyze()

    print("\nAI QA Agent Completed Successfully")


if __name__ == "__main__":
    main()