# Абстрактная фабрика (Abstract Factory) в Python

**Абстрактная фабрика** — это порождающий паттерн проектирования, который позволяет создавать семейства связанных объектов, не привязываясь к их конкретным классам.

### Применимость

- Когда бизнес-логика программы должна работать с различными видами взаимосвязанных продуктов, не завися от их конкретных классов.
- Когда необходимо гарантировать, что продукты одного семейства будут совместимы между собой.

### Преимущества и недостатки

**Преимущества:**

* Гарантирует сочетаемость создаваемых продуктов.
* Избавляет клиентский код от привязки к конкретным классам.
* Упрощает добавление новых семейств продуктов

**Недостатки:**
- Может усложнить код за счет множества классов для каждой вариации продуктов.

---

## Сущности паттерна

**Интерфейсы продуктов**:
   - `UserRepository`: Определяет интерфейс для всех типов репозиториев пользователей.
   - `OrderRepository`: Определяет интерфейс для всех типов репозиториев заказов.
   - `UserService`: Определяет интерфейс для всех типов сервисов пользователей.
   - `OrderService`: Определяет интерфейс для всех типов сервисов заказов.

**Конкретные продукты**:
   - `PostgresUserRepository`: Реализует репозиторий пользователей для PostgreSQL.
   - `PostgresOrderRepository`: Реализует репозиторий заказов для PostgreSQL.
   - `RedisUserRepository`: Реализует репозиторий пользователей для Redis.
   - `RedisOrderRepository`: Реализует репозиторий заказов для Redis.
   - `PostgresUserService`: Реализует сервис пользователей для PostgreSQL.
   - `PostgresOrderService`: Реализует сервис заказов для PostgreSQL.
   - `RedisUserService`: Реализует сервис пользователей для Redis.
   - `RedisOrderService`: Реализует сервис заказов для Redis.

**Абстрактная фабрика** (`ServiceFactory`): Определяет методы для создания сервисов пользователей (`UserService`) и заказов (`OrderService`).

**Конкретные фабрики**:
   - `PostgresServiceFactory`: Создаёт сервисы и репозитории для работы с PostgreSQL.
   - `RedisServiceFactory`: Создаёт сервисы и репозитории для работы с Redis.

**Клиент**: Испoльзует фабрики для создания взаимосвязанных объектов (сервисов пользователей и заказов) и взаимодействует с ними через абстрактные интерфейсы.
