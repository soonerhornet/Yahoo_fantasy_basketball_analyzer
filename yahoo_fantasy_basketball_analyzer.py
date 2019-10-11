'''
yahoo_fantasy_basketball_analyzer
'''

from yahoo_fantasy_basketball_analyzer import yahoo_fantasy_api_client, utilities, nba_data, fantasy_league_data

def main():

  ''' Retrieve league data in Yahoo Fantasy Basketball '''
  yfa_client = yahoo_fantasy_api_client.YahooFantasyApiClient("oauth2.json")

  print("  Parsing Basketball Reference NBA players total stats ...", end = " ", flush = True)
  stats_table = utilities.create_player_stats_table(yfa_client.get_year())
  print("Done")

  print("  Calculating player performace...", end = " ", flush = True)
  my_nba_data = nba_data.NBAData(stats_table)
  print("Done")

  csv_name = ""
  if yfa_client.get_mode() == 0:
    print("  Calculating Fantasy team performace ...", end = " ", flush = True)
    my_fantasy_league_data = fantasy_league_data.FantasyLeagueData(yfa_client.get_yahoo_fantasy_api_league(), my_nba_data)
    print("Done")
    csv_name = "{}-{}_{}_teams.csv".format(yfa_client.get_year(), yfa_client.get_year() + 1, my_fantasy_league_data.get_name())
    utilities.create_csv_output_file(csv_name, my_fantasy_league_data.get_teams(), my_fantasy_league_data.get_stat_categories())
  elif yfa_client.get_mode() == 1:
    csv_name = "{}-{}_players.csv".format(yfa_client.get_year(), yfa_client.get_year() + 1)
    utilities.create_csv_output_file(csv_name, my_nba_data.get_players(), yfa_client.get_user_selected_categories())

  print("  Finished! please import \"{}\" to excel as CSV format to see the results.".format(csv_name))

if __name__== "__main__":
  main()