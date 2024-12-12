from abc import ABC, abstractmethod


class UserRepository(ABC):
    @abstractmethod
    def get_user(self, username: str) -> str:
        pass


class OrderRepository(ABC):
    @abstractmethod
    def get_order(self, order_id: int) -> str:
        pass


class UserService(ABC):
    @abstractmethod
    def fetch_user(self, username: str) -> str:
        pass


class OrderService(ABC):
    @abstractmethod
    def fetch_order(self, order_id: int) -> str:
        pass


class PostgresUserRepository(UserRepository):
    def get_user(self, username: str) -> str:
        return f"User '{username}' retrieved from PostgreSQL."


class PostgresOrderRepository(OrderRepository):
    def get_order(self, order_id: int) -> str:
        return f"Order '{order_id}' retrieved from PostgreSQL."


class PostgresUserService(UserService):
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def fetch_user(self, username: str) -> str:
        return self.repo.get_user(username)


class PostgresOrderService(OrderService):
    def __init__(self, repo: OrderRepository):
        self.repo = repo

    def fetch_order(self, order_id: int) -> str:
        return self.repo.get_order(order_id)


class RedisUserRepository(UserRepository):
    def get_user(self, username: str) -> str:
        return f"User '{username}' retrieved from Redis cache."


class RedisOrderRepository(OrderRepository):
    def get_order(self, order_id: int) -> str:
        return f"Order '{order_id}' retrieved from Redis cache."


class RedisUserService(UserService):
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def fetch_user(self, username: str) -> str:
        return self.repo.get_user(username)


class RedisOrderService(OrderService):
    def __init__(self, repo: OrderRepository):
        self.repo = repo

    def fetch_order(self, order_id: int) -> str:
        return self.repo.get_order(order_id)


# Абстрактная фабрика
class ServiceFactory(ABC):
    @abstractmethod
    def create_user_service(self) -> UserService:
        pass

    @abstractmethod
    def create_order_service(self) -> OrderService:
        pass


# Конкретная фабрика для PostgreSQL
class PostgresServiceFactory(ServiceFactory):
    def create_user_service(self) -> UserService:
        return PostgresUserService(PostgresUserRepository())

    def create_order_service(self) -> OrderService:
        return PostgresOrderService(PostgresOrderRepository())


# Конкретная фабрика для Redis
class RedisServiceFactory(ServiceFactory):
    def create_user_service(self) -> UserService:
        return RedisUserService(RedisUserRepository())

    def create_order_service(self) -> OrderService:
        return RedisOrderService(RedisOrderRepository())


# Клиентский код
def client_code(factory: ServiceFactory):
    user_service = factory.create_user_service()
    order_service = factory.create_order_service()

    print(user_service.fetch_user("maxim"))
    print(order_service.fetch_order(42))


if __name__ == "__main__":
    print("Using PostgreSQL services:")
    client_code(PostgresServiceFactory())

    print("\nUsing Redis services:")
    client_code(RedisServiceFactory())
