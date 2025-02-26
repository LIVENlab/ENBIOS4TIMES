from Sparks.util.base import SoftLink


enbios_mod = SoftLink(r'C:\Users\altz7\PycharmProjects\ENBIOS4TIMES_\testing\data_test\ElectricgenerationTIMES-Sinergia.xlsx',
                      r'C:\Users\altz7\PycharmProjects\ENBIOS4TIMES_\testing\data_test\Times_ecoinvent.xlsx',
                       'Seeds_exp4',
                      'db_experiments')



enbios_mod.preprocess(subregions=False)
pass

enbios_mod.data_for_ENBIOS(smaller_vers=False,
                           path_save=r'test.json')




