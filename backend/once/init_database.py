from library.DAL.models import *
from library.controllers import loadAndInsertData, insertCategories, initAdminAccount, initRoles, initAnomyCustomer

db.create_all()
loadAndInsertData()
insertCategories()
initRoles()
initAdminAccount()
initAnomyCustomer()
