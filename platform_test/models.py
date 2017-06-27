from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Ellen Feng'

doc = """
Platform Game 
25/06/2017

Errors:
2 columns of Payoffs in db, preset. 
"""


class Constants(BaseConstants):
    name_in_url = 'platform_test'
    players_per_group = 2
    num_rounds = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    def set_payoffs(self):
        for p in self.get_players():
            payoff = 5000
    '''
        locations = [p for p in self.get_players()]
        hash_population = locations.count('#')
        at_population = Constants.players_per_group - hash_population

        for p in self.get_players() :
            if p.platform_selection == '#' :
                p.payoff = hash_population

            elif p.platform_selection == '@' :
                p.payoff = at_population
            else :
                p.payoff = 
    '''




class Player(BasePlayer):
    platform_selection = models.CharField(
        choices=['#', '@','No!'],
        widget=widgets.RadioSelect()
    )
    payoff = models.CurrencyField()


