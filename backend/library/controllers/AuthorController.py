from library import app
from library.BLL import AuthorSvc
from flask import jsonify, request, make_response
import json

from library.common.Req.AuthorReq import CreateAuthorReq, DeleteAuthorByIdReq, UpdateAuthorReq, SearchAuthorReq
from library.common.Req.GetItemsByPageReq import GetItemsByPageReq
from library.common.Rsp.AuthorRsp import CreateAuthorRsp, SearchAuthorRsp
from library.common.Rsp.GetImtesByPageRsp import GetItemsByPageRsp
from library.common.Rsp.SingleRsp import ErrorRsp


@app.route('/admin/author-management/get-authors', methods=['POST'])
def GetAuthors():
    req = GetItemsByPageReq(request.json)
    result = AuthorSvc.GetAuthorByPage(req)
    res = GetItemsByPageRsp(has_next=result['has_next'], has_prev=result['has_prev'],
                            items=result['authors']).serialize()
    return jsonify(res)


@app.route('/admin/author-management/create-author', methods=['POST'])
def CreateAuthor():
    req = CreateAuthorReq(request.json)
    result = AuthorSvc.CreateAuthor(req)
    res = CreateAuthorRsp(result).serialize()
    return jsonify(res)


@app.route('/admin/author-management/delete-author', methods=['POST'])
def DeleteAuthor():
    req = DeleteAuthorByIdReq(request.json)
    result = AuthorSvc.DeleteAuthorById(req)
    return jsonify(result)


@app.route('/admin/author-management/update-author', methods=['POST'])
def UpdateAuthor():
    req = UpdateAuthorReq(request.json)
    result = AuthorSvc.UpdateAuthor(req)
    return jsonify(result)


@app.route('/admin/author-management/search-author', methods=['POST'])
def SearchAuthor():
    req = SearchAuthorReq(request.json)
    result = AuthorSvc.SearchAuthor(req)
    res = SearchAuthorRsp(result).serialize()
    return jsonify(res['authors'])
