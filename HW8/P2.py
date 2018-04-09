import HW6.Classes as Cls
import HW8.Parameters as P
import HW8.TransientStateSupport as TransientStateSupport

print("Gambler's Perspective (Transient-State Analysis):")

# simulate multiple cohorts for when the coin is fair
multi_games_fair_coin = Cls.MultipleGameSets(
    ids=range(P.n_simulated_games),
    prob_head=P.prob_head,
    n_games_in_a_set=P.games_in_set)
multi_games_fair_coin.simulation()
# print outcomes when a fair coin is used
TransientStateSupport.outcomes(multi_games_fair_coin, '  When coin is fair:')

# simulate multiple cohorts for when the coin is biased
multi_games_biased_coin = Cls.MultipleGameSets(
    ids=range(P.n_simulated_games, 2*P.n_simulated_games),
    prob_head=P.prob_head_unfair,
    n_games_in_a_set=P.games_in_set)
multi_games_biased_coin.simulation()
# print outcomes when a unfair coin is used
TransientStateSupport.outcomes(multi_games_biased_coin, '  When coin is biased:')

# make plots
TransientStateSupport.make_plots(multi_games_fair_coin, multi_games_biased_coin)

# print comparative outcomes
TransientStateSupport.outcomes_comparative(multi_games_fair_coin, multi_games_biased_coin)