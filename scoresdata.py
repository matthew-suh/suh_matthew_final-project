# # Team Data according to 

# # dallasScores = {
# #     "Average PPG (2023)": "31.5",
# #     "Last 3": "42.3",
# #     "Last 1": "45.0",
# #     "Average Home Points": "41.0",
# #     "Average Away Points": "23.7",
# #     "Average PPG (2022)": "26.8"
# # }
# # print(dallasScores)

# scoresData = {
#     'Arizona': {'PPG/F Home': 23.2, 'PPG/F Away': 11.2, 'Pass TD/F Home': 1.2, 'Pass TD/F Away': 0.5, 'Rush TD/F Home': 1.5, 'Rush TD/F Away': 0.3, 'FGM/F Home': 1.7, 'FGM/F Away': 1.5, 'PPG/A Home': 28.7, 'PPG/A Away': 24.8, 'Pass TD/A Home': 2, 'Pass TD/A Away': 1.5, 'Rush TD/A Home': 1.3, 'Rush TD/A Away': 1.3, 'FGM/A Home': 1.5, 'FGM/A Away': 1.7, 'Home Off Str.': '107.52%', 'Away Off Str.': '50.87%', 'Home Def Str.': '147.33%', 'Away Def Str.': '112.83%'},
    
#     'Atlanta': {'PPG/F Home': 23, 'PPG/F Away': 15, 'Pass TD/F Home': 1.2, 'Pass TD/F Away': 0.6, 'Rush TD/F Home': 1, 'Rush TD/F Away': 0.8, 'FGM/F Home': 2.2, 'FGM/F Away': 1.8, 'PPG/A Home': 20.5, 'PPG/A Away': 21.8, 'Pass TD/A Home': 1.7, 'Pass TD/A Away': 1.4, 'Rush TD/A Home': 0.2, 'Rush TD/A Away': 0.6, 'FGM/A Home': 2.5, 'FGM/A Away': 2.2, 'Home Off Str.': '98.88%', 'Away Off Str.': '75.19%', 'Home Def Str.': '101.92%', 'Away Def Str.': '92.74%'},
    
#     'Baltimore': {'PPG/F Home': 30.7, 'PPG/F Away': 23.3, 'Pass TD/F Home': 1.2, 'Pass TD/F Away': 1.2, 'Rush TD/F Home': 2.3, 'Rush TD/F Away': 1.3, 'FGM/F Home': 1.5, 'FGM/F Away': 2, 'PPG/A Home': 15.5, 'PPG/A Away': 15.7, 'Pass TD/A Home': 0.7, 'Pass TD/A Away': 1, 'Rush TD/A Home': 0.3, 'Rush TD/A Away': 0.3, 'FGM/A Home': 2.5, 'FGM/A Away': 1.7, 'Home Off Str.': '137.43%', 'Away Off Str.': '120.62%', 'Home Def Str.': '69.57%', 'Away Def Str.': '64.34%'},
    
#     'Buffalo': {'PPG/F Home': 29.7, 'PPG/F Away': 25, 'Pass TD/F Home': 2.5, 'Pass TD/F Away': 1.5, 'Rush TD/F Home': 1.2, 'Rush TD/F Away': 1.2, 'FGM/F Home': 1.3, 'FGM/F Away': 1.7, 'PPG/A Home': 14.5, 'PPG/A Away': 23.3, 'Pass TD/A Home': 1.2, 'Pass TD/A Away': 1.5, 'Rush TD/A Home': 0.3, 'Rush TD/A Away': 1, 'FGM/A Home': 1.5, 'FGM/A Away': 1.7, 'Home Off Str.': '135.01%', 'Away Off Str.': '127.45%', 'Home Def Str.': '74.48%', 'Away Def Str.': '103.44%'},
    
#     'Carolina': {'PPG/F Home': 13.6, 'PPG/F Away': 17.5, 'Pass TD/F Home': 0.8, 'Pass TD/F Away': 1.2, 'Rush TD/F Home': 0, 'Rush TD/F Away': 0.5, 'FGM/F Home': 2.2, 'FGM/F Away': 1.2, 'PPG/A Home': 22.8, 'PPG/A Away': 29.7, 'Pass TD/A Home': 1, 'Pass TD/A Away': 1.3, 'Rush TD/A Home': 1, 'Rush TD/A Away': 2.2, 'FGM/A Home': 1.2, 'FGM/A Away': 1.2, 'Home Off Str.': '52.22%', 'Away Off Str.': '84.55%', 'Home Def Str.': '101.47%', 'Away Def Str.': '137.74%'},
    
#     'Chicago': {'PPG/F Home': 21.4, 'PPG/F Away': 19.3, 'Pass TD/F Home': 1.2, 'Pass TD/F Away': 1.3, 'Rush TD/F Home': 1, 'Rush TD/F Away': 0.6, 'FGM/F Home': 1.6, 'FGM/F Away': 2.1, 'PPG/A Home': 22.6, 'PPG/A Away': 26.1, 'Pass TD/A Home': 1.6, 'Pass TD/A Away': 2.1, 'Rush TD/A Home': 0.2, 'Rush TD/A Away': 0.7, 'FGM/A Home': 1.6, 'FGM/A Away': 1.6, 'Home Off Str.': '92.55%', 'Away Off Str.': '98.26%', 'Home Def Str.': '98.37%', 'Away Def Str.': '113.00%'},
    
#     'Cincinnati': {'PPG/F Home': 20.2, 'PPG/F Away': 18.2, 'Pass TD/F Home': 1.5, 'Pass TD/F Away': 1.6, 'Rush TD/F Home': 0.5, 'Rush TD/F Away': 0.2, 'FGM/F Home': 1.7, 'FGM/F Away': 1.4, 'PPG/A Home': 20, 'PPG/A Away': 24.4, 'Pass TD/A Home': 0.8, 'Pass TD/A Away': 1.6, 'Rush TD/A Home': 1, 'Rush TD/A Away': 1.2, 'FGM/A Home': 2.3, 'FGM/A Away': 1.6, 'Home Off Str.': '85.63%', 'Away Off Str.': '89.77%', 'Home Def Str.': '97.27%', 'Away Def Str.': '111.28%'},
    
#     'Cleveland': {'PPG/F Home': 18.8, 'PPG/F Away': 25.2, 'Pass TD/F Home': 0.8, 'Pass TD/F Away': 0.8, 'Rush TD/F Home': 0.8, 'Rush TD/F Away': 1.2, 'FGM/F Home': 2.3, 'FGM/F Away': 2.8, 'PPG/A Home': 10.2, 'PPG/A Away': 29.6, 'Pass TD/A Home': 0.5, 'Pass TD/A Away': 1.4, 'Rush TD/A Home': 0.7, 'Rush TD/A Away': 1.6, 'FGM/A Home': 0.7, 'FGM/A Away': 1.4, 'Home Off Str.': '79.87%', 'Away Off Str.': '116.09%', 'Home Def Str.': '53.99%', 'Away Def Str.': '124.32%'},
    
#     'Dallas': {'PPG/F Home': 41, 'PPG/F Away': 23.7, 'Pass TD/F Home': 3, 'Pass TD/F Away': 1.3, 'Rush TD/F Home': 1, 'Rush TD/F Away': 0.8, 'FGM/F Home': 2.2, 'FGM/F Away': 1.8, 'PPG/A Home': 12, 'PPG/A Away': 20.8, 'Pass TD/A Home': 0.8, 'Pass TD/A Away': 1.7, 'Rush TD/A Home': 0.4, 'Rush TD/A Away': 1, 'FGM/A Home': 1.2, 'FGM/A Away': 0.8, 'Home Off Str.': '165.27%', 'Away Off Str.': '110.25%', 'Home Def Str.': '60.36%', 'Away Def Str.': '97.73%'},
    
#     'Denver': {'PPG/F Home': 23.3, 'PPG/F Away': 20.8, 'Pass TD/F Home': 1.9, 'Pass TD/F Away': 1.8, 'Rush TD/F Home': 0.4, 'Rush TD/F Away': 0, 'FGM/F Home': 2.4, 'FGM/F Away': 1.8, 'PPG/A Home': 20.1, 'PPG/A Away': 34.8, 'Pass TD/A Home': 1.1, 'Pass TD/A Away': 2.8, 'Rush TD/A Home': 0.6, 'Rush TD/A Away': 1.8, 'FGM/A Home': 2.3, 'FGM/A Away': 1, 'Home Off Str.': '100.68%', 'Away Off Str.': '97.23%', 'Home Def Str.': '94.96%', 'Away Def Str.': '163.50%'},
    
#     'Detroit': {'PPG/F Home': 28.7, 'PPG/F Away': 24.4, 'Pass TD/F Home': 2, 'Pass TD/F Away': 1.2, 'Rush TD/F Home': 1.5, 'Rush TD/F Away': 1.6, 'FGM/F Home': 1.2, 'FGM/F Away': 1.2, 'PPG/A Home': 22.7, 'PPG/A Away': 24.4, 'Pass TD/A Home': 1.5, 'Pass TD/A Away': 2, 'Rush TD/A Home': 0.7, 'Rush TD/A Away': 0.8, 'FGM/A Home': 1.5, 'FGM/A Away': 1.6, 'Home Off Str.': '129.72%', 'Away Off Str.': '125.82%', 'Home Def Str.': '108.03%', 'Away Def Str.': '110.25%'},
    
#     'Green Bay': {'PPG/F Home': 18.2, 'PPG/F Away': 23.3, 'Pass TD/F Home': 1.2, 'Pass TD/F Away': 2.2, 'Rush TD/F Home': 0.8, 'Rush TD/F Away': 0.3, 'FGM/F Home': 1.4, 'FGM/F Away': 1.3, 'PPG/A Home': 19.6, 'PPG/A Away': 21, 'Pass TD/A Home': 1.2, 'Pass TD/A Away': 1, 'Rush TD/A Home': 0.8, 'Rush TD/A Away': 1, 'FGM/A Home': 1.4, 'FGM/A Away': 2.3, 'Home Off Str.': '81.29%', 'Away Off Str.': '117.14%', 'Home Def Str.': '96.39%', 'Away Def Str.': '92.94%'},
    
#     'Houston': {'PPG/F Home': 25.2, 'PPG/F Away': 21.6, 'Pass TD/F Home': 2.7, 'Pass TD/F Away': 0.8, 'Rush TD/F Home': 0.3, 'Rush TD/F Away': 1, 'FGM/F Home': 1.5, 'FGM/F Away': 2.6, 'PPG/A Home': 21.2, 'PPG/A Away': 21, 'Pass TD/A Home': 1, 'Pass TD/A Away': 1, 'Rush TD/A Home': 1.2, 'Rush TD/A Away': 1.2, 'FGM/A Home': 2, 'FGM/A Away': 1.8, 'Home Off Str.': '111.99%', 'Away Off Str.': '102.85%', 'Home Def Str.': '107.94%', 'Away Def Str.': '94.51%'},
    
#     'Indianapolis': {'PPG/F Home': 26.5, 'PPG/F Away': 22, 'Pass TD/F Home': 1.2, 'Pass TD/F Away': 0.8, 'Rush TD/F Home': 1.8, 'Rush TD/F Away': 1, 'FGM/F Home': 1.3, 'FGM/F Away': 2.2, 'PPG/A Home': 28.8, 'PPG/A Away': 19, 'Pass TD/A Home': 1.2, 'Pass TD/A Away': 1, 'Rush TD/A Home': 1.8, 'Rush TD/A Away': 0.8, 'FGM/A Home': 2.3, 'FGM/A Away': 2, 'Home Off Str.': '117.68%', 'Away Off Str.': '101.37%', 'Home Def Str.': '144.54%', 'Away Def Str.': '83.16%'},
    
#     'Jacksonville': {'PPG/F Home': 20, 'PPG/F Away': 25.7, 'Pass TD/F Home': 1, 'Pass TD/F Away': 1.2, 'Rush TD/F Home': 1, 'Rush TD/F Away': 1.2, 'FGM/F Home': 2, 'FGM/F Away': 2.2, 'PPG/A Home': 24.4, 'PPG/A Away': 17.2, 'Pass TD/A Home': 2, 'Pass TD/A Away': 1.3, 'Rush TD/A Home': 0.6, 'Rush TD/A Away': 0.7, 'FGM/A Home': 1.6, 'FGM/A Away': 0.7, 'Home Off Str.': '88.58%', 'Away Off Str.': '123.95%', 'Home Def Str.': '121.96%', 'Away Def Str.': '76.09%'},
    
#     'Kansas City': {'PPG/F Home': 25.6, 'PPG/F Away': 21.3, 'Pass TD/F Home': 2.4, 'Pass TD/F Away': 1.5, 'Rush TD/F Home': 0.4, 'Rush TD/F Away': 0.7, 'FGM/F Home': 2, 'FGM/F Away': 1.7, 'PPG/A Home': 15.4, 'PPG/A Away': 17.3, 'Pass TD/A Home': 0.8, 'Pass TD/A Away': 1.5, 'Rush TD/A Home': 1, 'Rush TD/A Away': 0.3, 'FGM/A Home': 0.4, 'FGM/A Away': 1.3, 'Home Off Str.': '112.05%', 'Away Off Str.': '107.58%', 'Home Def Str.': '77.47%', 'Away Def Str.': '74.77%'},
    
#     'LA Chargers': {'PPG/F Home': 25.5, 'PPG/F Away': 23.2, 'Pass TD/F Home': 2, 'Pass TD/F Away': 1.8, 'Rush TD/F Home': 1, 'Rush TD/F Away': 0.6, 'FGM/F Home': 1.5, 'FGM/F Away': 1.6, 'PPG/A Home': 24.5, 'PPG/A Away': 22.2, 'Pass TD/A Home': 1.2, 'Pass TD/A Away': 2, 'Rush TD/A Home': 1.7, 'Rush TD/A Away': 0.6, 'FGM/A Home': 1.7, 'FGM/A Away': 1.4, 'Home Off Str.': '114.65%', 'Away Off Str.': '115.93%', 'Home Def Str.': '130.23%', 'Away Def Str.': '100.70%'},
    
#     'LA Rams': {'PPG/F Home': 19.4, 'PPG/F Away': 22.5, 'Pass TD/F Home': 1.2, 'Pass TD/F Away': 1.2, 'Rush TD/F Home': 0.8, 'Rush TD/F Away': 1.2, 'FGM/F Home': 1.8, 'FGM/F Away': 2.2, 'PPG/A Home': 20.4, 'PPG/A Away': 22, 'Pass TD/A Home': 0.4, 'Pass TD/A Away': 1.5, 'Rush TD/A Home': 1.4, 'Rush TD/A Away': 0.7, 'FGM/A Home': 2.6, 'FGM/A Away': 1.7, 'Home Off Str.': '85.74%', 'Away Off Str.': '117.66%', 'Home Def Str.': '99.75%', 'Away Def Str.': '94.41%'},
    
#     'Las Vegas': {'PPG/F Home': 19.8, 'PPG/F Away': 13.8, 'Pass TD/F Home': 1, 'Pass TD/F Away': 0.8, 'Rush TD/F Home': 0.8, 'Rush TD/F Away': 0.5, 'FGM/F Home': 2.2, 'FGM/F Away': 1.2, 'PPG/A Home': 17, 'PPG/A Away': 25.7, 'Pass TD/A Home': 0.8, 'Pass TD/A Away': 1.7, 'Rush TD/A Home': 0.8, 'Rush TD/A Away': 1.2, 'FGM/A Home': 1.8, 'FGM/A Away': 1.7, 'Home Off Str.': '84.91%', 'Away Off Str.': '67.02%', 'Home Def Str.': '83.56%', 'Away Def Str.': '116.16%'},
    
#     'Miami': {'PPG/F Home': 38.8, 'PPG/F Away': 24.2, 'Pass TD/F Home': 3, 'Pass TD/F Away': 1.3, 'Rush TD/F Home': 2.2, 'Rush TD/F Away': 1.3, 'FGM/F Home': 0.8, 'FGM/F Away': 1.2, 'PPG/A Home': 17.4, 'PPG/A Away': 27.3, 'Pass TD/A Home': 1, 'Pass TD/A Away': 1.8, 'Rush TD/A Home': 0.2, 'Rush TD/A Away': 1.3, 'FGM/A Home': 1.6, 'FGM/A Away': 1, 'Home Off Str.': '180.15%', 'Away Off Str.': '120.43%', 'Home Def Str.': '73.16%', 'Away Def Str.': '119.12%'},
    
#     'Minnesota': {'PPG/F Home': 20, 'PPG/F Away': 23.8, 'Pass TD/F Home': 1.8, 'Pass TD/F Away': 2, 'Rush TD/F Home': 0.3, 'Rush TD/F Away': 0.5, 'FGM/F Home': 1.7, 'FGM/F Away': 1.3, 'PPG/A Home': 20.5, 'PPG/A Away': 19.8, 'Pass TD/A Home': 1.8, 'Pass TD/A Away': 0.7, 'Rush TD/A Home': 0.3, 'Rush TD/A Away': 0.8, 'FGM/A Home': 1.7, 'FGM/A Away': 2.7, 'Home Off Str.': '86.61%', 'Away Off Str.': '118.02%', 'Home Def Str.': '102.38%', 'Away Def Str.': '82.71%'},
    
#     'New England': {'PPG/F Home': 16.6, 'PPG/F Away': 10.8, 'Pass TD/F Home': 1.4, 'Pass TD/F Away': 0.5, 'Rush TD/F Home': 0.6, 'Rush TD/F Away': 0.5, 'FGM/F Home': 1, 'FGM/F Away': 1.2, 'PPG/A Home': 25.6, 'PPG/A Away': 20, 'Pass TD/A Home': 1.4, 'Pass TD/A Away': 1, 'Rush TD/A Home': 1, 'Rush TD/A Away': 0.7, 'FGM/A Home': 2, 'FGM/A Away': 1.8, 'Home Off Str.': '75.53%', 'Away Off Str.': '53.43%', 'Home Def Str.': '121.54%', 'Away Def Str.': '81.51%'},
    
#     'New Orleans': {'PPG/F Home': 18.3, 'PPG/F Away': 22.3, 'Pass TD/F Home': 1.3, 'Pass TD/F Away': 1.1, 'Rush TD/F Home': 0.3, 'Rush TD/F Away': 0.9, 'FGM/F Home': 2.5, 'FGM/F Away': 2, 'PPG/A Home': 22.3, 'PPG/A Away': 19, 'Pass TD/A Home': 1.5, 'Pass TD/A Away': 1.1, 'Rush TD/A Home': 0.5, 'Rush TD/A Away': 0.7, 'FGM/A Home': 2.3, 'FGM/A Away': 1.6, 'Home Off Str.': '78.64%', 'Away Off Str.': '106.01%', 'Home Def Str.': '106.79%', 'Away Def Str.': '80.56%'},
    
#     'NY Giants': {'PPG/F Home': 7.4, 'PPG/F Away': 17.4, 'Pass TD/F Home': 0.6, 'Pass TD/F Away': 1.1, 'Rush TD/F Home': 0.2, 'Rush TD/F Away': 0.4, 'FGM/F Home': 0.6, 'FGM/F Away': 1.6, 'PPG/A Home': 18.2, 'PPG/A Away': 28.7, 'Pass TD/A Home': 0.4, 'Pass TD/A Away': 1.7, 'Rush TD/A Home': 1.2, 'Rush TD/A Away': 1.7, 'FGM/A Home': 1, 'FGM/A Away': 1.6, 'Home Off Str.': '32.59%', 'Away Off Str.': '81.53%', 'Home Def Str.': '81.32%', 'Away Def Str.': '132.11%'},
    
#     'NY Jets': {'PPG/F Home': 15.2, 'PPG/F Away': 14.4, 'Pass TD/F Home': 0.7, 'Pass TD/F Away': 0.6, 'Rush TD/F Home': 0.3, 'Rush TD/F Away': 0.2, 'FGM/F Home': 1.8, 'FGM/F Away': 2.4, 'PPG/A Home': 21.5, 'PPG/A Away': 21.8, 'Pass TD/A Home': 0.8, 'Pass TD/A Away': 1.6, 'Rush TD/A Home': 1, 'Rush TD/A Away': 0.2, 'FGM/A Home': 2, 'FGM/A Away': 3, 'Home Off Str.': '57.47%', 'Away Off Str.': '62.29%', 'Home Def Str.': '98.48%', 'Away Def Str.': '92.42%'},
    
#     'Philadelphia': {'PPG/F Home': 32.8, 'PPG/F Away': 24.3, 'Pass TD/F Home': 2, 'Pass TD/F Away': 1.3, 'Rush TD/F Home': 2, 'Rush TD/F Away': 1.2, 'FGM/F Home': 1.6, 'FGM/F Away': 1.8, 'PPG/A Home': 26.6, 'PPG/A Away': 18.8, 'Pass TD/A Home': 2.2, 'Pass TD/A Away': 2, 'Rush TD/A Home': 0.8, 'Rush TD/A Away': 0.2, 'FGM/A Home': 1, 'FGM/A Away': 1.2, 'Home Off Str.': '150.47%', 'Away Off Str.': '121.50%', 'Home Def Str.': '132.87%', 'Away Def Str.': '84.53%'},
    
#     'Pittsburgh': {'PPG/F Home': 17.2, 'PPG/F Away': 15.8, 'Pass TD/F Home': 0.8, 'Pass TD/F Away': 0.4, 'Rush TD/F Home': 0.5, 'Rush TD/F Away': 1, 'FGM/F Home': 1.8, 'FGM/F Away': 2, 'PPG/A Home': 19.5, 'PPG/A Away': 17.6, 'Pass TD/A Home': 1, 'Pass TD/A Away': 1.4, 'Rush TD/A Home': 0.7, 'Rush TD/A Away': 0.4, 'FGM/A Home': 2.5, 'FGM/A Away': 1.6, 'Home Off Str.': '67.40%', 'Away Off Str.': '77.80%', 'Home Def Str.': '94.93%', 'Away Def Str.': '77.31%'},
    
#     'San Francisco': {'PPG/F Home': 30.2, 'PPG/F Away': 26.5, 'Pass TD/F Home': 2.2, 'Pass TD/F Away': 1.3, 'Rush TD/F Home': 1.6, 'Rush TD/F Away': 1.7, 'FGM/F Home': 1.2, 'FGM/F Away': 1.8, 'PPG/A Home': 16.6, 'PPG/A Away': 14.5, 'Pass TD/A Home': 1.4, 'Pass TD/A Away': 0.7, 'Rush TD/A Home': 0.6, 'Rush TD/A Away': 0.3, 'FGM/A Home': 1, 'FGM/A Away': 2.2, 'Home Off Str.': '138.47%', 'Away Off Str.': '138.42%', 'Home Def Str.': '88.27%', 'Away Def Str.': '59.18%'},
    
#     'Seattle': {'PPG/F Home': 22.7, 'PPG/F Away': 18.6, 'Pass TD/F Home': 1.3, 'Pass TD/F Away': 0.8, 'Rush TD/F Home': 0.5, 'Rush TD/F Away': 0.8, 'FGM/F Home': 2.8, 'FGM/F Away': 1.6, 'PPG/A Home': 24, 'PPG/A Away': 21, 'Pass TD/A Home': 1.2, 'Pass TD/A Away': 1.4, 'Rush TD/A Home': 1.5, 'Rush TD/A Away': 1, 'FGM/A Home': 1.8, 'FGM/A Away': 1.4, 'Home Off Str.': '92.59%', 'Away Off Str.': '86.26%', 'Home Def Str.': '124.81%', 'Away Def. Str.': '95.63%'},
    
#     'Tampa Bay': {'PPG/F Home': 15.4, 'PPG/F Away': 22.5, 'Pass TD/F Home': 1, 'Pass TD/F Away': 2, 'Rush TD/F Home': 0.2, 'Rush TD/F Away': 0.5, 'FGM/F Home': 1.8, 'FGM/F Away': 1.7, 'PPG/A Home': 16.8, 'PPG/A Away': 23.8, 'Pass TD/A Home': 0.8, 'Pass TD/A Away': 2, 'Rush TD/A Home': 0.6, 'Rush TD/A Away': 0.7, 'FGM/A Home': 2.2, 'FGM/A Away': 1.8, 'Home Off Str.': '61.39%', 'Away Off Str.': '117.73%', 'Home Def Str.': '80.43%', 'Away Def. Str.': '108.11%'},
    
#     'Tennessee': {'PPG/F Home': 24.8, 'PPG/F Away': 12.3, 'Pass TD/F Home': 1.8, 'Pass TD/F Away': 0.3, 'Rush TD/F Home': 1.3, 'Rush TD/F Away': 0.4, 'FGM/F Home': 1.3, 'FGM/F Away': 2.4, 'PPG/A Home': 15, 'PPG/A Away': 23.4, 'Pass TD/A Home': 0.8, 'Pass TD/A Away': 1.3, 'Rush TD/A Home': 0.5, 'Rush TD/A Away': 0.9, 'FGM/A Home': 2, 'FGM/A Away': 2.9, 'Home Off Str.': '115.11%', 'Away Off Str.': '55.50%', 'Home Def Str.': '73.27%', 'Away Def. Str.': '104.42%'},
    
#     'Washington': {'PPG/F Home': 18.6, 'PPG/F Away': 21.9, 'Pass TD/F Home': 1.6, 'Pass TD/F Away': 1.4, 'Rush TD/F Home': 0.4, 'Rush TD/F Away': 1, 'FGM/F Home': 1.6, 'FGM/F Away': 1.3, 'PPG/A Home': 32.4, 'PPG/A Away': 26.9, 'Pass TD/A Home': 2.4, 'Pass TD/A Away': 2.3, 'Rush TD/A Home': 0.6, 'Rush TD/A Away': 0.6, 'FGM/A Home': 2.4, 'FGM/A Away': 2, 'Home Off Str.': '81.94%', 'Away Off Str.': '111.49%', 'Home Def Str.': '152.16%', 'Away Def. Str.': '118.49%'},
# }

# import pandas as pd

# Replace 'your_file_path.csv' with the path to the downloaded CSV file
file_path = 'C:\Users\Jack.Gately25\Downloads\2023 NFL Model (Data) - NFL Basic Back-End.csv'

# Read the CSV file into a pandas DataFrame
# df = pd.read_csv(file_path)

# Display the DataFrame
# print(df)