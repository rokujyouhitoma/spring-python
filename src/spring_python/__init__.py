from abc import abstractmethod
from typing import Any

# Framework codes


class Configuration(object):
    appConfig = None

    def __init__(self, AppConfig) -> None:
        self.appConfig = AppConfig()

    def get(self, name):
        return getattr(self.appConfig, name)


class ApplicationContext(object):
    def getBean(self, Klass) -> Any:
        pass


class AnnotationConfigApplicationContext(ApplicationContext):
    configuration: Configuration = None

    def __init__(self, configuration: Configuration) -> None:
        self.configuration = configuration

    def getBean(self, Klass) -> Any:
        name = Klass.__name__

        def getMethodName(s):
            return s[:1].lower() + s[1:]

        methodName = getMethodName(name)
        return self.configuration.get(methodName)()


# User codes


class User(object):
    pass


class UserRepository(object):
    @abstractmethod
    def register(user: User, rawPassword: str) -> None:
        pass


class PasswordEncoder(object):
    @abstractmethod
    def encode(rawPassword: str) -> str:
        pass


class UserService(object):
    @abstractmethod
    def save(User, user):
        pass

    @abstractmethod
    def countByUserName(userName: str) -> int:
        pass


class UserRepositoryImpl(UserRepository):
    pass


class UserServiceImpl(UserService):
    pass


class Bean(object):
    method = None

    def __init__(self, method):
        self.method = method

    def __call__(self):
        return self.method({})


@Configuration
class AppConfig(object):
    @Bean
    def userRepository(self) -> UserRepository:
        return UserRepositoryImpl()

    @Bean
    def userService(self) -> UserService:
        return UserServiceImpl()
