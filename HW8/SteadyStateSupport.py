import scr.FormatFunctions as Format
import scr.FigureSupport as Figs
import scr.StatisticalClasses as Stat
import HW8.Parameters as P


def outcomes(simulation_output, strategy):
    # mean and CI of game reward
    rewardCImean = Format.format_estimate_interval(
        estimate=simulation_output.get_ave_reward(),
        interval=simulation_output.get_CI_reward(alpha=P.alpha),
        deci=1)

    # print game reward statistics
    print(strategy)
    print("     Estimate of the gambler's mean game reward and {:.{prec}%} confidence interval:".format(1 - P.alpha, prec=0),
          rewardCImean)


def make_plots(output_fair_coin, output_biased_coin):
    # makes histogram of the game rewards

    # histograms of game rewards
    set_of_game_rewards = [
        output_fair_coin.get_rewards(),
        output_biased_coin.get_rewards()
    ]

    Figs.graph_histograms(
        data_sets=set_of_game_rewards,
        title='Histogram of Game Rewards',
        x_label='Game rewards',
        y_label='Counts',
        bin_width=20,
        legend=['Fair coin', 'Unfair coin'],
        transparency=0.6
    )


def outcomes_comparative(output_fair_coin, output_biased_coin):
    ##prints the expected increase in game rewards when the coin is biased

    # what is the increase in game reward?
    increaseReward = Stat.DifferenceStatIndp(
        name='Increase in game reward',
        x=output_biased_coin.get_rewards(),
        y_ref=output_fair_coin.get_rewards()
    )
    # estimate and CI
    estimateCI = Format.format_estimate_interval(
        estimate=increaseReward.get_mean(),
        interval=increaseReward.get_t_CI(alpha=P.alpha),
        deci=1
    )
    print("  The expected increase in gambler's total reward from playing 10 games and {:.{prec}%} confidence interval:".format(1 - P.alpha, prec=0),
          estimateCI)
