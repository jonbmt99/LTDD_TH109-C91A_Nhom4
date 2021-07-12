from library.common.Req.CategoryReq import CreateCategoryReq, UpdateCategoryReq, DeleteCategoryByIdReq, SearchCategoryReq
from library.DAL import CategoryRep


def GetCategoriesByPage(req):
    has_next, has_prev, categories = CategoryRep.GetCategoriesByPage(req)
    result = {
        "has_next": has_next,
        "has_prev": has_prev,
        "categories": categories
    }
    return result


def CreateCategory(new_cate_req: CreateCategoryReq):
    new_category = CategoryRep.CreateCategory(new_cate_req)
    return new_category


def UpdateCategory(update_cate_req: UpdateCategoryReq):
    update_category = CategoryRep.UpdateCategory(update_cate_req)
    return update_category


def DeleteCategoryById(req: DeleteCategoryByIdReq):
    delete_category = CategoryRep.DeleteCategoryById(req)
    return delete_category

def SearchCategory(req: SearchCategoryReq):
    search_category = CategoryRep.SearchCategory(req)
    return search_category

