from datetime import datetime

from library import db
from library.DAL import LocationRep, CategoryRep, models, AccountRep
from library.DAL.models import Roles, Customers
from library.common.Req.AccountReq import CreateEmployeeAccountReq
from library.controllers import BookController
from library.controllers import CategoryController
from library.controllers import AccountController
from library.controllers import AuthorController, SupplierController, EmployeeController, CustomerController, \
    OrderController, ScheduleController, BorrowTicketController, OrderDetailController, RevenueController, UploadImageController,MessageController, LoginController
import requests

def loadAndInsertData():
    provincesRes = requests.post(url="http://shop.d.etop.vn/api/etop.Location/GetProvinces", data={}, json={})
    provinces = provincesRes.json()["provinces"]

    districtsRes = requests.post(url="http://shop.d.etop.vn/api/etop.Location/GetDistricts", data={}, json={})
    districts = districtsRes.json()["districts"]

    wardsRes = requests.post(url="http://shop.d.etop.vn/api/etop.Location/GetWards", data={}, json={})
    wards = wardsRes.json()["wards"]

    for province in provinces:
        LocationRep.createProvince(province)

    for district in districts:
        LocationRep.createDistrict(district)

    for ward in wards:
        LocationRep.createWard(ward)



def insertCategories():
    categoryDicts = [
        {
            "categoryName": "Sách tư duy - Kỹ năng sống",
            "description": "MÔ tả điênh thoại máy tính bảng",
            "note": "GHI CHÚ MÁY TINH BẢNG",
            "createAt": datetime.now(),
            "image": "https://vnwriter.net/wp-content/uploads/2017/06/sach-toi-tu-duy-toi-thanh-dat.jpg"
        },
        {
            "categoryName": "Tiểu thuyết",
            "description": "MÔ tả điênh thoại máy tính bảng",
            "note": "GHI CHÚ MÁY TINH BẢNG",
            "createAt":datetime.now(),
            "image": "https://upload.wikimedia.org/wikipedia/vi/2/23/Tiengchimhot2012.jpg"
        },
        {
            "categoryName": "Kiến thức - Bách khoa",
            "description": "MÔ tả điênh thoại máy tính bảng",
            "note": "GHI CHÚ MÁY TINH BẢNG",
            "createAt":datetime.now(),
            "image": "https://salt.tikicdn.com/ts/product/8c/64/c9/8b1ec9939b56751c44eeddcf7a7bc9fe.jpg"
        },
        {
            "categoryName":"Sách kỹ năng làm việc",
            "description":"MÔ tả điênh thoại máy tính bảng",
            "note":"GHI CHÚ MÁY TINH BẢNG",
            "createAt":datetime.now(),
            "image": "https://cdn0.fahasa.com/media/catalog/product/cache/1/small_image/400x400/9df78eab33525d08d6e5fb8d27136e95/k/y/kynangvietbaocaohieuqua_bia1.jpg"
        },
        {
            "categoryName":"Sách nghệ thuật sách đẹp",
            "description":"MÔ tả điênh thoại máy tính bảng",
            "note":"GHI CHÚ MÁY TINH BẢNG",
            "createAt":datetime.now(),
            "image":"https://chi.vn/data/files/image-20200929151745-10.jpeg"
        },
        {
            "categoryName": "Sách tư liệu",
            "description": "MÔ tả điênh thoại máy tính bảng",
            "note": "GHI CHÚ MÁY TINH BẢNG",
            "createAt": datetime.now(),
            "image":"https://bizweb.dktcdn.net/100/116/097/files/vn-267.jpg?v=1567161580877",
        },
        {
            "categoryName":"Sách, VPP & Qùa tặng",
            "description":"MÔ tả điênh thoại máy tính bảng",
            "note": "GHI CHÚ MÁY TINH BẢNG",
            "createAt": datetime.now(),
            "image":"https://lh3.googleusercontent.com/proxy/byLkDPXBQs8TbsUk9xSLp1p_mqxdey-7ly-efDHa1sotUPLGQ4tkpdEZJtvSny9sN4tsxbfHbUle836DVEht_1vLQjZLdlmAyp3RZHl1lVCsdm8NmP16T4JZK-bFsxP0_hm-ohK5WQ"
        },
        {
            "categoryName":"Voucher, Dịch vụ, Thẻ cào",
            "description":"MÔ tả điênh thoại máy tính bảng",
            "note": "GHI CHÚ MÁY TINH BẢNG",
            "createAt": datetime.now(),
            "image":"https://img.timviec.com.vn/2020/10/voucher-la-gi-3.jpg"
        },
    ]
    for category in categoryDicts:
        categoryModel = models.Categories(
                             category_name = category['categoryName'],
                             description = category['description'],
                                image = category['image'],
                             note = category['note'],
                        )
        CategoryRep.CreateCategory(categoryModel)

def initAdminAccount():
    req = CreateEmployeeAccountReq({
        "role_id": 1,
        "account_name": "admin",
        "account_password":"123456789",
        # Employee
        "last_name": "Nguyễn Văn",
        "first_name": "Kim Hải",
        "phone": "0865248526",
        "email": "1751012015hai@ou.edu.vn",
        "address": "381 Nguyễn Kiệm",
        "gender": True,
        "image":"",
        "basic_rate": 50000,
        "note": "Tài khoản admin đầu tiên của chương trình",
    })
    account, employee = AccountRep.CreateEmployeeAccount(req)



def initRoles():
    role1 = Roles(role_id=1, role_name="admin");
    role2 = Roles(role_id=2, role_name= "admin-manager");
    role3 = Roles(role_id=3, role_name="user");
    db.session.add(role1)
    db.session.add(role2)
    db.session.add(role3)
    db.session.commit()

def initAnomyCustomer():
    indepentCustomer = Customers(customer_id=1, first_name="Khách lẻ")
    db.session.add(indepentCustomer)
    db.session.commit()


