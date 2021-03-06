import data
import numpy as np
from sklearn.naive_bayes import GaussianNB

if __name__ == "__main__":
    trainingX, trainingY, team_stats = data.get_data()

    print("Generated training set!")

    tourney_teams, team_id_map = data.get_tourney_teams(2017)
    tourney_teams.sort()

    print("Got tourney teams!")

    testingXtemp = []
    testingYtemp = []

    matchups = []

    for team_1 in tourney_teams:
        for team_2 in tourney_teams:
            if team_1 < team_2:
                game_features = data.get_game_features(team_1, team_2, 0, 2017, team_stats)
                testingXtemp.append(game_features)

                game = [team_1, team_2]
                matchups.append(game)

    testingX = np.array(testingXtemp)
    
    print("Generated testing set!")

    gnb = GaussianNB()
    gnb.fit(trainingX, np.ravel(trainingY))

    print("Done fitting the model!")

    # make predictions
    
    testPredictions = gnb.predict_proba(testingX)

    print("Finished Gaussian Naive Bayes predictions!")

    for i in range(0, len(matchups)):
        
        matchups[i].append(testPredictions[i][0])

    results = np.array(matchups)
    np.savetxt("NaiveBayes_Probs_2017.csv", results, delimiter=",", fmt='%s')

    
