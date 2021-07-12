from library.common.Req.MessageReq import GetMessagesInConversationByFilterReq, SendMessageReq, \
    GetConversationByCustomerAccountIdReq
from library.DAL import MessageRep


def GetMessagesInConversationByPage(req:  GetMessagesInConversationByFilterReq):
    has_next, has_prev, messages, current_page = MessageRep.GetMessagesInConversationByPage(req)
    result = {
        "has_next": has_next,
        "has_prev": has_prev,
        "messages": messages,
        "current_page": current_page
    }
    return result

def SendMessage(req: SendMessageReq):
    result = MessageRep.SendMessage(req)
    result['is_read'] = False
    return result

def ReadConversation(req):
    result = MessageRep.ReadConversation(req)
    return result

def GetConversationByCustomerAccountId(req: GetConversationByCustomerAccountIdReq):
    conversation = MessageRep.GetConversationByCustomerAccountId(req)
    return conversation

def GetAllConversations():
    all_conversation = MessageRep.GetAllConversations()
    return all_conversation
