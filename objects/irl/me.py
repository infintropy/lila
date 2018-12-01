from objects.irl.human import Human
from objects.core.planner import Planner
from objects.core.budget import Budget


class Me(Human):

    def __init__(self, **kwargs):
        super(Me, self).__init__(**kwargs)
        self._name = 'Donald'
        self.height = 71

        self.planner = Planner()
        self.planner.category = "Personal"
        self.planner.name = "My Planner!"

        self.budget = Budget()
        self.budget.category = "Personal"
        self.budget.name = "Monthly Budget"