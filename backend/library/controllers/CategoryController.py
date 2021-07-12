from library import app
from library.BLL import BookSvc, CategorySvc
from library.DAL import models
from library.common.Req.CategoryReq import CreateCategoryReq, UpdateCategoryReq, DeleteCategoryByIdReq, \
    SearchCategoryReq
from library.common.Req.GetItemsByPageReq import GetItemsByPageReq
from library.common.Rsp.CategoryRsp import SearchCategoryRsp
from library.common.Rsp.GetImtesByPageRsp import GetItemsByPageRsp
from flask import jsonify, request, make_response
import json

from library.common.Rsp.SingleRsp import ErrorRsp
from library.common.util import ConvertModelListToDictList


@app.route('/get-categories', methods=['GET', 'POST'])
def GetCategories():
    categoriesModel = models.Categories.query.filter(models.Categories.delete_at == None)
    categories = ConvertModelListToDictList(categoriesModel)
    return jsonify(categories)


@app.route('/admin/category-management/create-category', methods=['POST'])
def CreateCategory():
    req = CreateCategoryReq(request.json)
    created_category = CategorySvc.CreateCategory(req)
    return jsonify(created_category)


@app.route('/admin/category-management/update-category', methods=['POST'])
def UpdateCategory():
    req = UpdateCategoryReq(request.json)
    updated_category = CategorySvc.UpdateCategory(req)
    return jsonify(updated_category)


@app.route('/admin/category-management/delete-category', methods=['POST'])
def DeleteCategory():
    req = DeleteCategoryByIdReq(request.json)
    deleted_category = CategorySvc.DeleteCategoryById(req)
    return jsonify(deleted_category)


@app.route('/admin/category-management/search-category', methods=['POST'])
def SearchCategory():
    req = SearchCategoryReq(request.json)
    search_category = CategorySvc.SearchCategory(req)
    res = SearchCategoryRsp(search_category).serialize()
    return jsonify(res['categories'])

