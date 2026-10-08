from scripts.collect_jobs import main as collect_jobs
from scripts.report import main as report
from scripts.score_jobs import main as score_jobs


def main():

    print("=== Collecting jobs ===")
    collect_jobs()

    print("=== Scoring jobs ===")
    score_jobs()

    print("=== Generating report ===")
    report()


if __name__ == "__main__":
    main()
