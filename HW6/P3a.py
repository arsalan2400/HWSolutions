import HW6.Classes as Cls
import scr.FigureSupport as figureLibrary

# Calculate expected reward of 1000 games
trial = Cls.SetOfGames(prob_head=0.5, n_games=1000)
test=trial.simulation()

print("The Expected reward is:", test.get_ave_reward())
print("The 95% CI of expected reward is:", test.get_CI_reward(0.05))

# Create histogram of winnings
figureLibrary.graph_histogram(
    observations=trial.get_reward_list(),
    title="Histogram of Rewards from 1000 Games obtained from the steady-state simulation model",
    x_label="Game Rewards",
    y_label="Frequency")

print('We need a steady-state simulation for this perspective.')
print('We are able to rely on the Law of Large Numbers to make inference.')
print('This lets us use the sample mean and condience intervals for interpretation.')


