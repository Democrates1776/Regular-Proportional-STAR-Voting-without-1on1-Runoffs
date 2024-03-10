import pandas as pd
import numpy as np
#Credit to https://electowiki.org/wiki/Allocated_Score
#    Allocated Score is another name for STAR-PR

def gather_input():
    num_candidates = int(input("Enter the number of candidates: "))
    candidate_names = []
    for i in range(num_candidates):
        name = input(f"Enter the name of candidate {i + 1}: ")
        candidate_names.append(name)

    num_seats = int(input("Enter the number of seats: "))

    scores_input = input(
        "Enter all the ballots separated by space with no space within each ballot e.g. 231 215 421: ")
    scores_list = scores_input.split()

    if any(len(ballot) != num_candidates for ballot in scores_list):
        raise ValueError("Each ballot should have the same number of scores as the number of candidates.")

    num_voters = len(scores_list)
    scores_matrix = np.array([list(ballot) for ballot in scores_list], dtype=int)

    return pd.DataFrame(scores_matrix, columns=candidate_names), num_seats


def allocated_score(ballots, seats):
    max_score = 5  # Maximum score is always 5
    # ballots = ballots / max_score  # Normalize ballots
    voters, _ = ballots.shape
    quota = voters / seats
    ballot_weight = pd.Series(np.ones(voters), name="weights")
    winner_list = []
    round_num = 1

    while len(winner_list) < seats:
        weighted_scores = ballots.multiply(ballot_weight, axis="index")
        total_scores = weighted_scores.sum()

        print(f"\nRound {round_num} - Scores of the candidates:")
        for candidate, score in total_scores.sort_values(ascending=False).items():
            formatted_score = "{:.4f}".format(score).rstrip('0').rstrip('.')
            print(f"{candidate}: {formatted_score}")

        winner = total_scores.idxmax()
        winner_list.append(winner)
        ballots.drop(winner, axis=1, inplace=True)

        cand_df = pd.concat([ballot_weight, weighted_scores[winner]], axis=1).copy()
        cand_df_sort = cand_df.sort_values(by=[winner], ascending=False).copy()
        split_point = cand_df_sort[cand_df_sort["weights"].cumsum() < quota][winner].min()
        spent_above = cand_df[cand_df[winner] > split_point]["weights"].sum()

        if spent_above > 0:
            cand_df.loc[cand_df[winner] > split_point, "weights"] = 0.0

        weight_on_split = cand_df[cand_df[winner] == split_point]["weights"].sum()
        if weight_on_split > 0:
            spent_value = (quota - spent_above) / weight_on_split
            cand_df.loc[cand_df[winner] == split_point, "weights"] *= (1 - spent_value)

        ballot_weight = cand_df["weights"].clip(0.0, 1.0)
        round_num += 1

    return winner_list


# Main part of the script
if __name__ == "__main__":
    ballots, seats = gather_input()
    winners = allocated_score(ballots, seats)
    print("\nWinners:", winners)
