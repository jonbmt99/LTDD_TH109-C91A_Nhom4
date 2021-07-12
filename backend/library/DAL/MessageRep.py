from datetime import datetime, timezone

import pytz
from sqlalchemy import desc, asc
from library import db
from library.common.Req.MessageReq import GetMessagesInConversationByFilterReq, SendMessageReq, \
    GetConversationByCustomerAccountIdReq, ReadConversationReq
from library.common.util import ConvertModelListToDictList
from library.DAL import models


def GetMessagesInConversationByPage(req:  GetMessagesInConversationByFilterReq):
    current_page = 0
    if req.page == 0:
        total_messages_amount = models.Messages.query.filter(models.Messages.conversation_id == req.conversation_id).count()
        last_page_number = total_messages_amount // req.per_page if total_messages_amount % req.per_page == 0 else total_messages_amount // req.per_page + 1
        messages_pagination = models.Messages.query.filter(models.Messages.conversation_id == req.conversation_id) \
            .paginate(page=last_page_number, per_page=req.per_page)
        has_next = messages_pagination.has_next
        has_prev = messages_pagination.has_prev
        messages = ConvertModelListToDictList(messages_pagination.items)
        current_page = last_page_number
        return has_next, has_prev, messages, current_page
    else:
        messages_pagination = models.Messages.query.filter(models.Messages.conversation_id == req.conversation_id) \
            .paginate(page=req.page, per_page=req.per_page)
        has_next = messages_pagination.has_next
        has_prev = messages_pagination.has_prev
        messages = ConvertModelListToDictList(messages_pagination.items)
        current_page = req.page
        return has_next, has_prev, messages, current_page

def SendMessage(req: SendMessageReq):
    create_message = models.Messages(conversation_id=req.conversation_id, content=req.content, account_id=req.account_id, created_at= datetime.now(tz=pytz.timezone("Asia/Ho_Chi_Minh")))
    db.session.add(create_message)
    db.session.commit()
    conversation = models.Conversations.query.filter(models.Conversations.conversation_id == req.conversation_id).first()
    conversation.last_message = req.content
    conversation.updated_at = datetime.now(tz=pytz.timezone("Asia/Ho_Chi_Minh"))
    conversation.is_read = False
    db.session.add(conversation)
    db.session.commit()
    return create_message.serialize()

def ReadConversation(req: ReadConversationReq):
    conversation = models.Conversations.query.filter(models.Conversations.conversation_id == req.conversation_id).first()
    conversation.is_read = True
    db.session.add(conversation)
    db.session.commit()
    return conversation.serialize()

def CreateConversation(req):
    create_conversation = models.Conversations(customer_account_id=req['customer_account_id'], created_at=datetime.utcnow())
    db.session.add(create_conversation)
    db.session.commit()
    return create_conversation.serialize() if create_conversation != None else None

def GetConversationByCustomerAccountId(req:GetConversationByCustomerAccountIdReq):
    conversation = models.Conversations.query.filter(models.Conversations.customer_account_id == req.customer_account_id).first()
    return conversation.serialize() if conversation != None else None

def GetAllConversations():
    all_conversations = models.Conversations.query.order_by(desc(models.Conversations.updated_at)).all()
    return ConvertModelListToDictList(all_conversations)
