from datetime import datetime

from library import app, db
from library.BLL import OrderSvc
from library.DAL import models, CategoryRep
from library.DAL.models import Roles
from library.auth import user_required, owner_required
from library.common.Req.GetItemsByPageReq import GetItemsByPageReq, SearchItemsReq
from library.common.Req.OrderReq import CreateOrderReq, UpdateOrderReq, DeleteOrderReq, SearchOrdersReq
from library.common.Rsp.GetImtesByPageRsp import GetItemsByPageRsp
from flask import jsonify, request, make_response
import json

from library.common.Rsp.SingleRsp import ErrorRsp
from library.common.util import ConvertModelListToDictList


@app.route("/admin/order-management/get-orders", methods=['POST', 'GET'])
def GetOrders():
    req = GetItemsByPageReq(request.json)
    result = OrderSvc.GetOrdersByPage(req)
    res = GetItemsByPageRsp(has_next=result['has_next'], has_prev=result['has_prev'],
                            items=result['orders']).serialize()
    return jsonify(res)


@app.route("/admin/order-management/create-order", methods=['POST', 'GET'])
def CreateOrder():
    try:
        req = CreateOrderReq(request.json)
        result = OrderSvc.CreateOrder(req)

        return jsonify(result)
    except ErrorRsp as e:
        return json.dumps(e.__dict__, ensure_ascii=False).encode('utf8')

@app.route('/admin/order-management/create-order-by-momo', methods=['GET', 'POST'])
def RedirectMomoPage():
    req = CreateOrderReq(request.json)
    res = OrderSvc.CreateOrderByMomo(req)
    if res['errorCode'] == 0:
        result = OrderSvc.CreateOrder(req)
    return jsonify(res)

@app.route("/admin/order-management/update-order", methods=['POST', 'GET'])
def UpdateOrder():
    req = UpdateOrderReq(request.json)
    result = OrderSvc.UpdateOrder(req)
    return jsonify(result)


@app.route("/admin/order-management/delete-order", methods=['POST', 'GET'])
def DeleteOrder():
    req = DeleteOrderReq(request.json)
    result = OrderSvc.DeleteOrder(req)

    return jsonify(result)


@app.route("/admin/order-management/search-orders", methods=['POST', 'GET'])
@owner_required
def SearchOrders(session):
    req = SearchItemsReq(request.json)
    if (req.order_id):
        orders = models.Orders.query.filter(models.Orders.order_id == req.order_id)
        return jsonify(ConvertModelListToDictList(orders))

    orders = models.Orders.query.all()
    if req.type != None:
        orders = [order for order in orders if order.type == req.type]

    if req.customer_id != None:
        orders = [order for order in orders if order.customer != None and order.customer.customer_id == (req.customer_id)]

    if req.customer_phone != None:
        orders = [order for order in orders if order.customer != None and order.customer.phone == (req.customer_phone)]

    orders = [order for order in orders if order.delete_at == None]
    orders = ConvertModelListToDictList(orders)
    return jsonify(orders)

@app.route("/", methods=['POST', 'GET'])
def TestCreateOrder():
    categoryDicts = [
        {
            "categoryName": "??i???n tho???i - M??y t??nh b???ng",
            "description": "M?? t??? ??i??nh tho???i m??y t??nh b???ng",
            "note": "GHI CH?? M??Y TINH B???NG",
            "createAt": datetime.now(),
        },
        {
            "categoryName": "??i???n t??? - ??i???n l???nh",
            "description": "M?? t??? ??i??nh tho???i m??y t??nh b???ng",
            "note": "GHI CH?? M??Y TINH B???NG",
            "createAt": datetime.now(),
        },
        {
            "categoryName": "Ph??? ki???n - Thi???t b??? s???",
            "description": "M?? t??? ??i??nh tho???i m??y t??nh b???ng",
            "note": "GHI CH?? M??Y TINH B???NG",
            "createAt": datetime.now(),
        },
        {
            "categoryName": "Laptop - Thi???t b??? IT",
            "description": "M?? t??? ??i??nh tho???i m??y t??nh b???ng",
            "note": "GHI CH?? M??Y TINH B???NG",
            "createAt": datetime.now(),
        },
        {
            "categoryName": "M??y ???nh - Quay phim",
            "description": "M?? t??? ??i??nh tho???i m??y t??nh b???ng",
            "note": "GHI CH?? M??Y TINH B???NG",
            "createAt": datetime.now(),
        },
        {
            "categoryName": "??i???n gia d???ng",
            "description": "M?? t??? ??i??nh tho???i m??y t??nh b???ng",
            "note": "GHI CH?? M??Y TINH B???NG",
            "createAt": datetime.now(),
        },
        {
            "categoryName": "Nh?? c???a ?????i s???ng",
            "description": "M?? t??? ??i??nh tho???i m??y t??nh b???ng",
            "note": "GHI CH?? M??Y TINH B???NG",
            "createAt": datetime.now(),
        },
        {
            "categoryName": "H??ng ti??u d??ng - Th???c ph???m",
            "description": "M?? t??? ??i??nh tho???i m??y t??nh b???ng",
            "note": "GHI CH?? M??Y TINH B???NG",
            "createAt": datetime.now(),
        },
        {
            "categoryName": "????? ch??i - M??? & B??",
            "description": "M?? t??? ??i??nh tho???i m??y t??nh b???ng",
            "note": "GHI CH?? M??Y TINH B???NG",
            "createAt": datetime.now(),
        },
        {
            "categoryName": "L??m ?????p - S???c kh???e",
            "description": "M?? t??? ??i??nh tho???i m??y t??nh b???ng",
            "note": "GHI CH?? M??Y TINH B???NG",
            "createAt": datetime.now(),
        },
        {
            "categoryName": "Th???i trang - Ph??? ki???n",
            "description": "M?? t??? ??i??nh tho???i m??y t??nh b???ng",
            "note": "GHI CH?? M??Y TINH B???NG",
            "createAt": datetime.now(),
        },
        {
            "categoryName": "Th??? thao - D?? ngo???i",
            "description": "M?? t??? ??i??nh tho???i m??y t??nh b???ng",
            "note": "GHI CH?? M??Y TINH B???NG",
            "createAt": datetime.now(),
        },
        {
            "categoryName": "Xe m??y, oto, xe ?????p",
            "description": "M?? t??? ??i??nh tho???i m??y t??nh b???ng",
            "note": "GHI CH?? M??Y TINH B???NG",
            "createAt": datetime.now(),
        },
        {
            "categoryName": "H??ng qu???c t???\", \"M?? t??? ??i??nh tho???i m??y t??nh b???ng",
            "description": "M?? t??? ??i??nh tho???i m??y t??nh b???ng",
            "note": "GHI CH?? M??Y TINH B???NG",
            "createAt": datetime.now(),
        },
        {
            "categoryName": "S??ch, VPP & Q??a t???ng",
            "description": "M?? t??? ??i??nh tho???i m??y t??nh b???ng",
            "note": "GHI CH?? M??Y TINH B???NG",
            "createAt": datetime.now(),
        },
        {
            "categoryName": "Voucher, D???ch v???, Th??? c??o",
            "description": "M?? t??? ??i??nh tho???i m??y t??nh b???ng",
            "note": "GHI CH?? M??Y TINH B???NG",
            "createAt": datetime.now(),
        },
    ]
    for category in categoryDicts:
        categoryModel = models.Categories(
            category_name=category['categoryName'],
            description=category['description'],
            note=category['note'],
        )
        CategoryRep.CreateCategory(categoryModel)
    return "return"
