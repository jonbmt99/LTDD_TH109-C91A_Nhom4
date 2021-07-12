from library.DAL import CustomerRep


def GetCustomersByPage(req):
    has_next, has_prev, customers = CustomerRep.GetCustomersByPage(req)
    result = {
        "has_next": has_next,
        "has_prev": has_prev,
        "customers": customers
    }
    return result


def CreateCustomer(req):
    create_customer = CustomerRep.CreatCustomer(req)
    return create_customer


def UpdateCustomer(req):
    update_customer = CustomerRep.UpdateCustomer(req)
    return update_customer


def DeleteCustomer(req):
    delete_customer = CustomerRep.DeleteCustomer(req)
    return delete_customer


def SearchCustomers(req):
    search_customer = CustomerRep.SearchCustomers(req)
    return search_customer


