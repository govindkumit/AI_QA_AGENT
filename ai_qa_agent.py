from datetime import datetime


def banner():
    print("=" * 60)
    print("        AI QA AGENT")
    print("=" * 60)
    print(f"Started: {datetime.now()}")
    print("=" * 60)


def main():
    banner()

    print("Step 1 : Initializing AI Agent")
    print("Step 2 : Loading Configuration")
    print("Step 3 : Ready for Execution")


if __name__ == "__main__":
    main()