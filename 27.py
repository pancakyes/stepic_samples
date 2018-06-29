n = int(input())

teams = {}

for _ in range(n):
    team1, scores_team1, team2, scores_team2 = input().split(';')

    if team1 in teams:
        teams[team1][0] += 1
    else:
        teams[team1] = [1, 0, 0, 0, 0]
    
    if team2 in teams:
        teams[team2][0] += 1
    else:
        teams[team2] = [1, 0, 0, 0, 0]

    scores_team1 = int(scores_team1)
    scores_team2 = int(scores_team2)

    if scores_team1 > scores_team2:
        teams[team1][1] += 1
        teams[team1][4] += 3
        teams[team2][3] += 1
    elif scores_team1 == scores_team2:
        teams[team1][2] += 1
        teams[team2][2] += 1
        teams[team1][4] += 1
        teams[team2][4] += 1
    else:
        teams[team2][1] += 1
        teams[team2][4] += 3
        teams[team1][3] += 1

for every in teams:
    print(every + ':' + ' '.join([str(i) for i in teams[every]]))
