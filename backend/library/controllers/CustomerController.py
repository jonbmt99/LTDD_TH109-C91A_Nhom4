from sqlalchemy import or_

from library import app
from library.BLL import CustomerSvc
from library.DAL import models
from library.common.Req.CustomerReq import CreateCustomerReq, UpdateCustomerReq, DeleteCustomerReq, SearchCustomersReq
from library.common.Req.GetItemsByPageReq import GetItemsByPageReq, SearchItemsReq
from library.common.Rsp.CustomerRsp import SearchCustomersRsp
from library.common.Rsp.GetImtesByPageRsp import GetItemsByPageRsp
from flask import jsonify, request, make_response
import json

from library.common.Rsp.SingleRsp import ErrorRsp
from library.common.util import ConvertModelListToDictList


@app.route('/admin/customer-management/get-customers', methods=['POST', 'GET'])
def GetCustomers():
    req = GetItemsByPageReq(request.json)
    result = CustomerSvc.GetCustomersByPage(req)
    res = GetItemsByPageRsp(has_next=result['has_next'], has_prev=result['has_prev'],
                            items=result['customers']).serialize()
    return jsonify(res)


@app.route('/admin/customer-management/create-customer', methods=['POST', 'GET'])
def CreateCustomer():
    req = CreateCustomerReq(request.json)
    result = CustomerSvc.CreateCustomer(req)
    return jsonify(result)


@app.route('/admin/customer-management/update-customer', methods=['POST', 'GET'])
def UpdateCustomer():
    req = UpdateCustomerReq(request.json)
    result = CustomerSvc.UpdateCustomer(req)
    return jsonify(result)


@app.route('/admin/customer-management/delete-customer', methods=['POST', 'GET'])
def DeleteCustomer():
    req = DeleteCustomerReq(request.json)
    result = CustomerSvc.DeleteCustomer(req)
    return jsonify(result)


@app.route('/admin/customer-management/search-customers', methods=['POST', 'GET'])
def SearchCustomers():
    req = SearchItemsReq(request.json)
    if (req.customer_id):
        customers = models.Customers.query.filter(models.Customers.customer_id == req.customer_id)
        return jsonify(ConvertModelListToDictList(customers))

    all_customers = models.Customers.query.all()
    if req.customer_name != None:
        all_customers = models.Customers.query.filter((models.Customers.first_name.ilike(f'%{req.customer_name}%'))).all()


    if req.phone != None:
        all_customers = [customer for customer in all_customers if customer.phone == req.phone]

    all_customers = [customer for customer in all_customers if customer.delete_at == None]
    customers = ConvertModelListToDictList(all_customers)
    return jsonify(customers)


