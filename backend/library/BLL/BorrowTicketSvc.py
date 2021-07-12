from email.message import EmailMessage

from library import smtp, app
from library.common.Req.BorrowTicketReq import CreateBorrowTicketReq, \
    SendEmailForLateBorrowTicketReq
from library.common.Rsp.SingleRsp import ErrorRsp
from library.DAL import BorrowTicketRep


def GetBorrowTicketsByPage(req):
    has_next, has_prev, borrow_tickets = BorrowTicketRep.GetBorrowTicketsByPage(req)
    result = {
        "has_next": has_next,
        "has_prev": has_prev,
        "borrow_tickets": borrow_tickets
    }
    return result


def CreateBorrowTicket(req: CreateBorrowTicketReq):
    try :
        create_borrow_ticket = BorrowTicketRep.CreateBorrowTicket(req)
        return create_borrow_ticket
    except ErrorRsp as e:
        raise e


def UpdateBorrowTicket(req):
    update_borrow_ticket = BorrowTicketRep.UpdateBorrowTicket(req)
    return update_borrow_ticket


def FinishBorrowTicket(req):
    update_borrow_ticket = BorrowTicketRep.FinishBorrowTicket(req)
    return update_borrow_ticket

def DeleteBorrowTicket(req):
    delete_borrow_ticket = BorrowTicketRep.DeleteBorrowTicket(req)
    return delete_borrow_ticket


def SearchBorrowTicket(req):
    search_borrow_ticket = BorrowTicketRep.SearchBorrowTicket(req)
    return search_borrow_ticket

def SendMessageForLate(req: SendEmailForLateBorrowTicketReq):
    smtp.login(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
    msg = EmailMessage()
    msg['Subject'] = 'Thư gửi nhắc nhở hạn trả sách'
    msg['From'] = app.config['MAIL_USERNAME']
    msg['To'] = req.customer_email
    msg.set_content(
        f'''    Gửi {app.config['MAIL_USERNAME']},

    {req.message}.
    
    Nếu không phải bạn, hãy bỏ qua email này.

    Rất mong nhận được sự hợp tác từ bạn.
    Chúng tôi xin trân trọng cảm ơn!

    Đội ngũ quản lý thư quán Đại học Mở TPHCM!
''')
    smtp.send_message(msg)
    return " Vui lòng kiểm tra email để reset mật khẩu"
