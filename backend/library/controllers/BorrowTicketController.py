from datetime import datetime

from library import app
from flask import jsonify, request, make_response
import json

from library.BLL import BorrowTicketSvc
from library.DAL import models
from library.common.Req.BorrowTicketReq import CreateBorrowTicketReq, UpdateBorrowTicketReq, DeleteBorrowTicketReq, \
    SearchBorrowTicketReq, FinishBorrowTicketReq, SendEmailForLateBorrowTicketReq
from library.common.Req.GetItemsByPageReq import GetItemsByPageReq, SearchItemsReq
from library.common.Rsp.BorrowTicketRsp import SearchBorrowTicketRsp
from library.common.Rsp.GetImtesByPageRsp import GetItemsByPageRsp
from library.common.Rsp.SingleRsp import ErrorRsp
from library.common.util import ConvertModelListToDictList


@app.route('/admin/borrow-ticket-management/get-borrow-tickets', methods=['POST', 'GET'])
def GetBorrowTickets():
    req = GetItemsByPageReq(request.json)
    result = BorrowTicketSvc.GetBorrowTicketsByPage(req)
    res = GetItemsByPageRsp(has_next=result['has_next'], has_prev=result['has_prev'],
                            items=result['borrow_tickets']).serialize()
    return jsonify(res)


@app.route('/admin/borrow-ticket-management/create-borrow-ticket', methods=['POST', 'GET'])
def CreateBorrowTicket():
    req = CreateBorrowTicketReq(request.json)
    try:
        result = BorrowTicketSvc.CreateBorrowTicket(req)
        return jsonify(result)
    except ErrorRsp as e:
        return json.dumps(e.__dict__, ensure_ascii=False).encode('utf-8'), 401


@app.route('/admin/borrow-ticket-management/update-borrow-ticket', methods=['POST', 'GET'])
def UpdateBorrowTicket():
    req = UpdateBorrowTicketReq(request.json)
    result = BorrowTicketSvc.UpdateBorrowTicket(req)
    return jsonify(result)


@app.route('/admin/borrow-ticket-management/finish-borrow-ticket', methods=['POST', 'GET'])
def FinishBorrowTicket():
    req = FinishBorrowTicketReq(request.json)
    result = BorrowTicketSvc.FinishBorrowTicket(req)
    return jsonify(result)


@app.route('/admin/borrow-ticket-management/delete-borrow-ticket', methods=['POST', 'GET'])
def DeleteBorrowTicket():
    req = DeleteBorrowTicketReq(request.json)
    result = BorrowTicketSvc.DeleteBorrowTicket(req)
    return jsonify(result)


@app.route('/admin/borrow-ticket-management/get-borrow-ticket', methods=['POST', 'GET'])
def SearchBorrowTicket():
    req = SearchItemsReq(request.json)
    req = SearchBorrowTicketReq(request.json)
    result = BorrowTicketSvc.SearchBorrowTicket(req)
    res = SearchBorrowTicketRsp(result).serialize()
    return jsonify(res)

@app.route('/admin/borrow-ticket-management/send-email-for-late-borrow-ticket', methods=['POST', 'GET'])
def SendEmailForLateBorrowTicket():
    req = SendEmailForLateBorrowTicketReq(request.json)
    result = BorrowTicketSvc.SendMessageForLate(req)
    return jsonify(result)


@app.route('/admin/borrow-ticket-management/search-borrow-tickets', methods=['POST', 'GET'])
def searchBorrowTickets():
    req = SearchItemsReq(request.json)
    borrow_tickets = []
    if (req.borrow_ticket_id):
        borrow_tickets = models.Borrowtickets.query.filter(models.Borrowtickets.borrow_ticket_id == req.borrow_ticket_id)
        return jsonify({"borrow_tickets": ConvertModelListToDictList(borrow_tickets)})

    borrow_tickets = models.Borrowtickets.query.all()
    if req.customer_name != None:
        all_customers = models.Customers.query.filter((models.Customers.first_name.ilike(f'%{req.customer_name}%'))).all()
        customer_ids = []
        for customer in (all_customers):
            customer_ids.append(customer.customer_id)
        borrow_tickets = models.Borrowtickets.query.filter(models.Borrowtickets.customer_id.in_(customer_ids))

    if req.customer_phone != None:
        all_customers = models.Customers.query.filter((models.Customers.phone.ilike(f'%{req.customer_phone}%'))).all()
        customer_ids = []
        for customer in (all_customers):
            customer_ids.append(customer.customer_id)
        borrow_tickets = models.Borrowtickets.query.filter(models.Borrowtickets.customer_id.in_(customer_ids))

    if req.borrow_ticket_status != None and req.borrow_ticket_status != "":
        current_date = datetime.now()
        if req.borrow_ticket_status == "B":
            borrow_tickets = models.Borrowtickets.query.filter( (models.Borrowtickets.appointment_date >= current_date), (models.Borrowtickets.return_date == None) )
        if req.borrow_ticket_status == "L":
            borrow_tickets = models.Borrowtickets.query.filter((models.Borrowtickets.appointment_date < current_date),
                                                               (models.Borrowtickets.return_date == None))
        if req.borrow_ticket_status == "LF":
            borrow_tickets = models.Borrowtickets.query.filter((models.Borrowtickets.return_date > models.Borrowtickets.appointment_date),
                                                               (models.Borrowtickets.return_date != None))
        if req.borrow_ticket_status == "F":
            borrow_tickets = models.Borrowtickets.query.filter(
                (models.Borrowtickets.return_date <= models.Borrowtickets.appointment_date),
                (models.Borrowtickets.return_date != None))
    return jsonify({
        "borrow_tickets":ConvertModelListToDictList(borrow_tickets)
    })