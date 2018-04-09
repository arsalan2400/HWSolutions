import scr.FormatFunctions as Format
import scr.FigureSupport as Figs
import scr.StatisticalClasses as Stat
import HW8.Parameters as P


def outcomes(simulation_output, strategy):
    # mean and prediction interval text of game reward
    rewardPImean = Format.format_estimate_interval(
        estimate=simulation_output.get_mean_total_reward(),
        interval=simulation_output.get_PI_total_reward(alpha=P.alpha),
        deci=1)

    # print game reward statistics
    print(strategy)
    print("     Estimate of the gambler's total reward from 10 games and {:.{prec}%} prediction interval:".format(1 - P.alpha, prec=0),
          rewardPImean)


def make_plots(games_fair_coin, games_biased_coin):

    # histograms of total game rewards
    set_of_game_rewards = [
        games_fair_coin.get_all_total_rewards(),
        games_biased_coin.get_all_total_rewards()
    ]

    # graph histograms
    Figs.graph_histograms(
        data_sets=set_of_game_rewards,
        title="Histogram of the Gambler's Total Rewards from 10 Games",
        x_label='Total Rewards',
        y_label='Count',
        bin_width=40,
        legend=['Fair coin', 'Unfair coin'],
        transparency=0.6,
    )


def outcomes_comparative(games_fair_coin, games_biased_coin):
    ##prints the expected increase in game rewards when the coin is biased

    # what is the increase in game reward?
    increase = Stat.DifferenceStatIndp(
        name='Increase in gambler game reward',
        x=games_biased_coin.get_all_total_rewards(),
        y_ref=games_fair_coin.get_all_total_rewards()
    )
    # estimate and PI
    estimatePI = Format.format_estimate_interval(
        estimate=increase.get_mean(),
        interval=increase.get_PI(alpha=P.alpha),
        deci=1
    )
    print("  The average increase in gambler's total reward from 10 games and {:.{prec}%} projection interval:".format(1 - P.alpha, prec=0),
          estimatePI)
