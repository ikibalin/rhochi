import os
import cryspy

def test_UNPD_PbSo4():
    dir = os.path.dirname(__file__)
    f_name = os.path.join(dir, "main.rcif")
    rhochi = cryspy.file_to_globaln(f_name)
    rhochi.refine()
    chi_sq, n_points = rhochi.calc_chi_sq()

test_UNPD_PbSo4()