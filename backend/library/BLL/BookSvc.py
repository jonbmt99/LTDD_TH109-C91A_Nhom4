from library.DAL import BookRep
from library.common.Rsp.SingleRsp import ErrorRsp


def GetBooksByPage(req):
    has_next, has_prev, books = BookRep.GetBooksByPage(req)
    result = {
        "has_next": has_next,
        "has_prev": has_prev,
        "books": books
    }
    if (req.per_page == 0):
        raise ErrorRsp(code=400, message='Per page không được bằng 0')
    return result


def CreateBook(req):
    book = BookRep.CreateBook(req)
    return book


def DeleteBookById(req):
    book = BookRep.DeleteBookById(req)
    return book


def UpdateBook(req):
    book = BookRep.UpdateBook(req)
    return book


def SearchBooks(req):
    books = BookRep.SearchBooks(req)
    return books


