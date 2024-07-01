import pandas as pd

# Load the election results data from the CSV file
data = pd.read_csv('results_2024_winners.csv')

# Convert 'Margin Votes' to numeric
data['Margin Votes'] = pd.to_numeric(data['Margin Votes'], errors='coerce').fillna(0).astype(int)

# Common Insights
# 1. Winning Party Distribution
winning_party_distribution = data['Winning Party'].value_counts().reset_index()
winning_party_distribution.columns = ['Winning Party', 'Seats Won']
winning_party_distribution.to_csv('winning_party_distribution.csv', index=False)

# 2. Close Contests (Assuming a close contest has a margin of less than 1000 votes)
close_contests = data[data['Margin Votes'] < 1000]
close_contests.to_csv('close_contests.csv', index=False)

# 3. State-wise Party Performance
state_party_performance = data.groupby(['State', 'Winning Party']).size().unstack(fill_value=0)
state_party_performance.to_csv('state_party_performance.csv')

# 4. Stronghold Constituencies (Winning party with large margin, assume margin > 10000)
stronghold_constituencies = data[data['Margin Votes'] > 10000]
stronghold_constituencies.to_csv('stronghold_constituencies.csv', index=False)

# 5. Runner-Up Analysis
runner_up_analysis = data['Runner-up Party'].value_counts().reset_index()
runner_up_analysis.columns = ['Runner-up Party', 'Number of Runner-ups']
runner_up_analysis.to_csv('runner_up_analysis.csv', index=False)

# Unique Insights for Script 1
# 6. Top Candidates by Margin
top_candidates_by_margin = data.sort_values(by='Margin Votes', ascending=False).head(10)
top_candidates_by_margin.to_csv('top_candidates_by_margin.csv', index=False)

# 7. Regional Dominance
regional_dominance = state_party_performance.idxmax(axis=1).reset_index()
regional_dominance.columns = ['State', 'Dominant Party']
regional_dominance.to_csv('regional_dominance.csv', index=False)

# 8. Emerging Parties
emerging_parties = data['Winning Party'].value_counts().nsmallest(5).reset_index()
emerging_parties.columns = ['Emerging Party', 'Seats Won']
emerging_parties.to_csv('emerging_parties.csv', index=False)

# 9. Margin Analysis
margin_analysis = data['Margin Votes'].describe().reset_index()
margin_analysis.columns = ['Statistic', 'Value']
margin_analysis.to_csv('margin_analysis.csv', index=False)

# 10. Result Status Trends
result_status_trends = data['Results Status'].value_counts().reset_index()
result_status_trends.columns = ['Results Status', 'Count']
result_status_trends.to_csv('result_status_trends.csv', index=False)
