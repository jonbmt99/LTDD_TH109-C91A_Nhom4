from datetime import datetime, date, timedelta
from sqlalchemy import func, desc
from library import db
from library.DAL import models
from library.DAL.models import Books, Orderdetails, Orders, Employees


def GetOrdersToday():
    orders = models.Orders.query.filter(models.Orders.order_id,
                                    func.DATE(models.Orders.order_date) == datetime.utcnow().date()).all()
    return orders

def GetOrdersInMonth():
    month_orders = models.Orders.query.filter(func.MONTH(models.Orders.order_date) == datetime.utcnow().month).all()
    return month_orders


def GetOrdersInPrevMonth():
    prev_month_orders =models.Orders.query.filter(models.Orders.total, func.MONTH(models.Orders.order_date) == date.today().month - 1).all()
    return prev_month_orders


def GetTotalRevenueOfSpecificDay(specific_date = datetime.utcnow().date()):
    total_revenue_in_specific_date = db.session.query(func.sum(Orders.total))\
        .filter(func.DATE(models.Orders.order_date) == specific_date)\
        .first()
    return total_revenue_in_specific_date[0] if total_revenue_in_specific_date[0] else 0.0


def GetTotalRevenueOfSpecificMonth(month, year):
    total_revenue_in_specific_month = db.session.query(func.sum(Orders.total)) \
        .filter(func.MONTH(models.Orders.order_date) == month, func.YEAR(models.Orders.order_date) == year) \
        .first()
    return total_revenue_in_specific_month[0] if total_revenue_in_specific_month[0] else 0.0

def PercentageWithPrevDay():
    percentage = models.Orders.query.filter(models.Orders.total,
                                            func.DATE(models.Orders.order_date) == date.today() - timedelta(
                                                days=1)).all()

def GetTopBooks(limit = 10):
    total_quantity_of_each_book_model_arr = db.session.query(Orderdetails.book_id ,func.sum(Orderdetails.quantity).label("sum"), Books)\
        .group_by(Orderdetails.book_id)\
        .join(Books, Books.book_id == Orderdetails.book_id, isouter=True)\
        .join(Orders, Orders.order_id == Orderdetails.order_id )\
        .order_by(desc("sum"))\
        .limit(limit)\
        .all()
    return total_quantity_of_each_book_model_arr


def GetBestSellerInMonth():
    result = db.session.query(
        func.count(Orders.employee_id).label("order_amount"),
        Employees,
        func.sum(Orders.total).label("total_revenue"),
    ) \
        .filter(func.MONTH(models.Orders.order_date) == date.today().month and func.YEAR(models.Orders.order_date) == date.today().year) \
        .group_by(Orders.employee_id)\
        .join(Employees, Employees.employee_id == Orders.employee_id, isouter=True) \
        .order_by(desc("order_amount"))\
        .all()
    return result


def GetBorrowTicketsInSpecificDay(datetime = datetime.utcnow().date()):
    borrow_tickets_in_day = models.Borrowtickets.query.filter(
        func.MONTH(models.Borrowtickets.borrow_date) == datetime.month,
        func.YEAR(models.Borrowtickets.borrow_date) == datetime.year,
        func.DAY(models.Borrowtickets.borrow_date) == datetime.day
    ).all()
    return borrow_tickets_in_day




