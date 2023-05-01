from house_info import HouseInfo
from datetime import date


class EngeryData(HouseInfo):
    ENERGY_PER_BULB= 0.2
    ENERGY_BITS = 0x0F0
     
    def _convert_data(self, data):
        recs = []
        for rec in data:
            # Convert string of integers into actual integers based 10
            recs.append(float(rec) * 100)
        return recs

    def get_data_by_area(self, rec_area=0):
        recs = super().get_data_by_area("engery", rec_area)
        return self._convert_data(recs)


    def get_data_by_date(self, rec_date=date.today()):
        recs = super().get_data_by_date("engery", rec_date)
        return self._convert_data(recs)