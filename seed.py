import model
from datetime import datetime

u = model.User()
u.id = 1
u.email = "julie.hollek@gmail.com"
u.password = "julie"
u.cell_phone = "3136186587"
u.first_name = "Julie"
u.last_name = "Hollek"
u.baby_dob = datetime.strptime("2012-02-29", "%Y-%m-%d")
u.zip_code = "94501"
u.no_dairy = False
u.no_wheat = False
u.no_soy = False
u.no_caffeine = False
u.no_alcohol = False
u.has_health_info = False

a = model.User()
a.id = 2
a.email = "lzhou89@gmail.com"
a.password = "linda"
a.cell_phone = "6462891899"
a.first_name = "Linda"
a.last_name = "Zhou"
a.baby_dob = datetime.strptime("2014-09-29", "%Y-%m-%d")
a.zip_code = "94108"
a.no_dairy = True
a.no_wheat = True
a.no_soy = True
a.no_caffeine = True
a.no_alcohol = True
a.has_health_info = True

p = model.Post()
p.id = 1
p.user_id = 1
p.req_or_off = "request"
p.date = datetime.strptime("2014-11-14", "%Y-%m-%d")
p.amt_milk = "2 gallons"
p.recurring = True

m = model.Message()
m.id = 1
m.sender_id = 1
m.recipient_id = 2
m.date = datetime.strptime("2014-11-14", "%Y-%m-%d")
m.subject = "Hi!"
m.message = "This is spam."

model.session.add_all([u, a, p, m])
model.session.commit()




