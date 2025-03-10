import numpy

from cryspy.A_functions_base.debye_waller_factor import \
    calc_beta_by_u_ij, \
    calc_b_iso_beta, \
    calc_power_dwf_iso, \
    calc_power_dwf_aniso, \
    calc_dwf

na = numpy.newaxis

reciprocal_unit_cell_parameters = numpy.array([
    0.03, 0.007, 0.04, 1.3, 1.7, 1.2], dtype=float)

u_ij = numpy.array([10, 11., 12., 4., -7., -20], dtype=float)

unit_cell_parameters = numpy.array([
    7., 3., 15., 1.3, 1.7, 1.2], dtype=float)

atom_adp_type = numpy.array(["Uiso", "Uani", "Biso", "Bani", "Bovl", "Uovl", "Umpe"], dtype=str)
atom_iso_param = numpy.array([1., 2., 3., 1.5, 0.5, -1.1, 3.3], dtype=float)
b_iso = atom_iso_param
atom_aniso_param = numpy.array( [
    [1., 7., 3., 5.5, 0.6,  7.1, 10.3],
    [2., 4., 3., 1.4, 7.5,  4.1,-9.3],
    [3., 2., 3., 1.0, 0.5, -8.1, 3.7],
    [.5, 0.7, 2.3, 1.1,-0.7, -4.0, 3.7],
    [.8, 0.7,-4.3, 1.0, 0.4, -3.7, 4.3],
    [.1, 0.2, 4.3,-1.4,-3.5, -2.1, 3.1]], dtype=float)
beta = atom_aniso_param

sthovl = numpy.array([0., 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.], dtype=float)

index_hkl = numpy.array([
    [0, 0, 2, 2, 1, 1, 1, 1, 0, 1, 3],
    [0, 2, 0, 2, 2, 2, 2, 2, 3, 3, 3],
    [2, 0, 0, 2, 3, 4, 5, 6, 3, 2, 3]], dtype=int)



symm_elems_r = numpy.array([
    [1,-1,-1, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [1,-1, 1,-1],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [1,-1, 1,-1]], dtype=int)


beta_ij = numpy.array(
    [0.17765288,  0.01063943,  0.37899281,  0.01658094, -0.16580935, -0.11053957],
    dtype=float)

b_iso_out = numpy.array(
    [ 78.95683521, 0., 3., 0., 0.5, -86.85251873, 260.55755619],
    dtype=float)
beta_out = numpy.array([
    [ 0.        ,  0.       ,   0.        ,  0.        ,  0.        ,  0.        ],
    [ 3.46511151, 11.4184368,   0.20173214,  0.83211042,  0.15641564,  0.10731882],
    [ 0.        ,  0.       ,   0.        ,  0.        ,  0.        ,  0.        ],
    [ 5.5       ,  1.4      ,   1.        ,  1.1       ,  1.        , -1.4       ],
    [ 0.        ,  0.       ,   0.        ,  0.        ,  0.        ,  0.        ],
    [ 0.        ,  0.       ,   0.        ,  0.        ,  0.        ,  0.        ],
    [ 0.        ,  0.       ,   0.        ,  0.        ,  0.        ,  0.        ]], dtype=float).transpose()
power_dwf_iso = numpy.array([
    [ 0.  ,   0.  ,   0.  ,   0.   ,  0.   , -0.   ,  0.   ],
    [ 0.01,   0.02,   0.03,   0.015,  0.005, -0.011,  0.033],
    [ 0.04,   0.08,   0.12,   0.06 ,  0.02 , -0.044,  0.132],
    [ 0.09,   0.18,   0.27,   0.135,  0.045, -0.099,  0.297],
    [ 0.16,   0.32,   0.48,   0.24 ,  0.08 , -0.176,  0.528],
    [ 0.25,   0.5 ,   0.75,   0.375,  0.125, -0.275,  0.825],
    [ 0.36,   0.72,   1.08,   0.54 ,  0.18 , -0.396,  1.188],
    [ 0.49,   0.98,   1.47,   0.735,  0.245, -0.539,  1.617],
    [ 0.64,   1.28,   1.92,   0.96 ,  0.32 , -0.704,  2.112],
    [ 0.81,   1.62,   2.43,   1.215,  0.405, -0.891,  2.673],
    [ 1.  ,   2.  ,   3.  ,   1.5  ,  0.5  , -1.1  ,  3.3  ]], dtype=float)

power_dwf_aniso = numpy.array(
[[[  12.  ,  12.  ,  12.  ,  12. ],
  [   8.  ,   8.  ,   8.  ,   8. ],
  [  12.  ,  12.  ,  12.  ,  12. ],
  [   4.  ,   4.  ,   4.  ,   4. ],
  [   2.  ,   2.  ,   2.  ,   2. ],
  [ -32.4 , -32.4 , -32.4 , -32.4],
  [  14.8 ,  14.8 ,  14.8 ,  14.8]],
 [[   8.  ,   8.  ,   8.  ,   8. ],
  [  16.  ,  16.  ,  16.  ,  16. ],
  [  12.  ,  12.  ,  12.  ,  12. ],
  [   5.6 ,   5.6 ,   5.6 ,   5.6],
  [  30.  ,  30.  ,  30.  ,  30. ],
  [  16.4 ,  16.4 ,  16.4 ,  16.4],
  [ -37.2 , -37.2 , -37.2 , -37.2]],
 [[   4.  ,   4.  ,   4.  ,   4. ],
  [  28.  ,  28.  ,  28.  ,  28. ],
  [  12.  ,  12.  ,  12.  ,  12. ],
  [  22.  ,  22.  ,  22.  ,  22. ],
  [   2.4 ,   2.4 ,   2.4 ,   2.4],
  [  28.4 ,  28.4 ,  28.4 ,  28.4],
  [  41.2 ,  41.2 ,  41.2 ,  41.2]],
 [[  35.2 ,  35.2 ,  14.4 ,  14.4],
  [  64.8 ,  64.8 ,  42.4 ,  42.4],
  [  54.4 ,  54.4 ,  86.4 ,  86.4],
  [  37.2 ,  37.2 ,   3.6 ,   3.6],
  [   4.  ,   4.  ,   8.8 ,   8.8],
  [ -66.  , -66.  ,  57.2 ,  57.2],
  [ 107.6 , 107.6 , -20.4 , -20.4]],
 [[  44.  ,  44.  ,  30.4 ,  30.4],
  [  50.4 ,  50.4 ,  36.4 ,  36.4],
  [  77.  ,  77.  , 110.2 , 110.2],
  [  13.7 ,  13.7 ,  -7.1 ,  -7.1],
  [  -7.3 ,  -7.3 ,  -6.5 ,  -6.5],
  [-112.8 ,-112.8 , -36.4 , -36.4],
  [  84.2 ,  84.2 ,   3.  ,   3. ]],
 [[  67.  ,  67.  ,  50.2 ,  50.2],
  [  66.6 ,  66.6 ,  49.8 ,  49.8],
  [ 106.6 , 106.6 , 157.  , 157. ],
  [  17.1 ,  17.1 ,  -7.7 ,  -7.7],
  [ -17.  , -17.  , -17.8 , -17.8],
  [-185.3 ,-185.3 , -94.1 , -94.1],
  [ 131.1 , 131.1 ,  32.7 ,  32.7]],
 [[  96.  ,  96.  ,  76.  ,  76. ],
  [  86.8 ,  86.8 ,  67.2 ,  67.2],
  [ 142.2 , 142.2 , 209.8 , 209.8],
  [  22.5 ,  22.5 ,  -6.3 ,  -6.3],
  [ -25.7 , -25.7 , -28.1 , -28.1],
  [-274.  ,-274.  ,-168.  ,-168. ],
  [ 185.4 , 185.4 ,  69.8 ,  69.8]],
 [[ 131.  , 131.  , 107.8 , 107.8],
  [ 111.  , 111.  ,  88.6 ,  88.6],
  [ 183.8 , 183.8 , 268.6 , 268.6],
  [  29.9 ,  29.9 ,  -2.9 ,  -2.9],
  [ -33.4 , -33.4 , -37.4 , -37.4],
  [-378.9 ,-378.9 ,-258.1 ,-258.1],
  [ 247.1 , 247.1 , 114.3 , 114.3]],
 [[  46.8 ,  46.8 ,  46.8 ,  46.8],
  [  57.6 ,  57.6 ,  57.6 ,  57.6],
  [ 131.4 , 131.4 , 131.4 , 131.4],
  [  -3.6 ,  -3.6 ,  -3.6 ,  -3.6],
  [   9.  ,   9.  ,   9.  ,   9. ],
  [ -73.8 , -73.8 , -73.8 , -73.8],
  [   5.4 ,   5.4 ,   5.4 ,   5.4]],
 [[  38.4 ,  38.4 ,  26.  ,  26. ],
  [  60.4 ,  60.4 ,  46.4 ,  46.4],
  [  90.2 ,  90.2 ,  97.  ,  97. ],
  [  15.9 ,  15.9 ,  -5.3 ,  -5.3],
  [  25.5 ,  25.5 ,  30.7 ,  30.7],
  [ -52.4 , -52.4 ,  25.2 ,  25.2],
  [  18.  ,  18.  , -60.8 , -60.8]],
 [[  79.2 ,  79.2 ,  32.4 ,  32.4],
  [ 145.8 , 145.8 ,  95.4 ,  95.4],
  [ 122.4 , 122.4 , 194.4 , 194.4],
  [  83.7 ,  83.7 ,   8.1 ,   8.1],
  [   9.  ,   9.  ,  19.8 ,  19.8],
  [-148.5 ,-148.5 , 128.7 , 128.7],
  [ 242.1 , 242.1 , -45.9 , -45.9]]], dtype=float)

dwf = numpy.array(
[[[6.14421235e-006, 6.14421235e-006, 6.14421235e-006, 6.14421235e-006],
  [3.35462628e-004, 3.35462628e-004, 3.35462628e-004, 3.35462628e-004],
  [6.14421235e-006, 6.14421235e-006, 6.14421235e-006, 6.14421235e-006],
  [1.83156389e-002, 1.83156389e-002, 1.83156389e-002, 1.83156389e-002],
  [1.35335283e-001, 1.35335283e-001, 1.35335283e-001, 1.35335283e-001],
  [1.17798894e+014, 1.17798894e+014, 1.17798894e+014, 1.17798894e+014],
  [3.73629938e-007, 3.73629938e-007, 3.73629938e-007, 3.73629938e-007]],
 [[3.32124719e-004, 3.32124719e-004, 3.32124719e-004, 3.32124719e-004],
  [1.10306829e-007, 1.10306829e-007, 1.10306829e-007, 1.10306829e-007],
  [5.96262344e-006, 5.96262344e-006, 5.96262344e-006, 5.96262344e-006],
  [3.64280970e-003, 3.64280970e-003, 3.64280970e-003, 3.64280970e-003],
  [9.31095163e-014, 9.31095163e-014, 9.31095163e-014, 9.31095163e-014],
  [7.62689445e-008, 7.62689445e-008, 7.62689445e-008, 7.62689445e-008],
  [1.38491465e+016, 1.38491465e+016, 1.38491465e+016, 1.38491465e+016]],
 [[1.75974724e-002, 1.75974724e-002, 1.75974724e-002, 1.75974724e-002],
  [6.38279576e-013, 6.38279576e-013, 6.38279576e-013, 6.38279576e-013],
  [5.44942750e-006, 5.44942750e-006, 5.44942750e-006, 5.44942750e-006],
  [2.62702212e-010, 2.62702212e-010, 2.62702212e-010, 2.62702212e-010],
  [8.89216175e-002, 8.89216175e-002, 8.89216175e-002, 8.89216175e-002],
  [4.84334796e-013, 4.84334796e-013, 4.84334796e-013, 4.84334796e-013],
  [1.12134816e-018, 1.12134816e-018, 1.12134816e-018, 1.12134816e-018]],
 [[4.71788916e-016, 4.71788916e-016, 5.09416441e-007, 5.09416441e-007],
  [6.01928028e-029, 6.01928028e-029, 3.21914812e-019, 3.21914812e-019],
  [1.80767634e-024, 1.80767634e-024, 2.28927125e-038, 2.28927125e-038],
  [6.10401396e-017, 6.10401396e-017, 2.38731711e-002, 2.38731711e-002],
  [1.75097047e-002, 1.75097047e-002, 1.44100440e-004, 1.44100440e-004],
  [5.08663950e+028, 5.08663950e+028, 1.58983037e-025, 1.58983037e-025],
  [1.38333793e-047, 1.38333793e-047, 5.37801451e+008, 5.37801451e+008]],
 [[6.63064351e-020, 6.63064351e-020, 5.34515906e-014, 5.34515906e-014],
  [9.38823340e-023, 9.38823340e-023, 1.12903297e-016, 1.12903297e-016],
  [2.24317699e-034, 2.24317699e-034, 8.55631457e-049, 8.55631457e-049],
  [8.82947583e-007, 8.82947583e-007, 9.53367067e+002, 9.53367067e+002],
  [1.36648906e+003, 1.36648906e+003, 6.14003114e+002, 6.14003114e+002],
  [1.16105659e+049, 1.16105659e+049, 7.66928664e+015, 7.66928664e+015],
  [1.59623613e-037, 1.59623613e-037, 2.93635843e-002, 2.93635843e-002]],
 [[6.21864968e-030, 6.21864968e-030, 1.22982520e-022, 1.22982520e-022],
  [7.22504014e-030, 7.22504014e-030, 1.42885303e-022, 1.42885303e-022],
  [2.39049240e-047, 2.39049240e-047, 3.09061907e-069, 3.09061907e-069],
  [2.57456540e-008, 2.57456540e-008, 1.51777390e+003, 1.51777390e+003],
  [2.13166710e+007, 2.13166710e+007, 4.74411237e+007, 4.74411237e+007],
  [3.92824421e+080, 3.92824421e+080, 9.69486419e+040, 9.69486419e+040],
  [5.07809095e-058, 5.07809095e-058, 2.75598909e-015, 2.75598909e-015]],
 [[1.41704527e-042, 1.41704527e-042, 6.87501044e-034, 6.87501044e-034],
  [9.78468714e-039, 9.78468714e-039, 3.18213638e-030, 3.18213638e-030],
  [5.94684519e-063, 5.94684519e-063, 2.60603147e-092, 2.60603147e-092],
  [9.85950558e-011, 9.85950558e-011, 3.17348329e+002, 3.17348329e+002],
  [1.21114232e+011, 1.21114232e+011, 1.33506354e+012, 1.33506354e+012],
  [1.47458108e+119, 1.47458108e+119, 1.35973280e+073, 1.35973280e+073],
  [9.24402711e-082, 9.24402711e-082, 1.48014178e-031, 1.48014178e-031]],
 [[7.84546293e-058, 7.84546293e-058, 9.33792872e-048, 9.33792872e-048],
  [2.33186775e-049, 2.33186775e-049, 1.24709722e-039, 1.24709722e-039],
  [3.45351493e-081, 3.45351493e-081, 5.12966817e-118, 5.12966817e-118],
  [4.95893650e-014, 4.95893650e-014, 8.71460192e+000, 8.71460192e+000],
  [2.50630285e+014, 2.50630285e+014, 1.36839499e+016, 1.36839499e+016],
  [6.14135099e+164, 6.14135099e+164, 2.11587743e+112, 2.11587743e+112],
  [9.62895915e-109, 9.62895915e-109, 4.54869211e-051, 4.54869211e-051]],
 [[2.49499557e-021, 2.49499557e-021, 2.49499557e-021, 2.49499557e-021],
  [2.68374288e-026, 2.68374288e-026, 2.68374288e-026, 2.68374288e-026],
  [1.25851870e-058, 1.25851870e-058, 1.25851870e-058, 1.25851870e-058],
  [1.40132036e+001, 1.40132036e+001, 1.40132036e+001, 1.40132036e+001],
  [8.96139104e-005, 8.96139104e-005, 8.96139104e-005, 8.96139104e-005],
  [2.27340117e+032, 2.27340117e+032, 2.27340117e+032, 2.27340117e+032],
  [5.46487021e-004, 5.46487021e-004, 5.46487021e-004, 5.46487021e-004]],
 [[9.36080858e-018, 9.36080858e-018, 2.27281947e-012, 2.27281947e-012],
  [1.16159901e-027, 1.16159901e-027, 1.39694394e-021, 1.39694394e-021],
  [5.90611830e-041, 5.90611830e-041, 6.57808778e-044, 6.57808778e-044],
  [3.69020032e-008, 3.69020032e-008, 5.94419378e+001, 5.94419378e+001],
  [5.61825499e-012, 5.61825499e-012, 3.09934656e-014, 3.09934656e-014],
  [1.39311586e+023, 1.39311586e+023, 2.77163119e-011, 2.77163119e-011],
  [1.05155060e-009, 1.05155060e-009, 1.75483121e+025, 1.75483121e+025]],
 [[1.47768734e-035, 1.47768734e-035, 3.12294478e-015, 3.12294478e-015],
  [6.47553380e-065, 6.47553380e-065, 5.00861284e-043, 5.00861284e-043],
  [3.46315532e-055, 3.46315532e-055, 1.86324203e-086, 1.86324203e-086],
  [9.95657895e-038, 9.95657895e-038, 6.77287365e-005, 6.77287365e-005],
  [7.48518299e-005, 7.48518299e-005, 1.52694016e-009, 1.52694016e-009],
  [9.34231470e+064, 9.34231470e+064, 3.83728547e-056, 3.83728547e-056],
  [2.65542562e-107, 2.65542562e-107, 3.16916557e+018, 3.16916557e+018]]], dtype=float)

def test_calc_beta_by_u_ij():
    res = calc_beta_by_u_ij(u_ij, reciprocal_unit_cell_parameters)[0]
    print("res: ", res)
    print(beta_ij)

    assert numpy.all(numpy.isclose(res, beta_ij))


def test_calc_b_iso_beta():
    res_b_iso, res_beta = calc_b_iso_beta(
        unit_cell_parameters, atom_adp_type, atom_iso_param, atom_aniso_param)
    print("res_b_iso: ", res_b_iso)
    print(b_iso_out)
    print("res_beta: ", res_beta)
    print(beta_out)
    
    assert numpy.all(numpy.isclose(res_b_iso, b_iso_out))
    assert numpy.all(numpy.isclose(res_beta, beta_out))


def test_calc_power_dwf_iso():
    res, dder = calc_power_dwf_iso(sthovl[:, na], b_iso[na, :], flag_sthovl=True, flag_b_iso=True)
    print("res: ", res)
    print(power_dwf_iso)

    assert numpy.all(numpy.isclose(res, power_dwf_iso))


def test_calc_power_dwf_aniso():
    res, dder = calc_power_dwf_aniso(index_hkl[:, :, na, na], beta[:, na, :, na], symm_elems_r[:, na, na, :], flag_beta=True)
    print("res: ", res)
    print(power_dwf_aniso)

    assert numpy.all(numpy.isclose(res, power_dwf_aniso))


def test_calc_dwf():
    res, dder = calc_dwf(
        index_hkl[:, :, na, na], sthovl[:, na, na], b_iso[na, :, na], beta[:, na, :, na], symm_elems_r[:, na, na, :],
        flag_sthovl=True, flag_b_iso=True, flag_beta=True)
    print("res: ", res)
    print(dwf)
    
    assert numpy.all(numpy.isclose(res, dwf))
