import HW6.Classes as Cls
import scr.FigureSupport as figureLibrary

# create a multiple game sets
multipleGameSets= Cls.MultipleGameSets(ids=range(1000), prob_head=0.5, n_games_in_a_set=10)
# simulate all game sets
multipleGameSets.simulation()

# print projected mean reward
print('Projected mean reward',
      multipleGameSets.get_overall_mean_reward())
# print projection interval
print('95% projection interval of average rewards',
      multipleGameSets.get_PI_mean_reward(0.05))

#plot
figureLibrary.graph_histogram(
    observations=multipleGameSets.get_all_mean_rewards(),
    title='Histogram of Mean Rewards obtained from the transit-state simulation model',
    x_label='Mean Rewards',
    y_label='Count')

print('We need a transient-state simulation for this perspective.')
print('We are not able to rely on the Law of Large Numbers to make inference because our data is very limited.')
print('Therefore, we must use the sample mean and projection intervals for interpretation.')