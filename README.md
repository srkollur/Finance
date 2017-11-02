# Finance
Stock Price Predictor
IMPORTANT: The algorithm that should be run is called "Final Automatic Algorithm"

INSTRUCTIONS: In the data inputs, input the most recent day, the number of days forward that you want predicted
 (i.e. 30 days into the future, 60 days, etc.), and the ticker that you want predicted. Down at the bottom, comment IN methods relating to clf1 and accuracy1 if you want the RandomForest, or clf2 and accuracy2 if you want KNN, etc.). CLF1 - CLF7 are listed in order of accuracy. The final section (CLF1 - CLF3 and ECLF) is an ensemble method that uses a Voter Classification. You can play around with the weights, but it seems like the RandomForest is just more accurate. Comment OUT everything after X_train, X_test etc. if you want to use it. 
 
 IMPORTANT NOTE: Sometimes the yahoo finance API call doesn't work (you get some sort of query error). If this happens, just hit run again and it should work. If that doesn't work, close the shell and then run again. Just running it again should resolve the error. Currently trying to find a more consistent data source. 
