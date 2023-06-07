# Key pair of outputs, as individual points correlate to a specific output
# 0 = Love
# 1 = 15
# 2 = 30
# 3 = 40
# 4+++ == Winner if won by 2


point_output = {
    0: 'Love',
    1: '15',
    2: '30',
    3: '40'
}


# Scores will only have 2 values
def calculate_score(game_score: list) -> str:
    # Makes things easier to see who has the specific points
    raw_server, raw_opponent = game_score[0], game_score[1]

    # Getting the absolute value gives us the true difference without worrying about a negative value
    # If we get a negative value, this will affect how we check ad-in/ad-out
    point_difference = abs(raw_server - raw_opponent)

    # Cases where points for both players is greater than 3
    if raw_server >= 3 and raw_opponent >= 3:
        
        # By checking if our point difference is less than 2 and if our opponent has a value >= 3,
        # We can ensure we are able to check for deuces, as deuces can only occur once both players have hit 3
        if point_difference == 1:
            if raw_server > raw_opponent:
                return "Ad-in"
            if raw_opponent > raw_server:
                return "Ad-out"

        # In this case, we are at 3 or more points for both players. We have established that they do not 
        if raw_server > raw_opponent:
            return "Server wins"
        if raw_opponent > raw_server:
            return "Opponent wins"

        # Return deuces if we did not hit any of the cases mentioned above
        # If we are at 3 points, we have already checked for ad-in/ad-out, and winners
        return "Deuces"

    # If the players have less than 4 points, appoint them a score output
    if raw_server < 4:
        server_output = point_output[raw_server]
    if raw_opponent < 4:
        opponent_output = point_output[raw_opponent]

    # Check for winners when we are not above 3 for BOTH players
    if (raw_server == 4 or raw_opponent == 4) and point_difference >= 2:
        if raw_server > raw_opponent:
            return "Server wins"
        if raw_opponent > raw_server:
            return "Opponent wins"

    # Returning server_output if the score is tied and below 4 points, doesn't matter which player we choose
    if server_output == opponent_output:
        return f"{server_output} all"
    
    # Absolute case, if we don't hit anything, just return the regular score
    return f"{server_output} - {opponent_output}"


if __name__ == '__main__':
    print("main")