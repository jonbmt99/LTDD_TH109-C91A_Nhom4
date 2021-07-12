from flask import request, jsonify

from library import app
from library.BLL import SupplierSvc
from library.DAL import models
from library.common.Req.GetItemsByPageReq import GetItemsByPageReq, SearchItemsReq
from library.common.Req.SupplierReq import CreateSupplierReq, UpdateSupplierReq, DeleteSupplierReq, SearchSuppliersReq
from library.common.Rsp.GetImtesByPageRsp import GetItemsByPageRsp
from library.common.Rsp.SupplierRsp import SearchSuppliersRsp
from library.common.util import ConvertModelListToDictList


@app.route('/admin/supplier-management/get-suppliers', methods=['GET', 'POST'])
def GetSuplliers():
    req = GetItemsByPageReq(request.json)
    result = SupplierSvc.GetSupplierByPage(req)
    res = GetItemsByPageRsp(has_next=result['has_next'], has_prev=result['has_prev'],
                            items=result['suppliers']).serialize()
    return jsonify(res)


@app.route('/admin/supplier-management/create-supplier', methods=['POST'])
def CreateSupplier():
    req = CreateSupplierReq(request.json)
    result = SupplierSvc.CreateSupplier(req)
    return jsonify(result)


@app.route('/admin/supplier-management/update-supplier', methods=['POST'])
def UpdateSupplier():
    req = UpdateSupplierReq(request.json)
    result = SupplierSvc.UpdateSupplier(req)
    return jsonify(result)


@app.route('/admin/supplier-management/search-suppliers', methods=['POST'])
def SearchSuppliers():
    req = SearchItemsReq(request.json)
    if (req.supplier_id):
        suppliers = models.Suppliers.query.filter(models.Suppliers.supplier_id == req.supplier_id)
        return jsonify(ConvertModelListToDictList(suppliers))

    suppliers = models.Suppliers.query.all()
    if req.email != None:
        suppliers = [supplier for supplier in suppliers if supplier.email == req.email]

    if req.contact_name != None:
        suppliers = [supplier for supplier in suppliers if supplier.contact_name == (req.contact_name)]

    suppliers = [supplier for supplier in suppliers if supplier.delete_at == None]
    suppliers = ConvertModelListToDictList(suppliers)
    return jsonify(suppliers)


@app.route('/admin/supplier-management/delete-supplier', methods=['POST'])
def DeleteSupplier():
    req = DeleteSupplierReq(request.json)
    result = SupplierSvc.DeleteSupplier(req)
    return jsonify(result)
