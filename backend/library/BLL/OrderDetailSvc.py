from library.DAL import OrderDetailRep


def GeOrderDetailsByPage(req):
    has_next, has_prev, order_details = OrderDetailRep.GetOrderDetailsByPage(req)
    result = {
        "has_next": has_next,
        "has_prev": has_prev,
        "order_details": order_details
    }
    return result


def CreateOrderDetail(req):
    create_order_detail = OrderDetailRep.CreateOrderDetail(req)
    return create_order_detail
