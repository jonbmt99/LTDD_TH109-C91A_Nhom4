from sqlalchemy import or_

from library import db
from library.common.Req.BorrowTicketReq import CreateBorrowTicketReq, UpdateBorrowTicketReq, DeleteBorrowTicketReq, \
    SearchBorrowTicketReq, FinishBorrowTicketReq
from library.common.Rsp.SingleRsp import ErrorRsp
from library.DAL import models
from flask import jsonify, json
from library.common.util import ConvertModelListToDictList
from library.common.Req import GetItemsByPageReq
from datetime import datetime, timedelta


def GetBorrowTicketsByPage(req: GetItemsByPageReq):
    borrowticket_pagination = models.Borrowtickets.query.paginate \
        (per_page=req.per_page, page=req.page)
    has_next = borrowticket_pagination.has_next
    has_prev = borrowticket_pagination.has_prev
    borrow_tickets = ConvertModelListToDictList(borrowticket_pagination.items)
    return has_next, has_prev, borrow_tickets


def CreateBorrowTicket(req: CreateBorrowTicketReq):
    is_cus_lending_book = len(ConvertModelListToDictList(models.Borrowtickets.query.filter(models.Borrowtickets.customer_id == req.customer_id and models.Borrowtickets.return_date == None))) > 0
    if(is_cus_lending_book):
        raise ErrorRsp(code=400, message='Khách hàng đang có một phiếu mượn khác. Vui lòng hoàn thành phiếu mượn cũ trước khi mượn sách', msg='Khách hàng đang có một phiếu mượn khác. Vui lòng hoàn thành phiếu mượn cũ trước khi mượn sách')
    print(is_cus_lending_book)
    create_borrow_ticket = models.Borrowtickets(customer_id=req.customer_id,
                                                employee_id=req.employee_id,
                                                quantity=len(req.borrow_book_ids),
                                                borrow_date=datetime.now(),
                                                appointment_date=datetime.now() + timedelta(days=14),
                                                note=req.note
                                                )
    db.session.begin_nested()
    db.session.add(create_borrow_ticket)
    db.session.commit()
    count = 0
    for borrow_ticket_detail in req.borrow_book_ids:
        borrow_book = models.Books.query.get(borrow_ticket_detail)
        count += 1
        if borrow_book and count <= 3:
            borrow_book.old_amount -= 1
            new_borrow_ticket_detail = models.Borrowticketdetails(book_id=borrow_ticket_detail,borrow_ticket_id=create_borrow_ticket.serialize()['borrow_ticket_id'])
            create_borrow_ticket.borrow_ticket_detail.append(new_borrow_ticket_detail)
        else:
            db.session.rollback()
            raise ErrorRsp(code=400, message='nd', msg='sss')
    db.session.commit()
    return create_borrow_ticket.serialize()


def UpdateBorrowTicket(req: UpdateBorrowTicketReq):
    update_borrow_ticket = models.Borrowtickets.query.get(req.borrow_ticket_id)
    update_borrow_ticket.customer_id = req.customer_id
    update_borrow_ticket.employee_id = req.employee_id
    update_borrow_ticket.quantity = req.quantity
    update_borrow_ticket.borrow_date = req.borrow_date
    update_borrow_ticket.appointment_date = req.appointment_date
    update_borrow_ticket.return_date = req.return_date
    update_borrow_ticket.status = req.status
    update_borrow_ticket.delete_at = req.delete_at
    update_borrow_ticket.note = req.note
    db.session.commit()
    return update_borrow_ticket.serialize()


def DeleteBorrowTicket(req: DeleteBorrowTicketReq):
    delete_borrow_ticket = models.Borrowtickets.query.get(req.borrow_ticket_id)
    delete_borrow_ticket.delete_at = datetime.now()
    db.session.add(delete_borrow_ticket)
    db.session.commit()
    return delete_borrow_ticket.serialize()


def SearchBorrowTicket(req: SearchBorrowTicketReq):
    search_borrow_ticket = models.Borrowtickets.query.filter(or_(models.Borrowtickets.customer_id == req.customer_id,models.Borrowtickets.employee_id == req.employee_id,models.Borrowtickets.borrow_ticket_id == req.borrow_ticket_id)).all()

    borrow_tickets = ConvertModelListToDictList(search_borrow_ticket)
    return borrow_tickets


def FinishBorrowTicket(req: FinishBorrowTicketReq):
    finish_borrow_ticket = models.Borrowtickets.query.get(req.borrow_ticket_id)
    appointment_date = finish_borrow_ticket.appointment_date
    db.session.commit()
    return finish_borrow_ticket.serialize()
