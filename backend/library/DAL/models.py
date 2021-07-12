from datetime import datetime
from sqlalchemy.types import Enum
from library import db
from library.common.util import ConvertModelListToDictList

class OrderType(Enum):
    ONLINE  = "online"
    OFFLINE = "offline"

class BorrowTicketStatus(Enum):
    Borrowing = "B"
    Lating = "L"
    LateFinish = "LF"
    F = "F"
class Accounts(db.Model):
    account_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.role_id'))
    account_name = db.Column(db.String(50), nullable=False, unique=True)
    account_password = db.Column(db.String(50), nullable=False)
    note = db.Column(db.String(50))
    delete_at = db.Column(db.DateTime, default=None)
    customers = db.relationship('Customers', backref='account', lazy='subquery')
    employees = db.relationship('Employees', backref='account', lazy='subquery')
    conversations = db.relationship('Conversations', backref='account', lazy='subquery')
    messages = db.relationship('Messages', backref='account', lazy='subquery')

    def serialize(self):
        if self != None:
            return {"account_id": self.account_id, "account_name": self.account_name, "note": self.note,
                "delete_at": self.delete_at, "role": self.role.serialize() if self.role != None else None}
        else:
            return {}

    def __repr__(self):
        return f"Account('{self.account_id}','{self.account_name}','{self.note}', '{self.delete_at}', " \
               f"'{self.role.serialize()}')"


class Books(db.Model):
    book_id = db.Column(db.Integer, autoincrement=True, nullable=False, primary_key=True, unique=True)
    book_name = db.Column(db.String(150), nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.supplier_id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'))
    author_id = db.Column(db.Integer, db.ForeignKey('authors.author_id'))
    old_amount = db.Column(db.Integer)
    new_amount = db.Column(db.Integer)
    image = db.Column(db.String(1000))
    page_number = db.Column(db.Integer)
    description = db.Column(db.TEXT(16383))
    cost_price = db.Column(db.Float)
    retail_price = db.Column(db.Float)
    discount = db.Column(db.Float, default=0.0)
    ranking = db.Column(db.String(50))
    rate_star = db.Column(db.Float, name="rate_star", default=0)
    rate_count = db.Column(db.Integer, name="rate_count", default=0)
    delete_at = db.Column(db.DateTime, default=None)
    note = db.Column(db.String(1500))
    comments = db.relationship('Comments', backref='book', lazy=True)
    order_details = db.relationship('Orderdetails', backref='book', lazy=True)
    borrow_ticket_details = db.relationship('Borrowticketdetails', backref='book', lazy=True)
    def serialize(self):
        return {"book_id": self.book_id, "book_name": self.book_name, "note": self.note,
                "supplier": self.supplier.serialize() if self.supplier != None else None, "category": self.category.serialize() if self.category != None else None,
                "author": self.author.serialize() if self.author != None else None,
                "old_amount": self.old_amount, "new_amount": self.new_amount, "image": self.image,
                "page_number": self.page_number, "description": self.description, "cost_price": self.cost_price,
                "retail_price": self.retail_price, "discount": self.discount, "ranking": self.ranking, "rate_star": self.rate_star, "rate_count":self.rate_count,
                "delete_at": self.delete_at}

    def __repr__(self):
        return f"('book_id':{self.book_id},'book_name': {self.book_name},'note : {self.note},'supplier': {self.supplier.serialize()},'category': {self.category.serialize()}, " \
               f"'author': {self.author.serialize()},'old_amount': {self.old_amount},'new_amount': {self.new_amount},'image': {self.image},'page_number': {self.page_number}, " \
               f"'description ':{self.description},'cost_price': {self.cost_price},'retail_price': {self.retail_price},'discount': {self.discount},'ranking': {self.ranking})"

class Comments(db.Model):
    comment_id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.TEXT)
    create_at = db.Column(db.DateTime)
    book_id = db.Column(db.Integer, db.ForeignKey('books.book_id'))
    customer_id = db.Column(db.Integer)

    def serialize(self):
        return {
            "comment_id": self.comment_id,
            "content": self.content,
            "book_id": self.book_id,
            "customer_id": self.customer_id,
            "create_at": self.create_at,
            'book': self.book.serialize() if self.book != None else None,
        }

class Borrowticketdetails(db.Model):
    borrow_ticket_id = db.Column(db.Integer, db.ForeignKey('borrowtickets.borrow_ticket_id'), primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.book_id'), primary_key=True)
    delete_at = db.Column(db.DateTime, default=None)

    def serialize(self):
        return {"borrow_ticket_id": self.borrow_ticket_id, "book_id": self.book_id, "delete_at": self.delete_at, 'book': self.book.serialize() if self.book != None else None}

    def __repr__(self):
        return f"('book_id':{self.book_id}, 'borrow_ticket_id': {self.borrow_ticket_id})"


class Borrowtickets(db.Model):
    borrow_ticket_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'))
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.employee_id'))
    quantity = db.Column(db.Integer)
    borrow_date = db.Column(db.DateTime)
    appointment_date = db.Column(db.DateTime)
    return_date = db.Column(db.DateTime)
    status = db.Column(db.String(20))
    delete_at = db.Column(db.DateTime, default=None)
    note = db.Column(db.String(1500))
    borrow_ticket_detail = db.relationship('Borrowticketdetails', backref='borrowticket', lazy=True)

    def serialize(self):
        return {"borrow_ticket_id": self.borrow_ticket_id, "customer": self.customer.serialize() if self.customer != None else None, "note": self.note,
                "employee": self.employee.serialize() if self.employee != None else None, "quantity": self.quantity, "borrow_date": self.borrow_date,
                "appointment_date": self.appointment_date, "return_date": self.return_date, "status": self.status,
                "delete_at": self.delete_at, "borrow_ticket_details": ConvertModelListToDictList(self.borrow_ticket_detail)}

    def __repr__(self):
        return f"Borrowticket('{self.borrow_ticket_id}','{self.customer.serialize()}','{self.note}','{self.employee.serialize()}'," \
               f"'{self.quantity}','{self.borrow_date}','{self.appointment_date}','{self.return_date}','{self.status}', '{self.delete_at}')"



class Categories(db.Model):
    category_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    books = db.relationship("Books", backref="category", lazy=False)
    category_name = db.Column(db.String(50))
    image = db.Column(db.String(1500))
    description = db.Column(db.String(1500))
    note = db.Column(db.String(1500))
    delete_at = db.Column(db.DateTime, default=None)
    books = db.relationship('Books', backref="category", lazy=True)

    def serialize(self):
        return {"category_id": self.category_id, "category_name": self.category_name, "note": self.note,
                "description": self.description, "delete_at": self.delete_at, "image": self.image}

    def __repr__(self):
        return f"Category('{self.category_id}','{self.category_name}','{self.note}','{self.description}', '{self.delete_at}')"

class Customers(db.Model):
    customer_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.account_id'), unique=True)
    last_name = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    phone = db.Column(db.String(50))
    birth_date = db.Column(db.DateTime)
    province_id = db.Column(db.String(50), name="province_id")
    district_id = db.Column(db.String(50), name="district_id")
    ward_id = db.Column(db.String(50), name="ward_id")
    address = db.Column(db.String(1500))
    gender = db.Column(db.Boolean)
    note = db.Column(db.String(1500))
    image = db.Column(db.String(1500))
    delete_at = db.Column(db.DateTime, default=None)
    orders = db.relationship('Orders', backref='customer', lazy=True)
    borrow_tickets = db.relationship('Borrowtickets', backref='customer', lazy=True)
    def serialize(self):
        return {"customer_id": self.customer_id, "note": self.note,
                "account": self.account.serialize() if self.account != None else None, "last_name": self.last_name,
                "first_name": self.first_name, "email": self.email, "phone": self.phone, "birth_day": str(self.birth_date),
                "province_id": self.province_id,
                "district_id": self.district_id,
                "ward_id": self.ward_id,
                "address": self.address, "gender": self.gender, "delete_at": self.delete_at, "image": self.image
                }

    def __repr__(self):
        return f"Customer('{self.customer_id}','','{self.note}','{self.account.serialize()}'," \
               f"','{self.last_name}','{self.email}','{self.birth_date}','{self.address}'," \
               f"'{self.gender}','{self.phone}', '{self.delete_at}')"

class Conversations(db.Model):
    conversation_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False,
                                unique=True)
    customer_account_id = db.Column(db.Integer, db.ForeignKey('accounts.account_id'),
                                     primary_key=True, nullable=False, unique=True)
    messages = db.relationship('Messages', backref='conversation', lazy=True)
    created_at = db.Column(db.DateTime) #Ngay khi tạo tài khoản customer thành công
    updated_at = db.Column(db.DateTime) #Ngay khi tin nhắn gần nhất được gửi
    last_message = db.Column(db.String(2000))
    is_read = db.Column(db.Boolean)

    def serialize(self):
        return {'conversation_id': self.conversation_id,
                'customer_account_id': self.customer_account_id,
                'created_at': self.created_at,
                'updated_at': self.updated_at,
                'last_message': self.last_message,
                'account': self.account.serialize() if self.account != None else None,
                'is_read': self.is_read
                }

class Messages(db.Model):
    message_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False,
                           unique=True)
    conversation_id = db.Column(db.Integer, db.ForeignKey('conversations.conversation_id'),
                            nullable=False)
    content = db.Column(db.String(2000))
    created_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.account_id'), nullable=False)

    def serialize(self):
        return {
            'message_id': self.message_id,
            'conversation_id': self.conversation_id,
            'content': self.content,
            'created_at': self.created_at,
            'account_id': self.account_id,
            'deleted_at': self.deleted_at,
        }

class Employees(db.Model):
    employee_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.account_id'), unique=True)
    last_name = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    birth_date = db.Column(db.DateTime)
    hire_date = db.Column(db.DateTime)
    province_id = db.Column(db.String(50), name="province_id")
    district_id = db.Column(db.String(50), name="district_id")
    ward_id = db.Column(db.String(50), name="ward_id")
    address = db.Column(db.String(1500))
    gender = db.Column(db.Boolean)
    image = db.Column(db.String(1500))
    basic_rate = db.Column(db.Float)
    note = db.Column(db.String(1500))
    delete_at = db.Column(db.DateTime, default=None)
    orders = db.relationship('Orders', backref='employee', lazy=True)
    borrow_tickets = db.relationship('Borrowtickets', backref='employee', lazy=True)
    def serialize(self):
        return {"employee_id": self.employee_id,  "note": self.note,
                "account": self.account.serialize() if self.account != None else None, "last_name": self.last_name, "first_name": self.first_name,
                "phone": self.phone, "birth_day": self.birth_date, "provinceId": self.province_id,
                "districtId": self.district_id,
                "wardId": self.ward_id,
                "address": self.address, "gender": self.gender,
                "image": self.image, "basic_rate": self.basic_rate, "delete_at": self.delete_at, "email": self.email,
                "hire_date": self.hire_date}

    def __repr__(self):
        return f"Employee('{self.employee_id}','','{self.note}','{self.account.serialize()}','{self.first_name}'" \
               f",'{self.last_name}','{self.phone}','{self.birth_date}','{self.address}','{self.gender}','{self.image}'" \
               f",'{self.basic_rate}', '{self.delete_at}', '{self.hire_date}', '{self.email}')"


class Orderdetails(db.Model):
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id'), primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.book_id'), primary_key=True)
    retail_price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    discount = db.Column(db.Float)
    total = db.Column(db.Float)
    note = db.Column(db.String(1500))
    delete_at = db.Column(db.DateTime, default=None)

    def serialize(self):
        return {"book": self.book.serialize() if self.book != None else None,"order_id": self.order_id, "note": self.note,
                "retail_price": self.retail_price, "quantity": self.quantity, "discount": self.discount,
                "total": self.total, "delete_at": self.delete_at}

    def __repr__(self):
        return f"Orderdetail('{self.order.serialize()}','{self.note}','{self.retail_price}','{self.quantity}'," \
               f"'{self.discount}','{self.note}', {self.delete_at})"


class Orders(db.Model):
    order_id = db.Column(db.Integer, unique=True, autoincrement=True, primary_key=True, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'))
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.employee_id'))
    order_date = db.Column(db.DateTime)
    total = db.Column(db.Float)
    type = db.Column(db.Enum("online", "offline"), name="type", default="offline")
    note = db.Column(db.String(1500))
    delete_at = db.Column(db.DateTime, default=None)
    create_at = db.Column(db.DateTime, default=datetime.now())
    order_details = db.relationship('Orderdetails', backref="order", lazy=False)

    def serialize(self):
        return {"order_id": self.order_id, "customer": self.customer.serialize() if self.customer != None else None, "note": self.note,
                "employee": self.employee.serialize() if  self.employee != None else None, "create_at": self.create_at,
                "order_date": self.order_date, "total": self.total, "order_details": ConvertModelListToDictList(self.order_details),
                "type": self.type,
                "delete_at": self.delete_at}

    def __repr__(self):
        return f"Order('{self.order_id}', '{self.customer.serialize()}', '{self.employee.serialize()}','{self.note}', '{self.order_date}', '{self.total}', " \
               f"'{self.type}', '{self.delete_at}')"


class Roles(db.Model):
    role_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    role_name = db.Column(db.String(50))
    note = db.Column(db.String(1500))
    delete_at = db.Column(db.DateTime, default=None)
    accounts = db.relationship('Accounts', backref="role", lazy=True)

    def serialize(self):
        return {"role_id": self.role_id, "role_name": self.role_name, "note": self.note, "delete_at": self.delete_at}

    def __repr__(self):
        return f"Role('{self.role_id}','{self.role_name}','{self.note}', '{self.delete_at}')"


class Suppliers(db.Model):
    supplier_id = db.Column(db.Integer, unique=True, autoincrement=True, primary_key=True, nullable=False)
    contact_name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(1500))
    phone = db.Column(db.String(50))
    email = db.Column(db.String(50), nullable=False)
    note = db.Column(db.String(1500))
    delete_at = db.Column(db.DateTime, default=None)
    books = db.relationship('Books', backref='supplier', lazy=True)

    def serialize(self):
        return {"supplier_id": self.supplier_id, "contact_name": self.contact_name, "note": self.note,
                "address": self.address, "phone": self.phone, "email": self.email, "delete_at": self.delete_at}

    def __repr__(self):
        return f"Supplier('{self.supplier_id}','{self.contact_name}','{self.note}','{self.address}','{self.phone}'," \
               f"'{self.email}', '{self.delete_at}')"


class Authors(db.Model):
    author_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False, autoincrement=True)
    author_name = db.Column(db.String(50))

    books = db.relationship('Books', backref='author', lazy=True)
    delete_at = db.Column(db.DateTime, default=None)

    def serialize(self):
        return {"author_id": self.author_id, "author_name": self.author_name}

    def __repr__(self):
        return f"Author('{self.author_id}','{self.author_name}')"

class Ward(db.Model):
    id = db.Column(db.String(10), nullable=False)
    code = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    districtId = db.Column(db.String(50), name="district_id")

    def __init__(self, id, name, districtId) -> None:
        self.id = id
        self.name = name
        self.districtId = districtId
        super().__init__()

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "districtId": self.districtId,

        }

class Province(db.Model):
    id = db.Column(db.String(10), nullable=False)
    code = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    region = db.Column(db.String(50), name="region")

    def __init__(self, id, name, region) -> None:
        self.id = id
        self.name = name
        self.region = region
        super().__init__()

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "region": self.region,
        }

class District(db.Model):
    id = db.Column(db.String(10), nullable=False)
    code = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    provinceId = db.Column(db.String(50), name="province_id")

    def __init__(self, id, name, provinceId) -> None:
        self.id = id
        self.name = name
        self.provinceId = provinceId
        super().__init__()

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "provinceId": self.provinceId,
        }
