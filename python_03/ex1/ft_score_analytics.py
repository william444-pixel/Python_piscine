import sys


def score_manipulation():
    print("=== Player Score Analytics ===")
    try:
        scores = [int(x) for x in sys.argv[1:]]
        if not scores:
            print("No scores provided. Usage: "
                  "python3 ft_score_analytics.py <score1> <score2> ...")
            return
        total = sum(scores)
        length = len(scores)
        maxi = max(scores)
        mini = min(scores)
        rang = maxi - mini
        if len(scores) >= 1:
            print(f"Scores processed: {scores}")
            print(f"Total players: {len(scores)}")
            print(f"Total score: {total}")
            print(f"Average score: {total/length}")
            print(f"High score: {maxi}")
            print(f"Low score: {mini}")
            print(f"Score range: {rang}")
    except ValueError:
        print("Error: Please provide only integer numbers.")


score_manipulation()
