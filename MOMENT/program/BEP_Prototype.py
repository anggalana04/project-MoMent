def get_user_input_for_bep():
    data_input = input('Masukan jumlah unit yang anda produksi dalam sebulan: ')
    harga_per_unit = input('Masukkan harga per unit: ')
    fixed_cost = input('Masukkan fixed cost anda: ')
    variable_cost = input('Masukkan Variable Cost anda: ')

    return int(data_input), int(harga_per_unit), int(fixed_cost), int(variable_cost) 

def display_result():
    pass

class Breakevenpoint:
    @staticmethod
    def variabel_per_unit(unit, variable_cost):
        return variable_cost / unit

    @staticmethod
    def bep_unit(harga_per_unit, fixed_cost, vc_unit):
        bep_unit_hasil = fixed_cost / (harga_per_unit - vc_unit)
        return bep_unit_hasil

    @staticmethod
    def bep_rupiah(harga_per_unit, fixed_cost, vc_unit):
        bep_rupiah_hasil = fixed_cost / (1 - (vc_unit / harga_per_unit))
        return bep_rupiah_hasil