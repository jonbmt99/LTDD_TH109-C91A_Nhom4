from datetime import date, datetime, timedelta

from library.DAL import RevenueRep
from calendar import monthrange

def GetTodayOrderCount():
    ###Tổng đơn hàng trong ngày
    today_orders = RevenueRep.GetOrdersToday()
    res_today_order_count = dict({
        'label':'today_order_count',
        'value': len(today_orders)
    })
    return res_today_order_count

def GetMonthOrderCount():
    ###Tổng đơn hàng trong ngày
    month_orders = RevenueRep.GetOrdersInMonth()
    res_month_order_count = dict({
        'label':'month_order_count',
        'value': len(month_orders)
    })
    return res_month_order_count

def GetTodayRevenue():
    ### Tổng doanh thu trong ngày
    today_revenue = RevenueRep.GetTotalRevenueOfSpecificDay()
    res_revenue_today = dict({
        'label':'today_revenue',
        'value': today_revenue
    })
    return res_revenue_today

def GetPercentageTodayRevenueToPrevDay():
    ### Doanh thu so với hôm qua
    today_revenue = RevenueRep.GetTotalRevenueOfSpecificDay()
    prev_day_revenue = RevenueRep.GetTotalRevenueOfSpecificDay(datetime.now().date() - timedelta(days = 1))
    percentage_today_revenue_with_prev_day = 1 if prev_day_revenue == 0 else  round((today_revenue / prev_day_revenue), 4)
    res_percentage_today_revenue_with_prev_day = dict({
        'label':'percentage_today_revenue_with_prev_day',
        'value': percentage_today_revenue_with_prev_day
    })
    return res_percentage_today_revenue_with_prev_day

def GetPercentageMonthRevenueToPrevMonth():
    ### Doanh thu so voi81 tháng trước
    month_orders = RevenueRep.GetOrdersInMonth()
    prev_month_orders = RevenueRep.GetOrdersInPrevMonth()
    month_total_revenue = 0.0
    prev_month_total_revenue = 0.0
    for order in month_orders:
        month_total_revenue += order.total

    for order in prev_month_orders:
        prev_month_total_revenue += order.total

    percentage_month_revenue_to_prev_month = 1 if prev_month_total_revenue == 0 else round((month_total_revenue / prev_month_total_revenue), 4)
    res_percentage_month_revenue_to_prev_month = dict({
        'label': "res_percentage_month_revenue_to_prev_month",
        'value': percentage_month_revenue_to_prev_month
    })
    return res_percentage_month_revenue_to_prev_month

def GetGrowPercentageToPrevDay():
    ### Tốc độ tăng trưởng doanh thu so với hôm qua
    prev_day_revenue = RevenueRep.GetTotalRevenueOfSpecificDay(datetime.now().date() - timedelta(days = 1))
    today_revenue = RevenueRep.GetTotalRevenueOfSpecificDay()
    grow_percentage_to_prev_day = 1 if prev_day_revenue == 0 else round((today_revenue / prev_day_revenue), 4) -1
    if prev_day_revenue == today_revenue:
        grow_percentage_to_prev_day = 0

    res_grow_percentage_to_prev_day = dict({
        'label': 'grow_percentage_to_prev_day',
        'value': grow_percentage_to_prev_day
    })
    return res_grow_percentage_to_prev_day

def GetGrowPercentageToPrevMonth():
    ### Tốc độ tăng trường doanh thu so với tháng trước
    month_orders = RevenueRep.GetOrdersInMonth()
    prev_month_orders = RevenueRep.GetOrdersInPrevMonth()
    month_total_revenue = 0.0
    prev_month_total_revenue = 0.0
    for order in month_orders:
        month_total_revenue += order.total

    for order in prev_month_orders:
        prev_month_total_revenue += order.total

    grow_percentage_to_prev_month = 1 if prev_month_total_revenue == 0 else round((month_total_revenue / prev_month_total_revenue), 4) -1

    if prev_month_total_revenue == month_total_revenue:
        grow_percentage_to_prev_month = 0
    res_grow_percentage_to_prev_month = dict({
        'label': 'grow_percentage_to_prev_month',
        'value': grow_percentage_to_prev_month
    })
    return res_grow_percentage_to_prev_month

def GetRevenueEachDayInMonth():
    ### Doanh thu từng ngày trong tháng
    revenue_of_each_day_in_month_arr = []
    for i in range(1, monthrange(datetime.now().year, datetime.now().month)[1] + 1):
        datetime_day = datetime(datetime.now().year, datetime.now().month, i).date()
        revenue_of_each_day_dict = dict({
            'date': datetime(month=datetime_day.month, day=datetime_day.day, year=2020),
            'revenue': RevenueRep.GetTotalRevenueOfSpecificDay(datetime_day)
        })
        revenue_of_each_day_in_month_arr.append(revenue_of_each_day_dict)

    res_revenue_each_day_in_month_arr = dict({
        'label': 'revenue_each_day_in_month_arr',
        'value': revenue_of_each_day_in_month_arr
    })
    return res_revenue_each_day_in_month_arr


def GetRevenueEachMonthInYear():
    ### Doanh thu tứng tháng trong năm
    revenue_of_each_month_in_year_arr = []
    for month in range(1, 13):
        revenue_of_month = RevenueRep.GetTotalRevenueOfSpecificMonth(month, datetime.now().year)
        revenue_of_month_dict = dict({
            'month': month,
            'revenue': revenue_of_month
        })
        revenue_of_each_month_in_year_arr.append(revenue_of_month_dict)
    res_revenue_of_each_month_in_year_arr = dict({
        'label': 'revenue_of_each_month_in_year_arr',
        'value': revenue_of_each_month_in_year_arr
    })
    return res_revenue_of_each_month_in_year_arr


def GetTotalRevenueInMonth():
    ### Tổng doanh thu trong tháng
    month_orders = RevenueRep.GetOrdersInMonth()
    month_total_revenue = 0.0
    for order in month_orders:
        month_total_revenue += order.total

    res_month_total_revenue = dict({
        'label': 'month_total_revenue',
        'value': month_total_revenue
    })
    return res_month_total_revenue


def GetTopSellerInMonth():
    ### Top Best Sellers
    best_sellers_in_month_arr = []
    best_sellers_in_month_model_arr = RevenueRep.GetBestSellerInMonth()
    for best_seller in best_sellers_in_month_model_arr:
        total_quantity_of_each_book_dict = dict()
        total_quantity_of_each_book_dict['order_amount'] = int(best_seller[0]) if int(best_seller[0]) != None else None
        total_quantity_of_each_book_dict['employee'] = best_seller[1].serialize() if best_seller[1] != None else None
        total_quantity_of_each_book_dict['total_revenue'] = int(best_seller[2]) if int(best_seller[2]) != None else None
        best_sellers_in_month_arr.append(total_quantity_of_each_book_dict)
    res_best_sellers_in_month = dict({
        'label': 'best_sellers_in_month',
        'value': best_sellers_in_month_arr
    })
    return res_best_sellers_in_month


def GetMostFavoriteBooks():
    ### Top sách yêu thích
    most_favorite_books = []
    total_quantity_of_each_book_model_arr = RevenueRep.GetTopBooks()
    for total_quantity in total_quantity_of_each_book_model_arr:
        total_quantity_of_each_book_dict = dict()
        total_quantity_of_each_book_dict['total_quantity'] = int(total_quantity[1])
        total_quantity_of_each_book_dict['book'] = total_quantity[2].serialize()
        most_favorite_books.append(total_quantity_of_each_book_dict)

    res_most_favorite_books = dict({
        'label': 'most_favorite_books',
        'value': most_favorite_books
    })
    return res_most_favorite_books

def GetBorrowTicketsInMonth():
    ### Số lượng đơn mượn
    res_borrow_tickets_count = dict({
        'label': 'res_borrow_tickets_count',
        'value': len(RevenueRep.GetBorrowTicketsInSpecificDay())
    })
    return res_borrow_tickets_count
def Revenue():
    res_today_order_count = GetTodayOrderCount()
    res_month_order_count = GetMonthOrderCount()
    res_revenue_today = GetTodayRevenue()
    res_percentage_today_revenue_to_prev_day = GetPercentageTodayRevenueToPrevDay()
    res_percentage_month_revenue_to_prev_month = GetPercentageMonthRevenueToPrevMonth()
    res_grow_percentage_to_prev_day = GetGrowPercentageToPrevDay()
    res_grow_percentage_to_prev_month = GetGrowPercentageToPrevMonth()
    res_revenues_each_day_in_month = GetRevenueEachDayInMonth()
    res_revenue_of_each_month_in_year = GetRevenueEachMonthInYear()
    res_month_total_revenue = GetTotalRevenueInMonth()
    res_best_sellers_in_month = GetTopSellerInMonth()
    res_most_favorite_books = GetMostFavoriteBooks()
    res_borrow_tickets_count = GetBorrowTicketsInMonth()

    revenue_result = dict({
        'today_order_count': res_today_order_count,
        'month_order_count': res_month_order_count,
        'revenue_today': res_revenue_today,
        'percentage_today_revenue_to_prev_day': res_percentage_today_revenue_to_prev_day,
        'percentage_month_revenue_to_prev_month': res_percentage_month_revenue_to_prev_month,
        'grow_percentage_to_prev_day': res_grow_percentage_to_prev_day,
        'grow_percentage_to_prev_month': res_grow_percentage_to_prev_month,
        'revenues_each_day_in_month': res_revenues_each_day_in_month,
        'revenue_of_each_month_in_year': res_revenue_of_each_month_in_year,
        'month_total_revenue': res_month_total_revenue,
        'best_sellers_in_month': res_best_sellers_in_month,
        'most_favorite_books': res_most_favorite_books,
        'borrow_tickets_count': res_borrow_tickets_count,
    })

    return revenue_result










