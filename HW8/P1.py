import HW6.Classes as Cls
import HW8.Parameters as P
import HW8.SteadyStateSupport as SteadyStateSupport

print("Casino Owner's Perspective (Steady-State Analysis):")

# simulate a fair set of games
gamesFair = Cls.SetOfGames(
    id=1,
    n_games=P.n_games,
    prob_head=P.prob_head)
sim_output_fair_coin = gamesFair.simulation()
# print outcomes when a fair coin is used
SteadyStateSupport.outcomes(sim_output_fair_coin, '  When coin is fair:')

# simulate a biased set of games
gamesBiased = Cls.SetOfGames(
    id=2,
    n_games=P.n_games,
    prob_head=P.prob_head_unfair)
sim_output_unfair_coin = gamesBiased.simulation()
# print outcomes when a unfair coin is used
SteadyStateSupport.outcomes(sim_output_unfair_coin, '  When coin is unfair:')

# make plots
SteadyStateSupport.make_plots(sim_output_fair_coin, sim_output_unfair_coin)

# print comparative outcomes
SteadyStateSupport.outcomes_comparative(sim_output_fair_coin, sim_output_unfair_coin)