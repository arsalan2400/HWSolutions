import numpy as np
import scr.StatisticalClasses as Stat


class Game(object):
    def __init__(self, id, prob_head):
        self._id = id
        self._rnd = np.random
        self._rnd.seed(id)
        self._probHead = prob_head  # probability of flipping a head
        self._countWins = 0  # number of wins, set to 0 to begin

    def simulate(self, n_of_flips):

        count_tails = 0  # number of consecutive tails so far, set to 0 to begin

        ## flip the coin 20 times
        for i in range(n_of_flips):

            # in the case of flipping a heads
            if self._rnd.random_sample() < self._probHead:
                if count_tails >= 2:  # if the series is ..., T, T, H
                    self._countWins += 1  # increase the number of wins by 1
                count_tails = 0  # the tails counter needs to be reset to 0 because a heads was flipped

            # in the case of flipping a tails
            else:
                count_tails += 1  # increase tails count by one

    def get_reward(self):
        # calculate the reward from playing a single game
        return 100*self._countWins - 250


class SetOfGames:
    def __init__(self, id, prob_head, n_games):
        self._id = id
        self._gameRewards = [] # create an empty list where rewards will be stored
        self._prob_head=prob_head
        self._n_games=n_games
        self._prob_loss = 0
        self._count_loss = 0
        self._countLoss_list=[] # create an empty list where losses will be stored

    def simulation(self):
        # simulate the games
        for n in range(self._n_games):
            # create a new game
            game = Game(id= self._id*self._n_games+n, prob_head=self._prob_head)
            # simulate the game with 20 flips
            game.simulate(20)
            # store the reward
            self._gameRewards.append(game.get_reward())
            #return self._gameRewards

        # create a list of losses (1 is loss, 0 otherwise)
        for k in self._gameRewards:
            if k < 0:
                i=1
                self._countLoss_list.append(i)
            else:
                i=0
                self._countLoss_list.append(i)

        return SetOfGamesOutcomes(self)

    # return vector of game rewards
    def get_reward_list(self):
        return self._gameRewards

    # return vector of losses
    def get_loss_list(self):
        return self._countLoss_list


class SetOfGamesOutcomes:
    def __init__(self, simulated_cohort):

        self._simulatedCohort = simulated_cohort
        # game rewards summary statistics
        self._sumStat_gameRewards = \
            Stat.SummaryStat('Reward list', self._simulatedCohort.get_reward_list())
        # loss probability summary statistics
        self._sumStat_gameProbLoss = \
            Stat.SummaryStat('Probability of loss', self._simulatedCohort.get_loss_list())

    # average reward across all games
    def get_ave_reward(self):
        """ returns the average reward from all games"""
        return self._sumStat_gameRewards.get_mean()

    # CI of rewards from all games
    def get_CI_reward(self, alpha):
        return self._sumStat_gameRewards.get_t_CI(alpha)

    # min reward from all games
    def get_min_reward(self):
        return self._sumStat_gameRewards.get_min()

    # max reward from all games
    def get_max_reward(self):
        return self._sumStat_gameRewards.get_max()

    # probability of loss from all games
    def get_prob_loss(self):
        return self._sumStat_gameProbLoss.get_mean()

    # CI of probability of loss from all games
    def get_CI_probLoss(self, alpha):
        return self._sumStat_gameProbLoss.get_t_CI(alpha)


class MultipleGameSets:
    """ representing multiple sets of games"""
    def __init__(self, ids, prob_head, n_games_in_a_set):
        self._ids=ids   # ids of game sets
        self._probs_head=prob_head  # probability of head in each coin flip
        self._n_games_in_a_set=n_games_in_a_set # number of games in each set

        self._gameRewards=[] # create an empty list where rewards will be stored
        self._meanGameReward=[] # create an empty list where the means will be stored
        self._sumStat_meanGameReward = None

    def simulation(self):
        for i in self._ids:
            # create a new set of games
            setOfGames=SetOfGames(i, self._probs_head, self._n_games_in_a_set)
            # simulate the set of games using 20 flips
            setOfGames.simulation()
            # store the rewards
            self._gameRewards.append(setOfGames.get_reward_list())
            # store average of the reward
            self._meanGameReward.append(setOfGames.simulation().get_ave_reward())

        # summary statistics of mean rewards
        self._sumStat_meanGameReward=Stat.SummaryStat("Mean Rewards", self._meanGameReward)

    # max mean reward of a specific game
    def get_setOfGames_mean_rewards(self, index):
        return self._meanGameReward[index]

    # CI of mean reward of a specific game
    def get_setOfGames_CI_mean_rewards(self, index, alpha):
        stats = Stat.SummaryStat('', self._gameRewards[index])
        return stats.get_t_CI(alpha)

    # get list of all mean rewards
    def get_all_mean_rewards(self):
        return self._meanGameReward

    # get the overall mean (so the mean of the means)
    def get_overall_mean_reward(self):
        return self._sumStat_meanGameReward.get_mean()

    # get prediction interval for reward to a specific cohort
    def get_cohort_PI_reward(self, index, alpha):
        stats = Stat.SummaryStat('', self._gameRewards[index])
        return stats.get_PI(alpha)

    # get prediction interval for the overall mean reward
    def get_PI_mean_reward(self, alpha):
        return self._sumStat_meanGameReward.get_PI(alpha)