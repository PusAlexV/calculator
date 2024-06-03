import s_taper
from s_taper.consts import*
scheme = {"user_id": INT+KEY,
          "name":TEXT,
          "age":FLT,
          "first":BLN}
users = s_taper.Taper("users", "data.db").create_table(scheme)



scheme = {"user_id": INT+KEY,
          "имя":TEXT,
          "age":FLT,
          "first":BLN}
users = s_taper.Taper("users", "data2.db").create_table(scheme)