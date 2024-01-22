import sys
import pytest

from wizard import Wizard 


# #move: (1) for Next  / (2) for Prev
# @pytest.mark.parametrize("phase_number,move", [
#     (1, 1),
#     (1, 2),
#     (2,1),
    
# ])
# def test_prev_or_next(phase_number,move):
#     wizard = Wizard()
#     # Simulate choosing "1" for Next
#     if wizard.prev_or_next(phase_number,move):

#         # wizard.prev_or_next(1)
#         if move ==1:
#             assert wizard.phases[-1].num_phase == phase_number+1

#         # Simulate choosing "2" for Prev
#         if move ==2:
#             # wizard.prev_or_next(2)
#             assert wizard.phases[-1].num_phase == phase_number-1





