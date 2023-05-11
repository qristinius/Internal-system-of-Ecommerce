from app.extensions import db
from app.models.base import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash


class UserRole(BaseModel):
    __tablename__ = "user_roles"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("registered_users.id"))
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))


class User(BaseModel):
    __tablename__ = "registered_users"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column("email", db.String, unique=True, nullable=False)
    _password = db.Column("password", db.String, nullable=False)
    reset_password = db.Column(db.Boolean, default=False)
    confirmation = db.Column(db.Boolean, default=False)
    registration_date = db.Column(db.Text)

    comment = db.relationship("ProductComment", backref="user")

    def _get_password(self):
        return self._password

    def _set_password(self, password):
        self._password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    password = db.synonym("_password", descriptor=property(
        _get_password, _set_password))

    def check_permission(self, request):
        permissions = [getattr(permission, request) for permission in self.role]
        return any(permissions)


class Role(BaseModel):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    can_create_role = db.Column(db.Boolean, default=False)
    can_modify_employee_profile = db.Column(db.Boolean, default=False)
    can_send_message = db.Column(db.Boolean, default=False)

    can_create_product = db.Column(db.Boolean, default=False)
    can_create_sales = db.Column(db.Boolean, default=False)
    can_see_stats = db.Column(db.Boolean, default=False)

    can_deliver_items = db.Column(db.Boolean, default=False)
    can_modify_profile = db.Column(db.Boolean, default=False)
    can_buy_product = db.Column(db.Boolean, default=False)

    user = db.relationship("User", secondary="user_roles", backref="role")
